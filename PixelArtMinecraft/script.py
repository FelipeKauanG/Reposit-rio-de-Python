import PySimpleGUI as sg

colors = {"Grass": "127, 178, 56", "Sand":"247, 233, 163", "Wool": "199, 199, 199", "Fire": "255, 0, 0", "Ice": "160, 160, 255", "Metal": "167, 167, 167", "Plant": "0, 124, 0", "Snow": "255, 255, 255", "Clay": "164, 168, 184", "Dirt": "151, 109, 77", "Stone": "112, 112, 112", "Water": "64, 64, 255", "Wood": "143, 119, 72", "Quartz": "255, 252, 245", "Color_orange": "216, 127, 51", "Color_magenta" : "178, 76, 216", "Color_light_blue": "102, 153, 216", "Color_yellow": "229, 229, 51", "Color_light_green": "127, 229, 51", "Color_pink": "242, 127, 165", "Color_gray": "76, 76, 76", "Color_light_gray": "153, 153, 153", "Color_cyan": "76, 127, 153", "Color_purple": "127, 63, 178", "Color_blue": "51, 76, 178", "Color_brown": "102, 76, 51", "Color_green": "102, 127, 51", "Color_red": "153, 51, 51", "Color_black": "25, 25, 25", "Gold":"250, 238, 25", "Diamond": "92, 219, 213", "Lapis": "74, 128, 255", "Emerald": "0, 217, 58", "Podzol": "129, 86, 49", "Nether": "112, 2, 0", "Terracotta_white": "209, 177, 161", "Terracotta_orange": "159, 872, 36", "Terracotta_magenta": "149, 87, 108", "Terracotta_light_blue": "112, 108, 138", "Terracotta_yellow": "186, 133, 36", "Terracotta_light_green": "103, 117, 53", "Terracotta_pink": "160, 77, 78", "Terracotta_gray": "57, 41, 35", "Teracotta_light_gray": "137, 107, 98","Terracotta_cyan": "87, 92, 92", "Terracotta_purple": "122, 73, 88", "Terracotta_blue": "76, 62, 92", "Terracotta_brown": "76, 50, 35","Terracotta_green": "76, 82, 42", "Terracotta_red": "142, 60, 46", "Terracotta_black": "37, 22, 16","Crimson_nylium":"189, 48, 49","Crimson_hyphae":"92, 25, 29","Crimsom_stem":"148, 63, 97", "Warped_nylium" : "22, 126, 134","Warped_stem":"58, 142, 140","Warped_Hyphae":"86, 44, 62","Warped_wart_block":"20, 180, 133","Deepslate":"100, 100, 100","Raw_iron":"216, 175, 147", "Glow_lichen":"127, 167, 150"}

porcentagens = {}

def open_image():
    sg.theme("DarkGrey10")
    
    layout = [
        [sg.Text("Selecione uma imagem em formato PNG:")],
        [sg.InputText(key="image_path"), sg.FileBrowse(file_types=(("Imagens PNG", "*.png"),))],
        [sg.Button("Abrir Imagem"), sg.Button("Sair")],
    ]
    
    window = sg.Window("Abrir imagem", layout, finalize=True)
    
    
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        elif event == "Abrir Imagem":
            imagem_path = values["image_path"]
            if imagem_path:
                arquivo = r"PixelArtMinecraft/imagem.txt"
                
                from PIL import Image
                img = Image.open(imagem_path)
                largura, altura = img.size
                print(f"Largura: {largura}px\nAltura: {altura}px")
                with open(arquivo, "w+", encoding="utf-8") as textoImagem:
                    for larg in range(0, largura):
                        for altu in range(0, altura):
                            pixel = img.getpixel((larg, altu))
                            
                            melhor_cor = None
                            
                            menor_diferença = float("inf")
                            for nome, valor in colors.items():
                                valor_rgb = [int(x) for x in valor.split(", ")]
                                diferenca = sum(abs(a - b) for a, b in zip(pixel, valor_rgb))
                                if diferenca < menor_diferença:
                                    menor_diferença = diferenca
                                    melhor_cor = (valor_rgb, nome)
                                   
                            textoImagem.write(f"RGB: {melhor_cor[0]}, Nome do bloco: {melhor_cor[1]}\n")
                        print("\n")
    window.close()



if __name__ == "__main__":
    open_image()


