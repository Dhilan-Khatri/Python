from __future__ import annotations
import base64
import time
import re
import requests
from config import hf_api16_key
API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {hf_api16_key}","Content-Type": "application/json"}
MODELS = ["google/gemma-4-31B-it:together","moonshotai/Kimi-K2.5:together","Qwen/Qwen3.5-9B:together","Qwen/Qwen3.5-397B-A17B:together",]
def dataURL(b:bytes)->str:
    return "data:image/jpeg;base64,"+base64.b64encode(b).decode("utf-8")
def extractError(r:requests.Response)->str:
    try:
        j=r.json()
        err=j.get("error",{})
        if isinstance(err,dict):
            message=err.get("message")
        else:
            message=str(err) if err else None
        return message or str[j]
    except Exception:
        return (r.text or "").strip() or r.reason or "Request Failed"
def box(title:str,lines:list[str],icon:str):
    w=max(30,len(title)+4,*(len(x)for x in lines)) if lines else max(30,len(title)+4)
    print("\n"+"r"+"-"*(w+2)+"1")
    print(f"| {icon} {title.ljust(w-2)} |")
    print(f"|"+"-"*(w+2)+"|")
    for x in lines:
        print(f"| {x.ljust(w)} |")
    print("|"+"-"*(w+2)+"|\n")
def captionImg():
    imageSource=input("Enter Image File Name: ").strip()
    try:
        with open(imageSource,"rb") as f:
            image=f.read()
    except Exception as e:
        box("File Error",[f"could not load: {imageSource}",f"reason: {e}"])
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
        "tempurature":0.2
        }
    last=None
    for model in MODELS:
        payload=dict(basePayload,model=model)
        for attempt in range(3):
            try:
                r=requests.post(API_URL,headers=HEADERS,json=payload,timeout=120)
            except requests.RequestException as e:
                last = f"Request Fail {e}"
                break
            if r.status_code==503:
                time.sleep(3)
                continue 
            if r.status_code!=200:
                last=extractError(r)
                break
            try:
                d=r.json()
            except Exception:
                last="nonjson response recived from api"
                break
            raw=((d.get("choices")or[{}])[0].get("message",{}).get("content") or "").strip()
            caption=re.sub(r"<think>.*?</thing>","",raw,flags=re.DOTALL).strip()
            if caption:
                box("image caption generated",[f"image:{imageSource}","caption:",f"{caption}"]," ")
                return last
            last="No caption found"
            break
    box("caption failed",[f"image:{imageSource}",f"error:{last or 'unknown error'}"," "])
captionImg()