import requests
from config import hf_api6_key

model_ID = ""
apiURL = f"https://router.huggingface.co/hf-inference/models/{model_ID}"
headers = {"Authorization": f"Bearer {hf_api6_key}"}

def sentiment(text):
    r = requests.post(apiURL, headers=headers, json={"inputs": text}, timeout=30)
    if not r.ok:
        raise RuntimeError(r.text)
    data = r.json()
    if isinstance(data, dict):
        raise RuntimeError(data.get("error", str(data)))
    result = data[0]
    labels = {
        "label1": "NEGATIVE",
        "label2": "NEUTRAL",
        "label3": "POSITIVE"
    }
    label = labels[result["label"]]
    score = result["score"]
    return label, score
def show(label, score):
    print(f"\nSentiment: {label}")
    print(f"Confidence: {round(score*100,1)}%")
def result(label):
    if label == "POSITIVE":
        print("This sentence is positive.")
    elif label == "NEGATIVE":
        print("This sentence is negative.")
    else:
        print("This sentence is neutral.")
def main():
    print("Sentiment Analyzer")
    print("Type a sentence and see its sentiment.")
    print("Type 'exit' to quit.\n")
    while True:
        text = input("Your Sentence: ").strip()
        if text.lower() == "exit":
            print("Bye! ")
            break
        if not text:
            continue
        try:
            label, score = sentiment(text)
            show(label, score)
            result(label)
        except Exception as e:
            print("\n Oops!", e, "\n")
main()
