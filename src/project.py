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
    testbuttonacess1 = False
    testbuttonaccess2 = False
    while running:
        buttonclicked= False
        thing = None
        mouselocation = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.Rect((mouselocation[0], mouselocation[1]), (1,1))
                pygame.draw.rect(screen, "blue", click)
                if click.colliderect(button[13]) and testbuttonaccess2 == False:
                    print("blocked")
                    pass
                elif click.colliderect(button[3]):
                    print("file select")
                    buttonclicked= True
                    thing = 3
                    testbuttonacess1 = True
                elif click.colliderect(button[4]):
                    print("convert files")
                    buttonclicked= True
                    thing = 4
                    if testbuttonacess1 == True:
                        testbuttonaccess2 = True
                elif click.colliderect(button[5]):
                    print("show image 1")
                    buttonclicked= True
                    thing = 5
                elif click.colliderect(button[6]):
                    print("show image 2")
                    buttonclicked= True
                    thing = 6
                elif click.colliderect(button[7]):
                    print("show image 3")
                    buttonclicked= True
                    thing = 7
                elif click.colliderect(button[8]):
                    print("show image 4")
                    buttonclicked= True
                    thing = 8
                elif click.colliderect(button[9]):
                    print("save files")
                    buttonclicked= True
                    thing = 9
                    testbuttonacess1 = False
                    testbuttonaccess2 = False
                elif click.colliderect(button[10]):
                    print("clear all files")
                    buttonclicked= True
                    thing = 10
                    testbuttonacess1 = False
                    testbuttonaccess2 = False
                elif click.colliderect(button[11]):
                    print("Switch to compare mode")
                    buttonclicked= True
                    thing = 11
                elif click.colliderect(button[12]):
                    print("Insert Timestamp")
                    buttonclicked= True
                    thing = 12
            if event.type == pygame.QUIT:
                running = False

        place = 0
        section = 3
        screen.fill((55, 55, 55, 255))
        button = [pygame.Rect(( 25, 150), (750, 400)), pygame.Rect((25, 20), (750, 100)), pygame.Rect((350, 150), (100, 400)), pygame.Rect((40, 165), (295, 370)), 
                  pygame.Rect((362, 312), (75, 75)), pygame.Rect((700, 175), (50, 50)), pygame.Rect((700, 275), (50, 50)), pygame.Rect((700 , 375), (50, 50)), 
                  pygame.Rect((700, 475), (50, 50)), pygame.Rect((450, 560), (150, 30)), pygame.Rect((625, 560), (150, 30)), pygame.Rect((400, 70), (170, 40)), 
                  pygame.Rect((590, 70), (170, 40)), pygame.Rect((570,150), (200, 395))]
        color = [(80, 80, 80, 255), (25, 25, 25, 255), (125, 125, 125, 255), (40, 40, 40), (175, 175, 175), (200, 200, 200), (200, 200, 200), (200, 200, 200), 
                 (200, 200, 200), (235, 235, 235), (235, 235, 235), (20, 20, 20), (20, 20, 20), (80, 80, 80, 255)]
        color2 = [(70, 70, 70), (15, 15, 15), (115, 115, 115), (30, 30, 30), (155, 155, 155), (170, 170, 170), (170, 170, 170), (170, 170, 170), 
                         (170, 170, 170), (175, 175, 175), (175, 175, 175), (10, 10, 10), (10, 10, 10), (80, 80, 80, 255)]
        borderR = [7, 0, 0, 15, 10, 10, 10, 10, 10, 7, 7, 7, 7, 0]

        for number in range(0, 3):  
            pygame.draw.rect(screen, color[number], button[number], border_radius= borderR[number])

        for object in button:
            if place >= 3:
                if testbuttonacess1 == False and testbuttonaccess2 == False and place >= 5 and place < 9:
                    pass
                    pygame.draw.rect(screen, color[13], button[13])
                elif testbuttonacess1 == True and testbuttonaccess2 == False and place >= 5 and place < 9:
                    pass
                    pygame.draw.rect(screen, color[13], button[13])
                else:
                    shadow = object.copy()
                    if place < 9:
                        newshadow = shadow.move(-5, 5)
                    if place >= 9:
                        newshadow = shadow.move(-3, 3)
                    if place < 13:
                        pygame.draw.rect(screen, color2[place], newshadow, border_radius= borderR[place])
            place += 1
        
        for number in range(3, 13):
            if testbuttonacess1 == False and testbuttonaccess2 == False and section >= 5 and section < 9:
                pass
            elif testbuttonacess1 == True and testbuttonaccess2 == False and section >= 5 and section < 9:
                pass
            else:
                if buttonclicked == True and number == thing:
                    tempbutton = button[thing].copy()
                    if place < 9:
                        newpos = tempbutton.move(-5, 5)
                    if place >= 9:
                        newpos = tempbutton.move(-3, 3)
                    pygame.draw.rect(screen, color[number], newpos, border_radius= borderR[number])
                else:
                    if section < 13:
                        pygame.draw.rect(screen, color[number], button[number], border_radius= borderR[number])
            section += 1
            
        # Keeping these for the sake of remembering which value goes where, if I want to change them later.

        # canvas = pygame.Rect(( 25, 150), (750, 400))
        # options = pygame.Rect((25, 20), (750, 100))
        # divider = pygame.Rect((350, 150), (100, 400))
        # selectfilebutton = pygame.Rect((40, 165), (295, 370))
        # convertfilebutton = pygame.Rect((362, 312), (75, 75))
        # showimg1button = pygame.Rect((0,0), (50, 50))
        # savebutton = pygame.Rect((450, 560), (150, 30))
        # clearbutton = pygame.Rect((625, 560), (150, 30))
        # comparebutton = pygame.Rect((400, 70), (170, 40))
        # timebutton = pygame.Rect((590, 70), (170, 40))
        # pygame.draw.rect(screen, (80, 80, 80, 255), canvas)
        # pygame.draw.rect(screen, (40, 40, 40, 255), options)
        # pygame.draw.rect(screen, (125, 125, 125, 255), divider)
        # pygame.draw.rect(screen, (40, 40, 40), selectfilebutton, border_radius= 15)
        # pygame.draw.rect(screen, (175, 175, 175), convertfilebutton, border_radius= 10)
        # pygame.draw.rect(screen, (200, 200, 200), showimg1button, border_radius= 10)
        #pygame.draw.rect(screen, (235, 235, 235), savebutton, border_radius= 7)
        #pygame.draw.rect(screen, (235, 235, 235), clearbutton, border_radius= 7)
        #pygame.draw.rect(screen, (20, 20, 20), comparebutton, border_radius= 7)
        #pygame.draw.rect(screen, (20, 20, 20), timebutton, border_radius= 7)
        pygame.display.flip()
        dt = clock.tick(12)


if __name__ == "__main__":
    main()