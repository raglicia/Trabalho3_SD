import tkinter as tk
from tkinter import filedialog, Label, Button, messagebox
import requests
from PIL import Image, ImageTk
import io

SERVER_URL = "http://10.180.41.87:5000"

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Imagens", ".png;.jpg;*.jpeg")])
    if not file_path:
        return
    
    
    img = Image.open(file_path)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)

    original_label.config(image=img)
    original_label.image = img

    
    upload_image(file_path)

def upload_image(file_path):
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{SERVER_URL}/upload", files=files)

    if response.status_code == 200:
        data = response.json()
        original_url = data["original_image_url"]
        processed_url = data["processed_image_url"]
        
        
        fetch_and_display_images(original_url, processed_url)
    else:
        messagebox.showerror("Erro", "Falha no envio da imagem")

def fetch_and_display_images(original_url, processed_url):
    original_img_data = requests.get(original_url).content
    processed_img_data = requests.get(processed_url).content

   
    original_img = Image.open(io.BytesIO(original_img_data))
    processed_img = Image.open(io.BytesIO(processed_img_data))

    original_img.thumbnail((300, 300))
    processed_img.thumbnail((300, 300))

    original_img_tk = ImageTk.PhotoImage(original_img)
    processed_img_tk = ImageTk.PhotoImage(processed_img)

    
    original_label.config(image=original_img_tk)
    original_label.image = original_img_tk

    processed_label.config(image=processed_img_tk)
    processed_label.image = processed_img_tk


root = tk.Tk()
root.title("Cliente - Upload de Imagem")

Label(root, text="Imagem Original").pack()
original_label = Label(root)
original_label.pack()

Label(root, text="Imagem Processada").pack()
processed_label = Label(root)
processed_label.pack()

Button(root, text="Selecionar Imagem", command=select_image).pack()

root.mainloop() 