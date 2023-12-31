
Projeto OCR Automático com PyAutoGUI e Tesseract
Descrição do Projeto
Este projeto em Python utiliza as bibliotecas PyAutoGUI, Tesseract e OpenCV para realizar OCR (Optical Character Recognition) em uma região específica da tela. O programa captura periodicamente uma área de uma janela com o título "Creare Sistemas" usando PyAutoGUI, salva a captura de tela em um diretório local e realiza OCR na imagem usando Tesseract. O texto extraído é então impresso no console.

Requisitos
Python 3.x
Bibliotecas: cv2, pytesseract, pyautogui, pygetwindow, Pillow (instaláveis via pip)
Tesseract OCR instalado (certifique-se de configurar o caminho correto para o executável do Tesseract no código)

Instalação e Configuração

1°) Clone este repositório para o seu ambiente local.

2°) pip install opencv-python pytesseract pyautogui pygetwindow Pillow

3°) Instale o Tesseract OCR e configure o caminho no código.

Uso
Execute o script Python ocr_automatico.py. O programa capturará periodicamente a área da janela "Windows", salvará as imagens em um diretório local e realizará OCR nas imagens capturadas.

Observações
Certifique-se de ajustar o título da janela ("Window") e o caminho para o executável do Tesseract conforme necessário. Ajuste também os parâmetros de captura, tempo de espera e outras configurações de acordo com suas necessidades.

Contribuições
Contribuições são bem-vindas! Se você encontrar problemas, bugs ou melhorias possíveis, sinta-se à vontade para abrir uma issue ou enviar um pull request.

