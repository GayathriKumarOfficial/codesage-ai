import streamlit as st
from explainer import explain_code
from debugger import debug_code

st.set_page_config(page_title="CodeSageAI - Explain & Debug", layout="wide")
st.title("🧠 CodeSageAI - Code Explainer & Debugger")

code_input = st.text_area("Paste your code here:", height=300)

col1, col2 = st.columns(2)

with col1:
    if st.button("Explain"):
        if code_input.strip():
            explanation = explain_code(code_input)
            st.subheader("📘 Explanation")
            st.write(explanation)
        else:
            st.warning("Please paste some code first.")

with col2:
    if st.button("Debug"):
        if code_input.strip():
            debug_report = debug_code(code_input)
            st.subheader("🐞 Debug Output")
            st.write(debug_report)
        else:
            st.warning("Please paste some code first.")
