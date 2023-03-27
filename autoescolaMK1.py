import cv2
import numpy as np
import time
import winsound
from PIL import ImageGrab

# Cria uma janela para seleção da região
cv2.namedWindow("Selecionar Área", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Selecionar Área", 800,800)
selecionando = False

while True:
    # Captura a tela e exibe-a em uma janela
    screenshot = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_RGB2BGR)
    cv2.imshow("Selecionar Área", screenshot)

    # Seleciona a área
    key = cv2.waitKey(1)
    if key == ord("s"):
        selecionando = True
        while selecionando:
            screenshot = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_RGB2BGR)
            cv2.imshow("Selecionar Área", screenshot)
            key = cv2.waitKey(1)
            if key == ord("s"):
                break

        x1, y1, x2, y2 = cv2.selectROI("Selecionar Área", screenshot, False)
        area = (x1, y1, x2, y2)
        cv2.destroyAllWindows()
        break

#Define a região de interesse
x1, y1, x2, y2 = area
if x1 > x2:
    x1, x2 = x2, x1
if y1 > y2:
    y1, y2 = y2, y1
roi = (x1, y1, x2 - x1, y2 - y1)

#Inicializa o valor do último frame
last_frame = None

#Monitora a região selecionada
while True:
    # Captura a tela e converte para escala de cinza
    screenshot = cv2.cvtColor(np.array(ImageGrab.grab(bbox=roi)), cv2.COLOR_RGB2GRAY)

    # Verifica se o último frame não está vazio
    if last_frame is not None:
        # Calcula a diferença entre o frame atual e o último frame
        delta = cv2.absdiff(screenshot, last_frame)

        # Converte a diferença para preto e branco e aplica um limiar
        thresh = cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)[1]

        # Verifica se houve uma mudança brusca para a cor branca
        white_area_threshold = int(thresh.size * 0.50)  # define a quantidade de pixels brancos necessários
        white_area = np.sum(thresh == 255)
        if white_area > white_area_threshold:
            # Emite um aviso sonoro
            winsound.Beep(500, 5000)

    # Define o último frame como o frame atual
    last_frame = screenshot

    # Aguarda um segundo antes de capturar o próximo frame
    time.sleep(1)
