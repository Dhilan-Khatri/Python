from __future__ import annotations
from config import hf_api18_key
import requests, base64, os, re, time
from PIL import Image
from colorama import init, Fore, Style
init(autoreset=True)
ROUTER_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {hf_api18_key}", "Content-Type": "application/json"}
VISION_MODELS = [
    "google/gemma-4-31B-it:together", # Gemma 4 — multimodal, fast
    "meta-llama/Llama-3.2-11B-Vision-Instruct:together", # Llama 3.2 Vision — 11B
    "meta-llama/Llama-3.2-90B-Vision-Instruct:together", # Llama 3.2 Vision — 90B
    "moonshotai/Kimi-K2.5:together"] # Kimi — strong vision fallback]
TEXT_MODELS = [
    "Qwen/Qwen2.5-7B-Instruct:together",
    "Qwen/Qwen2.5-14B-Instruct:together",
    "Qwen/Qwen2.5-32B-Instruct:together",
    "mistralai/Mistral-7B-Instruct-v0.3:together",
    "mistralai/Mixtral-8x7B-Instruct-v0.1:together",]
def dataURL(b:bytes)->str:
    return "data:image/jpeg;base64,"+base64.b64encode(b).decode("utf-8")
def queryHFAPI(payload:dict):
    try:
        r=requests.post(ROUTER_URL,headers=HEADERS,json=payload,timouet=120)
    except requests.RequestException as error:
        return None, f"Request Failed: {error}"
    if r.status_code != 200:
        try:
            j=r.json()
            message=j.get("error",{}).get("message") or str(j)
        except Exception:
            message = (r.text or "").strip() or r.reason or "Request Failed"
        return None, f"Status {r.status_code} : {message}"
    try:
        return r.json(),None
    except Exception:
        return None,"None json respounce recived from API"
def extractText(data)->str:
    message=(data or {}).get("choice", [{}])[0].get("message",{}) or {}
    return (message.get("content") or "").strip()
def runModel(models:list[str], messages:list[dict],maxTokens:int=106,temperature:float=0.3):
    lastError=None
    for model in models:
        data, error = queryHFAPI({"model":model, "messages":messages, "max_tokens":maxTokens,"temperature":temperature})
        if error:
            lastError=error
            continue
        raw=extractText(data)
        out=re.sub(r"<think>.*?</think>","", raw, flats=re.DOTALL).strip()
        if out:
            return out, None
        lastError="Emptied Respounce from Model"
    return None, lastError or "All Models Failed"
def words(text:str)->list[str]:
    return re.findall(r"\S+",(text or "").strip())
def extractNWords(text:str,n:int)->str:
    return " ".join(words(text)[:n])
def ensureSentenceEnd(text:str)->str:
    t=(text or "").strip()
    if t and t[-1] not in ".!?":
        t+="."
    return t
def generateText(prompt:str,maxNewTokens:int=220)->str:
    messages=[{"role":"user","content":prompt}]
    out,error=runModel(TEXT_MODELS,messages=messages,maxTokens=maxNewTokens,temperature=0.5)
    if out:
        return out
    raise Exception(error or "All Text Models Failed")
def generateExactSentence(prompt:str,nWords:int,maxNewTokens:int,tries:int=6)->str:
    best=""
    for attempt in range(tries):
        enforcedPrompt=(
            f"Important: Write Exactly {nWords} Words."
            "Single Paragraph. End With A Period. No Title, No Bullets, No Extra Text. \n\n"
            +prompt)
        try:
            text=generateText(enforcedPrompt,maxNewTokens)
        except Exception as error:
            if attempt == tries-1 and not best:
                raise 
            continue
        if len(words(text))>len(words(best)):
            best=text
        if len(words(text))>=nWords:
            return ensureSentenceEnd(extractNWords(text,nWords))
    if best:
        return ensureSentenceEnd(extractNWords(text,nWords))
    raise Exception(f"Could Not Generate A {nWords}-words output after {tries} tries.")
