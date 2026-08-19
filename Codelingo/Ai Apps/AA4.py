from groq import generateResponse
from io import BytesIO
from huggingface_hub import InferenceClient
import streamlit as st
import requests, config

MODEL_ID = "stabilityai/stable-diffusion-3-medium-diffusers"
FILTER_API_URL = "https://filters-zeta.vercel.app/api/filter"
ENHANCE_SYS = ("Improve prompts for text-to-image. Return ONLY the enhanced prompt."
"Add subject, style, lighting, camera angle, background, colors. Keep it safe.")
negative="Low Quality, Blurry, Dispotted, Watermark, Text, Cropped."
imageClient=InferenceClient(provider="hf-inference",api_key=config.hfAPIKEY1)

def checkFilterAPI(prompt:str):
    try:
        response=requests.post(FILTER_API_URL, json={"prompt":prompt},timeout=10)
        response.raise_for_status()
        data=response.json()
        if not isinstance(data,dict):
            return {"ok":False, "Reason":"Invaild Filter API Response"}
        return data
    except Exception as e:
        return {"ok":False, "Reason":f"Filter API Error: {str(e)}"}
def enchancePrompt(raw:str)->str:
    out=generateResponse(f"{ENHANCE_SYS}\n User Prompt: {raw}", temperature=0.4, maxToken=220)
    return (out or raw).strip()
def generateImage(prompt:str):
    filterResult=checkFilterAPI(prompt)
    if not filterResult.get("ok"):
        return None, f"Prompt Blocked By Safety Filter{filterResult.get("reason","Unsafe Prompt")}"
    try:
        return imageClient.text_to_image(prompt=prompt,negative_prompt=negative,model=MODEL_ID),None
    except Exception as e:
        message=str(e)
        if "negative_prompt" in message or "unexpected keyword" in message:
            try:
                return imageClient.text_to_image(prompt=prompt,model=MODEL_ID),None
            except Exception as e2:
                message=str(e2)
            if any(x in message for x in ["402","Payment Required","pre-paidcredits"]):
                return None, "Image Backend Requires Credit Or Model Not Avaible."+message
            if "404" in message or "Not Found" in message:
                return None, "Model Not Served In This Provider"+message
            return None, "Error During Image Generation"+message
def main():
    st.set_page_config(page_title="AI Image Generator", layout="centered")
    st.title("AI Image Generator")
    st.info("Flow: Enter A Prompt -> Enchance Prompt -> Check Using Deployed Safety Ai -> Generate Image")
    with st.form("image_form"):
        raw=st.text_area("Image Describtion: ", height=120, placeholder="Example: Cabin in snowy mountains.")
        submit=st.form_submit_button("Generate Image")
    if submit:
        raw=raw.strip()
        if not raw:
            st.warning("Please Enter A Image Describtion.")
            return
        rawCheck=checkFilterAPI(raw)
        if not rawCheck.get("ok"):
            st.error(f"Prompt Block {rawCheck.get("reason", "Unsafe Prompt")}")
            return
        with st.spinner("Enchancing Your Prompt..."):
            finalPrompt=enchancePrompt(raw)
        enchanceCheck=checkFilterAPI(finalPrompt)
        if not enchanceCheck.get("ok"):
            st.error(f"Prompt Block {rawCheck.get("reason", "Unsafe Prompt")}")
            return
        st.markdown("Enhanced Prompt")
        st.code(finalPrompt)
        with st.spinner("Generating Image..."):
            image,error=generateImage(finalPrompt)
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
main()