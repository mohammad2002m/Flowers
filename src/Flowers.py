import math
import pygame , sys
from InputBox import InputBox
from Button import Button
import random

pygame.init()

WIDTH , HEIGHT = (700 , 700)
BORDER_HEIGHT = 5
RANGE = 620
SIDE = 300


screen = pygame.display.set_mode((700, 700))
Border = pygame.Rect(0 , 625, WIDTH , BORDER_HEIGHT)
radius = 1

#exit
#start button
#stop button
#clear button
#Counter

#number of starting points
#ratio of distance
#Speed/FrameRate

#Point
Points = []
frame_rate = 100
ColorsP = []
ColorsR = []
NumberOfDots = 500
Colors = []
delay = 0

def RandomColor():
    return (255 , 255 , 255)


COUNTER_FONT = pygame.font.SysFont('comicsans', 20)

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def DrawPoint(speed , angle):
    global Points , Counter , delay
    #clear

    if (Counter < NumberOfDots):
        Counter += 1
    else:
        return 

    center = (0 , pygame.Vector2(WIDTH / 2 , 350))

    if len(Points) == 0:
        Points.append(center)
        Colors.append(RandomColor())
    else:
        if delay % 3 == 0:
            for P in Points:
                P[1].x += math.cos(P[0]) * speed
                P[1].y += math.sin(P[0]) * speed
        
        delay = (delay +  1) % 3
        
        Last = Points[-1]
        new_angle = Last[0] + 2 * angle * math.pi
        print(speed)
        Points.append((new_angle, pygame.Vector2(center[1].x + math.cos(new_angle) * speed , center[1].y + math.sin(new_angle) * speed)))
        Colors.append(RandomColor())
        pass

def DrawAndRender(StartButton, ClearButton , ExitButton, input_boxes , Points , radius):
    screen.fill((30 , 30 , 30))

    StartButton.draw(screen)
    ClearButton.draw(screen)
    ExitButton.draw(screen)

    pygame.draw.rect(screen, pygame.Color("white") , Border)
    screen.blit(COUNTER_FONT.render(str(Counter) , 1 ,  pygame.Color("white")) , (5 , 5))

    #Draw The Screen
    for box in input_boxes:
        box.draw(screen)

    for i in range(0 , len(Points)):
        P = Points[i]
        C = Colors[i]
        pygame.draw.circle(screen, C , (P[1].x , P[1].y) , radius , 0)

    pygame.display.update()


radius = InputBox(10, WIDTH - 60, 150, 55 , "3")
speed = InputBox(170, WIDTH - 60, 150, 55 , "1")
angle = InputBox(330, WIDTH - 60, 150, 55 , "0.61803398875")
input_boxes = [speed , angle , radius]

real_radius = 3
real_speed = 1
real_angle = (math.sqrt(5) + 1) / 2

def main():
    global Points  , frame_rate , Counter , real_angle , real_radius , real_speed

    clock = pygame.time.Clock()
    Points = []

    screen.fill((30, 30, 30))


    #Buttons
    StartButton = Button(pygame.Color("white"), 490 , WIDTH - 60, 75, 25 , "Start")
    ClearButton = Button(pygame.Color("white"), 570 , WIDTH - 60, 75, 25 , "Clear")
    ExitButton = Button(pygame.Color("white"), 490 , WIDTH - 30, 75, 25 , "Exit")

    #Counter
    Counter = 0
    DrawNext = False

    while True:
        clock.tick(frame_rate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for box in input_boxes:
                box.handle_event(event)

            if ExitButton.isOver(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

            if StartButton.isOver(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and DrawNext == False:
                #check validty of input
                if radius.text.isnumeric() and speed.text.isnumeric() and is_float(angle.text) and float(angle.text) <= 1:
                    real_radius = int(radius.text)
                    real_speed = int(speed.text)
                    real_angle = float(angle.text)
                    DrawNext = True

            if ClearButton.isOver(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                main()

        
        if (Counter > NumberOfDots):
            DrawNext = False

        if DrawNext == True:
                DrawPoint(real_speed , real_angle)

        DrawAndRender(StartButton , ClearButton , ExitButton, input_boxes , Points , real_radius)


        


main()