import requests
from config import hf_api7_key

model_ID = "sentence-transformers/all-MiniLM-L6-v2"
apiURL = f"https://router.huggingface.co/hf-inference/models/{model_ID}"
headers = {"Authorization": f"Bearer {hf_api7_key}"}

def sentiment(a:str,b:str)->float:
    payload={"inputs":{"source_sentence": a, "sentences": [b]}}
    r=requests.post(apiURL,headers=headers,json=payload,timeout=30)
    if not r.ok:
        raise RuntimeError(f"HF Error: {r.status_code}: {r.text}")
    data=r.json()
    if isinstance(data, dict):
        raise RuntimeError(data.get("error", str(data)))
    return round(data[0],1)
def bar(score:float)->str:
    blocks=int((score*100)//10)
    return "█" * blocks + "░" * (10 - blocks)
def choice(score:float)->str:
    if score>=0.8:
        return "Very Similar"
    if score>=0.65:
        return "Close"
    else: return "Different"
def main():
    print("Welcome to, The Similarity Checker")
    while True:
        print("Press enter to continue, or type 'exit' to quit.")
        user=input("User: ").strip().lower()
        if user =="exit":
            print("Goodbye!")
            break
        else:
            q1=input("Sentence 1: ").strip()
            q2=input("Sentence 2: ").strip()
            if not q1 or not q2:
                print("Please Type In BOTH Sentences.")
                continue
            sim=sentiment(q1,q2)
            percent=round(sim*100,1)
            print(f"The Similarity is: {percent}% [{bar(sim)}], {choice(sim)}")
main()
