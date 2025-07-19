from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfMerger
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    files = request.files.getlist('pdfs')
    merger = PdfMerger()
    for f in files:
        merger.append(f)
    output = io.BytesIO()
    merger.write(output)
    output.seek(0)
    merger.close()
    return send_file(output, as_attachment=True, download_name='merged.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
