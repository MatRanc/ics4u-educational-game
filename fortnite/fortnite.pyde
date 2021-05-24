class playerCircle(object):
    def __init__(self, x_pos, y_pos, scale):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale
        
    def display(self):
        fill(19, 43, 83, 220)
        ellipse(self.x_pos, self.y_pos, 330 * self.scale, 85 * self.scale)
        fill(182, 255, 252)
        ellipse(self.x_pos, self.y_pos, 300 * self.scale, 75 * self.scale)
        
class player(object):
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
        
class action_button(object):
    def __init__(self, idk):
        self.idk = idk
        
class question(object):
    def __init__(self, question, correct_answer, answer_2, answer_3, answer_4):
        self.question = question
        self.correct_a = correct_answer
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4
        
        
############### class templates end #######################

circle_opp = playerCircle(1025, 350, 1.23)
circle_main_player = playerCircle(375, 500, 1.50)

opp_ninja = player(circle_opp.x_pos, circle_opp.y_pos, "Tyler \"Ninja\" Blevins", 100, 100, "/assets/characters/ninjablevins.png", 0.8)
opp_souljaboy = player(circle_opp.x_pos, circle_opp.y_pos, "Soulja Boy", 100, 100, "/assets/characters/souljaboy.png", 0.60)
main_player = player(circle_main_player.x_pos, circle_main_player.y_pos +50, "ASSIGN NAME", 100, 100, "/assets/characters/defaultplayer.png", 0.8)

def setup():
  size(1280, 720)
  
def draw():
  background(255);
  # Draw the image to the screen at coordinate (0,0)
  
  circle_opp.display()
  circle_main_player.display()
  #opp_ninja.display()
  opp_souljaboy.display()
  main_player.display()
  
  #bottom box
  fill(100, 150, 200)
  rect(0, 720-226, 1279, 225)
