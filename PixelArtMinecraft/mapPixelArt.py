import PySimpleGUIQt as sg #pip install PySimpleGUIQt
import numpy as np #pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
from time import sleep
import os
from tkinter import *
from fractions import Fraction

colors = {"Grass": "127, 178, 56", "Sand":"247, 233, 163", "wool": "199, 199, 199", "Redstone_block": "255, 0, 0", "Ice": "160, 160, 255", "Metal": "167, 167, 167", "cactus": "0, 124, 0", "Snow": "255, 255, 255", "Clay": "164, 168, 184", "Dirt": "151, 109, 77", "Stone": "112, 112, 112", "Water": "64, 64, 255", "Wood": "143, 119, 72", "Quartz": "255, 252, 245", "acacia_planks": "216, 127, 51", "Color_magenta" : "178, 76, 216", "Color_light_blue": "102, 153, 216", "Color_yellow": "229, 229, 51", "Color_light_green": "127, 229, 51", "Color_pink": "242, 127, 165", "gray_wool": "76, 76, 76", "Color_light_gray": "153, 153, 153", "Color_cyan": "76, 127, 153", "Color_purple": "127, 63, 178", "Color_blue": "51, 76, 178", "Color_brown": "102, 76, 51", "Color_green": "102, 127, 51", "Color_red": "153, 51, 51", "Color_black": "25, 25, 25", "Gold":"250, 238, 25", "Diamond": "92, 219, 213", "Lapis": "74, 128, 255", "Emerald": "0, 217, 58", "Spruce": "129, 86, 49", "Nether": "112, 2, 0", "Terracotta_white": "209, 177, 161", "Terracotta_orange": "159, 872, 36", "Terracotta_magenta": "149, 87, 108","Terracotta_light_blue": "112, 108, 138", "Terracotta_yellow": "186, 133, 36", "Terracotta_light_green": "103, 117, 53", "Terracotta_pink": "160, 77, 78", "Terracotta_gray": "57, 41, 35", "Terracotta_light_gray": "137, 107, 98","Terracotta_cyan": "87, 92, 92", "Terracotta_purple": "122, 73, 88", "Terracotta_blue": "76, 62, 92", "Terracotta_brown": "76, 50, 35","Terracotta_green": "76, 82, 42", "Terracotta_red": "142, 60, 46", "Terracotta_black": "37, 22, 16","Crimson_nylium":"189, 48, 49","Crimson_hyphae":"92, 25, 29","Crimsom_stem":"148, 63, 97", "Warped_nylium" : "22, 126, 134","Warped_stem":"58, 142, 140","Warped_hyphae":"86, 44, 62","Warped_wart_block":"20, 180, 133","Deepslate":"100, 100, 100","Raw_iron":"216, 175, 147", "verdant_froglight_top":"127, 167, 150"}
porcentagens = {}

def open_image():
    root = Tk()
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    window_height = 400
    window_width = 600
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.destroy()
    sg.theme("Dark")
    layout = [
        [sg.Text("Selecione uma imagem em formato PNG:", justification="Center")],
        [sg.InputText(key="image_path"), sg.FileBrowse(file_types=(("Imagens PNG", "*.png"),("Imagens JPG", "*.jpg")))],
        [sg.Button("Abrir Imagem"), sg.Button("Sair"), sg.Checkbox("Mostrar gráfico", default=False, key="toggle_button")]
    ]
    
    
    window = sg.Window("Abrir imagem", layout, element_justification='c', finalize=True, size=(window_width, window_height), location=(x, y), icon=r"PixelArtMinecraft/imagem/Icon.png")

    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        elif event == "Abrir Imagem":
            imagem_path = values["image_path"]
            if imagem_path:
                arquivo = r"PixelArtMinecraft/imagem.txt"
                
                from PIL import Image
                img = Image.open(imagem_path)
                img = img.convert("RGB")
                largura, altura = img.size
                if largura // altura == 1:
                    print("imagem quadrada")
                    print(f"Largura: {largura}px\nAltura: {altura}px")
                else:
                    print(f"Proporção {Fraction(largura,altura)}, Largura: {largura}px Altura: {altura}px")
                toggle = values["toggle_button"]
                
                window.close()
                print("criando a imagem", end="", flush=True)
                for i in range(1, 4):
                    print(".",end="", flush=True)
                    sleep(1)
                with open(arquivo, "w+", encoding="utf-8") as textoImagem:
                    for altu in range(0, altura):
                        for larg in range(0, largura):
                            
                            pixel = img.getpixel((larg, altu))
                            melhor_cor = None
                            menor_diferença = float("inf")
                            
                            for nome, valor in colors.items():
                                valor_rgb = [int(x) for x in valor.split(", ")]
                                #print(pixel)
                                diferenca = sum(abs(a - b) for a, b in zip(pixel, valor_rgb))
                                
                                if diferenca < menor_diferença:
                                    menor_diferença = diferenca
                                    melhor_cor = (valor_rgb, nome)
                                    str(melhor_cor).split(", ")
                                    
                            textoImagem.write(f"#{melhor_cor[0][0]:02x}{melhor_cor[0][1]:02x}{melhor_cor[0][2]:02x}\n{melhor_cor[1]}.png\n")
            break
    
    cores = []
    blocks = r"PixelArtMinecraft/blocos"
    blocks_itens = os.listdir(blocks)
    imagem_inicial = Image.new("RGB", (largura*16, altura*16), (255, 255, 255))
    x, y = 0, 0
    with open(arquivo, "r", encoding="utf-8") as textoImagem:
        lines = textoImagem.readlines()
        for line in range(0, len(lines), 2):
            cor = lines[line].split()
            r = int(cor[0][1:3], 16) / 255
            g = int(cor[0][3:5], 16) / 255
            b = int(cor[0][5:7], 16) / 255
            cores.append((r,g,b))
            
            if lines[line+1].strip() in blocks_itens:
                bloco = Image.open(os.path.join(blocks, f"{lines[line+1].strip()}"))
                for _ in range(largura):
                    imagem_inicial.paste(bloco, (x, y))
                x += 16
                if x >= largura * 16:
                    x = 0
                    y += 16
    cores = np.array(cores).reshape(altura, largura, 3)
    plt.axis("off")
    plt.autoscale(enable=True)
    plt.imshow(cores)
    if toggle == True:
        plt.show()
    
    imagem_inicial.show()
if __name__ == "__main__":
    open_image()
    input("\nPressiona enter para finalizar")
print("\033[34mFinalizado\033[m")
