from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        
        with open("./data.txt" ,mode="r") as data:
            a = data.read()
            self.high_score=int(a)
            # print(a)
            # print(b)
                
        
        
        # self.high_s=open("data.txt",mode="r")
        
        # self.high_score=(self.high_s.read())
        # self.high_score=(self.high_score)
        # self.high_s.close()
        # self.high_score=0
        super().__init__()
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.pencolor("white")
        self.write(f"Score : {(self.score)} High Score : {self.high_score} ", move=False,
                   align="center", font="normal")


    def reset(self):
        if self.score>self.high_score:
            
            with open("./data.txt" ,mode="w") as data:
                data.write(f"{self.score}")
            
            
            self.high_score=self.score
            
        self.score=0-1
        self.refresh()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over",
    #                align="center", font="normal")

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {(self.score)} High Score : {self.high_score} ", move=False,
                   align="center", font="normal")

        # self.write(f"Score : {(self.score)} ", move=False,
        #            align="center", font="normal")
