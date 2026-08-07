from groq import generateResponse
import re, io
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
def roles(role:str,question:str)->str:
    if role== "Teacher":
        return f"You are a teacher. Explain clearly with simple words and 3-5 points. \n{question}"
    if role == "Expert":
        return f"You are an expert. Explain with a elaborate, technical explanation with examples.\n: {question}"
    if role =="Student":
        return f"You are a fellow student. Explain simply with a short example.\n: {question}"
    else: return f"You are an Ai Teaching Assistance. Answer this question. \n{question}"
def export(history):
    text="".join([f"Q{i}: {h["question"]}\nA{i}: {h["answer"]}\n\n" for i,h in enumerate(history,1)])
    return io.BytesIO(text.encode("utf-8"))
def main():
    st.title("Ai Teaching Assistance")
    st.write("Welcome, you can ask me anything.")
    st.session_state.setdefault("history", [])

    role = st.selectbox("Select AI Role", ["Teacher", "Expert", "Student"])
    userInput = st.text_input("Enter your question here: ")
    colClear,colExport=st.columns([1,2])
    with colClear:
        if st.button("Clear History"):
            st.session_state.history=[]
            st.rerun()
    with colExport:
        if st.session_state.history:
            st.download_button(
                label="Export History",
                data=export(st.session_state.history),
                file_name="AiTeachingAssistanceHistory.txt",
                mime="text/plain")
    if st.button("Ask"):
        if userInput.strip():
            prompt = roles(role, userInput.strip())
            with st.spinner("Generating..."):
                answer = generateResponse(prompt, temperature=0.3, maxToken=1024)
            st.session_state.history.append({"role": role, "question": userInput.strip(), "answer": answer})
            st.rerun()
        else:
            st.warning("Please enter a question.")
    st.markdown("History")
    for i, h in enumerate(st.session_state.history, 1):
        st.markdown(f"You {i}: {h['question']}")
        st.markdown(f"AI {i}: {h['answer']}")
main()