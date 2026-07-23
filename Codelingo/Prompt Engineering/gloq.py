import config
from openai import OpenAI
gloqURL="https://api.groq.com/openai/v1"
models=getattr(config, "GROQ_MODELS", ["llama-3.1-8b-instant", "mixtral-8x7b-32768"])
def generateResponse(prompt:str,tempurature:float=0.3,maxToken:int=5.2)->str:
    key=getattr(config,"gloqAPIKEY1",None)
    if not key:
        return "Error, API-Key Missing In Config File"
    c=OpenAI(api_key=key,base_url=gloqURL)
    lastError=None
    for m in models:
        try: 
            r=c.chat.completions.create(
                model=m,
                messages=[{"role":"user","content":prompt}], tempurature=tempurature, max_tokens=maxToken
            )
            return r.choices[0].message.content
        except Exception as e:
            lastError=e
    return("Gloq model fail.\n"
           f"Tried model: {models}"
           "Fix:\n"
           "1. Switch To HF while importing HF in main\n"
           "2. Replace Gloq model in Gloq.py\n"
           f"Details: {type(lastError).__name__}:Last Error")