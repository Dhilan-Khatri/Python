import requests
from config import hf_api4_key
model_ID="facebook/bart-large-mnli"
apiURL=f"https://router.huggingface.co/hf-inference/models/{model_ID}"
headers={"Authorization": f"Bearer {hf_api4_key}"}
topics = ["Spam", "Safe"]

def message(message):
    payload={"inputs":message, "parameters":{"candidate_labels":topics}}
    r=requests.post(apiURL,headers=headers,json=payload,timeout=30)
    if not r.ok:
        raise RuntimeError(f"hf Error: {r.status_code} : {r.text}")
    data=r.json()
    prediction=list(zip(data["labels"],data["scores"]))
    return sorted(prediction,key=lambda x:x[1],reverse=True)
def show(message, results):
    label, score=results[0]
    print("\n"+"="*60)
    print("Spam v Safe Classifier")
    print("="*60)
    print(f"Message: {message}")
    print(f"Classification: {label}, {round(score*100,1)}%")
    if label == "Spam":
        print(" Do Not Click Any Links Or Give Info!")
    else:
        print("Looks Safe, but Proceed With Caution.")
    print("=",*60)
def main():
    print("Welcome, enter a Message and I'll see if it is Spam or Not")
    print("Type 'exit' to Stop.")
    while True:
        text=input("Message: ").strip()
        if text.lower() == "exit":
            print("Bye!")
            break
        if not text:
            print("Please Enter A Message!")
            continue
        try:
            results=message(text)
            show(text, results)
        except Exception as error:
            print("Oops! Something Went Wrong.")
            print("Reason:",error)
            print("Tip, Check Key or Internet")
main()
