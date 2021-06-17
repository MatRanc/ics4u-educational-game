import os
import random
import time

class PlayerCircle(object):
    def __init__(self, x_pos, y_pos, scale):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale

    def display(self):
        fill(19, 43, 83, 220)
        ellipse(self.x_pos, self.y_pos, 330 * self.scale, 85 * self.scale)
        fill(182, 255, 252)
        ellipse(self.x_pos, self.y_pos, 300 * self.scale, 75 * self.scale)

class Player(object):
    def __init__(self, x_pos, y_pos, name, shield_level, health_level, model, model_scale):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name
        self.shield_level = shield_level
        self.health_level = health_level
        self.model = model
        self.model_scale = model_scale

    def display(self):
        img = loadImage(self.model)
        imageMode(CENTER)
        img.resize(int(0 * self.model_scale), int(500 * self.model_scale))
        image(img, self.x_pos, self.y_pos - (img.height/2))

class RectButton(object):
    def __init__(self, x_pos, y_pos, x_size, y_size, words, txt_size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_size = x_size
        self.y_size = y_size
        self.words = words
        self.txt_size = txt_size
    def display(self):
        fill(255)
        rect(self.x_pos, self.y_pos, self.x_size,self.y_size)
        fill(0)
        textSize(self.txt_size)
        text(self.words,self.x_pos,self.y_pos, self.x_size, self.y_size)

    def over_but(self):
         if mouseX in range(self.x_pos, self.x_pos + self.x_size) and mouseY in range(self.y_pos, self.y_pos + self.y_size):
             return True
         else:
             return False



class HealthBar(object):
    def __init__(self, x_pos, y_pos, health_level, shield_level):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health_level = health_level
        self.shield_level = shield_level

    def display(self):
        #background of health bar
        fill(255, 230, 230)
        rect(self.x_pos, self.y_pos + 20, 200, 10)

        #main health bar
        fill(255, 60, 60)
        rect(self.x_pos, self.y_pos + 20, 200 * self.health_level / 100, 10)

        #health text
        textSize(15)
        text(self.health_level, self.x_pos - 30, self.y_pos + 22)

        #background shield bar
        fill(210, 210, 255)
        rect(self.x_pos, self.y_pos, 200, 10)

        #main shield bar
        fill(60, 60, 255)
        rect(self.x_pos, self.y_pos, 200 * self.shield_level / 100, 10)

        #shield text
        textSize(15)
        text(self.shield_level, self.x_pos - 30, self.y_pos + 2)

class Question(object):
    def __init__(self, question, correct_answer, answer_2, answer_3, answer_4):
        self.question = question
        self.correct_a = correct_answer
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4

class GalleryButton(object):
    def __init__(self, x_pos, y_pos, scale, x_dir):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale
        self.x_dir = x_dir
        self.counter = 0

        self.circle_x = (self.x_pos + (12/2 * self.x_dir)) * self.scale
        self.circle_y = (15/2 + self.y_pos) * self.scale

    def display(self):
        fill(255)
        circle(self.circle_x, self.circle_y, 30 * self.scale)

        fill(255, 255, 20)
        triangle(self.x_pos * self.scale, self.y_pos * self.scale, self.x_pos * self.scale, (15 + self.y_pos) * self.scale, (self.x_pos + (15 * self.x_dir))* self.scale, (15/2 + self.y_pos) * self.scale)

    def over_circle(self):
        if mouseX in range(self.circle_x - 15, self.circle_x + 15) and mouseY in range(self.circle_y - 15, self.circle_y + 15):
            return True
        else:
            return False


class QuestionButton(object):
    def __init__(self, x_pos, y_pos, scale, question):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale
        self.question = question

    def display(self):
        fill(250, 250, 10)
        rect(self.x_pos, self.y_pos, 200, 50)
        fill(0)
        textSize(15)
        text(self.question, self.x_pos+100, self.y_pos+25)
        textAlign(CENTER, CENTER)


############### class templates end #######################

#functions

def read_file_to_list_questions(file_name):
    file = open(file_name, "r")
    file_list = file.read().splitlines()
    file.close()
    questions_list = []

    print(len(file_list))

    for x in range(0, len(file_list), 6):
        sub_list = []
        for y in range(0, 6):
            sub_list.append(file_list[x+y])
        questions_list.append(sub_list)

    return questions_list

def questions_ui(questions_list):
    rand_int = random.randrange(0, len(questions_list))

    question_boxes = []
    
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(15)
    text(questions_list[rand_int][0], 660, 515)

    for x in range(0, 4):
        if x < 2:
            question_boxes.append(QuestionButton(450 + (225*x), 550, 1, questions_list[rand_int][x+1]))
        else:
            question_boxes.append(QuestionButton(450 + (225*(x-2)), 625, 1, questions_list[rand_int][x+1]))

    for x in question_boxes:
        x.display()
        
    return question_boxes






###### FUNCTIONS END #########


questions_list = read_file_to_list_questions("questions.txt")
#print(questions_list)

game_state = 1

main_player_character_list = os.listdir("assets/characters/playable/")  #gets all pngs for playable characters

main_player_character_selection = 0
main_player_character_selection_fullpath = "assets/characters/playable/" + main_player_character_list[main_player_character_selection]

circle_opp = PlayerCircle(1025, 350, 1.23)
circle_main_player = PlayerCircle(400, 500, 1.50)

opp_ninja = Player(circle_opp.x_pos, circle_opp.y_pos, "Tyler \"Ninja\" Blevins", 100, 100, "assets/characters/opponents/ninjablevins.png", 0.6)
opp_souljaboy = Player(circle_opp.x_pos, circle_opp.y_pos, "Soulja Boy", 100, 100, "assets/characters/opponents/souljaboy.png", 0.60)

opp_list  = [[opp_ninja, opp_souljaboy]]

#set current opponent so they can be changed out easier?
current_opp = opp_souljaboy

main_player = Player(400, 550, "Please enter a name", 100, 100, main_player_character_selection_fullpath, 0.8)

opp_health_bar = HealthBar(current_opp.x_pos-350, current_opp.y_pos-200, current_opp.health_level, current_opp.shield_level)
main_player_health_bar = HealthBar(main_player.x_pos - 350, main_player.y_pos - 200, main_player.health_level, main_player.shield_level)

next_character_button = GalleryButton(50+140, 500, 1, 1)
back_character_button = GalleryButton(25+140, 500, 1, -1)
start_button = RectButton(540,300,200,100, "Ready up", 40)

def main_menu():
    game_state = 1
    background(100, 100, 255)

    #title on screen
    title = "Canadian History Fortnite Pokemon Education Game (placeholder)"
    fill(255)
    textAlign(CENTER)
    textSize(20)
    text(title, 640-(250/2), 150, 250, 100)
    #text(string, x pos, y pos, container width, container height)

    next_character_button.display()
    back_character_button.display()
    start_button.display()
    #character selection
    full_counter = next_character_button.counter + back_character_button.counter

    if full_counter < 0:
        full_counter = len(main_player_character_list) - 1
        back_character_button.counter = len(main_player_character_list) - 1
        next_character_button.counter = 0

    if full_counter > len(main_player_character_list) - 1:
        full_counter = 0
        next_character_button.counter = 0
        back_character_button.counter = 0

    main_player_character_selection = full_counter
    main_player_character_selection_fullpath = "assets/characters/playable/" + main_player_character_list[main_player_character_selection]

    img = loadImage(main_player_character_selection_fullpath)
    imageMode(CENTER)
    img.resize(0, 250)
    image(img, 180, 350)

    main_player.model = main_player_character_selection_fullpath

current_round = 0

def battle_ui():
    global current_opp
    circle_opp.display()
    circle_main_player.display()

    current_opp.display()
    main_player.display()

    opp_health_bar.display()
    main_player_health_bar.display()

    #bottom box
    fill(100, 150, 200)
    rect(0, 720-226, 1279, 225)



class Notification(object):
    def __init__(self, x_pos, y_pos, show, show_time_seconds, input_text):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.show = show
        self.input_text = input_text
        self.counter = 0
        self.show_time = show_time_seconds
        
    def display(self):
        if self.show == True and self.counter < self.show_time:
            fill(255, 255, 10)
            rect(400, 25, 500, 100)
            fill(0)
            textSize(20)
            text(self.input_text, 400, 50, 500, 100)
        self.counter += 0.1


if current_round != 4:
    if current_round in [0,1]:
        current_opp = opp_list[0][random.randrange(0,1)]
    
    
    hit_or_get_hit = [0,0,1]
    
    enemy_noti = Notification(400, 100, False, 5, "You have encountered " + current_opp.name)
    if random.choice(hit_or_get_hit) == 0:
        enemy_noti.show = True
    else:
        enemy_noti.input_text = "You have been hit by " + current_opp.name + " for DAMAGE"
        enemy_noti.show_time = 10
        enemy_noti.show = True
        
        
        
        
        

def setup():
    size(1280, 720)

def draw():
    background(245)

    if game_state == 1:
        main_menu()
    elif game_state == 2:
        battle_ui()
        enemy_noti.display()


def mouseClicked():
    global game_state
    if game_state == 1:
        start_button.over_but()
        if next_character_button.over_circle() == True:
            next_character_button.counter += 1
        if back_character_button.over_circle() == True:
            back_character_button.counter -= 1
        if start_button.over_but() == True:
            game_state = 2
