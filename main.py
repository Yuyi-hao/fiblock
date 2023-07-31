from raylib import *
from pyray import Color, Rectangle
import datetime 

WIDTH = 800
HEIGHT = 600

dct = {
    'red': RED,
    'blue': BLUE,
    'green': GREEN,
    'white': WHITE
}

def get_block_colors(hours, minutes):
    res = ["white"]*5
    hours = hours%12
    minutes = minutes - (minutes%5)

    # hours 
    if hours >= 5:
        res[-1] = "red"
        hours -= 5
    if hours >= 3:
        res[-2] = "red"
        hours -= 3
    if hours >= 2:
        res[-3] = "red"
        hours -= 2
    if hours >= 1:
        res[-4] = "red"
        hours -=1 
    if hours >= 1:
        res[-5] = "red"
        hours -=1
    if hours > 0:
        print("hours", hours)
        return "ERROR"

    # minute 
    if minutes >= 25:
        if res[-1] != "white":
            res[-1] = "green"
        else:
            res[-1] = "blue"
        minutes -= 25


    if minutes >= 15:
        if res[-2] != "white":
            res[-2] = "green"
        else:
            res[-2] = "blue"
        minutes -= 15

    if minutes >= 10:
        if res[-3] != "white":
            res[-3] = "green"
        else:
            res[-3] = "blue"
        minutes -= 10

    if minutes >= 5:
        if res[-4] != "white":
            res[-4] = "green"
        else:
            res[-4] = "blue"
        minutes -= 5

    if minutes >= 5:
        if res[-5] != "white":
            res[-5] = "green"
        else:
            res[-5] = "blue"
        minutes -= 5

    if minutes > 0:
        return "ERROR"

    

    return res



def draw_fibonacci_rectangle(x, y, width, height, sequence):
    # [1, 1, 2, 3, 5]
    DrawRectangle(x+3*90, y, 90*5, 90*5, dct[sequence[-1]])
    DrawRectangle(x, y+2*90, 90*3, 90*3, dct[sequence[-2]])
    DrawRectangle(x, y, 2*90, 2*90, dct[sequence[-3]])
    DrawRectangle(x+2*90, y, 90, 90, dct[sequence[-4]])
    DrawRectangle(x+2*90, y+90, 90, 90, dct[sequence[-5]])


def get_time():
    lst = []
    time = datetime.datetime.now()
    lst.append(time.hour)
    lst.append(time.minute)
    lst.append(time.second)
    return lst

def draw_legend(x, y, width, height, color_code):
    keys = list(color_code.keys())
    # hours 
    DrawRectangle(x, y, 15, 15, color_code[keys[0]])
    DrawText(keys[0].encode('utf-8'), x+30, y, 15, WHITE)
    # minute 
    DrawRectangle(x+240, y, 15, 15, color_code[keys[1]])
    DrawText(keys[1].encode('utf-8'), x+30+240, y, 15, WHITE)
    # both 
    DrawRectangle(x+480, y, 15, 15, color_code[keys[2]])
    DrawText(keys[2].encode('utf-8'), x+30+480, y, 15, WHITE)


def main():
    sequence = ['red', 'blue', 'green', 'blue', 'white']
    InitWindow(WIDTH, HEIGHT, b"Asian Clock")
    rect = Rectangle(40, 530, 720, 30)
    while(not WindowShouldClose()):
        BeginDrawing()
        ClearBackground((74, 45, 74, 1))
        width_text = MeasureText(b"Fibonacci Clock", 20)
        DrawText(b"Fibonacci Clock", int((WIDTH - width_text)/2), 10, 20, VIOLET)
        hours, minutes, seconds = get_time()
        sequence = get_block_colors(hours, minutes)
        draw_fibonacci_rectangle(40, 40, WIDTH-20, HEIGHT-60, sequence)
        draw_legend(40, 500, 720, 15, {'Hour':RED, 'Minute': BLUE, 'BOTH': GREEN})
        DrawRectangleRounded(rect, 0.5, 32 , RED)
        # print(get_time())
        EndDrawing()
    CloseWindow()
    
    

if __name__=="__main__":
    main()


