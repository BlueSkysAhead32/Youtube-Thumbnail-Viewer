from PIL import Image
import os
import pygame
import tkinter as tk
from tkinter import filedialog
#One's below will most likely be temporary, TO BE REMOVED BY END.
import sys
import glob

def main():
    temp_img_path = (sys.argv[1])
    name, ext = os.path.splitext(temp_img_path)
    white_bg = Image.new("RGBA",(5996, 3223), color = "white")
    with (Image.open(temp_img_path)) as img:
        out_img = img.copy()
        print(out_img.mode)
        white_bg.paste(out_img, (0,0), mask= out_img)
        white_bg.save(f"{name}whitetest{ext}")


if __name__ == "__main__":
    main()