import os
import random
import time

# during battle_ui, what png's "stand" on
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
    def __init__(self, x_pos, y_pos, name, health_level, model, model_scale):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name
        self.health_level = health_level
        self.model = model
        self.model_scale = model_scale

    def display(self):
        img = loadImage(self.model)
        imageMode(CENTER)
        img.resize(int(0 * self.model_scale), int(500 * self.model_scale))
        image(img, self.x_pos, self.y_pos - (img.height/2))
        
        HealthBar(self.x_pos - 350, self.y_pos - 200, self.health_level).display()

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
    def __init__(self, x_pos, y_pos, health_level):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health_level = health_level

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
        self.question = question

    def display(self):
        fill(250, 250, 10)
        rect(self.x_pos, self.y_pos, 1239, 40)
        fill(0)
        textSize(15)
        textAlign(CENTER, CENTER)
        text(self.question, self.x_pos+620, self.y_pos+25)
        
    def over_button(self):
        if mouseX in range(self.x_pos, self.x_pos+1239) and mouseY in range(self.y_pos, self.y_pos+40):
            return True
        else:
            return False

class QuestionDisplay(object):
    def __init__(self, x_pos, y_pos, question):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.question = question
        
    def display(self):
        fill(250, 250, 10)
        ellipse(self.x_pos, self.y_pos, 500, 60)
        fill(0)
        textSize(15)
        textAlign(CENTER, CENTER)
        text(self.question, self.x_pos -(500/2), self.y_pos - (60/2), 500, 60)
        
        #rect(750, 0, 1, 2000) #just to display where the center of the elipse is

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
        if self.counter > self.show_time:
            self.show = False
        
class ActionBox(object):
    def __init__(self, x_pos, words):
        self.words = words
        self.x_pos = x_pos
        
    def display(self):
        fill(255,255,10)
        rect(self.x_pos,550,150,150)
        textSize(30)
        fill(0,0,0)
        textAlign(CENTER,CENTER)
        text(self.words, self.x_pos + 75, 620)
        
    def over_but(self):
        if mouseX in range(self.x_pos, self.x_pos+150) and mouseY in range(550, 700):
            return True
        else:
            return False
        
############### class templates end #######################


weapons_list  = [["Pickaxe", 10],
                 ["Pistol", [10, 15]],
                 ["Tac Shotgun", [5, 15, 20]],
                 ["Assault Rifle", [15, 20]],
                 ["Supressed Pistol", [15, 20]],
                 ["Hand Cannon", [0, 0, 50, 50, 50]],
                 ["Heavy Shotgun", [15, 30, 35, 40]],
                 ["Bolt Action Sniper", [0, 90]],
                 ["Tac Smg", [15, 20, 25]],
                 ["Minigun", [10, 15, 20]],
                 ["Gold Scar", [35, 40, 45, 50, 55]],
                 ["19 Dollar Fortnite Card", [30, 35, 70]]
                 ]


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


def questions_ui():
    global need_question
    global current_question
    global questions_list
    
    if need_question == True:
        current_question = random.randrange(0, len(questions_list))
        need_question = False

    question_asked = QuestionDisplay(750, 50, questions_list[current_question][0]) #displays question in ellipse
    question_asked.display()

    question_boxes = []
    
    for x in range(0, 4):
        global question_boxes
        question_boxes.append(QuestionButton(20, 535 + (x*45), 1, questions_list[current_question][x+1]))

    
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(15)

###### FUNCTIONS END #########

###### Global Variables ########

question_boxes = []
need_question = True
current_question = 0
remaining_guesses = 1
chosen_button = 0
game_state = 1
main_player_character_selection = 0
remaining_choices = 1
selected_answer = None
current_round = 0
user_correct = False

questions_list = read_file_to_list_questions("questions.txt")
main_player_character_list = os.listdir("assets/characters/playable/")  #gets all pngs for playable characters
main_player_character_selection_fullpath = "assets/characters/playable/" + main_player_character_list[main_player_character_selection]

circle_opp = PlayerCircle(1025, 350, 1.23) #Circle under opponent
circle_main_player = PlayerCircle(400, 500, 1.50) #Circle under main player

opp_ninja = Player(circle_opp.x_pos, circle_opp.y_pos, "Tyler \"Ninja\" Blevins", 100, "assets/characters/opponents/ninjablevins.png", 0.6)
opp_souljaboy = Player(circle_opp.x_pos, circle_opp.y_pos, "Soulja Boy", 100, "assets/characters/opponents/souljaboy.png", 0.60)
opp_list  = [[opp_ninja, opp_souljaboy]]

#set current opponent so they can be changed out easier? // yes.
current_opp = opp_souljaboy

main_player = Player(400, 550, "You", 100, main_player_character_selection_fullpath, 0.8)

next_character_button = GalleryButton(50+140, 500, 1, 1)
back_character_button = GalleryButton(25+140, 500, 1, -1)
start_button = RectButton(540,300,200,100, "Ready up", 40)
action_buttons = [Action_Box(470, "Attack"), Action_Box(660, "Heal")]

current_opp = opp_list[0][random.randrange(0,2)]
opp_damage = 15
print(current_opp.name)

enemy_noti = Notification(400, 100, True, 3, "You have encountered " + current_opp.name)
damage_noti = Notification(400,100, True, 3, "You have been hit for " + str(opp_damage))

action_buttons = [ActionBox(470, "Attack"), ActionBox(660, "Heal")]

##### Global Variables End ###########


def main_menu():
    game_state = 1
    background(100, 100, 255)

    #title on screen
    title = "Canadian Geography Fortnite Pokemon Education Game (placeholder)"
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



def battle_ui():
    global current_opp
    circle_opp.display()
    circle_main_player.display()

    current_opp.display()
    main_player.display()

    #bottom box
    fill(100, 150, 200)
    rect(0, 720-226, 1279, 225)
    
    enemy_noti.display()
    if enemy_noti.show == False:
        questions_ui()
        #display boxes when availible guesses
        for x in question_boxes:
            if remaining_guesses > 0:
                x.display()
            elif can_choose_action == True:
                for x in action_buttons:
                    x.display()

def setup():
    size(1280, 720)
    
    
def draw():
    #global question_boxes
    background(245)
    global uni_counter
    
    if game_state == 1:
        main_menu()
    elif game_state == 2:
        battle_ui()
        
        
def user_is_right():
    is_right = False
    
    if selected_answer.question == questions_list[current_question][5]:
        is_right = True
        
    return is_right


user_is_correct = False
can_choose_action = False

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
            
    if game_state == 2:
        global remaining_guesses
        global selected_answer
        global user_is_correct
        global can_choose_action
        
        if remaining_guesses > 0:
            for x in question_boxes:
                if x.over_button() == True:
                    if x.question == questions_list[current_question][5]:
                        print("BOX SELECTED")
                    else:
                        print("wrong")
                    selected_answer = x
                    remaining_guesses -= 1
        if remaining_guesses == 0:
            if user_is_right() == True:
                print("34")
                can_choose_action = True
                user_is_correct = True
            else:
                test_hit_value = 10
                main_player.health_level -= test_hit_value
                #noti saying how much hit for
            remaining_guesses -= 1 #stops from allowing any click to take away health

        #if can choose attack or heal, do it
        if action_buttons[0].over_but() == True and can_choose_action == True:
            print("Attack")
            can_choose_action = False
        elif action_buttons[1].over_but() == True and can_choose_action == True:
            print ("Heal")
            can_choose_action = False
            
        
            
