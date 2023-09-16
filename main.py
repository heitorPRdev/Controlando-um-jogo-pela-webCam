import pygame

pygame.init()
x = 100
y = 530
pos_cx = 0
pos_cy = 580
pos_espx = 700
pos_espy = 530
vel_esp = 10
vel_jump = 5
janela = pygame.display.set_mode((800,600))
background = pygame.image.load('sprits/background_sp.png')

chao = pygame.image.load('sprits/chao_sp.png')
chao = pygame.transform.scale(chao,(800,20))

player = pygame.image.load('sprits/player_sp.png')
espinhos = pygame.image.load('sprits/espinho_sp.png')
pygame.display.set_caption('Jogo controlado pela Webcam')
janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    pos_espx -= vel_esp
    if pos_espx == -30:
        pos_espx = 850


    janela.blit(background, (0, 0))
    janela.blit(espinhos, (pos_espx,pos_espy))
    janela.blit(chao,(pos_cx,pos_cy))
    janela.blit(player, (x, y))
    pygame.display.update()

pygame.quit()



