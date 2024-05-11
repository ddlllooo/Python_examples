import sys
import pygame

# 使用pygame之前必须初始化
from pygame import FULLSCREEN, HWSURFACE

pygame.init()

# 设置主屏窗口

screen = pygame.display.set_mode((800, 800),  HWSURFACE)

f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 50)
# 填充主窗口的背景颜色，参数值RGB（颜色元组）
screen.fill((255, 250, 250))
text = f.render("退出", True, (255, 0, 0), (255, 250, 250))
# 设置窗口标题
#text.fill
# 如果没有下列主循环代码，运行结果会一('pink')
# text_point = text.get_rect()
# text_point.center = (500, 200)
# pygame.display.set_caption('测试窗')
# screen.blit(text, text_point)闪而过
while True:
    # 循环获取事件，监听事件
    for event in pygame.event.get():
        # 判断用户是否点了关闭按钮
        if event.type == pygame.QUIT:
            # 卸载所有模块
            pygame.quit()
            # 终止程序
            sys.exit()
    # 更新屏幕内容
    pygame.display.flip()
