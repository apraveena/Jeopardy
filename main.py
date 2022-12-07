from turtle import *
import turtle, time, sys

s = Screen()
writer = turtle.Turtle()
reveal_answer_turtle = turtle.Turtle()
answer_turtle = turtle.Turtle()

start_x, start_y = -500, -300
board_width = 1000
board_height = 550
header_height = 50
rows = 5
cols = 5
row_height = (board_height - header_height)/rows #100
col_width = board_width / cols #120
col_start_coords = [ (-300, 200), (-300, 100), (-300, 0), (-300, -100), (-300, -200)]
first_row_first_col = [-300, -200, 200, 100]
coords = []
borders = []
col_box_borders = {}
writer.ht()
ht()
tracer(0, 0)
text_pos = (-300, 300)
first_time_reveal_answer_turtle = True
answer_turtle_pos = (start_x, -350)
reveal_ans_pos = (380, -350)


headers = ["Name\nthem!!","Operation\noperators!!", "Functions\nFun!!", "Turtles\nTime!!", "Sequences\nin Style!!"]
categories = { "col1" :
                  [
                    "Name the keyword you would use if you are importing only a variable or a function$from", 
                    "If you are a loyal python coder, then you are called a ____$Pythonista", 
                    "Name at least 4 types of operators$Arithmetic, Assignment, Relational, Logical, Membership",
                    "Name the company that Python was named after$Monty Python",
                    "Name the person who created Python$Guido Van Rossum"
                  ],
              "col2":
                  [
                    "(5%4) ** 10$1",
                    "What type of operator is '='$assignment",
                    "What type of operator is 'not'$logical",
                    "What are the seven arithmetic operators?$+, -, *, /, **, //, %",
                    "what is the result of 'not True or not True and not False'$ False"
                  ],
  
              "col3":
                  [
                    "Can you convert 'dog' to an integer?$No",
                    "What is the value sent to a function parameter called? Explain.$Argument. Only values are passed to parameters",
                    "Can a list be an element in a dictionary? Can a dictionary be an element in a list?$Yes, Yes",
                    "Is random.choice() a fruitful or void function? Explain.$Fruitful function. An element from the list is returned",
                    "How do you find the data type of variable my_var?$type(my_var)"
                  ],
               "col4":
                  [
                    "This command moves the turtle to a specific spot on the grid.$goto, eg. t.goto(x, y)", 
                    "What does turtle.Turtle() do?$Creates a new instance of the turtle",
                    "How do you get turtle's current angle?$t.heading()",
                    "Name three ways you could turn a turtle which is facing towards the east to the west$t.lt(180), t.rt(180), t.seth(180)",
                    "Which command allows keyboard click to perform an action. Explain.$s.onkey(function_name, 'key'), It requires s.listen() and s.mainloop()"
                  ],
                "col5":
                  [
                    "This command returns a series of numbers from 12 to 17$range(12, 18)",
                    "Name two immutable sequences$range, string, tuple",
                    "Best way to iterate over the sequence eg: colors = ['r','b','g']$for color in colors:",
                    "Name two ways to retrieve the last element from a sequence$list1[len(list1)] or list1[-1]",
                    "Write code to get the secret message out of '#t#e#r#c#e#S'$'#t#e#r#c#e#S'[::-2]"
                  ]
}
       
def init():
    speed(0)
    width(1)
    s.bgcolor("light green")
    s.setup(1500, 800)
    writer.penup()
    writer.goto(text_pos[0], text_pos[1])
    writer.write("** Let's play Jeopardy!! **", align = "left", font=('Arial', 20, 'bold'))
    writer.ht()
    answer_turtle.up()
    answer_turtle.goto(answer_turtle_pos)
    answer_turtle.color("blue")
    answer_turtle.ht() #necessary to duplicate this
  
def go_here(x, y):
    up()
    goto(x,y)
    down()

