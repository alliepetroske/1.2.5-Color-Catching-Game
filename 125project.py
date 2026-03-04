#Import turtle
#Import random module
#Import our own leaderboard module


import turtle as trtl
import random as rand
import leaderboard as lb


#Game configuration
#Define the leaderboard file’s name
leaderboard_file_name = "a122_leaderboard.txt"
#Ask the player for their name with an input
player_name = input("Please enter your name: ")


#Define the number of turtles
number_of_turtles = 5
turtle_list = []
move_interval = 800


#Make the score 0 as the initial score
score = 0
#Set the timer to 30 seconds
timer = 30
counter_interval = 1000
timer_up = False


#Define the list of colors
colors = ["#CB9CED", "#7E9BEB", "#F6E089", "#8EF7DD", "#FF8C62"]
#Define the list of the different turtle sizes
sizes = [1, 2, 3, 4, 5]
#Make the font for the timer and the score
font_setup = ("Arial", 20, "bold")


#Initialize the screen and make background
wn = trtl.Screen()
wn.bgcolor("#E09BCA")


#Functions


#Define a function for updating the score each time the player clicks the turtle
def update_score():
    global score
    #Score increases by 1 point each time
    score += 1
    #Clear the score writer
    scorewriter.clear()
    #Write the score in its allocated position
    scorewriter.write(f"Score: {score}", font=font_setup, align="center")


#For every move interval, the objects will move around the screen
def move_turtles():
    #If the timer isn’t up:
    if not timer_up:
        #For each thing in the turtle list:
        for t in turtle_list:
            #Set each turtle to go to a random location
            new_x = rand.randint(-350, 350)
            new_y = rand.randint(-200, 200)
            t.goto(new_x, new_y)
        #On the timer, go to the location
        wn.ontimer(move_turtles, move_interval)


#Define a function for the spot clicked
def spot_clicked(x, y):
    global timer_up
    if not timer_up:
        update_score()


#Define a function for the countdown
def countdown():
    global timer, timer_up
    counter.clear()
    #If the timer is less than or equal to 0:
    if timer <= 0:
        #Write “Time’s Up!” in the selected font
        counter.write("Time's Up!", font=font_setup, align="center")
        timer_up = True
        for t in turtle_list:
            t.hideturtle()
        #Manage the leaderboard
        manage_leaderboard()
    else:
        #Show the active timer in the selected font
        counter.write(f"Timer: {timer}", font=font_setup, align="center")
        #Keep decreasing the timer by 1
        timer -= 1
        wn.ontimer(countdown, counter_interval)




#Define a function to manage the leaderboard:
def manage_leaderboard():
    global score
    lb_turtle = trtl.Turtle()
    lb_turtle.hideturtle()
    #Get the names from the leaderboard’s file
    #Get the scores from the leaderboard file
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)
    #If the length of the leader scores is <5 or if the score is > than the last score in the file:
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        #Update the score
        #Draw the leaderboard
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, lb_turtle, score)
    else:
        #Don’t draw the leaderboard
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, lb_turtle, score)


#For every thing in the number of turtles list:
for i in range(number_of_turtles):
    #There’s a new turtle
    new_t = trtl.Turtle()
    #Random color and shape
    new_t.shape("turtle")
    new_t.fillcolor(rand.choice(colors))
    new_t.penup()
    #Speed is 1
    new_t.speed(1)
    #Go to a random location
    new_t.goto(rand.randint(-300, 300), rand.randint(-200, 200))
   
 #Define a function for when the player clicks on the turtle
    def click_turtle(x, y, t=new_t):
        #If the timer isn’t up:
        if not timer_up:
            #Update the score
            #Turtle gets a random color and shape
            #Turtle goes to a random location
            update_score()
            t.fillcolor(rand.choice(colors))
            t.shapesize(rand.choice(sizes))
            t.goto(rand.randint(-300, 300), rand.randint(-200, 200))


    new_t.onclick(click_turtle)
    turtle_list.append(new_t)


#Define scorewriter as the turtle  
scorewriter = trtl.Turtle()
#Scorewriter hides the turtle\  
scorewriter.hideturtle()
scorewriter.penup()
#Scorewriter goes to a certain position
scorewriter.goto(0, -280)




#Timer (counter) is another turtle
counter = trtl.Turtle()
#Counter's turtle is hidden
counter.hideturtle()
counter.penup()
#Counter goes to its location
counter.goto(0, 260)


#Scorewriter writes Score = 0 currently
scorewriter.write("Score: 0", font=font_setup, align="center")


#Events




#Screen sets the timer
wn.ontimer(countdown, counter_interval)
#Screen moves the turtles
wn.ontimer(move_turtles, move_interval)


#Mainloop displays the screen
wn.mainloop()
