# LBPH Face Recognition – “Every AI is not ML”
by [Benax Technologies](https://github.com/benax-rw)

A hands-on, **classical computer vision** project showing that *not every AI uses machine learning*.

---

## Pipeline Overview
1️⃣ **Create Dataset** – Detect, crop, and save face images  
2️⃣ **Review Dataset** – Delete poor or blurred images  
3️⃣ **Train Model** – Learn local texture patterns with LBPH  
4️⃣ **Recognize Faces** – Predict names from live webcam input  

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate     # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt