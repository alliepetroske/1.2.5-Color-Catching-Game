import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Please enter your name: ")

number_of_turtles = 5 
turtle_list = []
move_interval = 800 

score = 0
timer = 30
counter_interval = 1000 
timer_up = False

colors = ["#CB9CED", "#7E9BEB", "#F6E089", "#8EF7DD", "#FF8C62"]
sizes = [1, 2, 3, 4, 5]
font_setup = ("Arial", 20, "bold") 

#-----initialize screen-----
wn = trtl.Screen()
wn.bgcolor("#E09BCA")

#-----game functions--------

def update_score():
    global score
    score += 1
    scorewriter.clear()
    scorewriter.write(f"Score: {score}", font=font_setup, align="center")

#for every move interval, the objects will move around the screen
def move_turtles():
    if not timer_up:
        for t in turtle_list:
            new_x = rand.randint(-350, 350)
            new_y = rand.randint(-200, 200) 
            t.goto(new_x, new_y)
        wn.ontimer(move_turtles, move_interval)

def spot_clicked(x, y):
    global timer_up
    if not timer_up:
        update_score()

# make it so it says when the time is up
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up!", font=font_setup, align="center")
        timer_up = True
        for t in turtle_list:
            t.hideturtle()
        manage_leaderboard()
    else:
        counter.write(f"Timer: {timer}", font=font_setup, align="center")
        timer -= 1
        wn.ontimer(countdown, counter_interval)

def manage_leaderboard():
    global score
    lb_turtle = trtl.Turtle()
    lb_turtle.hideturtle()
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, lb_turtle, score)
    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, lb_turtle, score)

# loop to create all the objects and have them go to random location
for i in range(number_of_turtles):
    new_t = trtl.Turtle()
    new_t.shape("turtle")
    new_t.fillcolor(rand.choice(colors))
    new_t.penup()
    new_t.speed(1)
    new_t.goto(rand.randint(-300, 300), rand.randint(-200, 200))
    
 # once clicked, update score and move to new location
    def click_turtle(x, y, t=new_t):
        if not timer_up:
            update_score()
            t.fillcolor(rand.choice(colors))
            t.shapesize(rand.choice(sizes))
            t.goto(rand.randint(-300, 300), rand.randint(-200, 200))

    new_t.onclick(click_turtle)
    turtle_list.append(new_t)

# set up score writer
scorewriter = trtl.Turtle()
scorewriter.hideturtle()
scorewriter.penup()
scorewriter.goto(0, -280)

counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(0, 260) 

# start score at 0
scorewriter.write("Score: 0", font=font_setup, align="center")

#-----events----------------
wn.ontimer(countdown, counter_interval) 
wn.ontimer(move_turtles, move_interval)

wn.mainloop()