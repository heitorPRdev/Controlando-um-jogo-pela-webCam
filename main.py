import pygame
import  cv2
import mediapipe as mp

pygame.init()
webcam = cv2.VideoCapture(0)
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
x = 100
y = 530
pos_cx = 0
pos_cy = 580
pos_espx = 700
pos_espy = 530
vel_esp = 10
vel_jump = 100

cont_jump = 0
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
    check, img = webcam.read()
    if check:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resultado = Hand.process(imgRGB)
        handsPoints = resultado.multi_hand_landmarks
        h, w, p = img.shape
        pontos = []
        if handsPoints:
            for points in handsPoints:
                for cord in points.landmark:
                    mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
                    cx, cy = int(cord.x * w), int(cord.y * h)
                    pontos.append((cx, cy))

        dedos = [8, 12, 16, 20]
        if pontos:
            for ded_X in dedos:
                if pontos[ded_X][1] < pontos[ded_X-2][1]:

                    cont_jump += 1
                    if cont_jump > 2:
                        y -= vel_jump

                        cont_jump = 0
                    else:
                        y = 530
                else:
                    y = 530
        else:
            y = 530
    pos_espx -= vel_esp
    if pos_espx == -30:
        pos_espx = 850
    if x + 50 > pos_espx and y + 50 > pos_espy:
        y += 1000



    janela.blit(background, (0, 0))
    janela.blit(espinhos, (pos_espx,pos_espy))
    janela.blit(chao,(pos_cx,pos_cy))
    janela.blit(player, (x, y))
    pygame.display.update()
    cv2.imshow('imagem', img)


pygame.quit()
webcam.release()

