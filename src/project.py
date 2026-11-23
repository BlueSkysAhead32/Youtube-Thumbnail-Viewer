from PIL import Image, ImageDraw, ImageFont
import os
import pygame
import tkinter as tk
from tkinter import filedialog, simpledialog
#One's below will most likely be temporary, TO BE REMOVED BY END.
import sys
import glob

def sidebar_test_maker(template, thumbnail, Videotimestamp):
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
    if Videotimestamp != None:
        draw.text((5161, 1118), Videotimestamp, font= timestampfont)
    if Videotimestamp == None:
        draw.text((5161, 1118), "5:45", font= timestampfont)
    return output


def front_page_test_maker(template, thumbnail, Videotimestamp):
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
    if Videotimestamp != None:
        draw.text((2409, 1535), Videotimestamp, font= timestampfont)
    if Videotimestamp == None:
        draw.text((2409, 1535), "5:45", font= timestampfont)
    return output

def image_shower(name, select, filetype):
    with (Image.open(f"{name}testVV{select}{filetype}")) as img:
        img.show()

def commandbar_displayer(surface, textstyle, text):
    what_happening = textstyle.render(f"{text}", True, "white", wraplength= 600)
    surface.blit(what_happening, (10, 575))
def main():
    
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Youtube Thumbnail Viewer")
    textdisplay1 = pygame.font.SysFont('arial', 20)
    textdisplay2 = pygame.font.SysFont('arial', 45)
    textdisplay3 = pygame.font.SysFont('arial', 17)
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    running = True
    testbuttonaccess1 = False
    testbuttonaccess2 = False
    showitnow1 = False
    showitnow2 = False
    VideoTimeammount = None
    fadeaway = 0
    central_img_path= ""
    templ_img_path = ["C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-1.png", 
                      "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-2.png",
                      "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-3.png",
                      "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemplateFiles\\YTVTemplate-4.png"
                      ]
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
                    buttonclicked= True
                    thing = 3
                    testbuttonaccess2 = False
                    print("file select")
                    testbuttonaccess1 = True
                elif click.colliderect(button[4]):
                    print("convert files")
                    print(central_img_path)
                    buttonclicked= True
                    thing = 4
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
                    testbuttonaccess1 = False
                    testbuttonaccess2 = False
                elif click.colliderect(button[10]):
                    print("clear all files")
                    buttonclicked= True
                    thing = 10
                    testbuttonaccess1 = False
                    testbuttonaccess2 = False
                elif click.colliderect(button[11]):
                    print("Switch to compare mode")
                    buttonclicked= True
                    thing = 11
                    testbuttonaccess1 = False
                    testbuttonaccess2 = False
                elif click.colliderect(button[12]):
                    print("Insert Timestamp")
                    buttonclicked= True
                    thing = 12
            if event.type == pygame.QUIT:
                tempstorage = "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemporaryImageStorage"
                for path in os.scandir(tempstorage):
                    os.remove(path.path)
                    showitnow1 = False
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
                if testbuttonaccess1 == False and testbuttonaccess2 == False and place >= 5 and place < 9:
                    pass
                    pygame.draw.rect(screen, color[13], button[13])
                elif testbuttonaccess1 == True and testbuttonaccess2 == False and place >= 5 and place < 9:
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
            if testbuttonaccess1 == False and testbuttonaccess2 == False and section >= 5 and section < 9:
                pass
            elif testbuttonaccess1 == True and testbuttonaccess2 == False and section >= 5 and section < 9:
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

        if showitnow1 == True:
            if central_img_path == "":
                pass
            else:
                display_central_filename = central_img_path.split("/")
                selectedfilename = textdisplay1.render(f"File selected: {display_central_filename[-1]}", True, "white", wraplength= 250)
                screen.blit(selectedfilename, (80, 450))

        if showitnow1 == False:
            selectfiletext = textdisplay2.render("Click Here to Insert a .png File!", True, "white", wraplength= 350)
            screen.blit(selectfiletext, (60, 250))

        if showitnow2 == True:
            position = 0
            for file in os.scandir("C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemporaryImageStorage"):
                locations = [(450,175), (450, 275), (450, 375), (450, 475)]
                testimagename = textdisplay3.render(f"{file.name}", True, "white", wraplength = 250)
                screen.blit(testimagename, locations[position])
                position += 1

        if thing == 4 and central_img_path != "" and testbuttonaccess1 == True:
            commandbar_displayer(screen, textdisplay1, "Loading Images...")

        if thing == 9 and central_img_path != "" and os.listdir("C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemporaryImageStorage") != []:
            commandbar_displayer(screen, textdisplay1, "Saving Images...")

        if thing == 10 or fadeaway > 0:
            if fadeaway == 0:
                fadeaway += 15
            commandbar_displayer(screen, textdisplay1, "Files Cleared!")
            fadeaway -= 1
        
        pygame.display.flip()

        if thing == 3:
            tempstorage = "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemporaryImageStorage"
            for path in os.scandir(tempstorage):
                os.remove(path.path)
            fileinput= tk.Tk()
            fileinput.withdraw()
            filepath = filedialog.askopenfilename(filetypes= [("PNG files", "*.png")])
            central_img_path = filepath
            print(central_img_path)
            if central_img_path != "":
                showitnow1 = True
            else:
                showitnow1 = False

        if thing == 4:
            if central_img_path == "":
                pass
            else:
                ref = 0
                for file in templ_img_path:
                    ref +=1
                    templname, ext = os.path.splitext(file)
                    draftname, ext = os.path.splitext(central_img_path)
                    newpathname = templname.replace("\\TemplateFiles", "\\TemporaryImageStorage")
                    filename = draftname.split("/")
                    newername = newpathname.replace(f"YTVTemplate-{ref}", filename[-1])
                    with (Image.open(file)) as template, (Image.open(central_img_path)) as thumbnail:
                        if ref <= 2:
                            output = sidebar_test_maker(template, thumbnail, VideoTimeammount)
                            output.save(f"{newername}testVV{ref}{ext}")
                        if ref > 2:
                            output = front_page_test_maker(template, thumbnail, VideoTimeammount)
                            output.save(f"{newername}testVV{ref}{ext}")
                if testbuttonaccess1 == True:
                    testbuttonaccess2 = True
                    showitnow2 = True

        if thing in range(5,9):
            part = thing - 4
            image_shower(newername, part, ext)

        if thing == 9:
            fileexport = tk.Tk()
            fileexport.withdraw()
            exportpath = filedialog.askdirectory(title= "wheres the file going")
            tempstorage = "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemporaryImageStorage"
            for path in os.scandir(tempstorage):
                if exportpath == "":
                    os.remove(path.path)
                    pass
                else:
                    image_path = path.name
                    finalplace = os.path.join(exportpath, image_path)
                    with Image.open(path.path) as done:
                        done.save(finalplace)
                    os.remove(path.path)
            central_img_path = ""
            showitnow1 = False
            VideoTimeammount = None

        if thing == 10:
            tempstorage = "C:\\Users\\drewm\\OneDrive\\Desktop\\PFDAAssignments\\Youtube-Thumbnail-Viewer\\src\\TemporaryImageStorage"
            for path in os.scandir(tempstorage):
                os.remove(path.path)
            central_img_path = ""
            showitnow1 = False

        if thing == 12:
            VideoTimeammountsuggested = simpledialog.askstring("Insert Video Time", "How long is the video (Must be in 00:00:00 format)")
            VideoTimeammount = ""
            for character in VideoTimeammountsuggested:
                if character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6":
                    VideoTimeammount += character
                if character == "7" or character == "8" or character == "9" or character == ":" or character == "0":
                    VideoTimeammount += character
            print(VideoTimeammount)


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
        dt = clock.tick(12)


if __name__ == "__main__":
    main()