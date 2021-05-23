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
        
class opponent(object):
    def __init__(self, x_pos, y_pos, character, scale):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.character = character
        self.scale = scale
        
    def display(self):
        img = loadImage(self.character)
        imageMode(CENTER)
        img.resize(int(0 * self.scale), int(500 * self.scale))
        image(img, self.x_pos, self.y_pos - (img.height/2))
        
class action_button(object):
    def __init__(self, idk):
        self.idk = idk
        
        
############### class templates end #######################

circle_opp = playerCircle(1050, 400, 0.75)
circle_player = playerCircle(350, 500, 1)

opp_ninja = opponent(circle_opp.x_pos, circle_opp.y_pos, "/assets/characters/ninjablevins.png", 0.8)
opp_souljaboy = opponent(circle_opp.x_pos, circle_opp.y_pos, "/assets/characters/souljaboy.png", 0.8)

def setup():
  size(1280, 720)
  
def draw():
  background(255);
  # Draw the image to the screen at coordinate (0,0)
  
  circle_opp.display()
  circle_player.display()
  #opp_ninja.display()
  opp_souljaboy.display()
