import os, base64, requests, cv2
from io import BytesIO
from PIL import Image
from config import hf_api15_key
API_URL = "https://router.huggingface.co/hf-inference/models/Qwen/Qwen-Image-Edit"
HEADERS = {"Authorization": f"Bearer {hf_api15_key}","Content-Type": "application/json"}

def encode_image(image_bytes: bytes) -> str:
    return base64.b64encode(image_bytes).decode("utf-8")
def exist(path:str, name:str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{name} not found: {path}")
def makeHole(imagePath, maskPath)->bytes:
    img=Image.open(imagePath).convert("RGBA")
    mask=Image.open(maskPath).convert("L")
    if img.size != mask.size:
        mask=mask.resize(img.size,Image.NEAREST)
    alpha = Image.eval(mask, lambda p: 255 - p)
    r, g, b, _ = img.split()
    out = Image.merge("RGBA", (r, g, b, alpha))
    buffer = BytesIO()
    out.save(buffer, format="PNG")
    return buffer.getvalue()
def hfInPaint(prompt:str,image_bytes:bytes):
    payload = {
        "inputs": {
            "image": encode_image(image_bytes),
            "prompt": (
                prompt
                + ". Restore old photo naturally. "
                "Keep original style, lighting, and identity. "
                "Only fix damaged areas. No modern/art style.")}}
    try:
        r=requests.post(API_URL,headers=HEADERS,json=payload,timeout=120)
        if r.status_code==200:
            return Image.open(BytesIO(r.content))
        print(f"HF Failed: {r.status_code} - {r.text}")
        return None
    except Exception as e:
        print(f"HF Error: {e}")
        return None
def inPaint(image_path:str,mask_path:str)->Image.Image:
    img = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    if img is None or mask is None:
        raise Exception("Failed to load image or mask")
    h,w=img.shape[:2]
    if mask.shape[:2] != (h,w):
        mask = cv2.resize(mask, (w, h), interpolation=cv2.INTER_NEAREST)
    _,mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    return Image.fromarray(result)
def generate_inpainting_image(prompt: str, image_path: str, mask_path: str):
    exist(image_path, "Image")
    exist(mask_path, "Mask")
    print("\n Making image and  mask...")
    hole_png = makeHole(image_path, mask_path)
    print("Trying to restoration...")
    result = hfInPaint(prompt, hole_png)
    if result is None:
        print("API Failure")
        result = inPaint(image_path, mask_path)
    return result
def main():
    print("Vintage Photo Restorer")
    prompt = input("What Exactly Do You Want to Restore: ").strip()
    image_path = input("Enter Old Photo Path. (Default='old_photo.png'): ").strip() or "old_photo.png"
    mask_path = input("Enter Mask Path. (Default='old_photo_mask.png'): ").strip() or"old_photo_mask.png"
    try:
        result = generate_inpainting_image(prompt, image_path, mask_path)
        result.show()
        save = input("Do you want to save this restored image? (y/n): ").strip().lower()
        if save == "y":
            output_path = "old_photo_restored.png"
            result.save(output_path)
            print(f"Saved as '{output_path}'")
    except Exception as e:
        print(f" Error: {e}")
        
main()