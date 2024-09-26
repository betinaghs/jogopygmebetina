#https://vemfazermatematicaegames.blogspot.com/2021/02/pygames-sistema-de-batalhas-de-um-game.html
#https://vemfazermatematicaegames.blogspot.com/2021/02/pygames-sistema-de-batalhas-de-um-game_9.html

import pygame, sys
from random import randint
pygame.init()

#tela
#Setup de Entrada - Definições ----------------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Tela de Entrada')
screen = pygame.display.set_mode((800, 600),0,32)
background = pygame.image.load('imagens/fundo.png')
font = pygame.font.SysFont(None, 30)

#Definição de Escrita de Texto-------------------------------------------------#
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

#Definição de ações do Menu Inicial--------------------------------------------#
def main_menu():
    while True:

        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        draw_text('Menu Principal', font, (255, 255, 255), screen, 330, 40)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 200, 200, 50)
        button_2 = pygame.Rect(300, 300, 200, 50)
        button_3 = pygame.Rect(300, 400, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                exite()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Jogar', font, (255, 255, 255), screen, 372, 215)
        draw_text('Opções', font, (255, 255, 255), screen, 363, 315)
        draw_text('Sair', font, (255, 255, 255), screen, 378, 415)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

#Definições dos Submenus dos Botões - Game - Opções - Sair --------------------#
def game():
    #jogo 
    largura_janela = 800  
    altura_janela = 600
    tela = pygame.display.set_mode((largura_janela, altura_janela))
    pygame.display.set_caption('Estrada Mildau')
    clock = pygame.time.Clock()


    #cores da barra do especial
    branco = (255,255,255)
    preto = (0,0,0)
    verde = (219,112,147) #rosa
    vermelho = (30,144,255) #azul


    def texto(msg, cor, tam, x, y):
        font = pygame.font.SysFont( 'Timesnewroman' , 27)
        texto1 = font.render(msg, True, cor)
        tela.blit(texto1, [x, y])


    fgExit = False


    cenario = pygame.image.load('cenario.png')
    pikachu = pygame.image.load('pikachu.png')
    pikachu2 = pygame.transform.scale(pikachu, (400, 400))
    charmander = pygame.image.load('charmander.png')
    charmander2 = pygame.transform.scale(charmander, (400, 400))


    vidapikachu = 20 #total de vida do jogador 01
    vidacharmander = 20 #total de vida do jogador 02
    especialjogador1 = 10 #contador do especial do jogador 01
    especialcharmander = 10 #contador do especial do jogador 01
    turno = randint (0, 1) #variável responsável para indicar a vez de cada jogador


    #loop do reset do game e botões de combate


    while not fgExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fgExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: #K_r é o botão de reset
                    vidapikachu = 20
                    vidacharmander = 20 
                    especialjogador1 = 10
                    especialcharmander = 10
                    turno = randint (0, 1) #na primeira vez é sorteado a vez dos jogadores aleatoriamente usando o "randint (0, 1)"
                    pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
                    texto("Pontos de vida: "+str(vidapikachu), preto, 20, 10, altura_janela-30) #vida do jogador 1 #str()" que serve justamente para transformar os valores de batalha que são calculados numericamente em texto a ser exibido na tela.
                    texto("Pontos de vida: "+str(vidacharmander), preto, 20, 500, altura_janela-30) #vida do jogador 2
                    pygame.display.update()
            if event.type == pygame.KEYDOWN and vidapikachu >0 and vidacharmander >0:            
                if event.key == pygame.K_1 and turno == 0: 
                #k_1 é a tecla do ataque basico
                #turno é responsável por fazer a contagem 0 e 1 para indicar a vez de cada jogador.
                    vidacharmander = vidacharmander - 1 #tira 1 da vida do jogador 2
                    especialjogador1 = especialjogador1 + 3 #da 3 pontos para carregar o especial do jogador 1
                    turno = 1
                    print (vidapikachu)
                if event.key == pygame.K_2 and turno == 0: #k_2 é a tecla do ataque carregado
                    vidacharmander = vidacharmander - 2 #tira 2 da vida do jogador 2
                    especialjogador1 = especialjogador1 + 1 #da 2 pontos para carregar o especial do jogador 1
                    turno = 1
                    print (vidapikachu)
                if event.key == pygame.K_3 and especialjogador1 >= 10 and turno == 0: 
                 #k_3 é a tecla do especial
                 #especial=maior ou igual a 10 pontos,
                    vidacharmander = vidacharmander - randint(0, 5) #tira entre 0 e 5 pontos da vida do jogador 2
                    especialjogador1 = especialjogador1 - 9 
                    turno = 1
                    print (vidapikachu)
                if event.key == pygame.K_8 and turno == 1: #k_8 é a tecla do ataque basico
                    vidapikachu = vidapikachu - 1 #tira 1 da vida do jogador 1
                    especialcharmander = especialcharmander + 3 #da 3 pontos para carregar o especial do jogador 2
                    turno = 0
                    print (vidacharmander)
                if event.key == pygame.K_9 and turno == 1: #k_9 é a tecla do ataque carregado
                    vidapikachu = vidapikachu - 2  #tira 2 da vida do jogador 1
                    especialcharmander = especialcharmander + 1 #da 1 pontos para carregar o especial do jogador 2
                    turno = 0
                    print (vidacharmander)
                if event.key == pygame.K_0 and especialcharmander >= 10 and turno == 1:
                 #k_0 é a tecla do especial
                 #especial=maior ou igual a 10 pontos,
                    vidapikachu = vidapikachu - randint(0, 5) #tira entre 0 e 5 pontos da vida do jogador 2
                    especialcharmander = especialcharmander - 9
                    turno = 0
                    print (vidacharmander)


    #loop dos pontos do placar de vida

            if vidapikachu >0 and vidacharmander >0: #pontos de vida maior que 0
                pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
                texto("Pontos de Vida: "+str(vidapikachu), preto, 20, 10, altura_janela-30)
                texto("Pontos de Vida: "+str(vidacharmander), preto, 20, 500, altura_janela-30)
                pygame.display.update()
            if vidapikachu <= 0: #pontos de vida menor ou igual que 0
                print ('pikachu dead')
                pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40]) #desenho da área da escrita
                texto("Pontos de Vida: morto", preto, 20, 10, altura_janela-30)
                texto("Pontos de Vida: "+str(vidacharmander), preto, 20, 500, altura_janela-30)
                pygame.display.update()
            if vidacharmander <= 0: #pontos de vida menor ou igual que 0
                print ('charmander dead')
                pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
                texto("Pontos de Vida: morto", preto, 20, 500, altura_janela-30)
                texto("Pontos de Vida: "+str(vidapikachu), preto, 20, 10, altura_janela-30)
                pygame.display.update()


    #exibição de personagens/cenário, barra de especial e vez do jogador

        tela.blit(cenario,(0,0))
        tela.blit(pikachu2,(0,157))
        tela.blit(charmander2, (400, 157))
        pygame.draw.rect(tela, branco, [0, 0, largura_janela, 40])
        pygame.draw.rect(tela, vermelho, [0, 0,((largura_janela/2)/10)*especialjogador1, 40])
        texto("Especial Pikachu", preto, 0, 10, 10)
        pygame.draw.rect(tela, branco, [largura_janela/2, 0, largura_janela/2, 40])
        pygame.draw.rect(tela, verde, [largura_janela/2, 0, ((largura_janela/2)/10)*especialcharmander, 40])
        texto("Especial Charmander", preto, 0, (largura_janela/2)+10, 10)
        if turno == 0 and vidapikachu > 0 and vidacharmander > 0:
            texto("Jogador 1", preto, 0, 120, 100) #escrita na tela em cada turno
        if turno == 1 and vidapikachu > 0 and vidacharmander > 0:
            texto("Jogador 2", preto, 0, 550, 100) #escrita na tela em cada turno        
        pygame.display.update()
        clock.tick(60)


    pygame.quit()

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Opções', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def exite():
    pygame.quit()
    sys.exit()


main_menu()