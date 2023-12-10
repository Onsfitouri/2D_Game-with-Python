import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
             'click' : pygame.mixer.Sound("assets/PygameAssets-main/PygameAssets-main/sounds/click.ogg"),
             'game_over': pygame.mixer.Sound("assets/PygameAssets-main/PygameAssets-main/sounds/game_over.ogg"),
             'meteorite': pygame.mixer.Sound("assets/PygameAssets-main/PygameAssets-main/sounds/meteorite.ogg"),
             'tir':pygame.mixer.Sound("assets/PygameAssets-main/PygameAssets-main/sounds/tir.ogg"),
    
        }
           
    def play(self,name):
        self.sounds[name].play()
        