def draw_board():
    go_here(start_x, start_y)
    #Draw outline
    for i in range(2):
        fd(board_width)
        lt(90)
        fd(board_height)
        lt(90)
    
    seth(90)
    #Draw rows
    for i in range(5):
        for i in range(2):
            fd(row_height)
            rt(90)
            fd(board_width)
            rt(90)
        fd(row_height)
    
    #Draw columns
    goto(start_x, start_y + board_height)
    seth(0)
    for i in range(4):
        for i in range(2):
            fd(col_width)
            rt(90)
            fd(board_height)
            rt(90)
        fd(col_width)
    
def write_headings():
    move_from_start = 0
    for header in headers:
        go_here(move_from_start + start_x + (col_width/2) - 30, ((start_y + board_height) - (header_height/2)-20))
        write(header, align = "Center", font = ('Arial', 10, 'bold'))
        move_from_start += col_width
        
def write_scores():
    score = 0
    score_increment = 100
    for i in range(5):
        score += score_increment #100, 200, 300, 400, 500
        number_pos = (start_y + (board_height - header_height)) - (i * row_height) #200
        go_here(start_x, number_pos)
        
        penup()
        seth(270)
        fd(row_height/2)
        seth(0)
        fd(col_width/2)
        pendown()
        
        for j in range(5):
            write(score, align = "Center")
            penup()
            fd(col_width)
            pendown()
        
       
def load_coordinates():
    col =  1
    for j in range(5): #each row
        for i in range(5): #each column
            key = "col" + str(col) + "row" + str(i + 1)
            borders = []
            box_start_y = (start_y + (board_height - header_height)) - (i * row_height)
            box_start_x = start_x + (j * col_width)
            borders.append(box_start_x)
            borders.append(box_start_x + col_width)
            borders.append(box_start_y)
            borders.append(box_start_y - row_height)
            col_box_borders[key] = borders
        col = col + 1

question_count = 0

def reveal_answer_area():
    reveal_answer_turtle.ht()
    reveal_answer_turtle.up()
    reveal_answer_turtle.goto(reveal_ans_pos)
    reveal_answer_turtle.color("blue")
    reveal_answer_turtle.write("Reveal answer", move = True, font = ("Arial", 12, "bold"))
    

def screen_clicked(x, y):
    global question_count, answer, first_time_reveal_answer_turtle
    
    tracer(1)
        
    for key, value in col_box_borders.items():
        left_x = value[0]
        right_x = value[1]
        top_y = value[2]
        bottom_y = value[3]

        if question_count > 25:
            writer.undo()
            writer.undo()
            writer.write("**All done**", align = "Center", font=('Arial', 12, 'bold'))
            writer.ht()
            break
        
        #if clicked on reveal answer
        if x >= reveal_ans_pos[0] and x <= reveal_ans_pos[0] + 130 and y >= reveal_ans_pos[1] and y <= reveal_ans_pos[1] + 50 and answer != "":
            answer_turtle.ht()
            answer_turtle.write(answer, font = ("Arial", 14, "bold", "underline"))
            break
            
        #If clicked on one of the cells
        if x >= left_x and x <= right_x and y <= top_y and y >= bottom_y:
            writer.undo()
            writer.undo()
            answer_turtle.undo() 
            #TODO: Do not increment if clicked on same cell
            question_count += 1
            col = key[:4]
            row = int(key[-1])-1
            
            #write the question on the screen
            question = categories[col][row].split("$")[0]
            answer = categories[col][row].split("$")[1]
            writer.penup()
            writer.goto(text_pos[0], text_pos[1])
            writer.color("red")
            writer.write(str(question_count)+ ". " + question, align = "left", font=('Arial', 16, 'bold'))
            writer.ht()           
            
            go_here(left_x, bottom_y)
            seth(90)
            color("black","light blue")
            begin_fill()
            for i in range(2):
                fd(row_height)
                rt(90)
                fd(col_width)
                rt(90)
            end_fill()
            
        
def main():
    init()
    draw_board()
    write_headings()
    write_scores()
    load_coordinates()
    reveal_answer_area()
    s.onclick(screen_clicked)
    update()
    
main()
s.mainloop()




