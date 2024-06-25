"""
Este módulo extrai texto de uma imagem usando pytesseract e salva o resultado em um arquivo de texto.
"""

import pytesseract
from PIL import Image
from os.path import exists, join
from glob import glob

# Configurar o caminho do Tesseract se necessário
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


def extract(image_path: str = "data/input/target.png", output_text_path: str = "data/output/result.txt"):
    """
    Extrai texto de uma imagem e salva o resultado em um arquivo de texto.
    
    :param image_path: Caminho para a imagem de entrada.
    :param output_text_path: Caminho para o arquivo de saída onde o texto extraído será salvo.
    """
    if not exists(image_path):
        options = ["jpg", "png", "jpeg", "JPG", "PNG", "JPEG"]
        possbile = []
        for ext in options:
            possbile += glob(join("data", "input", f"*target.{ext}"))

        if len(possbile) == 0:
            print("Não Encontrei Nenhuma Imagem")
            exit()
        else:
            image_path = possbile[0]

    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    with open(output_text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

    print(f"Resultado da Extração:\n {text}\n\n")


if __name__ == "__main__":
    extract()
