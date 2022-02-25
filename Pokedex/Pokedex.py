# WebAPI 関連
import requests
import json
import pprint
# ウィンドウ関連
import tkinter as tk
import io
from PIL import Image, ImageTk
from urllib.request import urlopen

# クラス関連
import Window

def main():
    win = tk.Tk()
    frame = Window.WINDOW(win, 500, 500)

    Pokemon_code = input("Pokemon : ")
    PokeAPI_URL = "https://pokeapi.co/api/v2/pokemon/"
    PokeAPI_res = requests.get(f"{PokeAPI_URL}{Pokemon_code}")
    PokeAPI_res.raise_for_status()
    PokeAPI_res_json = PokeAPI_res.json()
    #pprint.pprint(PokeAPI_res_json)

    # 絵の表示
    Poke_img_URL = PokeAPI_res_json['sprites']['other']['official-artwork']['front_default']
    file = io.BytesIO(urlopen(Poke_img_URL).read())
    Poke_img = ImageTk.PhotoImage(Image.open(file))
    frame.canvas.create_image(250, 250, image = Poke_img, anchor = tk.CENTER)
    frame.mainloop()


if __name__ == "__main__":
    main()
