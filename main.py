from raylib import *
from pyray import  Rectangle, Font
import datetime 

WIDTH = 800
HEIGHT = 630

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

    fibonacci_series = [5, 3, 2, 1, 1]

    for idx, value in enumerate(fibonacci_series):
        if hours >= value:
            res[-(idx+1)] = "red"
            hours -= value 

    for idx, value in enumerate(fibonacci_series):
        if minutes >= value*5:
            if res[-(idx+1)] != "white":
                res[-(idx+1)] = "green"
            else:
                res[-(idx+1)] = "blue"
            minutes -= value*5 

    return res



def draw_fibonacci_rectangle(x, y, width, height, sequence):
    DrawRectangle(x, y, 90*8, 90*5, BLACK)
    DrawRectangle(x+3*90+3, y+5, 90*5-10, 90*5-10, dct[sequence[-1]])
    DrawRectangle(x+5, y+2*90+5, 90*3-10, 90*3-10, dct[sequence[-2]])
    DrawRectangle(x+5, y+5, 2*90-10, 2*90-10, dct[sequence[-3]])
    DrawRectangle(x+2*90+5, y+5, 90-10, 90-10, dct[sequence[-4]])
    DrawRectangle(x+2*90+5, y+90+5, 90-10, 90-10, dct[sequence[-5]])


def get_time():
    lst = []
    time = datetime.datetime.now()
    lst.append(time.hour)
    lst.append(time.minute)
    lst.append(time.second)
    lst.append(time.strftime("%p"))
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


def draw_minute_bar(seconds):
    rect = Rectangle(40, 530, 600, 30)
    rect_passed = Rectangle(40, 530, seconds*(600//(5*60)), 30)
    DrawRectangleRounded(rect, 0.5, 32 , RED)
    DrawRectangleRounded(rect_passed, 0.5, 32 , GREEN)
    factor = 600//(60*5)
    for i in range(5):
        DrawRectangle(40+(i*60*factor), 530, 5, 30, WHITE)


def show_time(hours, minutes, seconds, am_or_pm):
    time_string = f"{str(hours).zfill(2)}: {str(minutes).zfill(2)}: {str(seconds).zfill(2)} {am_or_pm}"
    DrawText(time_string.encode('utf-8'), 650+5, 530+5, 20, RED)

def show_command():
    DrawText(b"Press h for help. m to return to main page. q to quite", 40, 580, 18, PINK)


def draw_main_page():
    hours, minutes, seconds, am_or_pm = get_time()
    sequence = get_block_colors(hours, minutes)
    draw_fibonacci_rectangle(40, 40, WIDTH-20, HEIGHT-60, sequence)
    draw_legend(40, 500, 720, 15, {'Hour':RED, 'Minute': BLUE, 'BOTH': GREEN})
    draw_minute_bar(seconds + ((minutes%5)*60))
    show_time(hours, minutes, seconds, am_or_pm)
    show_command()

def draw_help_page(help_file, custom_font):
    text = ""
    with open(help_file, 'r') as file:
        if file == None:
            text = "Can't open help file"
        else:
            text = file.read()
    DrawTextEx(custom_font, text.encode('utf-8'), (40, 40), 15, 0, WHITE)

def main():
    sequence = ['white', 'white', 'white', 'white', 'white']
    InitWindow(WIDTH, HEIGHT, b"Asian Clock")
    custom_font_help = LoadFont(b"fonts/Roboto-Medium.ttf")
    heading_font = LoadFont(b"fonts/Kalam-Regular.ttf")
    current_page = "main_page"
    while(not WindowShouldClose()):
        BeginDrawing()
        ClearBackground((74, 45, 74, 1))
        width_text = MeasureTextEx(heading_font, "Fibonacci Clock".encode('utf-8'), 40, 0).x
        DrawTextEx(heading_font, b"Fibonacci Clock", (int((WIDTH - width_text)/2), 10), 40, 0, VIOLET)
        if(IsKeyPressed(KEY_H)):
            current_page = "help_page"
        elif (IsKeyPressed(KEY_M)):
            current_page = "main_page"
        elif (IsKeyPressed(KEY_Q)):
            exit()

        if current_page == "main_page":
            draw_main_page()
        elif current_page == 'help_page':
            draw_help_page('instructions.txt', custom_font_help)

        EndDrawing()
    CloseWindow()
    
    

if __name__=="__main__":
    main()


