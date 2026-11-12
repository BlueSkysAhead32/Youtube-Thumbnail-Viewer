from PIL import Image
import os
import pygame
import tkinter as tk
from tkinter import filedialog
#One's below will most likely be temporary, TO BE REMOVED BY END.
import sys
import glob

def main():
    templ_img_path = ["C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-1.png", 
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-2.png",
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-3.png",
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-4.png"
                     ]
    
    central_img_path = "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\PDFA ThumbnailTestSubject.png"
    


    #number = 0
    #for template in templ_img_path:
        #number +=1
        #name, ext = os.path.splitext(template)
        #newname = name.replace("\\TemplateFiles", "\\TemporaryImageStorage")
        #white_bg = Image.new("RGBA",(5996, 3223), color = "white")
        #with (Image.open(template)) as img:
            #out_img = img.copy()
            #white_bg.paste(out_img, (0,0), mask= out_img)
            #white_bg.save(f"{newname}{number}whitetest{ext}")
    

    white_bg = Image.new("RGBA",(5996, 3223), color = "white")
    name, ext = os.path.splitext(central_img_path)
    with (Image.open(central_img_path)) as thumbnail, Image.open(templ_img_path[0]) as template:
        out_thumbnail = thumbnail.copy()
        out_thumbnail2 = out_thumbnail.resize((1014,570))
        white_bg.paste(out_thumbnail2, (4266, 631))
        white_bg.paste(template, (0,0), mask = template)
        white_bg.save(f"{name}placetest{ext}")





if __name__ == "__main__":
    main()