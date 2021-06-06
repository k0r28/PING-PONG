from pygame import *
font.init()
font = font.Font(None , 70)
i = 0
z = 0
finish = False
speed_x = 3
speed_y = 3
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("ПИНГ-ПОНГ")
#задай фон сцены
background = transform.scale(image.load("Безымянный.png"), (700, 500))
#создай 2 спрайта и размести их на сцене

clock = time.Clock()
FPS = 1200

sped = 1


x3 = 350
y3 = 250
#обработай событие «клик по кнопке "Закрыть окно"»
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed , size_x , size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x , size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
        def run (self):
            kn = key.get_pressed()
            if kn[K_w]:
                self.rect.y = self.rect.y - self.speed
            if kn[K_s]:
                self.rect.y = self.rect.y + self.speed
        def run2 (self):
            kn = key.get_pressed()
            if kn[K_UP]:
                self.rect.y = self.rect.y - self.speed
            if kn[K_DOWN]:
                self.rect.y = self.rect.y + self.speed
hero = Player("Безымянный2.png",50 , 220 , 8 , 70 , 100)
hero2 = Player("Безымянный2.png",590 , 220 , 8 , 70 , 100)
sprite3 = GameSprite("Безымянный3.png",250 , 350, sped ,30, 30)
game = True
while game:

    if finish != True:
        sprite3.rect.x += speed_x
        sprite3.rect.y += speed_y
        window.blit(background, (0,0))
        sprite3.reset()
        hero2.run()
        hero.reset()
        hero2.reset()
        hero.run2()
        kill1 = font.render("Побед 1  - " + str(i), True ,(255 ,200 , 0))
        window.blit(kill1, (0 , 40))
        
        kill2 = font.render(" Побед 2 - " + str(z), True ,(255 ,100 , 0))
        window.blit(kill2, (0 , 80))

        kill3 = font.render(" Победил 1 , 1 + 1 балл ", True ,(255 ,100 ,0))
        kill4 = font.render(" Победил 2 , 2 + 1 балл ", True ,(255 ,100 ,0))
        if sprite3.rect.y > 450 or sprite3.rect.y < 0:
            speed_y *= -1
        if sprite3.rect.x > 650 :
            i = i + 1
            sprite3.rect.x = 250
            sprite3.rect.y = 350
        if sprite3.rect.x < 0:
            z = z + 1
            sprite3.rect.x = 250
            sprite3.rect.y = 350
        if sprite.collide_rect(hero , sprite3):
            speed_x *= -1
            sped += 1
        if sprite.collide_rect(hero2 , sprite3):
            speed_x *= -1
            sped += 1 

        if i >= 10 :
            window.blit(kill3, (50 , 250))
            time.delay(30000)
            
            game = False

        if z >= 10 :
            window.blit(kill4, (50 , 250))
            time.delay(30000)

            game = False
    clock.tick(FPS)

        
    for every_event in event.get():
        if every_event.type == QUIT:
            game = False
        
        #1
       

        


    display.update()