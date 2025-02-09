# 📝 CV Scanner - AI-Powered Resume Analysis

🚀 **CV Scanner** is a Flask-based web application that analyzes resumes and compares them against a job description to generate a **compatibility score (0-100)**. It helps HR professionals and job seekers quickly evaluate resumes based on **keyword matching** and **readability**.

---

## ⚡ Features

- ✅ **Upload** your resume (PDF or DOCX) and input a job description.
- 🔍 **Keyword Extraction**: Extracts the most relevant keywords from the job description.
- 📊 **Resume Scoring**: Calculates a **match score (0-100)** based on keyword presence and readability.
- 📖 **Readability Score**: Uses the Flesch Reading Ease formula to evaluate clarity.
- 💡 **Insights Panel**: Displays key missing keywords and recommendations for improvement.
- 🖥 **Simple & Clean UI**: Built with **Flask** and **Bootstrap** for ease of use.

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone git@github.com:Game0verZeus/CV_SCANNER.git
cd CV_SCANNER
2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
3️⃣ Install Dependencies
bash
Copier
Modifier
pip install -r requirements.txt
🚀 Usage
1️⃣ Start the Web Application
bash
Copier
Modifier
python app.py
The application will be available at: http://127.0.0.1:5000

2️⃣ Upload a Resume & Job Description
Click "Choose File" to upload a resume in PDF or DOCX format.
Copy-paste the job description into the text area.
Click "Analyze" to get the results.
3️⃣ View Results
🎯 Match Score: How well the resume aligns with the job description.
🔑 Keywords Found/Missing: Which keywords from the job description are in the resume.
📖 Readability Score: Indicates how easy the resume is to read.
💡 Insights Panel: Displays recommendations for improving the resume.
📦 Project Structure
php
Copier
Modifier
CV_SCANNER/
│── templates/         # HTML Templates for Flask UI
│   ├── index.html     # Upload page
│   ├── results.html   # Results display page
│── static/            # (Optional) CSS/JS files for UI customization
│── app.py             # Main Flask application
│── requirements.txt   # Dependencies list
│── README.md          # This file
🏗️ Built With
Python 🐍
Flask 🖥️ (Web Framework)
PyPDF2 & python-docx 📄 (Resume text extraction)
Textstat 📖 (Readability analysis)
Bootstrap 🎨 (Responsive UI)
🤖 Future Enhancements
🔹 AI-powered insights (e.g., integrating GPT for resume feedback).
🔹 More advanced keyword analysis (synonyms, industry-specific terms).
🔹 Export results to PDF or CSV for better usability.

📜 License
This project is licensed under the MIT License – feel free to use and modify it.

🌟 Show Your Support!
If you like this project, give it a ⭐ on GitHub and feel free to contribute! 😊
