from flask import Flask, render_template, request, redirect, url_for, flash
import os
import re
from collections import Counter
import PyPDF2
import docx
import textstat

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'  # Remplacez par votre propre clé secrète

# Extensions de fichiers autorisés
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- Fonctions d'extraction de texte ---
def extract_text_from_pdf(file_stream):
    text = ""
    try:
        reader = PyPDF2.PdfReader(file_stream)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print("Erreur lors de la lecture du PDF:", e)
    return text

def extract_text_from_docx(file_stream):
    text = ""
    try:
        document = docx.Document(file_stream)
        text = "\n".join([para.text for para in document.paragraphs])
    except Exception as e:
        print("Erreur lors de la lecture du DOCX:", e)
    return text

def extract_resume_text(file):
    filename = file.filename.lower()
    if filename.endswith('.pdf'):
        return extract_text_from_pdf(file)
    elif filename.endswith('.docx'):
        return extract_text_from_docx(file)
    else:
        return ""

# --- Extraction des mots-clés à partir de la description de poste ---
def extract_keywords(job_description, max_keywords=10):
    # Extraction simple basée sur la fréquence des mots (sans API externe)
    words = re.findall(r'\b\w+\b', job_description.lower())
    stopwords = set([
        "le", "la", "les", "un", "une", "de", "des", "et", "ou", "à", "en", "pour", "dans",
        "du", "au", "aux", "ce", "cet", "cette", "ces", "est", "sont", "qui", "que", "quoi", "avec"
    ])
    filtered = [word for word in words if word not in stopwords and len(word) > 3]
    counter = Counter(filtered)
    most_common = [word for word, count in counter.most_common(max_keywords)]
    return most_common

# --- Correspondance des mots-clés ---
def match_keywords(resume_text, keywords):
    resume_text_lower = resume_text.lower()
    matched = []
    missing = []
    for kw in keywords:
        if re.search(r'\b' + re.escape(kw) + r'\b', resume_text_lower):
            matched.append(kw)
        else:
            missing.append(kw)
    return matched, missing

# --- Calcul du score de lisibilité ---
def compute_readability(text):
    try:
        score = textstat.flesch_reading_ease(text)
        # On s'assure que le score reste entre 0 et 100
        score = max(min(score, 100), 0)
        return score
    except Exception as e:
        print("Erreur lors du calcul de la lisibilité:", e)
        return 0

# --- Calcul du score global (80% correspondance des mots-clés, 20% lisibilité) ---
def compute_overall_score(keyword_match_score, readability_score):
    return round(keyword_match_score * 0.8 + readability_score * 0.2, 2)

# --- Route principale ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Vérifier si le fichier a été envoyé
        if 'resume' not in request.files:
            flash("Aucun fichier n'a été sélectionné.")
            return redirect(request.url)
        file = request.files['resume']
        if file.filename == '':
            flash("Aucun fichier n'a été sélectionné.")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            resume_text = extract_resume_text(file)
            if not resume_text.strip():
                flash("Impossible d'extraire le texte du CV.")
                return redirect(request.url)
            # Récupérer la description de poste depuis le formulaire
            job_description = request.form.get('job_description', '')
            if not job_description.strip():
                flash("Veuillez fournir une description de poste.")
                return redirect(request.url)
            
            # Traitement de la description pour extraire les mots-clés
            keywords = extract_keywords(job_description)
            matched, missing = match_keywords(resume_text, keywords)
            keyword_match_score = (len(matched) / len(keywords)) * 100 if keywords else 0
            
            readability_score = compute_readability(resume_text)
            overall_score = compute_overall_score(keyword_match_score, readability_score)
            
            # Insights de base sans API externe
            insights = "Aucun insight supplémentaire n'est disponible dans cette version."
            
            results = {
                "overall_score": overall_score,
                "keyword_match_score": round(keyword_match_score, 2),
                "readability_score": round(readability_score, 2),
                "keywords": keywords,
                "matched_keywords": matched,
                "missing_keywords": missing,
                "insights": insights,
            }
            
            return render_template('results.html', results=results)
        else:
            flash("Format de fichier non supporté. Seuls les fichiers PDF et DOCX sont autorisés.")
            return redirect(request.url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
