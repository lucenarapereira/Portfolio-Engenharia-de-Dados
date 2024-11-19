import sys
print(sys.path)

from image_processing_clahe.algoritmo import process_image

# Altere para o caminho da sua imagem ou forneça como argumento
if len(sys.argv) > 1:
    image_path = sys.argv[1]  
else:
    image_path = 'C:\\Users\\lucenara.pereira\\Downloads\\Bootcamp_Engenharia_Dados\\2. Pacote_Python\\cactos.jpg'  

# Chama a função para processar a imagem
process_image(image_path)
