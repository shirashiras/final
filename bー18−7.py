import pyxel

pyxel.init(200, 200)
pyxel.sounds[0].set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)


class Ball:
    speed = 1

    def __init__(self):
        self.x = pyxel.rndi(0, 199)
        self.y = 0
        angle = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)
    def move(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed
        if self.x > 200 or self.x < 0:
            self.vx = -self.vx
    def restart(self):
        self.x = pyxel.rndi(0, 199)    #0から画面の横幅-1の間
        self.y = 0
        angle = pyxel.rndi(30, 150)    #30度から150度の間
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)
        Ball.speed += 0.3

class Pad:
    
    def __init__(self, padx):
        self.padx = padx
        
    def catch(self, x):
        if ((x >= (self.padx - 20)) and x <= (self.padx + 20)):
            return True
        else:
            return False

class Bullet:
    def __init__(self, x): # x座標は毎回変化できるように引数に。（色は変化させず、下端から発射するので一部を削除）
        self.x = x
        self.y = 195

    def move(self):
        self.y -= 5

    def draw(self):
        pyxel.circ(self.x, self.y, 2, 4)

class App:
    def __init__(self):
        #ball1 = Ball()
        self.balls = [Ball(), Ball(), Ball()] 

        self.pad = Pad(100)

        self.p = 0
        self.gameover = 0
        
        self.bullets = []    # 最初は中身が空のリストを用意
        
        pyxel.run(self.update, self.draw)

    def update(self):
        self.pad.padx = pyxel.mouse_x
        
        if pyxel.btnp(pyxel.KEY_SPACE):  
            self.bullets.append(Bullet(self.pad.padx))
        for bullet in self.bullets:
            bullet.move()
        
        for ball in self.balls:
            #i = Ball()
            ball.move()
            if ball.y >= 195:
                if self.pad.catch(ball.x):
                    pyxel.play(0, 0)
                    self.p += 1
                    ball.restart()
                else:
                    ball.restart()
                    self.gameover += 1
                      
    def draw(self):
        if not (self.gameover >= 10):
            pyxel.cls(7)
            for ball in self.balls:
                pyxel.circ(ball.x, ball.y, 10, 6)
            pyxel.rect(self.pad.padx - 20, 195, 40, 5, 14)
            pyxel.text(10, 0, "point: " + str(self.p), 0)

        if self.gameover >= 10:
            pyxel.text(70, 90, "GAME OVER", pyxel.COLOR_RED)
            return
        
        for bullet in self.bullets:
            bullet.draw()
App()

