from huggingface_hub import InferenceClient
import streamlit as st

st.set_page_config(page_title="Kas AI - MCQ Generator", page_icon="🧠")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#eef2ff,#f5f3ff,#ecfeff);
}
.title {
    text-align:center;
    color:#4f46e5;
    font-size:40px;
    font-weight:bold;
}
.card {
    background:white;
    padding:20px;
    border-radius:15px;
    margin:15px 0;
    box-shadow:0 4px 15px #c7d2fe;
}
.answer {
    background:#ecfdf5;
    padding:10px;
    border-radius:10px;
    color:#047857;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧠 Kas AI</div>', unsafe_allow_html=True)
st.write("### AI-Powered MCQ Generator")

topic = st.text_input(
    "📚 Enter Topic",
    placeholder="Example: Photosynthesis"
)

col1, col2 = st.columns(2)

with col1:
    number = st.number_input("🔢 Questions", 1, 20, 5)

with col2:
    difficulty = st.selectbox(
        "🎯 Difficulty",
        ["Easy", "Medium", "Hard"]
    )

client = InferenceClient(api_key=st.secrets["token"])

if st.button("✨ Generate MCQs"):

    if not topic:
        st.warning("Please enter a topic.")
    else:

        prompt = f"""
Generate {number} {difficulty} MCQs on {topic}.
Give 4 options A-D, the correct answer and a short explanation.

Format:
Question 1: ...
A) ...
B) ...
C) ...
D) ...
Answer: ...
Explanation: ...
"""

        with st.spinner("Kas AI is generating questions..."):

            response = client.chat.completions.create(
                model="meta-llama/Llama-3.1-8B-Instruct",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=3000
            )

        st.success("MCQs generated!")

        for q in response.choices[0].message.content.split("Question ")[1:]:

            st.markdown(
                f'<div class="card"><b>Question {q}</div>',
                unsafe_allow_html=True
            )