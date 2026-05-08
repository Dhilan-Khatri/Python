import os, base64, requests, time, re
from config import hf_api17_key
API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {hf_api17_key}","Content-Type": "application/json"}
MODELS = ["Qwen/Qwen3-VL-8B-Instruct:together",
    "Qwen/Qwen3-VL-32B-Instruct:together",
    "Qwen/Qwen2.5-VL-32B-Instruct:together",
    "Qwen/Qwen2-VL-7B-Instruct:together"]
def dataURL(b:bytes)-> str:
    return "data:image/jpeg;base64," + base64.b64encode(b).decode("utf-8")
def error(r:requests.Response)->str:
    try:
        er=r.json()
        return er.get("error",{}).get("message") or str(er)
    except Exception:
        return (r.text or "").strip() or r.reason or "Request Failed"
def box(title:str,lines:list[str],icon:str):
    w=max(30,len(title)+4,*(len(x)for x in lines)) if lines else max(30,len(title)+4)
    print("\n+" + "-"*(w+2) + "+")
    print(f"| {icon} {title.ljust(w-2)} |")
    print(f"|"+"-"*(w+2)+"|")
    for x in lines:
        print(f"| {x.ljust(w)} |")
    print("|"+"-"*(w+2)+"|\n")
def caption(imgFile): 
    try:
        with open(imgFile,"rb") as f:
            image=f.read()
    except Exception as e:
        box("File Error",[f"could not load: {imgFile}",f"reason: {e}", " "])
        return
    basePayload={
        "messages":[{
            "role":"user",
            "content":[
                {"type":"text","text":"Give a short caption for this image"},
                {"type":"image_url","image_url":{"url":dataURL(image)}},
            ],
        }],
        "max_tokens":512,
        "temperature":0.2
        }
    last=None
    for model in MODELS:
        payload=dict(basePayload,model=model)
        try:
            r=requests.post(API_URL,headers=HEADERS,json=payload,timeout=120)
        except requests.RequestException as e:
            last = f"Request Fail {e}"
            break
        if r.status_code==503:
            time.sleep(3)
            continue 
        if r.status_code!=200:
            last=error(r)
            break
        try:
            d=r.json()
        except Exception:
            last="nonjson response recived from api"
            break
        raw=((d.get("choices")or[{}])[0].get("message",{}).get("content") or "").strip()
        cCaption = re.sub(r"<think>.*?</think>","",raw,flags=re.DOTALL).strip()
        if cCaption:
            box("image caption generated",[f"image:{imgFile}","caption:",f"{cCaption}"]," ")
            return cCaption, None
        last="No caption found"
        break
    box("caption failed",[f"image:{imgFile}", f"error:{last or 'unknown error'}"]," ")
    return None, last
def main():
    folder_path = input("Paste the path to your images: ").strip() or "images"
    if not os.path.isdir(folder_path):
        print(f"'{folder_path}' does not exist.")
        return
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not image_files:
        print(f"No valid image files found in, '{folder_path}'.")
        return
    captions = []
    for img_name in image_files:
        img_path = os.path.join(folder_path, img_name)
        print(f"\nProcessing; {img_path}")
        cap, err = caption(img_path)
        if err:
            print(f"[API Error] {err} for '{img_name}'")
            continue
        print(f"The caption is: {cap}")
        captions.append((img_name, cap))
    if captions:
        summary_file = os.path.join(folder_path, "captionsSummary.txt")
        with open(summary_file, "w", encoding="utf-8") as sf:
            for img_name, img_caption in captions:
                sf.write(f"{img_name}: {img_caption}\n")
        print(f"\nAll captions will be saved to, {summary_file}")
    else:
        print("\nPlease check for errors or try different images.")

main()