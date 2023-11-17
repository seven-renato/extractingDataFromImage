# pip install opencv-python pytesseract pyautogui pygetwindow Pillow
import cv2
import pytesseract
from pytesseract import Output
import pyautogui
import pygetwindow
import time
from PIL import Image
import os
import re

# Instalar tesseract usando: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i -> se lembrar de salvar onde foi instalado
tesseractPath = r"C:\Users\user\AppData\Local\Programs\Tesseract-OCR" # r para o python entender que é o caminho
pytesseract.pytesseract.tesseract_cmd = tesseractPath + r"\tesseract.exe"
# Certifique-se de que o diretório existe; se não, crie-o
def tem_numero(string):
    for caractere in string:
        if caractere.isdigit():
            return True
    return False
def criar_dicionario(string):
    # Substituir "oOo" por uma quebra de linha para facilitar a separação
    string = string.split("M")[1:]
    dicionario = {}
    vet = []
    for linha in string:
        if tem_numero(linha):
           vet.append(linha.split(":")) 
    madeiras = ["M"+string[0][:-2]]
    madeiras.append("M"+vet[0][0])
    madeiras.append("M"+string[2][:-2])
    madeiras.append("M"+vet[1][0])
    quantidade = vet[0][1].split(" ") + vet[1][1].split(" ")
    index = 0
    for madeira in madeiras:
        if index == 0:
            dicionario[madeira.split(' ')[1]] = quantidade[index]
        else:
            dicionario[madeira.split(' ')[2]] = quantidade[index]
        index += 1
    return dicionario

imagePath = "./imgs"
os.makedirs(imagePath, exist_ok=True)
titles = pygetwindow.getAllTitles()
print(titles)
title = "Creare-Sistemas-Agrolog"
cont = 0
string = ""
contador = 0
while contador < 5:
    window = pygetwindow.getWindowsWithTitle(title)[0]
    left, top = window.topleft
    right, bottom = window.bottomright
    screenshot_path = os.path.join(imagePath, "screenshot.png")
    pyautogui.screenshot(screenshot_path)
    im = Image.open(screenshot_path)
    im = im.crop((left, top, right-466, bottom-100))
    im.save(os.path.join(imagePath, f"screenshot_{cont}.png"))
    img = cv2.imread(f'./imgs/screenshot_{cont}.png')
    if cont > 0:
        os.remove(f'./imgs/screenshot_{cont-1}.png')
    d = pytesseract.image_to_string(img, output_type=Output.DICT)
    text = d["text"]
    resultado = ''.join(filter(lambda i: i not in "\n", text))
    resultado = (criar_dicionario(resultado))
    print(resultado)
    for key in resultado.keys():
        string += f"{key}:{resultado[key]};"
    string = string[:-1]+ "\n"
    cont += 1
    contador += 1

arq = open("resultado.csv", "w")
arq.write(string)
arq.close()
