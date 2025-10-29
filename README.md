# 🧠 AI Doctor with Vision and Voice

## ⚕️ Project Overview

**AI Doctor with Vision and Voice** is a web-based application that simulates a medical consultation experience. Users can type their medical questions and optionally upload an image (e.g., of a skin condition or a general body part) for the AI Doctor to analyze. The AI leverages advanced large language models to provide a concise, human-like medical response, which is then converted into spoken audio for an interactive experience.

This project demonstrates the powerful integration of multimodal AI capabilities (**text + image input**, **text + audio output**) for a practical application.

---
## Working Project

https://github.com/user-attachments/assets/dc1af2ae-8177-486c-8e6d-d4d01c4c91fc

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

---


## 🧠 Model Details

This project uses the **Llama 4 Maverick (Meta)**—a cutting-edge multimodal model designed for state-of-the-art understanding of both text and images. Llama 4 Maverick allows the AI Doctor to interpret patient questions along with uploaded images, enabling deeper, context-aware medical responses. This model was selected after comparing current multimodal solutions for healthcare and AI chatbot tasks.

---

### 🤖 Why Llama 4 Maverick?

- **Multimodal Capability:** Processes both text and image inputs together for rich, contextually relevant answers.
- **Performance:** Consistently outperforms most open-source models in handling medical Q&A and image-based reasoning.
- **Scalability:** Large context window (up to 1,000,000 tokens) for understanding complex medical cases.
- **Integration:** Fully supported with APIs (Groq, HuggingFace) and easy to connect via Gradio.
- **Open Source:** Cost-effective and supports academic/production use.

---

### 🏆 Model Comparison

| Feature                      | Llama 4 Maverick (Meta)      | GLM-4.5V (Zhipu AI)         | Medical VLM-24B (John Snow Labs)  |
|------------------------------|------------------------------|-----------------------------|-----------------------------------|
| Multimodal (Text + Image)    | Yes                          | Yes                         | Yes                               |
| Context Window               | 1,000,000 tokens             | 131,072 tokens              | 65,000 tokens                     |
| Medical Specialization       | General + Reasoning          | Imaging + Diagnostics       | Clinical Report Generation        |
| Performance                  | Excellent (General, VQA, QA) | Strong (Imaging tasks)      | Best for Radiology/Clinical Tasks |
| Inference Speed/Scalability  | Very High                    | Moderate                    | High                              |
| Open Source                  | Yes                          | Yes                         | Yes                               |
| Cost Efficiency              | High                         | Moderate                    | Moderate                          |

*Llama 4 Maverick was chosen because it balances vision-language power, speed, easy integration, and cost, making it ideal for quickly building robust, scalable health-AI applications.*


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
