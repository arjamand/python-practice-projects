from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score=0
        
        self.hideturtle()
        self.penup()
        self.setpos(-270,260)
        self.write(f"Level : {self.Score}",font=FONT)
        
        
       
    
    def refresh_score(self):
        self.clear()
        self.pendown()
        self.Score+=1
        self.write(f"Level : {self.Score}",font=FONT)
        
    def game_over(self):
        self.penup()
        self.goto(-40, 0)
        self.write("Game Over",font=FONT)
        
        
