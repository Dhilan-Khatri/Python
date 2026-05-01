import requests, os,io,time,random,mimetypes
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime
from config import hf_api14_key
MODEL = "facebook/detr-resnet-101"
API = f"https://router.huggingface.co/hf-inference/models/{MODEL}"
ALLOWED, MAX_MB = {".jpg",".jpeg",".png",".bmp",".gif",".webp",".tiff"}, 8
EMOJI = {"person":"🧍","car":"🚗","truck":"🚚","bus":"🚌","bicycle":"🚲","motorcycle":"🏍️","dog":"🐶","cat":"🐱",
"bird":"🐦","horse":"🐴","sheep":"🐑","cow":"🐮","bear":"🐻","giraffe":"🦒","zebra":"🦓","banana":"🍌",
"apple":"🍎","orange":"🍊","pizza":"🍕","broccoli":"🥦","book":"📘","laptop":"💻","tv":"📺","bottle":"🧴","cup":"🥤"}

def font(size=13):
    for i in ("Arial.ttf", "DejaVuSense.ttf"):
        try: 
            return ImageFont.truetype(i,size)
        except:
            pass 
    return ImageFont.load_default()
def askImage():
    print(f"Pick an image (.jpg,.png,.WeBP,.BMP,.IFF, <=8MP). From this folder.")
    while True:
        p=input(f"Input Path: ").strip()
        if not p or not os.path.isfile(p):
            print(f"File Not Found")
            continue
        if os.path.splitext(p)[1].lower() not in ALLOWED:
            print(f"Unsupported Type")
            continue
        if os.path.get (p)/(1024*1024) > MAX_MB:
            print(f"Image Size To Big")
            continue
        try:
            Image.open(p).verify()
        except:
            print(f"Corrupt File")
            continue
        return p
def info(path, imageBytes, tries=8):
    m,_=mimetypes.guess_type(path)
    for _ in range(tries):
        if m and m.startswith("image/"):
            r=requests.post(API,headers={"Authorization":f"Bearer {hf_api14_key}","Content-Type":m}, data=imageBytes, timeout=60)
        else:
            r=requests.post(API,headers={"Authorization":f"Bearer {hf_api14_key}","Content-Type":m}, files={"inputs":(os.path.basename(path),imageBytes,"application/octet-stream")},timeout=60)
        if r.status_code==200:
            d=r.json()
            if isinstance(d,dict)and"error" in d:
                raise RuntimeError(d["error"])
            if not isinstance(d,list): raise RuntimeError("Bad API Response")
            return d
        if r.status_code==503: time.sleep(2); continue
        raise RuntimeError(f"API {r.status_code}:{r.text[:300]}")
    raise RuntimeError("Model Warm Up Timeout")
def draw(image, details, threshold=0.5):
    data=ImageDraw.Draw(image); f=font(18); count={}
    for de in details[:50]:
        s=float(de.get("score", 0))
        if s < threshold:
            continue
        lab = de.get("label","object");b=de.get("box",{})
        x1,y1,x2,y2=(int(b.get(k,0)))
        for k in ("xmin","ymin","xmax","ymax"):
            if not (x2>0 and y2>0):
                x,y,w,h=int(b.get("x",0)),int(b.get("y",0)),int(b.get("w",0)),int(b.get("h",0))
                x1,y1,x2,y2=x,y,x+w,y+h
            color=tuple(random.randint(80,255)for _ in range(3))
            data.rectangle([(x1,y1),(x2,y2)],outline=color,width=4)
            text=f"{EMOJI.get(lab.lower())} {lab} {s*100:.0f%}"
            tw,th=data.textlength(text,font=f),f.size+6
            data.rectangle([(x1,max(0,y1-th)),(x1+tw+8),y1], fill=color)
            data.text((x1+4,y1-th+3),text,font=f,fill=(0,0,0))
            count[lab]=count.get(lab,0)+1
        return count
def main():
    path = askImage()
    with open(path,"rb") as fh: by = fh.read()
    try: dets = info(path, by)
    except Exception as e: return print("❌", e)
    img = Image.open(io.BytesIO(by)).convert("RGB")
    counts = draw(img, dets, thr=0.5)
    out = f"annotated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    img.save(out); print(f"✅ Saved: {out}")
    if counts:
        print("🎉 I found:");
        for k,v in sorted(counts.items(), key=lambda kv:(-kv[1],kv[0])):
            print(f" • {EMOJI.get(k.lower(),'✨')} {k}: {v}")
        else:
            print("🤔 No confident detections—try a clearer or busier scene!")
            print("\n⚠️ Disclaimer: This is an AI model demo. " "Detections may not always be accurate or complete. " "Use it for fun and learning, not for safety-critical decisions.")