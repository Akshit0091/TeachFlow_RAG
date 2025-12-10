# 🎓 TeachFlow-RAG

> **An AI-powered video learning assistant that converts long lectures into searchable knowledge.**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

## 🚀 How It Works

```mermaid
graph LR
    A[📹 Video] --> B[🎧 MP3]
    B --> C[📝 JSON]
    C --> D[🧠 Embeddings]
    D --> E[💾 Joblib]
    E --> F[❓ Query]
    F --> G[🔍 Search]
    G --> H[💬 LLM Answer]
    
    style A fill:#91BBDE
    style H fill:#0CE15C
```

| Step | What Happens | Tech Used |
|------|--------------|-----------|
| 1️⃣ | **Extract Audio** from videos | FFmpeg |
| 2️⃣ | **Transcribe** MP3 to text | Whisper AI |
| 3️⃣ | **Store** transcripts as JSON | Python JSON |
| 4️⃣ | **Generate** embeddings for semantic search | Sentence Transformers |
| 5️⃣ | **Save** vectors as Joblib pickle | Joblib |
| 6️⃣ | **Query** and retrieve relevant context | Vector Search |
| 7️⃣ | **Answer** questions using LLM | OpenAI / Local LLM |

---

## 📁 Project Structure

```
TeachFlow-RAG/
├── Audios/                    # Stores audio files
├── Jsons/                     # Transcribed JSON files
├── Unused/                    # Backup/unused files
├── Videos/                    # 📹 Place your lecture videos here
├── whisper-data/              # Whisper model cache
├── embeddings.joblib          # 🧠 Vector embeddings storage
├── mp3_to_json.py             # Step 3: Convert MP3 → JSON
├── preprocess_json.py         # Step 4: JSON → Embeddings
├── process_incoming.py        # Main processing pipeline
├── prompt.txt                 # LLM prompt template
├── response.txt               # Sample response output
├── video_to_mp3.py            # Step 2: Video → MP3
└── README.md                  # You are here!
```

---

## ⚡ Quick Start

<details open>
<summary><b>📦 Installation</b></summary>

```bash
# Clone the repository
git clone https://github.com/Akshit0091/TeachFlow-RAG.git
cd TeachFlow-RAG

# Install dependencies
pip install -r requirements.txt

# Install FFmpeg (if not already installed)
# Mac: brew install ffmpeg
# Linux: sudo apt install ffmpeg
# Windows: Download from https://ffmpeg.org
```

</details>

<details>
<summary><b>🎯 Usage - Step by Step</b></summary>

### Step 1: Collect Your Videos 📹
Place all your lecture video files in the `Videos/` folder.

```bash
Videos/
├── lecture1.mp4
├── lecture2.mp4
└── lecture3.mp4
```

### Step 2: Convert Videos to MP3 🎵
Run the video-to-audio conversion script:

```bash
python video_to_mp3.py
```

This will create MP3 files in the `Audios/` folder.

### Step 3: Transcribe MP3 to JSON 📝
Convert audio files to text transcriptions:

```bash
python mp3_to_json.py
```

This uses Whisper AI to generate JSON transcripts in the `Jsons/` folder.

### Step 4: Generate Embeddings 🧠
Convert JSON transcripts into vector embeddings:

```bash
python preprocess_json.py
```

This creates `embeddings.joblib` containing all vectorized data.

### Step 5: Query and Get Answers 💬
Process incoming questions and get AI-powered answers:

```bash
python process_incoming.py
```

The system will:
- Load embeddings from `embeddings.joblib`
- Search for relevant context based on your query
- Generate a prompt using `prompt.txt`
- Feed it to the LLM
- Return an accurate, context-aware answer

</details>

<details>
<summary><b>💡 Example Usage</b></summary>

```python
# Load the RAG system
from process_incoming import TeachFlowRAG

# Initialize
rag = TeachFlowRAG()

# Ask a question
question = "What is Newton's second law of motion?"
answer = rag.query(question)

print(answer)
# Output: "According to the lecture, Newton's second law states that 
# Force equals mass times acceleration (F = ma)..."
```

</details>

---

## 🛠️ Tech Stack

<table>
<tr>
<td align="center" width="20%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48" height="48" alt="Python" />
<br><b>Python</b>
</td>
<td align="center" width="20%">
<img src="https://www.gstatic.com/lamda/images/favicon_v1_150160cddff7f294ce30.svg" width="48" height="48" alt="Whisper" />
<br><b>Whisper AI</b>
</td>
<td align="center" width="20%">
🎵
<br><b>FFmpeg</b>
</td>
<td align="center" width="20%">
🧠
<br><b>Embeddings</b>
</td>
<td align="center" width="20%">
🤖
<br><b>LLM</b>
</td>
</tr>
</table>

**Core Technologies:**
- **Whisper AI** - Speech-to-text transcription
- **Sentence Transformers** - Generate semantic embeddings
- **Joblib** - Efficient storage of vector data
- **OpenAI API / Local LLM** - Generate intelligent responses
- **FFmpeg** - Video/audio processing

---

## ✨ What This Project Does

<table>
<tr>
<td width="33%" align="center">
<h3>🎥 → 📝</h3>
<b>Video to Text</b><br>
Converts lecture videos into searchable transcripts
</td>
<td width="33%" align="center">
<h3>❓ → 🎯</h3>
<b>Smart Q&A</b><br>
Ask questions, get precise answers
</td>
<td width="33%" align="center">
<h3>📚 → 💡</h3>
<b>Context-Aware</b><br>
Responses backed by actual lecture content
</td>
</tr>
</table>

### 🎯 Project Goal

> Build a simple, complete RAG-based educational assistant that helps students **study smarter, not harder**.

---

## 📊 Features Comparison

| Feature | Traditional Notes | TeachFlow-RAG |
|---------|------------------|---------------|
| Search Speed | ⏱️ Minutes | ⚡ Seconds |
| Accuracy | 📝 Manual | 🎯 AI-Powered |
| Context | ❌ Limited | ✅ Full Video |
| Updates | ❌ Manual | ✅ Automatic |
| Scalability | ❌ Time-consuming | ✅ Batch Process |

---

## 🗺️ Roadmap

- [x] Video to MP3 conversion
- [x] Whisper transcription
- [x] JSON storage
- [x] Embedding generation
- [x] RAG pipeline with LLM
- [ ] Web interface (Streamlit/Gradio)
- [ ] Multi-video support in single query
- [ ] Timestamp linking to video
- [ ] Export study notes as PDF
- [ ] Support for multiple languages

---

## 🐛 Troubleshooting

<details>
<summary><b>FFmpeg not found error</b></summary>

Install FFmpeg:
- **Mac**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org)

</details>

<details>
<summary><b>Whisper model download issues</b></summary>

Whisper models are downloaded automatically on first run. If you face issues:
```bash
# Pre-download the model
python -c "import whisper; whisper.load_model('base')"
```

</details>

<details>
<summary><b>Out of memory errors</b></summary>

- Use smaller Whisper models (`tiny`, `base` instead of `large`)
- Process videos in smaller batches
- Reduce embedding dimensions

</details>

---

### 💬 Questions? Suggestions?

**Open an issue** or **start a discussion**

[⭐ Star this repo](https://github.com/Akshit0091/TeachFlow-RAG) • [🐛 Report Bug](https://github.com/Akshit0091/TeachFlow-RAG/issues) • [✨ Request Feature](https://github.com/Akshit0091/TeachFlow-RAG/issues)

---

Made with ❤️ for learners everywhere

</div>
