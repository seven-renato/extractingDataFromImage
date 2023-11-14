import cv2 #pip install opencv-python
# Instalar usando: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i -> se lembrar de salvar onde foi instalado
import pytesseract #pip install pytesseract
from pytesseract import Output
import pyautogui
import pygetwindow
import time
from PIL import Image
import os  # Importe a biblioteca os para manipulação de caminhos

tesseractPath = r"C:\Program Files\Tesseract-OCR" # r para o python entender que é o caminho
pytesseract.pytesseract.tesseract_cmd = tesseractPath + r"\tesseract.exe"
imagePath = "./imgs"
# Certifique-se de que o diretório existe; se não, crie-o
os.makedirs(imagePath, exist_ok=True)

titles = pygetwindow.getAllTitles()
cont = 0
while True:
    window = pygetwindow.getWindowsWithTitle("Creare Sistemas")[0]
    left, top = window.topleft
    right, bottom = window.bottomright
    screenshot_path = os.path.join(imagePath, "screenshot.png")
    pyautogui.screenshot(screenshot_path)
    im = Image.open(screenshot_path)
    im = im.crop((left, top, right, bottom))
    im.save(os.path.join(imagePath, f"screenshot_{cont}.png"))
    img = cv2.imread(f'./imgs/screenshot_{cont}.png')
    if cont > 0:
        os.remove(f'./imgs/screenshot_{cont-1}.png')
    d = pytesseract.image_to_string(img, output_type=Output.DICT)
    text = d["text"].split("\n")
    print(text[2])
    cont += 1
    time.sleep(2)


