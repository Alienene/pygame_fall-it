# pip install pygame-menu
# pygame menu documentation
import pygame
import pygame_menu
from main import *


pygame.init()

window = pygame.display.set_mode((600,400))
font1 = pygame_menu.font.FONT_DIGITAL
my_theme = pygame_menu.Theme(widget_font=font1, # шрифт меню
                             background_color=(0,0,0), # колір фону меню
                             widget_font_color=(255,0,0)) # колір тексту меню
url = "main.py"
def start():
    game()

menu_rules = pygame_menu.Menu("Rules",600,400,
                        theme=my_theme)
menu_rules.add.label("Games rule:\n 1. Don't lose!\n")    
menu_rules.add.button("Back",pygame_menu.events.BACK)


menu_settings = pygame_menu.Menu("Settings",600,400,
                        theme=my_theme)
menu_settings.add.label("Settings\n")    
menu_settings.add.selector("Difficulty:\n",[('Easy',1),('Hard',2)])
#---------------------------------------------------
menu = pygame_menu.Menu("Main menu",600,400,
                        theme=my_theme)
menu.add.button("Start",start)
menu.add.button("Settings",menu_settings)
menu.add.button("Rules",menu_rules)
menu.add.button("Finish",pygame_menu.events.EXIT)

menu.mainloop(window)

