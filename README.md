# AI Personality Chatbot

An interactive AI chatbot built using Streamlit and LangChain that allows users to switch between multiple assistant personalities and chat in real time.

## Features

* Funny Assistant Mode
* Serious Assistant Mode
* Sarcastic Assistant Mode
* Real-time conversation
* Streamlit Chat UI
* Session-based chat history
* LLM integration using Groq

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* dotenv

---

## Project Structure

```plaintext
genai_main/
│
├── chatmodels/
│   └── UIchatbot.py
├── assets/
│   ├── demo.mp4
│   └── ui.png
├── .env
├── requirements.txt
├── README.md
```

---

## Demo

Project demonstration video available inside:

```plaintext
assets/demo.mp4
```

---

## Installation

Clone repository:

```bash
git clone <repo-url>
```

Move into project:

```bash
cd genai_main
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run .\chatmodels\UIchatbot.py
```

---

## Architecture

User
↓
Streamlit UI
↓
LangChain
↓
Groq API
↓
Response Generation

---

## Future Improvements

* Authentication
* Persistent chat memory
* More AI personalities
* Cloud deployment

---

## Author

Harshal
