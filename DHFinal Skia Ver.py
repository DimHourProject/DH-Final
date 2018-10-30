#DimHourFinal
import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 500
HEIGHT = 680
FPS = 60

#colorfulstuffs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# pygame and windowsan
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DimHour Final: Truth or Darkness")
clock = pygame.time.Clock()
transColor = pygame.Color(255, 0, 255)
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midleft = (x, y)
    surf.blit(text_surface, text_rect)
    
def newgunera():
    g = Guneraskillfirst()
    all_sprites.add(g)
    guneras.add(g)

def newgunerasecond():
    h = Guneraskillsecond()
    all_sprites.add(h)
    guneras.add(h)   

def newdimskill():
    d = Dimskillfirst()
    all_sprites.add(d)
    dimskills.add(d)

def newdimskillsecond():
    t = Dimskillsecond()
    all_sprites.add(t)
    dimskills.add(t)    


def newfboss():
    m = Fboss()
    all_sprites.add(m)
    fboss.add(m)
    
def newunchar():
    u = Unknownchar()
    all_sprites.add(u)
    unchar.add(u)


def draw_resistance_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 15
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, BLUE, fill_rect)
    pygame.draw.rect(surf, BLACK, outline_rect, 3)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
        



class Scara(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 58))
        self.image = pygame.transform.scale(scara_img, (45, 58))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 12
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.resistance = 100
        self.shoot_delay = 200
        self.last_dimshot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
       

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = (WIDTH / 2, HEIGHT - 10)
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -6
        if keystate[pygame.K_RIGHT]:
            self.speedx = 6
        if keystate[pygame.K_z]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0     
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_dimshot > self.shoot_delay:
            self.last_dimshot = now
            dimshot = Dimshot(self.rect.centerx, self.rect.top)
            all_sprites.add(dimshot)
            dimshots.add(dimshot)
            shot_sound.play()
            
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)


class Dimskillfirst(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,50))
        self.image = gunera_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .80 / 2)
       # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
                          
        self.rect.y = -400
        self.speedy = 2
        self.speedx = 2 
        self.rect.y = -400
        self.speedy = 1
        self.speedx = 1
        

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < - 27 or self.rect.right > WIDTH + 20:
            self.rect.x = 400
            self.rect.y = -400 
            self.speedy = 2
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 20 or self.rect.left < - 27 or self.rect.right > WIDTH + 20:
            self.rect.x = 100
            self.rect.y = -100
            self.speedy = 2 

class Dimskillsecond(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,50))
        self.image = gunera_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .80 / 2)
       # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
                          
        self.rect.y = 500
        self.speedy = 1
        self.speedx = 1
        self.rect.y = 400
        self.speedy = 1
        self.speedx = 1
        

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < - 27 or self.rect.right > WIDTH + 20:
            self.rect.x = 100
            self.rect.y = 300 
            self.speedy = 1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 20 or self.rect.left < - 27 or self.rect.right > WIDTH + 20:
            self.rect.x = 200
            self.rect.y = 400
            self.speedy = 1

class Guneraskillfirst(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,50))
        self.image = gunera_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .80 / 2)
       # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
                          
        self.rect.y = -10
        self.speedy = 2
        self.speedx = 2 
        self.rect.y = -20
        self.speedy = 1
        self.speedx = 1
        

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < - 27 or self.rect.right > WIDTH + 20:
            self.rect.x = 10
            self.rect.y = -10 
            self.speedy = 2
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 20 or self.rect.left < - 27 or self.rect.right > WIDTH + 20:
            self.rect.x = 5
            self.rect.y = -20
            self.speedy = 2 

class Guneraskillsecond(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,50))
        self.image = gunera_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .80 / 2)
       # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
                          
        self.rect.y = 300
        self.speedy = 1
        self.speedx = 1
        self.rect.y = 300
        self.speedy = 1
        self.speedx = 1
        

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < - 27 or self.rect.right > WIDTH + 20:
            self.rect.x = 300
            self.rect.y = 300 
            self.speedy = 1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 20 or self.rect.left < - 27 or self.rect.right > WIDTH + 20:
            self.rect.x = 300
            self.rect.y = 300
            self.speedy = 1
            
                        
            
class Dimshot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image = pygame.transform.scale(dimshot_img, (25, 19))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Fboss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image = pygame.transform.scale(unchar_img, (150, 160))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 12
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = 100
        self.speedx = 0

    def update(self):
     self.rect.center = (WIDTH / 2, 100)
     self.speedx = 0

class Unknownchar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image = pygame.transform.scale(fboss_img, (150, 200))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 12
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = 100
        self.speedx = 0

    def update(self):
     self.rect.center = (WIDTH / 2, 100)
     self.speedx = 0



