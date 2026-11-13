from PIL import Image, ImageDraw, ImageFont
import os
import pygame
import tkinter as tk
from tkinter import filedialog
#One's below will most likely be temporary, TO BE REMOVED BY END.
import sys
import glob

def sidebar_test_maker(template, thumbnail):
    white_bg = Image.new("RGBA",(5996, 3223), color = "white")
    blender = Image.new("RGBA",(5996, 3223), color = (0,0,0,0))
    timestampfont = ImageFont.truetype('Pillow/Tests/fonts/arialbd.ttf', size= 37)
    timestamp = ImageDraw.Draw(blender)
    out_thumbnail2 = thumbnail.resize((1014,570))
    white_bg.paste(out_thumbnail2, (4266, 631))
    white_bg.paste(template, (0,0), mask = template)
    timestamp.rounded_rectangle([(5144, 1105), (5252, 1171)], 15, (0,0,0, 155))
    output = Image.alpha_composite(white_bg, blender)
    draw = ImageDraw.Draw(output)
    draw.text((5161, 1118), "5:45", font= timestampfont)
    return output


def front_page_test_maker(template, thumbnail):
    white_bg = Image.new("RGBA",(5996, 3223), color = "white")
    blender = Image.new("RGBA",(5996, 3223), color = (0,0,0,0))
    timestampfont = ImageFont.truetype('Pillow/Tests/fonts/arialbd.ttf', size= 40)
    timestamp = ImageDraw.Draw(blender)
    out_thumbnail2 = thumbnail.resize((1626,914))
    white_bg.paste(out_thumbnail2, (910, 712))
    white_bg.paste(template, (0,0), mask = template)
    timestamp.rounded_rectangle([(2394,1525), (2502,1593)], 15, (0,0,0, 155))
    output = Image.alpha_composite(white_bg, blender)
    draw = ImageDraw.Draw(output)
    draw.text((2409, 1535), "5:45", font= timestampfont)
    return output

def main():
    templ_img_path = ["C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-1.png", 
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-2.png",
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-3.png",
                     "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-4.png"
                     ]
    central_img_path = "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\ClouddropUpdateVideo_1Thumbnail.png"

    number = 0
    for file in templ_img_path:
        number +=1
        templname, ext = os.path.splitext(file)
        draftname, ext = os.path.splitext(central_img_path)
        newpathname = templname.replace("\\TemplateFiles", "\\TemporaryImageStorage")
        filename = draftname.split("\\")
        newername = newpathname.replace(f"YTVTemplate-{number}", filename[-1])
        with (Image.open(file)) as template, (Image.open(central_img_path)) as thumbnail:
            if number <= 2:
                output = sidebar_test_maker(template, thumbnail)
                output.save(f"{newername}testV{number}{ext}")
            if number > 2:
                output = front_page_test_maker(template, thumbnail)
                output.save(f"{newername}testV{number}{ext}")
    


if __name__ == "__main__":
    main()