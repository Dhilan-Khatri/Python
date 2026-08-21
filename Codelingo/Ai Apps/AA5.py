from hf import generateResponse
from io import BytesIO
from huggingface_hub import InferenceClient
import streamlit as st
import requests, config
MATH_SYSTEM = """You are a Math Mastermind.
Solve with clear step-by-step reasoning, correct notation, and a final answer.
Verify when possible; mention an alternative method briefly if relevant."""
CHAT_CSS = """
<style>
.wrap {max-height: 520px; overflow-y: auto; padding-right: 6px;}
.card{border:1px solid #e6e6e6;background:#fff;border-radius:10px;padding:14px 16px;margin:10px 0;
box-shadow:0 1px 2px rgba(0,0,0,0.04);}
.q{font-weight:700;color:#0a6ebd;margin-bottom:8px;}
.meta{display:inline-block;background:#FF9800;color:#fff;padding:2px 8px;border-radius:12px;font-size:12px;margin-left:8px}
.a{white-space:pre-wrap;color:#333;line-height:1.5;}
</style>"""
negative="Low Quality, Blurry, Dispotted, Watermark, Text, Cropped."
imageClient=InferenceClient(provider="hf-inference",api_key=config.hfAPIKEY1)
def exportTxT(history):
    text="".join([f"Q{i}: {h["Question"]}\nA{i}: {h["Answer"]}\n\n" for i,h in enumerate(history,1)])
    bio=BytesIO(text.encode("utf-8"))
    bio.seek(0)
    return bio
def checkFilterAPI(prompt:str):
    try:
        response=requests.post("https://filters-zeta.vercel.app/api/filter", json={"prompt":prompt},timeout=10)
        response.raise_for_status()
        data=response.json()
        if not isinstance(data,dict):
            return {"ok":False, "Reason":"Invaild Filter API Response"}
        return data
    except Exception as e:
        return {"ok":False, "Reason":f"Filter API Error: {str(e)}"}
def teachingAnswer(q:str)->str:
    return generateResponse(q,temperature=0.3,maxToken=1024)
def mathAnswer(q:str,level:str)->str:
    prompt=f"{MATH_SYSTEM}\n\nDifficultly: {level}\nMath Problem: {q}"
    return generateResponse(prompt=prompt,temperature=0.1,maxToken=1024)
def imgAnswer(prompt:str):
    filterResult=checkFilterAPI(prompt)
    if not filterResult.get("ok"):
        return None, f"Prompt Blocked By Safety Filter{filterResult.get("reason","Unsafe Prompt")}"
    try:
        return imageClient.text_to_image(prompt=prompt,negative_prompt=negative,model="stabilityai/stable-diffusion-3-medium-diffusers"),None
    except Exception as e:
        message=str(e)
        if "negative_prompt" in message or "unexpected keyword" in message:
            try:
                return imageClient.text_to_image(prompt=prompt,model="stabilityai/stable-diffusion-3-medium-diffusers"),None
            except Exception as e2:
                message=str(e2)
        if any(x in message for x in ["402","Payment Required","pre-paidcredits"]):
            return None, "Image Backend Requires Credit Or Model Not Avaible."+message
        if "404" in message or "Not Found" in message:
            return None, "Model Not Served In This Provider"+message
        return None, "Error During Image Generation"+message
def aiTeach():
    st.title("Ai Teaching Asistance")
    st.session_state.setdefault("History_ATA",[])
    c1,c2=st.columns([1,2])
    if c1.button("Clear",key="c1_ATA"):
        st.session_state.History_ATA=[]
        st.rerun()
    if st.session_state.History_ATA:
        c2.download_button("Export History", exportTxT(st.session_state.History_ATA),"ATAhistory.txt","text/plain")
    q=st.text_area("Enter Any Question That You Might Have:", key="q_ATA", placeholder="Enter any questions about any subject. \n" \
    "   If there is a concept you find confusing, let's clear it up right now.")
    if st.button("Ask",key="a_ATA"):
        if not q.strip():
            st.warning("Enter A Question!")
        else:
            with st.spinner("Generating Answer"):
                st.session_state.History_ATA.append({"Question":q.strip(),"Answer":teachingAnswer(q.strip())})
            st.rerun()
    if not st.session_state.History_ATA:
        return
    st.markdown(CHAT_CSS, unsafe_allow_html=True)
    html="<div class='wrap'>"
    for i,qa in enumerate(st.session_state.History_ATA,1):
        html+=f"<div class='card'><div class='q'>Q{i}:{qa["Question"]}</div><div class='a'>{qa["Answer"]}</div></div>"
    st.markdown(html+"</div>",unsafe_allow_html=True)
