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
def main():
    st.title("Ai Teaching Assistance")
    st.write("Welcome, you can ask me anything.")
    st.session_state.setdefault("conversation", [])
    role = st.selectbox("Select AI Role", ["Teacher", "Expert", "Student"])
    user_input = st.text_input("Enter your question here: ")
    c1, c2 = st.columns([1, 1])
    with c1:
        ask = st.button("Ask")
    with c2:
        clear = st.button("Clear History")
    if ask:
        if user_input.strip():
            prompt = roles(role, user_input.strip())
            with st.spinner("Generating..."):
                answer = generateResponse(prompt, temperature=0.3, max_tokens=1024)
            st.session_state.conversation.append({"role": role, "question": user_input.strip(), "answer": answer})
            st.rerun()
        else:
            st.warning("Please enter a question.")
    if clear:
        st.session_state.conversation = []
        st.rerun()
    if st.session_state.conversation:
        export_text = ""
        for i, chat in enumerate(st.session_state.conversation, 1):
            export_text += f"Q{i} ({chat['role']}): {chat['question']}\nA{i}: {chat['answer']}\n\n"
        st.download_button(
            "Export History",
            io.BytesIO(export_text.encode("utf-8")),
            "AITeachingAssistantConversation.txt",
            "text/plain",)
        st.markdown("History")
        for i, chat in enumerate(st.session_state.conversation, 1):
            st.markdown(f"You: {chat['question']}")
            st.markdown(f"AI ({chat['role']}): {chat['answer']}")
main()