def show_new_scene():
    screen.fill(BLUE)
    pygame.mixer.music.load(path.join(snd_dir, 'reimi theme.mp3'))
    draw_text(screen, "Thanks for playing DimHour! Stay Tuned!", 20, 10, 10)
    draw_text(screen, "Skia - Looks like we did it Mother. I jujst wish you were here", 15, 10, 30)
    draw_text(screen, "Skyria - Behave child. Haha", 15, 10, 50)
    draw_text(screen, "Skia - Mother! Im sorry I couldnt save you!", 15, 1, 70)
    draw_text(screen, "Skyria - I have one final wish and I dont have time", 15, 10, 100)
    draw_text(screen, "Skyria - Please be good for Scara. And accept her as your mother", 15, 10, 120)
    draw_text(screen, "Skyria - Im afraid times will be hard for you two so support her", 15, 10, 140)
    draw_text(screen, "Skyria - You will be the best thing she has. Be true to yourself...That is my wish", 15, 10, 160)
    draw_text(screen, "The end/credits - all art, music, etc was created by me Reimi, of the DimHourProject.", 15, 10, 180)
    pygame.mixer.music.play(loops =- 1)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    

background = pygame.image.load(path.join(img_dir, "DHFBackground.png")).convert()   
background_rect = background.get_rect()
fboss_img = pygame.image.load(path.join(img_dir, "DimFinalBoss.png")).convert()
fboss_img.set_colorkey(WHITE)
unchar_img = pygame.image.load(path.join(img_dir, "UnknownChar.png")).convert()
unchar_img.set_colorkey(BLACK)
scara_img = pygame.image.load(path.join(img_dir, "skiasprite.png")).convert()
lives_img = pygame.image.load(path.join(img_dir, "LifeIcon.png")).convert()
lives_img = pygame.transform.scale(lives_img, (25, 25))
lives_img.set_colorkey(WHITE)
gunera_img = pygame.image.load(path.join(img_dir, "darkbullet.png")).convert()
dimshot_img = pygame.image.load(path.join(img_dir, "skiashot.png")).convert()
shot_sound = pygame.mixer.Sound(path.join(snd_dir, 'dimshot.wav'))
destroyed_sound = pygame.mixer.Sound(path.join(snd_dir, 'destroyed.wav'))
pygame.mixer.music.load(path.join(snd_dir, 'final boss deathraid.mp3'))





all_sprites = pygame.sprite.Group()
guneras = pygame.sprite.Group()
dimshots = pygame.sprite.Group()
fboss = pygame.sprite.Group()
guneras = pygame.sprite.Group()
dimskills = pygame.sprite.Group()
unchar = pygame.sprite.Group()
scara = Scara()
all_sprites.add(scara)
for i in range(6):
    newgunera()
for i in range(60):
    newfboss()
for i in range(5):
    newgunerasecond()

GuneraHealth = 120
DimScore = 0


pygame.mixer.music.play(loops =- 1)
    
# Gloop
new_screen = False


running = True
while running:
    
    clock.tick(FPS)
    # event process stuffs
    for event in pygame.event.get():
        # checking window for close cmon man
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                scara.shoot()

    if new_screen:
        show_new_scene()
        new_screen = True


    # Uperdater
    all_sprites.update()
    #Did it hit?

    attacks = pygame.sprite.groupcollide(guneras, dimshots, True, True)
    for attack in attacks:
        DimScore += 1
        destroyed_sound.play()
        newgunera()
        newgunerasecond()
        if DimScore >= 40:
            all_sprites.remove(guneras)
       




                   
            
    
    attacks = pygame.sprite.groupcollide(fboss, dimshots, True, True)
    for attack in attacks:
        GuneraHealth -= 1
        if GuneraHealth == 60:
            all_sprites.remove(fboss)

                

        
    
            for i in range(60):
                newunchar()
            for i in range(10):
                newdimskill()
            for i in range(8):
                newdimskillsecond()


    attacks = pygame.sprite.groupcollide(unchar, dimshots, True, True)
    for attack in attacks:
        GuneraHealth -= 1
        if GuneraHealth == 0:
            all_sprites.remove(unchar)
            pygame.mixer.music.stop()
            show_new_scene()
        
    #did the gunera hit scara

        
    attacks = pygame.sprite.spritecollide(scara, guneras, True, pygame.sprite.collide_circle)
    for attack in attacks:
        scara.resistance -= attack.radius * 2
        newgunera()
        if scara.resistance <= 0:
            scara.hide()
            scara.lives -= 1
            scara.resistance = 100

        if scara.lives == 0:
            running = False
    attacks = pygame.sprite.spritecollide(scara, dimskills, True, pygame.sprite.collide_circle)
    for attack in attacks:
        scara.resistance -= attack.radius * 2
        newdimskill()
        if scara.resistance <= 0:
            scara.hide()
            scara.lives -= 1
            scara.resistance = 100

        if scara.lives == 0:
            running = False

    # D-raw and dude-render
    screen.fill(WHITE)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    
    
    draw_text(screen, str(GuneraHealth), 50, 400, 20)
    draw_resistance_bar(screen, 270, 660, scara.resistance)
    draw_lives(screen, WIDTH - 100, 650, scara.lives, lives_img)
    # after drawing flip it... flip the display!!!
    pygame.display.flip()

pygame.quit()
