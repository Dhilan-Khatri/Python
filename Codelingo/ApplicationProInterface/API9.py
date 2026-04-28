import requests
from PIL import Image
import urllib.parse
from io import BytesIO
from config import hf_api8_key
model_ID= ["ByteDance/SDXL-Lightning","stabilityai/stable-diffusion-xl-base-1.0","stabilityai/sdxl-turbo","runwayml/stable-diffusion-v1-5"]
headers={"Authorization": f"Bearer {hf_api8_key}"}

def generateImage(prompt:str, negative_prompt: str = None)->Image.Image:
    try:
        if negative_prompt:
            prompt=f"{prompt}, avoid: {negative_prompt}"
        encodedPrompt=urllib.parse.quote(prompt)
        url=f"https://image.pollinations.ai/prompt/{encodedPrompt}?width=512&height=512&nologo=true"
        response=requests.get(url,timeout=120)
        response.raise_for_status()
        image=Image.open(BytesIO(response.content))
        return image
    except requests.exceptions.RequestException as error:
        raise Exception(f"Request Failed, {error}")
def main():
    print("Welcome to Text-To-Image Generator")
    print("Type 'exit' to exit.")
    while True:
        prompt=input("Enter An Discription For The Image You Want To Generate Or Type 'exit' To Exit The Generator: ").strip()
        if prompt.lower() == "exit":
            print("Goodbye.")
            break
        if not prompt:
            print("Prompt cannot be empty please try again.")
            continue
        negativePrompt=input("Also Enter An Discription For The Image You Want To Avoid: ").strip() 
        print("Generating Image.....")
        try:
            image=generateImage(prompt,negativePrompt)
            image.show()
            saveOption=input("Do you want to keep the image? (yes/no): ").strip().lower()
            if saveOption=="yes":
                fileName=input("What is the name of Image File, without extension: ").strip() or "Generated Image"
                fileName="".join(c for c in fileName if c.isalnum()or c in ("_", "-")).rstrip()
                image.save(f"{fileName}.png")
                print(f"Image Saved As {fileName}.png")
        except Exception as error:
            print(f"An Error Happened {error}")
main()