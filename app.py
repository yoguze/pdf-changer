from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfMerger
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if not file1 or not file2:
        return '2つのPDFファイルを選択してください。', 400

    merger = PdfMerger()
    merger.append(file1)
    merger.append(file2)

    output = io.BytesIO()
    merger.write(output)
    merger.close()
    output.seek(0)

    return send_file(output, as_attachment=True, download_name='merged.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
