import curses
import os
import sys

def do_it(win):  # Shia LeBeouf!
    curses.start_color()

    # curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # matrix
    #curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED) # coke
    #curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE) # blue
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_MAGENTA) # purple
    win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)

# Make a function to print a line in the center of screen

def printCenter(message,Screen):
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 2)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    Screen.addstr(middle_row, x_position, message)
    return 0


def printCenterPlus(message,Screen,plus):
    plus = int(plus)
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 2.5)

    # Calculate center column, and then adjust starting position based
    # on the length of the message

    middle_column = int(num_cols / 3)
    x_position = middle_column -len('Project List') 


    middle_row += plus
    # Draw the text
    if  middle_row > int(num_rows / 1.2) -3:
        Screen.addstr( int(num_rows / 1.2) -1, x_position, '.......  use "run in mode more"') 
    else:
        Screen.addstr(middle_row , x_position, message)
    return 0


def printTop(message,Screen):
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 3)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    Screen.addstr(middle_row, x_position, message)
    return 0

def printBottomCenter(message,Screen):
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 1.5)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    Screen.addstr(middle_row, x_position, message)
    return 0
       
def printBottom(message,Screen):
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 1.05)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 8)
    x_position = middle_column - half_length_of_message

    # Draw the text
    Screen.addstr(middle_row -2, x_position, message)
    return 0

def printFooterLeft(message,Screen):
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 1.05)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 8)
    x_position = middle_column - half_length_of_message

    # Draw the text
    Screen.addstr(middle_row, x_position, message)
    return 0
def printFooterRight(message,Screen):
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 1.05)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 1.2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    Screen.addstr(middle_row, x_position, message)
    return 0
    
def printFooter(message,Screen):
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 1.05)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    Screen.addstr(middle_row, x_position, message)
    return 0
    
def my_raw_input(message,Screen):
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 1.2)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    curses.echo() 
    Screen.addstr(middle_row, x_position, message)
    Screen.refresh()
    inputt = Screen.getstr(middle_row + 1,x_position, 5) #       ^^^^  reading input at next line 
    return inputt
    
def my_int_input(message,Screen, errorFlag):
    num_rows, num_cols = Screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 1.2)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message
    
    if errorFlag:
        messageError = 'Error Insert a Valid Option' 
        x_position2= middle_column - int(len(messageError)/2)
        Screen.addstr(middle_row -2,x_position2,messageError)
        Screen.addstr(middle_row +1,x_position,'        ')
        curses.echo() 
    Screen.addstr(middle_row, x_position, message)
    Screen.refresh()
    inputt = Screen.getstr(middle_row + 1,x_position, 5) #       ^^^^  reading input at next line 

    try:
        return int(inputt)
    except ValueError:
        return my_int_input(message,Screen,True)