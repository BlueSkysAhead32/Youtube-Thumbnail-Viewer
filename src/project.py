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
    # templ_img_path = ["C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-1.png", 
    #                  "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-2.png",
    #                  "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-3.png",
    #                  "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-4.png"
    #                  ]
    # central_img_path = "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\ClouddropUpdateVideo_1Thumbnail.png"

    # number = 0
    # for file in templ_img_path:
    #     number +=1
    #     templname, ext = os.path.splitext(file)
    #     draftname, ext = os.path.splitext(central_img_path)
    #     newpathname = templname.replace("\\TemplateFiles", "\\TemporaryImageStorage")
    #     filename = draftname.split("\\")
    #     newername = newpathname.replace(f"YTVTemplate-{number}", filename[-1])
    #     with (Image.open(file)) as template, (Image.open(central_img_path)) as thumbnail:
    #         if number <= 2:
    #             output = sidebar_test_maker(template, thumbnail)
    #             output.save(f"{newername}testV{number}{ext}")
    #         if number > 2:
    #             output = front_page_test_maker(template, thumbnail)
    #             output.save(f"{newername}testV{number}{ext}")
    
    pygame.init()
    pygame.display.set_caption("Youtube Thumbnail Viewer")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        screen.fill((55, 55, 55, 255))
        button = [pygame.Rect(( 25, 150), (750, 400)), pygame.Rect((25, 20), (750, 100)), pygame.Rect((350, 150), (100, 400)), pygame.Rect((40, 165), (295, 370)), 
                  pygame.Rect((362, 312), (75, 75)), pygame.Rect((700, 175), (50, 50)), pygame.Rect((700, 275), (50, 50)), pygame.Rect((700 , 375), (50, 50)), 
                  pygame.Rect((700, 475), (50, 50))]
        color = [(80, 80, 80, 255), (40, 40, 40, 255), (125, 125, 125, 255), (40, 40, 40), (175, 175, 175), (200, 200, 200), (200, 200, 200), (200, 200, 200), 
                 (200, 200, 200)]
        borderR = [0, 0, 0, 15, 10, 10, 10, 10, 10]
        selectfilebutton = pygame.Rect((40, 165), (295, 370))
        convertfilebutton = pygame.Rect((362, 312), (75, 75))
        showimg1button = pygame.Rect((0,0), (50, 50))
        
        for number in range(len(button)):
            pygame.draw.rect(screen, color[number], button[number], border_radius= borderR[number])
            
            
        canvas = pygame.Rect(( 25, 150), (750, 400))
        options = pygame.Rect((25, 20), (750, 100))
        divider = pygame.Rect((350, 150), (100, 400))
        # pygame.draw.rect(screen, (80, 80, 80, 255), canvas)
        # pygame.draw.rect(screen, (40, 40, 40, 255), options)
        # pygame.draw.rect(screen, (125, 125, 125, 255), divider)
        # pygame.draw.rect(screen, (40, 40, 40), selectfilebutton, border_radius= 15)
        # pygame.draw.rect(screen, (175, 175, 175), convertfilebutton, border_radius= 10)
        # pygame.draw.rect(screen, (200, 200, 200), showimg1button, border_radius= 10)
        pygame.display.flip()
        dt = clock.tick(12)


if __name__ == "__main__":
    main()