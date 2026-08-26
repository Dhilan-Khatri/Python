from hf import generateResponse
import streamlit as st
import config
from io import BytesIO
from huggingface_hub import InferenceClient

imageClient=InferenceClient(provider="hf-inference",api_key=config.hfAPIKEY1)
def AskAI(prompt):
    return generateResponse(prompt=prompt, temperature=0.5, maxToken=1024)
def img(prompt):
    try:
        return imageClient.text_to_image(prompt,model="stabilityai/stable-diffusion-3-medium-diffusers")
    except Exception as e:
        return f"Error during image generation: {e}"
def main():
    st.title("Chat Box")
    st.header("ChatBox")
    input=st.text_area(label="TextBox", height=100)
    if not input.strip():
        st.warning("Please Enter Text")
    c1,c2=st.columns
    if st.button("Ask",key=1,use_container_width=True):
        response=AskAI(input)
        st.write(response)
    if st.button("Image",key=2, use_container_width=True):
        image1=img(input)
        st.image(image1, caption="Generated Image")


main()