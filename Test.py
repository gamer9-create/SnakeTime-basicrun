# import the Tools we need to make the game
import pygame
import random
import time
import datetime
import pickle
import os
import sys
import math

# Set up the Hardness Askers
Setter = 2
Name = "PLAYER"
# Ask pygame to get ready
pygame.init()
# Make varibles
count_epual = 300
Window_width = 700
Window_height = 700
Window = pygame.display.set_mode((Window_width, Window_height))
pygame.display.set_caption("TEXTBODY NAMEAPP")
today = datetime.datetime.now()
count = count_epual
lost_time = "TEXTBODY LOSE"
width = 40
timer_count = 0
ob2x = 0
ob2y = 0
x_leaf = random.randint(0, 660)
y_leaf = random.randint(0, 660)
x = 120
y = 0
Speed = 40
x_mouse = 5
score_plus = 20
y_mouse = 5
lives = 4
Speed_snake = 15
y_button = 630
x_button = 630
leaf_width = 20
font = pygame.font.Font(None, 30)
Beta = False
Win = False
NameTag_font = pygame.font.Font(None, 15)
Button_font = pygame.font.Font(None, 50)
game_font_over = pygame.font.Font(None, 60)
leaf_height = 20
livegettext = pygame.font.Font(None, 60)
Score_saver = "ScoreSaver.txt"
score = 0
ob1x = x_leaf + 120
ob1y = y_leaf + 100
f = open("Higs.txt", "a")
x_c = 0
red = pygame.Color(255, 51, 0)
y_c = 0
checkout_y = 640
Random_out_live = 0.1
checkout_x = 580
height = 40
x_gro = 0
y_gro = 640
millisecond = 0.5
second = millisecond + millisecond
width_gro = 970
height_gro = 40
Exit = "Your score is: " + str(score)
# Make the run Variable
running = True
clock = pygame.time.Clock()
# Set up the game loop
while running:
    # Set up Mouse Pos
    mouse = pygame.mouse.get_pos()
    (x_mouse, y_mouse) = pygame.mouse.get_pos()

    # Set up the background color
    white = pygame.Color(225, 225, 225)
    Window.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Set up Mouse button clicks
    if event.type == pygame.MOUSEBUTTONDOWN:
        if Button.colliderect(mousegh):
            running = False
            print(Exit)
        if Win == True and Button.colliderect(mousegh):
            running = False
            Exit = "TEXTBODY WON" + str(score)
            print(Exit)
    # Make sure the user restarts with only 2 lives when the time limit has gone up.
    if count <= 0:
        count = 300
        lives = 2
    # Activate the timer
    count = count - 1
    # Set up Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_c = x_c + -Speed
        y_c = 0
    if keys[pygame.K_RIGHT]:
        x_c = x_c + Speed
        y_c = 0
    if keys[pygame.K_DOWN]:
        y_c = y_c + Speed
        x_c = 0
    if keys[pygame.K_UP]:
        y_c = y_c + -Speed
        x_c = 0
    # Cal and max the speed
    x = x + x_c
    y = y + y_c
    clock.tick(Speed_snake)
    # Create Game Objects
    char1 = pygame.draw.rect(Window, (255, 51, 0), (x_leaf, y_leaf, leaf_width, leaf_height))
    mousegh = pygame.draw.rect(Window, (0, 0, 0), (x_mouse, y_mouse, 15, 15))
    Button = pygame.draw.rect(Window, (0, 0, 0), (x_button, y_button, 100, 35))
    checkout = pygame.draw.rect(Window, red, (checkout_x, checkout_y, 15, 15))
    Button_say = Button_font.render("Exit", True, red)
    ob1 = pygame.draw.rect(Window, (0, 0, 0), (ob1x, ob1x, 20, 20))
    ob2 = pygame.draw.rect(Window, (0, 0, 0), (ob2x, ob2y, 20, 20))
    Window.blit(Button_say, (x_button, y_button + 2))
    char = pygame.draw.rect(Window, (0, 204, 102), (x, y, width, height))
    # Set up the eating apple part!
    if char.colliderect(char1):
        count = count_epual
        Speed = Speed - 5
        width = width - 1
        height = height - 1
        score = score + score_plus
        lives = lives + 10
        y = y
        x = x
        y_c = 0
        x_c = 0
        x_leaf = random.randint(0, 660)
        y_leaf = random.randint(0, 660)
    # Set up the Crashing with the Ob.
    if char.colliderect(ob1):
        lives = lives - 4
        x = 200
        y = 0
        y_c = 0
        x_c = 0
    # Leave the game at you like it or not
    if keys[pygame.K_ESCAPE]:
        print(Exit)
        running = False
    # Go back to to the 0, 0 pos.
    if keys[pygame.K_g]:
        y = 0
        lives = lives - 1
        x = 160
        x_c = 0
        y_c = 0
    # Make sure the user is dead when the user runs out of lives

    if lives == 0 or 0 > lives:
        running = False
        print("TEXTBODY DIED")

    # Set up the win part
    if score == 100 or score > 100:
        lives = 100
        Win = True
        red = pygame.Color(0, 204, 102)
        count = 300
        winner = font.render("TEXTBODY", True, (0, 0, 0))
        Window.blit(winner, (0, 350))
    # Code to tell the Computer What to do with the User input Hardness.
    if Setter == 1:
        if y == 640 or y == -640 or x == 640 or x == -640:
            lives -= 20
            if lives == 0:
                running = False
                print("TEXTBODY LOST")
        lives = 0.5
        if count == 100 or count == 200 or count == 300 or count == 40:
            lives = lives - Random_out_live
        if char.colliderect(ob2):
            lives = lives - 50
            x = 240
            y = 0
        if Speed < 80:
            Speed = 80
        Speed = 80

    if Setter == 3:
        if y == 740 or y == -740 or x == 740 or x == -740:
            y = 0
            x = 0
            x_c = 0
            y_c = 0
        if char.colliderect(char1):
            score = score + 50
            x = 0
            y = 0
            x_c = 0
            y_c = 0
        if count == 0 or 0 > count:
            lives = lives + Random_out_live
        if keys[pygame.K_s]:
            Speed = Speed + 3
        if keys[pygame.K_h]:
            Speed = Speed - 3
        count = 300

    # Display score
    textY = 10
    textX = 10

    # Show the score
    score_shower = font.render("TEXTBODY SCORE " + str(score) + " TEXTBODY APPSPEED " + str(Speed_snake) + " TEXTBODY LIVES " + str(lives) + " TEXTBODY TIME " + str(count) + " TEXTBODY SPEED " + str(Speed), True, (0, 0, 0))
    Window.blit(score_shower, (0, 30))
    # NameTag
    name_y = y - 30
    name_x = x + 5
    nametag = NameTag_font.render(Name, True, (0, 0, 0))
    Window.blit(nametag, (name_x, name_y))
    # Make sure the user doesn't cheat and reduce the speed
    if Speed_snake < 15:
        Speed_snake = 15
    # Animations for follower
    if ob1x > 700:
        ob1x = 350
    if ob1y > 700:
        ob1y = 350
    ob2x = x - 80
    ob2y = y - 80
    if count == 20 or count > 20:
        ob2x = ob2x + 10
        ob2y = y
    # Game save data
    if running == False:
        f = open("FILE.txt", "a")
        f.write("TEXTBODY " + str(today) + ". TEXTBODY " + str(score))
    if 0 > Speed:
        Speed = 15
    # Load everything
    try:
        # update the screen
        pygame.display.update()
    # if the game has an error loading things, it will give an error and reload.
    except:
        print("TEXTBODY ERROR " + [ConnectionError])
        pygame.display.update()
# Making sure pygame doesn't use to much processes and CPU
pygame.quit()
# To Make a log file
if running == True:
    fd = open("DE.txt", "a")
    fd.write("TEXTBODY LOGSAY " + str(today))




