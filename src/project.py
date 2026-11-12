from PIL import Image
import os
import pygame
import tkinter as tk
from tkinter import filedialog
#One's below will most likely be temporary, TO BE REMOVED BY END.
import sys
import glob

def sidebar_test_maker(template, thumbnail):
    white_bg = Image.new("RGBA",(5996, 3223), color = "white")
    copythumbnail = thumbnail.copy()
    out_thumbnail2 = copythumbnail.resize((1014,570))
    copytemplate = template.copy()
    white_bg.paste(out_thumbnail2, (4266, 631))
    white_bg.paste(copytemplate, (0,0), mask = copytemplate)
    return white_bg


def front_page_test_maker(template, thumbnail):
    blah = blah

def main():
    templ_img_path = ["C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-1.png", 
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-2.png",
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-3.png",
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-4.png"
                     ]
    
    central_img_path = "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\PDFA ThumbnailTestSubject.png"
    

    number = 0
    for file in templ_img_path:
        number +=1
        name1, ext = os.path.splitext(file)
        name2, ext = os.path.splitext(central_img_path)
        newname = name1.replace("\\TemplateFiles", "\\TemporaryImageStorage")
        newname2 = name2.split("\\")
        newername = newname.replace(f"YTVTemplate-{number}", newname2[-1])
        with (Image.open(file)) as template, (Image.open(central_img_path)) as thumbnail:
            if number <= 2:
                output = sidebar_test_maker(template, thumbnail)
                output.save(f"{newername}testV{number}{ext}")
            #if number > 2:
                #output = front_page_test_maker(template, thumbnail)
                #output.save(f"{newername}testV{number}{ext}")
    

    # white_bg = Image.new("RGBA",(5996, 3223), color = "white")
    # name, ext = os.path.splitext(central_img_path)
    # with (Image.open(central_img_path)) as thumbnail, Image.open(templ_img_path[0]) as template:
    #     out_thumbnail = thumbnail.copy()
    #     out_thumbnail2 = out_thumbnail.resize((1014,570))
    #     white_bg.paste(out_thumbnail2, (4266, 631))
    #     white_bg.paste(template, (0,0), mask = template)
    #     white_bg.save(f"{name}placetest{ext}")





if __name__ == "__main__":
    main()