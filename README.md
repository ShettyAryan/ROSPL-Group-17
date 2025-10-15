<h1 align="center">📰 ROSPL Project – Group 17</h1>
<h2 align="center">AI News Summarizer</h2>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?logo=python" alt="Python Badge">
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit" alt="Streamlit Badge">
  <img src="https://img.shields.io/badge/Model-BART--Large--CNN-yellow?logo=huggingface" alt="BART Badge">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License Badge">
</p>

---

### 📘 About the Project
The **AI News Summarizer** is an open-source project developed as part of the **ROSPL (Reports on Open Source Projects and Libraries)** subject for **Semester 7, Mumbai University**.  

This project leverages the power of **Natural Language Processing (NLP)** and **Transformer models** to automatically summarize lengthy online news articles into concise and readable paragraphs.  
It uses **Hugging Face Transformers** for summarization and **Streamlit** for an interactive and minimal web interface.

---

### 🚀 Features
✅ **Automatic News Extraction** – Fetches full article text from a URL using Newspaper3k.  
✅ **AI-Powered Summarization** – Uses the `facebook/bart-large-cnn` model for high-quality summaries.  
✅ **Interactive UI** – Built with Streamlit for easy use.  
✅ **Side-by-Side Comparison** – View both the original and summarized versions.  
✅ **Open Source** – Built entirely using free, open-source tools.

---

### 🍵Grouo Members
| Name | Details |
|----------|----------|
| **Aryan Shetty** | BE IT2 36 |
| **yash Surve** | BE IT2 43 |
| **Vedant Reddy** | BE IT2 21 |
| **Shivam Wadkar** | BE IT2 54 |


---

### 🧩 Tech Stack
| Component | Technology Used |
|------------|-----------------|
| **Frontend / UI** | Streamlit |
| **Backend / AI Model** | Hugging Face Transformers |
| **ML Framework** | PyTorch |
| **Article Extraction** | Newspaper3k |
| **Language** | Python |
| **Version Control** | Git & GitHub |

---

### 🧰 Open Source Libraries Used
| Library | Purpose |
|----------|----------|
| **Streamlit** | To create a simple and interactive frontend. |
| **Newspaper3k** | To scrape and extract clean news article text. |
| **Transformers (Hugging Face)** | To load and use pre-trained summarization models. |
| **Torch (PyTorch)** | Backend deep learning framework powering the model. |
| **lxml_html_clean** | For safe HTML parsing and cleaning. |

---

### ⚙️ Installation & Setup

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShettyAryan/ROSPL-Group-17.git
cd ROSPL-Group-17
```
#### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
#### 3️⃣ Activate Virtual Environment
```bash
venv\Scripts\activate
```

#### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 5️⃣ Run the application
```bash
streamlit run app.py
```

