from transformers import pipeline
import streamlit as st
from newspaper import Article

# --- Load Summarization Model ---
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# --- Streamlit App ---
st.set_page_config(page_title="AI News Summarizer", page_icon="📰")
st.title("📰 AI News Summarizer")
st.write("Paste any news article text or provide a news URL to get a short AI-generated summary.")

option = st.radio("Choose Input Type:", ("Paste Text", "Provide URL"))

text = ""

if option == "Paste Text":
    text = st.text_area("Paste your article text here:", height=200)

elif option == "Provide URL":
    url = st.text_input("Enter news article URL:")
    if url:
        try:
            article = Article(url)
            article.download()
            article.parse()
            text = article.text
            st.success("✅ Article successfully fetched!")
            st.text_area("Extracted Article Text:", value=text, height=200)
        except Exception as e:
            st.error(f"Error fetching article: {e}")

if st.button("Summarize"):
    if len(text.strip()) == 0:
        st.warning("⚠️ Please provide text or a valid URL.")
    else:
        st.info("⏳ Summarizing... please wait")
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        st.subheader("🧾 Summary:")
        st.write(summary[0]['summary_text'])
