from PIL import Image
import os
import pygame
import tkinter as tk
from tkinter import filedialog
#One's below will most likely be temporary, TO BE REMOVED BY END.
import sys
import glob

def main():
    temp_img_path = ["C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-1.png", 
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-2.png",
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-3.png",
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-4.png"
                     ]

    number = 0
    for file in temp_img_path:
        number +=1
        name, ext = os.path.splitext(file)
        white_bg = Image.new("RGBA",(5996, 3223), color = "white")
        with (Image.open(file)) as img:
            out_img = img.copy()
            white_bg.paste(out_img, (0,0), mask= out_img)
            white_bg.save(f"{name}{number}whitetest{ext}")


if __name__ == "__main__":
    main()