def math():
    st.title("Math Mastermind")
    st.session_state.setdefault("History_MM",[])
    st.session_state.setdefault("k_MM",0)
    c1,c2=st.columns([1,2])
    if c1.button("Clear",key="c_MM"):
        st.session_state.History_MM=[]
        st.rerun()
    if st.session_state.History_MM:
        c2.download_button("Export History",exportTxT(st.session_state.History_MM),"MathMastermind.txt","text/plain")
    with st.form("mm_Form", clear_on_submit=True):
        q=st.text_area("Math Problem:", height=200, key=f"mm_{st.session_state.k_MM}", 
                       placeholder="Example:\n  -Algebra: 'Solve Ax^2+5x-3=0\n  -Calculus: 'Derivative of sinx^2+logx\n" \
                       "  -Probability: 'p(sum=7 with 2 dice)\n  -Geometry: 'Area of triangle (0,0),(3,4),(6,0)'\n" \
                       "  -Statistics 'Standard deviation of [10, 20, 30, 40]'\n  -Trigonometry 'Simplify tan(x) * cos(x)'")
        a,b=st.columns([3,1])
        go=a.form_submit_button("Solve",use_container_width=True)
        lvl=b.selectbox("Level", ["Basic", "Intermediate", "Advanced", "Expert"], index=1)
        if go:
            if not q.strip():
                st.warning("Enter A Problem")
            else:
                with st.spinner("Solving..."):
                    ans=mathAnswer(q.strip(),lvl)
                st.session_state.History_MM.insert(0,{"Question":q.strip(),"Answer":ans,"Level":lvl})
                st.session_state.k_MM+=1
                st.rerun()
    if not st.session_state.History_MM:
        return
    st.markdown(CHAT_CSS, unsafe_allow_html=True)
    html="<div class='wrap'>"
    for i,qa in enumerate(st.session_state.History_MM,1):
        html+=f"<div class='card'><div class='q'>Q{i}:{qa["Question"]}</div><div class='a'>{qa["Answer"]}</div></div>"
    st.markdown(html+"</div>",unsafe_allow_html=True)
def image():
    st.set_page_config(page_title="AI Image Generator", layout="centered")
    st.title("AI Image Generator")
    st.info("Flow: Enter A Prompt -> Enchance Prompt -> Check Using Deployed Safety Ai -> Generate Image")
    with st.form("image_form"):
        raw=st.text_area("Image Describtion: ", height=120, placeholder="Photorealistic close-up of a majestic red fox in a sunlit autumn forest.")
        submit=st.form_submit_button("Generate Image")
    if submit:
        raw=raw.strip()
        if not raw:
            st.warning("Please Enter A Image Describtion.")
            return
        rawCheck=checkFilterAPI(raw)
        if not rawCheck.get("ok"):
            st.error(f"Prompt Block #1 {rawCheck.get("reason", "Unsafe Prompt")}")
            return
        with st.spinner("Enchancing Your Prompt..."):
            finalPrompt=(generateResponse(f"Improve prompts for text-to-image. Return ONLY the enhanced prompt."
"Add subject, style, lighting, camera angle, background, colors. Keep it safe.\n User Prompt: {raw}", temperature=0.4, maxToken=220) or raw).strip()
        enchanceCheck=checkFilterAPI(raw)
        if not enchanceCheck.get("ok"):
            st.error(f"Prompt Block #2 {rawCheck.get("reason", "Unsafe Prompt")}")
            return
        st.markdown("Enhanced Prompt")
        st.code(finalPrompt)
        with st.spinner("Generating Image..."):
            image,error=imgAnswer(finalPrompt)
        if error:
            st.error(error)
            return
        st.image(image,caption="Generated Image", use_container_width=True)
        st.session_state.generated_image=image
    image=st.session_state.get("generated_image")
    if image:
        buffer=BytesIO()
        image.save(buffer, format="PNG")
        st.download_button("Download Image", buffer.getvalue(),"AIGeneratedImage.png","image/png")
def main():
    st.sidebar.title("Choose AI Feature")
    option=st.sidebar.selectbox("",["Teaching Assistance", "Math Mastermind", "Image Generator"])
    if option == "Teaching Assistance":
        aiTeach()
    if option == "Math Mastermind":
        math()
    if option == "Image Generator":
        image()
main()