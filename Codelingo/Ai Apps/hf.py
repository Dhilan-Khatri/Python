import config
from huggingface_hub import InferenceClient
models=getattr(config, "HF_MODELS", ["meta-llama/Llama-3.1-8B-Instruct"])
def generateResponse(prompt:str,temperature:float=0.3,maxToken:int=512)->str:
    key=getattr(config,"hfAPIKEY1",None)
    if not key:
        return "Error, API-Key Missing In Config File"
    lastError=None
    for m in models:
        try: 
            c=InferenceClient(model=m,token=key)
            r=c.chat.completions.create(
                            model=m,
                            messages=[{"role":"user","content":prompt}], temperature=temperature, max_tokens=maxToken
                        )
            return r.choices[0].message.content
        except Exception as e:
            lastError=e
    return("Hugging Face model fail.\n"
           f"Tried model: {models}"
           "Fix:\n"
           "1. Switch To Groq while importing Groq in main\n"
           "2. Replace HF model in HF.py\n"
           f"Details: {type(lastError).__name__}:{lastError}")