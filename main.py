from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import PyPDF2
import io

qa_model = pipeline(model="distilbert-base-uncased-distilled-squad")

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("home.html")

@app.route('/answer', methods=['POST'])
def answer():
  pdf_file = request.files.get('pdfFile')
  text_input = request.form.get('textInput')
  question_input = request.form.get('questionInput')
  
  pdf_bytes = pdf_file.read()
  pdf_io = io.BytesIO(pdf_bytes)
  reader = PyPDF2.PdfReader(pdf_io)

  pdf_text = ''
  for i in range(len(reader.pages)):
    page = reader.pages[i]
    pdf_text += page.extract_text()

  context = pdf_text
  if text_input:
    context += text_input

  context = context.replace('\n', ' ')
  answer = qa_model(question = question_input, context = context)
  
  return jsonify(answer)

if __name__ == "__main__":
  app.run(host="0.0.0.0")