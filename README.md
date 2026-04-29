# 🤖 Groq AI Chatbot (Streamlit + LLaMA 3)

A simple and fast AI chatbot built using **Streamlit** and **Groq API**, powered by the **LLaMA 3.1 8B Instant model**.

It provides a ChatGPT-like experience with conversation memory and a clean UI.

---

## 🚀 Features

- 💬 Real-time AI chat interface
- 🧠 Conversation memory (session-based)
- ⚡ Fast responses using Groq API
- 🤖 Powered by LLaMA 3.1 8B Instant model
- 🎨 Simple and clean Streamlit UI

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🌐
- Groq API 🤖
- LLaMA 3 (Meta AI)

---

## 📸 Demo

(Add screenshot here if you want)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/hamza0972/groq-chatbot-streamlit.git
cd groq-chatbot-streamlit
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

You must set your Groq API key:

### Option 1 (Local)

```bash
export GROQ_API_KEY="your_api_key_here"
```

### Option 2 (Streamlit Cloud)

Add in `secrets.toml`:

```toml
GROQ_API_KEY = "your_api_key_here"
```

---

## 📁 Project Structure

```
groq-chatbot-streamlit/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📌 Model Used

* `llama-3.1-8b-instant` (Groq)

---

## ✨ Future Improvements

* Add chat history database (MongoDB / Firebase)
* Streaming responses (typing effect)
* User authentication
* Dark/light mode UI

---

## 👨‍💻 Author

Muhammad Hamza

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!

```
