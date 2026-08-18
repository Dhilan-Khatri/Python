from hf import generateResponse
import io
import streamlit as st
instructions="""
You are a math Solver. For Every Math Problem:
1. Show Step by Step Solution 
2. Explain Reasoning 
3. Give Alternate Methods If Possible
4. Verify Answer If Possible
5. Use Proper Notation
6. Break Complex Problem Into Parts
Format: Problem->Steps->Final Answer->Concept Used.
Be Consise And Educational"""
def mathGen(problem:str,level:str,temperature=0.1,maxToken=1024)->str:
    prompt=f"{instructions}\n\n Math Problem({level}):{problem}"
    return generateResponse(prompt=prompt,temperature=temperature,maxToken=maxToken)
def export(history):
    text="".join([f"Q{i}: {h["q"]}\nA{i}: {h["a"]}\n\n" for i,h in enumerate(history,1)])
    return io.BytesIO(text.encode("utf-8"))
def setup():
    st.set_page_config(page_title="Math Solver", layout="centered")
    st.title("Math Solver")
    st.write("I Can Solve Any Math Problem With Detailed Explanations.")
    with st.expander("Example"):
        st.markdown(
            "-Algebra: 'Solve Ax^2+5x-3=0\n" \
            "-Calculus: 'Derivative of sinx^2+logx\n" \
            "-Probility: 'p(sum=7 with 2 dice)\n" \
            "-Geometry: 'Area of triangle (0,0),(3,4),(6,0)'\n" \
            "-Probability: 'P(sum=7 with two dice)'")
    st.session_state.setdefault("history", [])
    st.session_state.setdefault("k", 0)
    c1,c2=st.columns([1, 2])
    if c1.button("Clear"):
        st.session_state.history=[]; st.rerun()
    if st.session_state.history:
        c2.download_button("Export", export(st.session_state.history),"mathSolverAnswer.txt", "text/plain")
    with st.form("math_form", clear_on_submit=True):
        q=st.text_area("Type your math problem:", height=100,placeholder="Example: Solve x² + 5x + 6=0",key=f"q_{st.session_state.k}")
        a,b=st.columns([3, 1])
        solve=a.form_submit_button("Solve", use_container_width=True)
        level=b.selectbox("Level", ["Beginner", "Intermediate", "Advanced", "Expert"], index=1)
        if solve:
            if not q.strip(): st.warning("Type a problem first.")
            else:
                with st.spinner("Solving Problem..."):
                    ans=mathGen(q.strip(), level)
                st.session_state.history.insert(0, {"q": q.strip(), "a": ans, "lvl": level})
                st.session_state.k += 1; st.rerun()
    if not st.session_state.history: return
    st.markdown("### 🧾 Solution History (Latest First)")
    st.markdown("""<style>
    .box{max-height:500px;overflow-y:auto;border:2px solid #4CAF50;padding:12px;background:#f7fbff;border-radius:10px}
    .q{font-weight:700;color:#2E7D32;margin-top:12px}
    .lvl{display:inline-block;background:#FF9800;color:#fff;padding:2px 8px;border-radius:12px;font-size:12px;margin-left:8px}
    .a{white-space:pre-wrap;color:#1B5E20;background:#fff;padding:10px;border-radius:8px;border-left:4px solid #4CAF50;margin:6px 0 14px}
    </style>""", unsafe_allow_html=True)
    html='<div class="box">'
    for i, h in enumerate(st.session_state.history, 1):
        html += f'<div class="q">Q{i}: {h["q"]}<span class="lvl">{h["lvl"]}</span></div>'
        html += f'<div class="a">{h["a"]}</div>'
    st.markdown(html + "</div>", unsafe_allow_html=True)

setup()
