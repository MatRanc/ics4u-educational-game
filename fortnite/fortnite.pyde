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
        
class ActionButton(object):
    def __init__(self, idk):
        self.idk = idk
        
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
        text(self.health_level, self.x_pos - 30, self.y_pos + 30)
        
        #background shield bar
        fill(210, 210, 255)
        rect(self.x_pos, self.y_pos, 200, 10)
        
        #main shield bar
        fill(60, 60, 255)
        rect(self.x_pos, self.y_pos, 200 * self.shield_level / 100, 10)
        
        #shield text
        text(self.shield_level, self.x_pos - 30, self.y_pos + 10)
        
class Question(object):
    def __init__(self, question, correct_answer, answer_2, answer_3, answer_4):
        self.question = question
        self.correct_a = correct_answer
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4
        
        
############### class templates end #######################

circle_opp = PlayerCircle(1025, 350, 1.23)
circle_main_player = PlayerCircle(400, 500, 1.50)

opp_ninja = Player(circle_opp.x_pos, circle_opp.y_pos, "Tyler \"Ninja\" Blevins", 100, 100, "assets/characters/ninjablevins.png", 0.8)
opp_souljaboy = Player(circle_opp.x_pos, circle_opp.y_pos, "Soulja Boy", 100, 100, "assets/characters/souljaboy.png", 0.60)

#set current opponent so they can be changed out easier?
current_opp = opp_souljaboy

main_player = Player(circle_main_player.x_pos, circle_main_player.y_pos +50, "ASSIGN NAME", 100, 100, "assets/characters/defaultplayer.png", 0.8)

opp_health_bar = HealthBar(current_opp.x_pos-350, current_opp.y_pos-200, current_opp.health_level, current_opp.shield_level)
main_player_health_bar = HealthBar(main_player.x_pos-350, main_player.y_pos-200, main_player.health_level, main_player.shield_level)



def setup():
  size(1280, 720)
  
def draw():
  background(245);
    
  circle_opp.display()
  circle_main_player.display()
  
  #opp_ninja.display()
  opp_souljaboy.display()
  
  main_player.display()
  
  opp_health_bar.display()
  main_player_health_bar.display()
  
  #bottom box
  fill(100, 150, 200)
  rect(0, 720-226, 1279, 225)
