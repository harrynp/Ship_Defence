import pygame, sys, menu
#Harry Pham 79422112
pygame.init()
mainClock = pygame.time.Clock()

def game():
  _display = pygame.display.set_mode((600, 300), 0, 32)
  pygame.display.set_caption('Ship Defence')

  """SCREENS"""
  background = pygame.image.load('images/background.png')
  bgSize = background.get_rect()
  red_win = pygame.image.load('images/red_win.png')
  blue_win = pygame.image.load('images/blue_win.png')

  """BALL"""
  ball = pygame.image.load('images/ball.png')
  ballX = 300
  ballY = 150

  dirX = 2
  dirY = 1
  speed = 1

  """PADDLES"""
  pygame.key.set_repeat(30, 30)
  paddle = pygame.image.load('images/paddle.png')
  paddleX = 500 - paddle.get_width() - 10
  paddleY = (250 - paddle.get_height()) / 2
  paddle2 = pygame.image.load('images/paddle2.png')
  paddle2X = paddle.get_width()+ 80
  paddle2Y = (250 - paddle.get_height()) / 2
  paddleDir = 5

  """SPACESHIP"""
  redss = pygame.image.load('images/RedSS.png')
  redssX = 650 - redss.get_width() - 10
  redssY = (300 - redss.get_height()) / 2
  bluess = pygame.image.load('images/BlueSS.png')
  bluessX = 90 - bluess.get_width() - 10
  bluessY = (300 - bluess.get_height()) / 2

  """SHIELD"""
  regshield = pygame.image.load('images/shield.png')
  broken_shield = pygame.image.load('images/broken_shield.png')
  class Shield:
    def __init__(self, X, Y, HP):
      '''Initialize this shield to have given, X, Y, HP Values'''
      self._X = X
      self._Y = Y
      self._HP = HP
    def X(self):
      '''Returns the X value of this shield'''
      return self._X
    def Y(self):
      '''Returns the Y value of this shield'''
      return self._Y
    def HP(self):
      '''Returns the HP value of this shield'''
      return self._HP
    def change_HP(self, HP):
      self._HP = HP
    
  """RED SHIELDS"""
  red_shield = Shield(575 - regshield.get_width() - 40, 0, 100)
  red_shield2 = Shield(575 - regshield.get_width() - 40, 40, 100)
  red_shield3 = Shield(575 - regshield.get_width() - 40, 80, 100)
  red_shield4 = Shield(575 - regshield.get_width() - 40, 120, 100)
  red_shield5 = Shield(575 - regshield.get_width() - 40, 160, 100)
  red_shield6 = Shield(575 - regshield.get_width() - 40, 200, 100)
  red_shield7 = Shield(575 - regshield.get_width() - 40, 240, 100)
  red_shield8 = Shield(575 - regshield.get_width() - 40, 280, 100)
  
  red_shields = [red_shield, red_shield2, red_shield3, red_shield4,
                 red_shield5, red_shield6, red_shield7, red_shield8]

  """BLUE SHIELDS"""

  blue_shield = Shield(regshield.get_width() + 40, 0, 100)
  blue_shield2 = Shield(regshield.get_width() + 40, 40, 100)
  blue_shield3 = Shield(regshield.get_width() + 40, 80, 100)
  blue_shield4 = Shield(regshield.get_width() + 40, 120, 100)
  blue_shield5 = Shield(regshield.get_width() + 40, 160, 100)
  blue_shield6 = Shield(regshield.get_width() + 40, 200, 100)
  blue_shield7 = Shield(regshield.get_width() + 40, 240, 100)
  blue_shield8 = Shield(regshield.get_width() + 40, 280, 100)

  blue_shields = [blue_shield, blue_shield2, blue_shield3, blue_shield4,
                  blue_shield5, blue_shield6, blue_shield7, blue_shield8]
  
  """PAUSE"""
  pause = False
  while True:
    _display.blit(background, bgSize)
    _display.blit(redss, (redssX, redssY))
    _display.blit(bluess, (bluessX, bluessY))
    ballX = ballX + dirX * speed
    ballY = ballY + dirY * speed
    if speed < 3 and speed != 0:
      speed += .005
    if ballY <= 0 or ballY >= 275:
      dirY = -dirY

    if dirX > 0 and ballY > paddleY-10 and ballY < (paddleY + paddle.get_height()):
      if ballX >= 475 - paddle.get_width() - 10:
        dirX = -dirX
        
    if dirX < 0 and ballY > paddle2Y-10 and ballY < (paddle2Y + paddle2.get_height()):
      if ballX <= paddle2.get_width() + paddle2X:
        dirX = -dirX
        
    for shield in red_shields:
      if shield.HP() == 0:
        _display.blit(background, (shield.X(), shield.Y()),pygame.Rect(shield.X(),shield.Y(),25,40))
        if dirX > 0 and ballY > shield.Y() and ballY < (shield.Y() + regshield.get_height()):
          if ballX >= 550 - regshield.get_width() - 10:
            dirX=dirX
      elif shield.HP() == 50:
        _display.blit(broken_shield, (shield.X(), shield.Y()))
        if dirX > 0 and ballY > shield.Y() and ballY < (shield.Y() + broken_shield.get_height()):
          if ballX >= 550 - broken_shield.get_width() - 10:
            shield.change_HP(0)
            dirX = -dirX
      elif shield.HP() == 100:
        _display.blit(regshield, (shield.X(), shield.Y()))
        if dirX > 0 and ballY > shield.Y() and ballY < (shield.Y() + regshield.get_height()):
          if ballX >= 550 - regshield.get_width() - 10:
            shield.change_HP(50)
            dirX = -dirX

    for shield in blue_shields:
      if shield.HP() == 0:
        _display.blit(background, (shield.X(), shield.Y()),pygame.Rect(shield.X(), shield.Y(), 25, 40))
        if dirX < 0 and ballY > shield.Y() and ballY < (shield.Y() + regshield.get_height()):
          if ballX <= regshield.get_width() + shield.X():
            dirX=dirX
      elif shield.HP() == 50:
        _display.blit(broken_shield, (shield.X(), shield.Y()))
        if dirX < 0 and ballY > shield.Y() and ballY < (shield.Y() + broken_shield.get_height()):
          if ballX <= broken_shield.get_width() + shield.X():
            shield.change_HP(0)
            dirX = -dirX
      elif shield.HP() == 100:
        _display.blit(regshield, (shield.X(), shield.Y()))
        if dirX < 0 and ballY > shield.Y() and ballY < (shield.Y() + regshield.get_height()):
          if ballX <= regshield.get_width() + shield.X():
            shield.change_HP(50)
            dirX = -dirX

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
          paddleY -= paddleDir
        elif keys[pygame.K_DOWN]:
          paddleY += paddleDir
        elif keys[pygame.K_w]:
          paddle2Y -= paddleDir
        elif keys[pygame.K_s]:
          paddle2Y += paddleDir
        elif keys[pygame.K_p]:
          pause = True
    if pause == True:
      while pause == True:
        pygame.time.delay(100)
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_p]:
              pause = False

    if paddleY <= 1: paddleY = 1
    if paddleY >= (300 - paddle.get_height()):
      paddleY = (300 - paddle.get_height())
    if paddle2Y <= 1: paddle2Y = 1
    if paddle2Y >= (300 - paddle2.get_height()):
      paddle2Y = (300 - paddle2.get_height())
    

    _display.blit(ball, (ballX, ballY))
    _display.blit(paddle, (paddleX, paddleY))
    _display.blit(paddle2, (paddle2X, paddle2Y))
    
    if ballX < 30:
      ballX=0
      _display.blit(red_win, bgSize)
    elif ballX > 545:
      ballX=600
      _display.blit(blue_win, bgSize)
    pygame.display.flip()
    mainClock.tick(32)
    
