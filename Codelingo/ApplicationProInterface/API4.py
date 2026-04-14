import requests
from config import hf_api4_key
model_ID="facebook/bart-large-mnli"
apiURL=f"https://router.huggingface.co/hf-inference/models/{model_ID}"
headers={"Authorization":f"Bearer {hf_api4_key}"}
topics=["Sports", "Technology", "Business", "Politics", "Health"]

def askHF(headline:str):
    payload={"inputs":headline, "parameters":{"candidate_labels":topics}}
    r=requests.post(apiURL,headers=headers,json=payload,timeout=30)
    print(r.ok)
    print(r)
    if not r.ok:
        raise RuntimeError(f"hf Error: {r.status_code} : {r.text}")
    return r.json()
def bestTopic(prediction:list):
    best=max(prediction,key=lambda x:x["score"])
    return best["label"],best["score"]
def bar(score:float)->str:
    points=score*100
    blocks= int(points//10)
    return "█" * blocks + "░" * (10 - blocks)
def show(headline:str,prediction:list):
    topLabel,topScore=bestTopic(prediction)
    print("\n"+"=",*60)
    print("News Topic Classifier")
    print("="*60)
    print("headline:",headline)
    print(f"Best Topic: {topLabel}")
    print(f"Confidence:{round(topScore*100,1)}% [{bar(topScore)}]")
    print("Top 3 Guesses")
    top = sorted(prediction,key=lambda x:x["score"],reverse=True)[:3]
    for i,p in enumerate(top, start=1):
        print(f"{i}.{p['label']:<11}{round(p['score']*100,1)}% [{bar(p['score'])}]")
    print("="*60)
def main():
    print("Welcome, type a News Headline and I'll guess the topic.")
    print("Topics:", ", ".join(topics))
    print("Type Exit to Stop.")
    while True:
        headline=input("Headline: ").strip()
        if headline.lower() == "exit":
            print("Bye!")
            break
        if not headline:
            print("Please Type a Headline, (Not Empty).\n")
            continue
        try:
            prediction=askHF(headline)
            if isinstance(prediction, list) and prediction and "label" in prediction[0]:
                show(headline, prediction)
            else:
                print("Oops! Unexspected Reply", prediction)
        except Exception as error:
            print("Oops! Something Went Wrong.")
            print("Reason:",error)
            print("Tip, Check Key or Internet")
main()
