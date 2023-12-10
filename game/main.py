import pygame
import math
from game import Game
pygame.init()

#Definir une clock
clock = pygame.time.Clock()
#frame par second 
FPS = 60

#générer la fenetre de notre jeu
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer charger l'arrière plan du jeu
background = pygame.image.load('assets/PygameAssets-main/PygameAssets-main/bg.jpg')

#importer charger notre banniere 
banner=pygame.image.load('assets/PygameAssets-main/PygameAssets-main/banner.png')
banner=pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x= math.ceil(screen.get_width()/4)

# importer charger le bouton pour lancer la partie
play_button=pygame.image.load('assets/PygameAssets-main/PygameAssets-main/button.png')
play_button=pygame.transform.scale(play_button,(400,150))
play_button_rect=play_button.get_rect()
play_button_rect.x=math.ceil(screen.get_width()/3.33)
play_button_rect.y=math.ceil(screen.get_height()/2)

#charger notre jeu
game = Game()
running = True

#boucle tant que cette condition est vrai
while running:

    #appliquer la fenetre de jeu
    screen.blit(background, (0, -200))

    # vérifier si le jeu a commencé ou non
    if game.is_playing:
        #declencher les instruction de la partie
        game.update(screen)
    # verifier si le jeu n'a pas commencé 
    else: 
        # ajouter l'écran de bienvenue 
        screen.blit(play_button,play_button_rect) 
        screen.blit(banner,banner_rect) 
      


    #mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme le fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture de jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
             game.pressed[event.key] = True

             #detecter si la touche espace est enclenchée pour lancer noter projectile
             if event.key == pygame.K_SPACE:
                 if game.is_playing:
                    game.player.launch_projectile()
                 else: 
                      #mettre le jeu en mode "lancé"
                      game.start() 
                      #jouer le son
                      game.sound_manager.play('click')  


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode "lancé"
                game.start() 
                #jouer le son
                game.sound_manager.play('click')
    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)            
              

