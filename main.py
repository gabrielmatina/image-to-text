import pytesseract
from PIL import Image
from os.path import exists, join
from glob import glob

def extract(image_path: str = "data/input/target.png", output_text_path: str = "data/output/result.txt"):
    
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