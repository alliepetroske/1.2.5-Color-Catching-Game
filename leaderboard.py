# leaderboard.py
# set the levels of scoring
#Bronze is 37
bronze_score = 37


#silver is 40
silver_score = 40


#gold is 41
gold_score = 41




#Define a function to get names from the leaderboard file (defined in the main file)
#open file
def get_names(file_name):
  leaderboard_file = open(file_name, "r")  




 #For each line in the leaderboard file:
  names = []
  for line in leaderboard_file:
    leader_name = ""
    #Start index at 0
    index = 0




#While the character isn’t a comma:
    while (line[index] != ","):
      leader_name = leader_name + line[index]
      #Increase the index


      index = index + 1
#Add the completed name to the names list
    print("leader:" + leader_name)
    names.append(leader_name)
#return the names list 
   
  return names




 
# Define a function to get the scores
def get_scores(file_name):
  #open file
  leaderboard_file = open(file_name, "r")  # be sure you have created this



  #create empty list for the scores
  scores = []
  for line in leaderboard_file:
    leader_score = ""    
    #start at index 0
    index = 0



    #most past the comma
    while (line[index] != ","):
      index=index+1
    index=index+1




    #while the character isnt a new line
    while (line[index] != "\n"):
      #add character to the score
      leader_score= leader_score + line[index]
      #increase the index
      index = index+1
    #add the scores to the scores list
    #convert score to an integer
    print("Score:", leader_score)
    scores.append(int(leader_score))
   
   
  leaderboard_file.close()




  #return the list of scores
  return scores




#Define a function to update the leaderboard

def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):



#start index at 0
  index = 0
  # loop through the leaderboard scores
 
  for index in range(len(leader_scores)):


    # If the player’s score is more than the current score:

    if (player_score >= leader_scores[index]):

      #stop the loop
      break
    else:
      index = index + 1


 
	#Insert the player’s score in the leader scores
	#Insert the player’s name in the leader names
  leader_scores.insert(index, player_score)
  leader_names.insert(index, player_name)


  #If list in longer than 5
  if (len(leader_names) > 5):
    #remove last name
    leader_names.pop(5)
    #remove last score
    leader_scores.pop(5)




  #Rewrite the updated leaderboard
  leaderboard_file = open(file_name, "w")  
 
  for index in range(len(leader_names)):


    leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")

    #close the file
  leaderboard_file.close()
   


#Define a function to draw the leaderboard

def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
 
  # clear turtle screen
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  #move turtle to starting position
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()




  # for each player in leaderboard:
  for index in range(len(leader_names)):
    #Write rank, name, and score
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
 
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()




  # If player’s score is high enough for leaderboard:
  if (player_score >= leader_scores[index]):
    #Write congratulations message
    turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
  else:
    #  Write sorry message
    turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)
 


  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
 
  # Check medal levels:
  #  If within bronze range, write bronze message
  if (player_score >= bronze_score and player_score < silver_score):
    turtle_object.write("You earned a bronze medal!", font=font_setup)
  #  If within silver range, write silver message
  elif (player_score >= silver_score and player_score < gold_score):
    turtle_object.write("You earned a silver medal!", font=font_setup)
  #  If within gold range, write gold message
  elif (player_score >= gold_score):
    turtle_object.write("You earned a gold medal!", font=font_setup)

