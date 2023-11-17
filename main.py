import os
import subprocess
import sys
def install_dependencies():
    try:
        import cv2
        import pytesseract
        import pyautogui
        import pygetwindow
        from PIL import Image
    except ImportError as e:
        print(f"Biblioteca {e.name} não encontrada. Instalando...")
        if e.name == "cv2":
            e.name = "opencv-python"
        subprocess.check_call([sys.executable, "-m", "pip", "install", e.name])

install_dependencies()

import pyautogui
import pygetwindow
from PIL import Image
import cv2
import pytesseract
from pytesseract import Output

def find_tesseract():
    try:
        # Tenta encontrar o Tesseract no PATH do sistema
        subprocess.run(["tesseract", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return "tesseract"
    except FileNotFoundError:
        pass

    # Se não encontrado no PATH, procura em locais comuns
    common_paths = [
        "/usr/bin/tesseract",                   # Linux
        "/usr/local/bin/tesseract",             # Linux
        "/opt/local/bin/tesseract",             # macOS (MacPorts)
        "/usr/local/Cellar/tesseract/*/bin/tesseract",  # macOS (Homebrew)
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",  # Windows
        r"C:\Users\user\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    ]

    for path in common_paths:
        if os.path.exists(path):
            return path

    return None

# Obtém o caminho do Tesseract OCR
tesseract_cmd = find_tesseract()

if tesseract_cmd is None:
    print("Tesseract OCR não encontrado. Instalação manual necessária.")
    tesseract_cmd = input("Insira o caminho o qual você utilizou para instalar o Tesseract OCR: ")
    tesseract_cmd = r"{}".format(tesseract_cmd)
    if "tesseract.exe" not in tesseract_cmd:
        tesseract_cmd = tesseract_cmd + r"\tesseract.exe"
# Define o caminho do Tesseract para uso com pytesseract
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
# Certificar se o diretório existe; se não, crie-o
imagePath = "./imgs"
os.makedirs(imagePath, exist_ok=True)
# Pegar o título de todas as janelas
titles = pygetwindow.getAllTitles()
print(titles)

title = input("Insira o título da janela a qual quer extrair os dados (escreva **exatamente** como está escrito): ")
cont = 0 
string = ""
print("\nExecutando...\nPressione 'cntrl + c' para terminar a execução.")
try:
    while True:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        left, top = window.topleft
        right, bottom = window.bottomright

        screenshot_path = os.path.join(imagePath, f"screenshot_{cont}.png")
        pyautogui.screenshot(screenshot_path)

        im = Image.open(screenshot_path)
        im = im.crop((left, top, right, bottom))
        im.save(screenshot_path)

        img = cv2.imread(screenshot_path)
        
        if cont > 0:
            os.remove(os.path.join(imagePath, f"screenshot_{cont-1}.png"))

        d = pytesseract.image_to_string(img, output_type=Output.DICT)
        text = d["text"]
        string += text + "\n"

        cont += 1
except KeyboardInterrupt:
    pass

# Grava a string no arquivo CSV
with open("resultado.csv", "w") as arq:
    arq.write(string)
