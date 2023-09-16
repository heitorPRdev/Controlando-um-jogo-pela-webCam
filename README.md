# Controlando-um-jogo-pela-webCam
Nesse jogo feito no python nós controlamos um quadrado com as mãos.Usamos a WebCam para controla-lo.
As bibliotecas usadas são: **OPENCV**, **MEDIAPIPE** e **PYGAME**.

## Tabela de comados
|comandos|SIgnificado|
-------- |-----------|
|  🤚    |pular|
|  ✊    |ficar parado|

## Como Fiz

A Pygame permite nós criarmos o jogo e facilitar a implementação do Open-Cv e Mediapipe.E existe um codego base, que é:

````commandline
pygame.init()
janela = pygame.display.set_mode((800,600))
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    pygame.display.update()

pygame.quit()
````
E colocamos as sprits(fotos do jogo):

````commandline

background = pygame.image.load('sprits/background_sp.png')

chao = pygame.image.load('sprits/chao_sp.png')
chao = pygame.transform.scale(chao,(800,20))

player = pygame.image.load('sprits/player_sp.png')
espinhos = pygame.image.load('sprits/espinho_sp.png')
pygame.display.set_caption('Jogo controlado pela Webcam')

[...]
janela.blit(background, (0, 0))
janela.blit(espinhos, (pos_espx,pos_espy))
janela.blit(chao,(pos_cx,pos_cy))
janela.blit(player, (x, y))
[...]

````
Depois no inicio eu coloquei as seguintes variaveis:
````commandline
x = 100
y = 530
pos_cx = 0
pos_cy = 580
pos_espx = 700
pos_espy = 530
vel_esp = 10
vel_jump = 100
````
Para controle das sprits.
E fiz a logica da movimentação, e implementamos o Open-Cv e MediaPipe com essa varíaveis:
````commandline
webcam = cv2.VideoCapture(0)
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
[...]
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
[...]
````

### Obs
O jogo não esxite colisão e sim é para teste da implementação do Pygame, OpenCv e Medipipe e também com isso ele ocorre alguns erros de performace
