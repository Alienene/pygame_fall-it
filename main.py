#імпортуємо pygame, random, time
import pygame 
import random 
pygame.init() 
import time 

def game():
    #створюємо вікно гри та фон
    sound = pygame.mixer.Sound("poedanie-s-chavkaniem-i-slyunoy.mp3")
    pygame.mixer.music.load("mp.mp3")
    pygame.mixer.music.play()
    
    back = (100, 100, 200) 
    mw = pygame.display.set_mode((500, 500)) 
    mw.fill(back) 
    clock = pygame.time.Clock() 
    wh = (500,500)
    backgroud = pygame.transform.scale(pygame.image.load('background5.png'), wh)
 
    start_time = time.time() 

    #обидві встановлені на False це значить що на початку гри рух не відбувається
    move_right = False 
    move_left = False 
 
    #визначаємо клас Area який представляє прямокутну область у грі
    class Area(): 
        def __init__(self, x=0, y=0, width=10, height=10, color=None): 
            self.rect = pygame.Rect(x, y, width, height) 
            self.fill_color = back 
            if color: 
                self.fill_color = color 
 
        #Визначаємо метод color, отримує новий колір та присвоює його об'єкту 
        def color(self, new_color): 
            self.fill_color = new_color 
 
        #визначає метод fill для відображення прямокутної області 
        def fill(self): 
            pygame.draw.rect(mw, self.fill_color, self.rect) 
 
        #Метод для перевірки чи знаходиться точка з координатами в межах прямокутної області
        def collidepoint(self, x, y): 
            return self.rect.collidepoint(x, y) 
 
        #Метод для перевірки колізії "self.rect" та "rect"
        def colliderect(self, rect): 
            
            return self.rect.colliderect(rect) 
            
            
 
    #визначаємо клас Label який призначений для встановлення тексту 
    class Label(Area): 
        def set_text(self, text, fsize=12, text_color=(0, 0, 0)): 
            self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color) 
 
        #визначаємо метод draw який представляє графічний об'єкт
        def draw(self, shift_x=0, shift_y=0): 
            self.fill() 
            mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) 
 
    #визначаємо клас Picture який призначений для представлення графічного елемента
    class Picture(Area): 
        def __init__(self, filename, x=0, y=0, width=10, height=10): 
            Area.__init__(self, x=x, y=y, width=width, height=height, color=None) 
            self.image = pygame.image.load(filename) 
 
        #визначаємо метод draw який використовує бібліоеку Pygame для відображення зображень
        def draw(self): 
            mw.blit(self.image, (self.rect.x, self.rect.y)) 

    #створюємо об'єкт ball і встановлюємо його властивості 
    ball = Picture('ball3.png', 220, 400, 40, 40) 
 
    #створюємо об'єкт fruits і встановлюємо його властивості
    fruits = [] 
    for f in range(1): 
        y = 0 
        x = random.randint(0, 450) 
        fruit = Picture('fruit4.png', x, y, 20, 20)  # Поміняйте 'fruit.png' на реальний файл фрукта 
        fruits.append(fruit) 

    #створюємо об'єкт watermelons і встановлюємо його властивості 
    watermelons = [] 
    for w in range(1): 
        y = 0 
        x = random.randint(0, 450) 
        watermelon = Picture('watermelon3.png', x, y, 20, 20)  # Поміняйте 'fruit.png' на реальний файл фрукта 
        watermelons.append(watermelon) 
 
    #створорюємо об'єкт enemies
    enemies = [] 
    for e in range(1): 
        y = 0 
        x = random.randint(0, 450) 
        enemie = Picture('bomba.png', x, y, 55, 55)  # Поміняйте 'fruit.png' на реальний файл фрукта 
        enemies.append(enemie) 
 
    life = 3 
    game_over = False 
    score = 0 
    #створюємо керування м'ячем на клавіши A та D 
    while not game_over: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game_over = True 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_d: 
                    move_right = True 
                if event.key == pygame.K_a: 
                    move_left = True 
            elif event.type == pygame.KEYUP: 
                if event.key == pygame.K_d: 
                    move_right = False 
                if event.key == pygame.K_a: 
                    move_left = False 
    
        #встановлюємо швидкість руху м'яча
        if move_right: 
            ball.rect.x += 8
        if move_left: 
            ball.rect.x -= 8
    
        #відображення фону
        mw.blit(backgroud,(0,0))
        
        #створюємо швидкість падіння об'єкту enemies та його колізію з м'ячем 
        for enemie in enemies: 
            enemie.rect.y += 4 
            if ball.rect.colliderect(enemie.rect): 
                enemies.remove(enemie) 
                game_over = True 

            #якщо об'єкт enemie виходить за межі вікна то з'являється новий 
            if enemie.rect.y > 500: 
                y = 0 
                x = random.randint(0, 450) 
                enemie.rect.x = x 
                enemie.rect.y = y 
    
        #створюємо швидкисть падіння фрукту та його колізію з м'ячем
        for fruit in fruits: 
            fruit.rect.y += 4 
            if ball.rect.colliderect(fruit.rect):
                sound.play() 
                fruits.remove(fruit) 
                score += 1 
                y = 0 
                x = random.randint(0, 450) 
                fruit = Picture('fruit4.png', x, y, 80, 80)  
                fruits.append(fruit)  

            #якщо фрукт виходить за межі вікна то віднімається одне життя
            if  fruit.rect.y > 420: 
                life -= 1 
                fruits.remove(fruit)
                y = 0 
                x = random.randint(0, 450) 
                fruit = Picture('fruit4.png', x, y, 80, 80)  # Поміняйте 'fruit.png' на реальний файл фрукта 
                fruits.append(fruit) 

            #якщо фрукт виходить за межі вікна то з'явяється новий
            if fruit.rect.y > 500:
                y = 0 
                x = random.randint(0, 450) 
                fruit.rect.x = x 
                fruit.rect.y = y 
            
            
        #створюємо швидкість падіння другого фрукта та його колізію з м'ячем
        for watermelon in watermelons: 
            watermelon.rect.y += 4   
            if ball.rect.colliderect(watermelon.rect): 
                watermelons.remove(watermelon) 
                score += 2 
                y = 0 
                x = random.randint(0, 450) 
                watermelon = Picture('watermelon3.png', x, y, 100, 100) 
                watermelons.append(watermelon) 

            #якщо фрукт виходить за межі вікна то віднімається одне життя
            if  watermelon.rect.y > 420: 
                life -= 1 
                watermelons.remove(watermelon) 
                y = 0 
                x = random.randint(0, 450) 
                watermelon = Picture('watermelon3.png', x, y, 100, 100) 
                watermelons.append(watermelon) 

            #якщо фрукт виходить а межі вікна то з'являється новий
            if watermelon.rect.y > 500:   
                y = 0 
                x = random.randint(0, 450) 
                watermelon.rect.x = x 
                watermelon.rect.y = y 
    
            
    
        #якщо життя дорівнює 0 то гра завершується
        if life == 0: 
            game_over = True 
    
        #відображення зображень вікна та м'яча
        mw.fill(back) 
        mw.blit(backgroud,(0,0))
        ball.draw() 
        
        #відображення зображень фруктів і ворогів
        for fruit in fruits: 
            fruit.draw() 
            if ball.rect.colliderect(fruit.rect): 
                score += 1
        for e in enemies: 
            e.draw() 
        for watermelon in watermelons: 
            watermelon.draw() 
        
        #відображення таймера 
        t = int(time.time() - start_time) 
        f = pygame.font.Font(None,30) 
        time_text = f.render(f'Час {t} секунд', True, (1,1,1)) 
        mw.blit(time_text,(10,10)) 
        
        #відображення рахунку гри
        font = pygame.font.Font(None,30)
        score_text = font.render(str(score) + ':', True, (1,1,1))
        mw.blit(score_text,(10,40))

        #відображення тексту Ти програв якщо гра завершилася
        if game_over == True:
            final_text = f.render(f'Ти програв', True, (1,1,1)) 
            mw.blit(final_text,(220,230)) 

        #відображення життів
        time_text = f.render(f'Життя: {life} ', True, (1,1,1)) 
        mw.blit(time_text,(400,10))
            
        #оновлення вікна, частоа кадрів та закриття вікна Pygame
        pygame.display.update() 
        clock.tick(40) 
        
    

