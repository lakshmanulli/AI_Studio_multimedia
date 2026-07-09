# 🤖 AI Studio

AI Studio is an end-to-end Generative AI application built using **Google Gemini**, **Streamlit**, and **FAISS**. It provides a single interface for AI Chat, Vision, Image Generation, and Retrieval-Augmented Generation (RAG) from PDF documents.

---

# 🚀 Features

* 💬 Gemini AI Chatbot
* 👁️ Gemini Vision (Image Understanding)
* 🎨 AI Image Generator
* 📄 PDF Question Answering (RAG)
* 🌐 Streamlit Web Interface
* 📁 Upload PDF Documents
* 🖼️ Upload Images
* 💾 Local Vector Database (FAISS)
* 📥 Download Generated Images

---

# 📂 Project Structure

```text
AI-Studio/
│
├── app.py
├── config.py
├── chatbot.py
├── vision.py
├── image_generator.py
├── rag.py
├── requirements.txt
├── README.md
├── .env
│
├── uploads/
│   └── pdfs/
│
├── generated_images/
│
├── vector_db/
│
└── models/
```

---

# ⚙️ Technologies Used

| Technology    | Purpose                  |
| ------------- | ------------------------ |
| Python        | Programming Language     |
| Streamlit     | Web Application          |
| Google Gemini | Chat, Vision, Embeddings |
| FAISS         | Vector Database          |
| PyPDF         | PDF Reader               |
| Pillow        | Image Processing         |
| Requests      | HTTP Requests            |
| NumPy         | Numerical Computing      |

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/lakshmanulli/AI_Studio.git

cd AI_Studio
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
HF_TOKEN=YOUR_HUGGINGFACE_TOKEN
```

> **Note:** `HF_TOKEN` is optional if you are not using Hugging Face services.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

# 💬 Gemini Chatbot

Run from the terminal:

```bash
python chatbot.py
```

Features:

* Ask questions
* General AI conversations
* Code explanations
* Programming help

---

# 👁️ Gemini Vision

Run:

```bash
python vision.py
```

Capabilities:

* Describe images
* Image captioning
* OCR (Extract Text)
* Visual question answering

---

# 🎨 Image Generator

Run:

```bash
python image_generator.py
```

Example prompt:

```text
A futuristic AI robot working in a modern laboratory,
cinematic lighting,
ultra realistic,
8K,
highly detailed
```

Generated images are saved to:

```text
generated_images/
```

---

# 📄 RAG (PDF Question Answering)

Run:

```bash
python rag.py
```

Workflow:

1. Upload a PDF
2. Extract text
3. Split into chunks
4. Create embeddings
5. Store vectors in FAISS
6. Ask questions about the document

---

# 📚 Learning Concepts

This project demonstrates:

* Large Language Models (LLMs)
* Prompt Engineering
* Gemini API
* Computer Vision
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* Semantic Search
* Streamlit Applications

---

# 📋 Requirements

Install all required packages with:

```bash
pip install -r requirements.txt
```

---

# 📷 Screenshots

You can add screenshots of:

* Home Page
* Chatbot
* Vision
* Image Generator
* RAG PDF Interface

---

# 🛠️ Future Improvements

* Multi-PDF RAG
* Chat History
* Conversation Memory
* Local LLM Support (Ollama)
* Voice Chat
* Text-to-Speech
* Speech-to-Text
* AI Video Generation
* Authentication
* Database Integration

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Lakshman Ulli**

* GitHub: https://github.com/lakshmanulli
* LinkedIn: Add your LinkedIn profile here

---

⭐ If you found this project useful, please consider giving it a star on GitHub!
