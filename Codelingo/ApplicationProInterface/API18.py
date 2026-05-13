from __future__ import annotations
from config import hf_api18_key
import requests, base64, os, re, time
from PIL import Image
from colorama import init, Fore, Style
init(autoreset=True)
ROUTER_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {hf_api18_key}", "Content-Type": "application/json"}
VISION_MODELS = [
    "google/gemma-4-31B-it:together", # Gemma 4 — multimodal, fast
    "meta-llama/Llama-3.2-11B-Vision-Instruct:together", # Llama 3.2 Vision — 11B
    "meta-llama/Llama-3.2-90B-Vision-Instruct:together", # Llama 3.2 Vision — 90B
    "moonshotai/Kimi-K2.5:together"] # Kimi — strong vision fallback]
TEXT_MODELS = [
    "Qwen/Qwen2.5-7B-Instruct:together",
    "Qwen/Qwen2.5-14B-Instruct:together",
    "Qwen/Qwen2.5-32B-Instruct:together",
    "mistralai/Mistral-7B-Instruct-v0.3:together",
    "mistralai/Mixtral-8x7B-Instruct-v0.1:together",]
def dataURL(path:str)->str:
    with open(path,"rb") as f:
        return "data:image/jpeg;base64,"+base64.b64encode(f).decode("utf-8")
def query(payload:dict):
    try:
        request=requests.post(ROUTER_URL,headers=HEADERS,json=payload,timeout=120)
    except Exception as error:
        print(f"Error: {error}")
    if request.status_code() != 200:
        try:
            j=request.json()
            errorMessage=j.get("error",{}).get("message") or str(j)
        except Exception:
            errorMessage="Request Failed"
        return f"Status {request.status_code}:{errorMessage}"
    try:
        return request.json()
    except Exception:
        return "No JSON Message From API"
def extractMessage(data)->str:
    message=(data or {}).get("choices",[{}])[0].get("message",{}) 
    return message.get("content")
def model(models:list,messages,maxTokens):
    recentError=None
    for model in models:
        data, error=query({"model":model, "messages":messages})
