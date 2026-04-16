import requests
from PIL import Image
from io import BytesIO
from config import hf_api8_key
model_ID= ["ByteDance/SDXL-Lightning","stabilityai/stable-diffusion-xl-base-1.0","stabilityai/sdxl-turbo","runwayml/stable-diffusion-v1-5"]
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers={"Authorization": f"Bearer{hf_api8_key}"}

def generateImage(prompt:str):
    try:    
        payload={"inputs":prompt}
        response=requests.post(API_URL,headers=headers,json=payload,timeout=30)
        response.raise_for_status()
        if 'image' in response.headers.get('Content-Type',''):
            image=Image.open(BytesIO(response.content))
            return image
        else: 
            raise Exception("Response is not an Image, Might Be error Message")
    except requests.exceptions.RequestException as error:
        raise Exception(f"Request Failed, {error}")
def main():
    print("Welcome to Text-To-Image Generator")
    print("Type 'exit' to exit.")
    while True:
        prompt=input("Enter An Discription For The Image You Want To Generate: ").strip()
        if prompt.lower() == "exit":
            print("Goodbye")
            break
        print("Generating Image")
        try:
            image=generateImage(prompt)
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