from hf import generateResponse
import io
import streamlit as st
css="""
<style>
.historywrap{max-height:420px; overflow-y:auto;padding-right:6px;}
.qacard{border:1px solid white; background:black; border-radius:10px; padding:14px 16px; margin:10px 0; box-shadow:0 1px 2px red;}
.q{font-weight:700; color:yellow; margin-bottom:8px;}
.a{white-space:pre-wrap; color:blue; line-height:1.5;}
</style>
"""
def export(history):
    text="".join([f"Q{i}: {h["Question"]}\nA{i}: {h["Answer"]}\n\n" for i,h in enumerate(history,1)])
    return io.BytesIO(text.encode("utf-8"))
def setup():
    st.set_page_config(page_title="Ai Teaching Assistance",layout="centered")
    st.title("Ai Teaching Assistance")
    st.write("Welcome, Ask Me About Various Subjects\n And I'll Provide Answers.")
    st.session_state.setdefault("History",[])
    colClear,colExport=st.columns([1,2])
    with colClear:
        if st.button("🧹 Clear Conversation"):
            st.session_state.history=[]
            st.rerun()
    with colExport:
        if st.session_state.history:
            st.download_button(
                label="Export History",
                data=export(st.session_state.history),
                file_name="AiTeachingAssistanceHistory.txt",
                mime="text/plain")
    userInput=st.text_input("Enter Your Question Here: ")
    if st.button("Ask"):
        question=userInput.strip()
        if question:
            with st.spinner("Generating..."):
                ans=generateResponse(question,0.3,1024)
            st.session_state.history.insert(0,{"Question":question,"Answer":ans})
            st.rerun()
        else:
            st.warning("Please Enter A Question")
    st.markdown("history")
    st.markdown(css,unsafe_allow_html=True)
    cards=[]
    for i,h in enumerate(st.session_state.history,1):
        cards.append(f"<div class='qacard'><div class='q'>Q{i}:{h["Question"]}</div></div>")
    st.markdown('<div class="historywrap">'+"".join(cards)+"</div>",unsafe_allow_html=True)
setup()
