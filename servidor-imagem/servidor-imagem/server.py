from flask import Flask, request, jsonify, send_from_directory
from PIL import Image, ImageFilter
import os
import sqlite3
import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "images"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

DB_FILE = "images.db"

def init_db():
    """Inicializa o banco de dados SQLite."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS images (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        filter TEXT,
                        timestamp TEXT)''')
    conn.commit()
    conn.close()

@app.route("/upload", methods=["POST"])
def upload_file():
    """Recebe uma imagem, aplica um filtro e retorna as URLs das imagens original e processada."""
    if "file" not in request.files:
        return jsonify({"error": "Nenhuma imagem enviada"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Nome de arquivo inválido"}), 400

    # Salva a imagem original
    original_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(original_path)

    # Aplica filtro (exemplo: Contorno)
    img = Image.open(original_path)
    filtered_img = img.filter(ImageFilter.CONTOUR)

    # Salva a imagem processada
    processed_filename = f"processed_{file.filename}"
    processed_path = os.path.join(UPLOAD_FOLDER, processed_filename)
    filtered_img.save(processed_path)

    # Salva os metadados no banco de dados
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO images (name, filter, timestamp) VALUES (?, ?, ?)", 
                   (file.filename, "CONTOUR", timestamp))
    conn.commit()
    conn.close()

    # Retorna os caminhos das imagens acessíveis pelo cliente
    return jsonify({
        "message": "Imagem processada com sucesso",
        "original_image_url": f"http://localhost:5000/images/{file.filename}",
        "processed_image_url": f"http://localhost:5000/images/{processed_filename}"
    }), 200

@app.route("/images/<filename>", methods=["GET"])
def get_image(filename):
    """Serve as imagens salvas no diretório `images/`."""
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