def getBasicCaption(imagePath:str)->str:
    print(f"Generate Basic Caption")
    messages=[{
        "role":"user",
             "content":[
                {"type":"text","text":"Give a short caption for this image"},
                {"type":"image_url","image_url":{"url":dataURL(imagePath)}}
            ]
    }]
    caption,error=runModel(VISION_MODELS,messages,maxTokens=300, temperature=0.2)
    return caption if caption else f"Error: {error}"
def print_menu():
    print(f"""{Style.BRIGHT}{Fore.GREEN}
    ================ Image-to-Text Conversion =================
    Select output type:
    1. Caption (5 words)
    2. Description (30 words)
    3. Summary (50 words)
    4. Exit
    =============================================================
    """)
def main():
    # ── load & validate image ──────────────────────────────────────────────────
    image_path = input(
    f"{Fore.BLUE}Enter the path of the image (e.g., test.jpg): {Style.RESET_ALL}"
    ).strip()
    if not os.path.exists(image_path):
        print(f"{Fore.RED}❌ File not found: '{image_path}'")
        return
    try:
        Image.open(image_path).verify()
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to open image: {e}")
        return
    # ── get initial caption from vision model ─────────────────────────────────
    basic_caption = getBasicCaption(image_path)
    print(f"{Fore.YELLOW}📝 Basic caption: {Style.BRIGHT}{basic_caption}\n")
    # ── menu loop ─────────────────────────────────────────────────────────────
    while True:
        print_menu()
        choice = input(
        f"{Fore.CYAN}Enter your choice (1-4): {Style.RESET_ALL}").strip()
        # auto-retry caption if it previously errored and user picks 1-3
        if basic_caption.startswith("[Error]") and choice in {"1", "2", "3"}:
            basic_caption = getBasicCaption(image_path)
            print(f"{Fore.YELLOW}📝 Basic caption: {Style.BRIGHT}{basic_caption}\n")
        if choice == "1":
            if basic_caption.startswith("[Error]"):
                print(f"{Fore.RED}❌ Caption (5 words): {basic_caption}\n")
            else:
                out = ensureSentenceEnd(extractNWords(basic_caption, 5))
                print(f"{Fore.GREEN}✅ Caption (5 words): {Fore.YELLOW}{Style.BRIGHT}{out}\n")
        elif choice == "2":
            if basic_caption.startswith("[Error]"):
                print(f"{Fore.RED}❌ Failed to generate description: {basic_caption}")
                continue
            prompt = (
            "Rewrite as EXACTLY 30 words. Single paragraph. One complete sentence. " 
            "End with a period. No title/bullets.\n\nText: " + basic_caption)
            try:
                out = generateExactSentence(prompt, 30, max_new_tokens=220, tries=6)
                print(f"{Fore.GREEN}✅ Description (30 words): {Fore.YELLOW}{Style.BRIGHT}{out}\n")
            except Exception as e:
                print(f"{Fore.RED}❌ Failed to generate description: {e}")
        elif choice == "3":
            if basic_caption.startswith("[Error]"):
                print(f"{Fore.RED}❌ Failed to generate summary: {basic_caption}")
                continue
            prompt = (
            "Write EXACTLY 50 words. Single paragraph. One complete sentence. "
            "End with a period. No title/bullets/extra text.\n\nImage seed: " + basic_caption)
            try:
                out = generateExactSentence(prompt, 50, max_new_tokens=280, tries=7)
                print(f"{Fore.GREEN}✅ Summary (50 words): {Fore.YELLOW}{Style.BRIGHT}{out}\n")
            except Exception as e:
                print(f"{Fore.RED}❌ Failed to generate summary: {e}")
        elif choice == "4":
            print(f"{Fore.GREEN}👋 Goodbye!")
            break
        else:
            print(f"{Fore.RED}❌ Invalid choice. Please enter 1-4.")
main()