def credits():
    """Displays Credit Screen"""
    _display = pygame.display.set_mode((600, 300), 0, 32)
    pygame.display.set_caption('Ship Defence Credits')
    credits = pygame.image.load('images/credits.png')
    bgSize = credits.get_rect()
    _display.blit(credits,bgSize)
    
def controls():
    """Displays Controls Screen"""
    _display = pygame.display.set_mode((600, 300), 0, 32)
    pygame.display.set_caption('Ship Defence Controls')
    controls = pygame.image.load('images/controls.png')
    bgSize = controls.get_rect()
    _display.blit(controls,bgSize)


if __name__ == "__main__":
  surface = pygame.display.set_mode((600,300))
  surface.fill((51,51,51))
  menu = menu.Menu()
  menu.init(['Start','Credits', 'Controls', 'Quit'], surface)
  menu.draw()
  pygame.key.set_repeat(199,69)
  pygame.display.update()
  while 1:
      for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_UP:
                  menu.draw(-1)
              if event.key == pygame.K_DOWN:
                  menu.draw(1)
              if event.key == pygame.K_RETURN:
                  if menu.get_position() == 0:
                    game()
                  if menu.get_position() == 1:
                    credits()
                  if menu.get_position() == 2:
                    controls()
                  if menu.get_position() == 3:
                      pygame.display.quit()
                      sys.exit()                        
              if event.key == pygame.K_ESCAPE:
                  pygame.display.quit()
                  sys.exit()
              pygame.display.update()
          elif event.type == pygame.QUIT:
              pygame.display.quit()
              sys.exit()
      pygame.time.wait(8)
        
