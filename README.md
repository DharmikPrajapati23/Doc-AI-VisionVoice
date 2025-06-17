# 🧠 AI Doctor with Vision and Voice

## ⚕️ Project Overview

**AI Doctor with Vision and Voice** is a web-based application that simulates a medical consultation experience. Users can type their medical questions and optionally upload an image (e.g., of a skin condition or a general body part) for the AI Doctor to analyze. The AI leverages advanced large language models to provide a concise, human-like medical response, which is then converted into spoken audio for an interactive experience.

This project demonstrates the powerful integration of multimodal AI capabilities (**text + image input**, **text + audio output**) for a practical application.

---

## ✨ Features

- **Text-Based Questions**: Ask any health-related question by typing it into the interface.
- **Optional Image Input**: Upload an image for the AI Doctor to visually analyze.
- **Intelligent AI Responses**: Powered by **Groq's** low-latency inference (LLaMA 4).
- **Voice Output**: Converts responses into natural-sounding speech using **ElevenLabs**.
- **User-Friendly Interface**: Built with **Gradio** for an interactive experience.

---

## 🚀 Technologies Used

- **Python 3.x**
- **Gradio** – Interactive Web UI
- **Groq API** – High-speed inference with meta-llama/llama-4-maverick-17b-128e-instruct
- **ElevenLabs API** – Converts text responses into voice
- **python-dotenv** – For managing API keys securely
- **uuid** – Generates unique filenames for audio files

---

## ⚙️ Setup and Installation

### 🔧 Prerequisites

- Python 3.8+
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/DharmikPrajapati23/Doc-AI-VisionVoice.git
cd AI-Doctor-with-Vision-and-Voice
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv myenv

# On Windows
.\myenv\Scriptsctivate

# On macOS/Linux
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY="your_groq_api_key_here"
ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"
```

---

## 🏃 How to Run

```bash
python app.py
```

---

## 📂 Project Structure

```
AI-Doctor-with-Vision-and-Voice/
│
├── brain_of_the_doctor.py     # Groq API logic: image encoding, response generation
├── voice_of_the_doctor.py     # ElevenLabs voice synthesis
├── app.py                     # Gradio interface setup
├── .env                       # Environment variables (not committed)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
