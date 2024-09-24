import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") #ウインドウの左上のタイトル設定
    screen = pg.display.set_mode((800, 600)) #ウインドウのサイズを設定(横, 縦)
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #画像をパスを指定して読み込む
    fbg_img = pg.transform.flip(bg_img, True, False)
    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0]) #自身に別のSurdaceを貼り付ける
        screen.blit(fbg_img, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(fbg_img, [x+4800, 0])
        screen.blit(kt_img, [200, 300])
        pg.display.update()
        #if tmr >= 800:
        #    tmr = 0
        tmr += 1
        #print(tmr)    
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()