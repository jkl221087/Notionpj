import pygame as pg
import math
from collections import deque



pg.init()
Height = 720
width = 1280 
screen = pg.display.set_mode((width, Height))
clock = pg.time.Clock()



WHITE = (255,255,255)
BLUE = (0, 0, 255)




X, Y = 650, 300
radius = 90
velocity_y = 0
velocity_x = 0
gravity = 9.8 / 60 #　模擬現實重力(9.8 m/s² / 60 FPS)
bounce_factor = 0.7#　彈跳因子
wall_bounce_factor = 0.8 #針對牆壁的反彈
gound_y = Height - radius #計算球碰到地面
gound_x = width - radius


prev_mouse_x, prev_mouse_y = 0, 0

dragging = False
mouse_history = deque(maxlen=10)# []
print(mouse_history)

sportstrail = [] #儲存歷史座標


runner = True
while True:
    screen.fill ("black")
    
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runner = False
            
            #滑鼠點下 # mouse_history = []
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = math.sqrt((mouse_x - X) ** 2 + (mouse_y - Y) ** 2)
            if distance < radius:
                dragging = True
                velocity_x = 0
                velocity_y = 0
                mouse_history.clear()

        elif event.type == pg.MOUSEMOTION and dragging:
            X, Y = event.pos
            Y = max(radius, min(Y, gound_y)) # 不讓球掉出地面以下
            X = max(radius, min(X, gound_x))

            mouse_history.append(event.pos)
            #紀錄座標

                

        #滑鼠放開 # mouse_history = [] 座標計算速度
        elif event.type == pg.MOUSEBUTTONUP:
            print(len(mouse_history))
            if dragging and len(mouse_history) > 1:
                prev_x, prev_y = mouse_history[0]  # 最早的滑鼠位置
                print(prev_x, prev_y)
                print(mouse_history[0])
                curr_x, curr_y = mouse_history[-1] # 最新
                print(curr_x, curr_y)
                print(mouse_history[-1])

                velocity_x = (curr_x - prev_x) / len(mouse_history) * 2# 速度計算 最新-最早/單偵的平均數度 加快速度* 3
                print(velocity_x)
                velocity_y = (curr_y - prev_y) / len(mouse_history) * 2
                print(velocity_y)
            dragging = False

    #運動軌跡
    sportstrail.append((X,Y))
    print(X,Y)
    if len(sportstrail) > 50:
        sportstrail.pop(0)
    
    for i, point in enumerate(sportstrail):
        size = max(2, 20 - i // 5)  # 越舊的點越小
        pg.draw.circle(screen, BLUE, point, size)

        
    #計算反彈
    if not dragging:
        velocity_y += gravity
        Y += velocity_y
        X += velocity_x
        
        if Y >= gound_y:
            Y = gound_y
            velocity_y = -velocity_y * bounce_factor #反向彈跳並減少速度

        #天花板
        if Y - radius <= 0:
            Y = radius
            velocity_y = -velocity_y * bounce_factor

        #左牆
        if X - radius <= 0:
            X = radius
            velocity_x = -velocity_x * wall_bounce_factor
        #右牆壁
        if X + radius >= width:
            X = width - radius
            velocity_x = -velocity_x * wall_bounce_factor
    
    #draw 球
    pg.draw.circle(screen, WHITE, (int(X), int(Y)), radius)
    
    
    pg.display.flip()
    clock.tick(60)
    
pg.quit()
    
    
    