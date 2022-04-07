import turtle as t                             
import random
import winsound #for windows
#import os for mac and linux to handle sound

#setting screen

try:
  
 wn=t.Screen()
 wn.title("PONG GAME")
 wn.bgcolor("black")
 wn.setup(width=800,height=600)
 wn.tracer(0)

#setting paddle a using turtle

 paddle_a=t.Turtle()
 paddle_a.speed(0)
 paddle_a.color("purple")
 paddle_a.shape("square")
 paddle_a.shapesize(stretch_wid=5,stretch_len=1)
 paddle_a.penup()
 paddle_a.goto(-350,0)

#setting paddle using turtle

 paddle_b=t.Turtle()
 paddle_b.speed(0)
 paddle_b.color("purple")
 paddle_b.shape("square")
 paddle_b.shapesize(stretch_wid=5,stretch_len=1)
 paddle_b.penup()
 paddle_b.goto(350,0)

#setting ball using turtle ,ball movement should be infinite and should be under a loop

 ball=t.Turtle()
 ball.speed(1)
 ball.color("yellow")
 ball.shape("circle")
 ball.penup()
 ball.home() # or goto(x,y)

 ball.dx=.3 #variable 
 ball.dy=.3

#score
 score_a=0
 score_b=0

#pen to write score

 pen=t.Turtle()
 pen.speed(0)
 pen.color("white")
 pen.penup()
 pen.hideturtle()
 pen.goto(0,260)
 pen.write("palyer A: 0, player B: 0",align="center",font=("courier",24,"normal"))#to write score on the top usiing turtle pen
 
#paddle movement functions

 def paddle_a_up():
     y=paddle_a.ycor()#ycor returns the current y value
     y+=30
     if y>=250:
          y=250
     paddle_a.sety(y)#set the trutles second cordinate to y leave first cordinate unchanged       

 def paddle_a_down():
     y=paddle_a.ycor()
     y-=30
     if y<=-250: #to limit the paddle to the border using y axis stops at boundaries
          y=-250
     paddle_a.sety(y)
     

 def paddle_b_up():
     y=paddle_b.ycor()
     y+=30 # y codinate moves by 30 unit
     if y>=250:
          y=250
     paddle_b.sety(y)


 def paddle_b_down():
     y=paddle_b.ycor()
     y-=30
     if y<=-250:
          y=-250
     paddle_b.sety(y)
     

#keyboard binding
     
 wn.listen()#
 wn.onkeypress(paddle_a_up,"w")#fucntion, on that onkeypress of "w" the corresponding function will work
 wn.onkeypress(paddle_a_down,"s")

 wn.onkeypress(paddle_b_up,"Up")
 wn.onkeypress(paddle_b_down,"Down")
 

 while True:# infinite loop
     
    wn.update()#window update for movement animation
    
    ball.setx(ball.xcor()+ball.dx) # setting the x cordinate to current x cordinate and adding x value or increment
    ball.sety(ball.ycor()+ball.dy)
 
#boundary setting
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        #winsound.Playsound("hit.wav",winsound.SND_ASYNC)#Asynchronize you need the sound in your folder o synchronize
     
    if ball.xcor()>390:
         ball.goto(0,0)#whenit hits on the x axis boundary it needs to restart
         ball.dx*=random.choice([-1,1])
         #score using turtle
         score_a+=1
         pen.clear()
         pen.write("player A: {} player B: {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
             
    if ball.ycor()<-290:
         ball.sety(-290)
         ball.dy*=-1
        
    if ball.xcor()<-390:
     ball.goto(0,0)
     ball.dx*=random.choice([-1,1])
     #score using turtle
     score_b+=1
     pen.clear()
     pen.write("player A: {} player B: {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
     
     
     
   
#paddle and ball collison and return
     
    if ball.xcor()>330 and ball.xcor()<340 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50: # when the ball's current x axis value is lessthan-
        #the current paddle a's +50 added to the y axis value then it means ball and paddle is collided ..centre axisil ethiyal aa paddle aa axis ethi ennu parayam 
        ball.setx(330)
        ball.dx*=-1

    if ball.xcor()<-330 and ball.xcor()>-340 and ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50:
        ball.setx(-330)
        ball.dx*=-1

#experimental codes
    if ball.xcor()>350 and ball.xcor()<380 and ball.ycor()>=paddle_b.ycor()+50 and ball.ycor()<=paddle_b.ycor()+60:
        ball.setx(360)
        ball.dx*=-1

        
        
except Exception as e:
    print(e)
 
