from groq import generateResponse
import re 
import streamlit as st
def incompleteness(text:str)->bool:
    if not text or len(text.strip())<10:
        return True
    t=text.strip()
    if t.endswith(("**","*","-","--",":",",","(","[","{")):
        return True
    if re.search(r"\d+\.\s*\*\*$",t):
        return True
    if not re.search(r"[.!?]\s*$",t):
        return True
    return False
def completeAns(question:str,maxRounds:int=2)->str:
    basePrompt=(
        "Answer Clearly In Numbered Points."
        "Do Not Cut Sentences Finish Each Point Fully\n\n"
        f"Question: {question}")
    answer=generateResponse(basePrompt, 0.3, 1024)
    rounds=0
    while rounds<maxRounds and incompleteness(answer):
        conPrompt=(
            "Continue Exactly Of Where You Stoped."
            "Do Not Repeat Earlier Text."
            "Finish The Incomplete Points And Then Complete Answer\n\n"
            f"Question: {question}\n\n"
            f"Answer So Far:\n {answer}\n\n continue")
        morAnswer=generateResponse(conPrompt,0.3,1024)
        if not morAnswer or morAnswer.strip() in answer:
            break
        answer=(answer.rstrip()+"\n"+morAnswer.lstrip()).strip()
        round=round+1
    return answer
def main():
    st.title("Ai Teaching Assistance")
    st.write("Welcome, you can ask me anything.")
    input=st.text_input("Enter Your Question: ").strip()
    if input:
        st.write(f"Your Question: {input}")
        response=completeAns(input)
        st.write("Ai Answer: ")
        st.markdown(response)
    else:
        st.info("Please enter a question to ask.")
main()