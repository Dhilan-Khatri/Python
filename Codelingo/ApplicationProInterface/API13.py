import urllib.parse
import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
APIurl="https://image.pollinations.ai/prompt/{prompt}?width=768&height=768&nologo=true&model={model}"
POLLINATIONS_MODELS = ["flux", "turbo", "flux-realism"]
def generateImage(prompt:str):
    for model in POLLINATIONS_MODELS:
        url=APIurl.format(prompt=urllib.parse.quote(prompt),model=model)
        try:
            print(f"Trying Pollination[{model}]")
            response=requests.get(url,timeout=120)
            response.raise_for_status()
            if response.status_code==200 and "image" in (response.headers.get("content-type")or ""):
                image=Image.open(BytesIO(response.content)).convert("RGB")
                return image
            else:
                print(f"Skipping [{model}]: http {response.status_code}")
        except Exception as error:
            print(f"Skipping [{model}]: http {error}")
def daylight(image):
    image=ImageEnhance.Brightness(image).enhance(1.3)
    image=ImageEnhance.Contrast(image).enhance(1.1)
    image=image.filter(ImageFilter.GaussianBlur(radius=1))
    image.show()
def nightlight(image):
    image=ImageEnhance.Brightness(image).enhance(0.9)
    image=ImageEnhance.Contrast(image).enhance(1.4)
    image=image.filter(ImageFilter.GaussianBlur(radius=.5))
    image.show()
def main():
    print("Welcome To The Advanced Image Generator!")
    username=input("What is your name?: ")
    while True:
        print(f"What would you like to generate {username}? Or type 'exit' at any point to quit the Generator. ")
        prompt=input(f"{username}: ").strip()
        if prompt.lower()=="exit":
            print("Goodbye!")
            break
        else:
            print("Generating Image...")
            image=generateImage(prompt)
            choice=input(f"{username}, Would you like a Daylight or a Nightlight on your image? (d/n): ").lower().strip()
            if choice=="d":
                daylight(image)
            elif choice=="n":
                nightlight(image)
            elif choice=="exit":
                break
            else:
                continue
            saveImage=input("Do you want to save this image? (no/yes): ").strip().lower()
            if saveImage=="exit":
                break
            if saveImage=="yes":
                fileName=input(f"{username}, what is your prefered filename?: ").strip()
                image.save(f"{fileName}.png")
                print(f"Saved as {fileName}.png")
            print("-"*80)
            
main()