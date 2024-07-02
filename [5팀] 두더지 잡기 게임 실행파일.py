import turtle as t
import random

# 기본 설정 (외부 두더지 이미지를 가져옴)
screen = t.Screen()
screen.title("두더지 게임")
image = 'mole.gif'
screen.addshape(image)

# 점수 및 타이머 초기화
score = 0
timer = 10

# 두더지 객체 생성 및 설정
mole = t.Turtle()
mole.shape(image)
mole.penup()
mole.hideturtle()

# 점수판 객체 생성
pen = t.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.color("black")
pen.hideturtle()

# 타원 그리기 함수
def draw_oval():
    mole.penup()
    mole.fd(8)
    mole.left(90)
    mole.fd(13)
    mole.right(10)
    mole.pendown()
    mole.color("black")
    mole.begin_fill()
    mole.setheading(-45)
    for _ in range(2):
        mole.circle(60, 90)
        mole.circle(15, 90)
    mole.end_fill()
    mole.setheading(0)

#점수판과 타이머 출력 함수
def set_scoreboard():
    pen.clear()
    pen.write(f"점수 : {score} 타이머 : {timer}", False, "center", ("Arial", 20))

# 클릭 시 점수가 올라가고 두더지를 숨김
def catch(x, y):
    global score
    score += 1
    set_scoreboard()
    mole.hideturtle()

# 두더지를 랜덤하게 이동시키는 함수
def turtle_move():
    global timer
    if timer > 0:
        mole.penup()
        position = random.choice(circle_list)
        mole.goto(position[0] + 50, position[1] + 70)
        mole.showturtle()
        screen.ontimer(mole.hideturtle, 1000)  # 1초 후에 터틀을 숨기기
        screen.ontimer(turtle_move, 2000)  # 2초 후에 turtle_move 함수를 다시 호출
    else:
        game_over()

# 타이머를 1초마다 감소시키는 함수
def countdown():
    global timer
    if timer > 0:
        timer -= 1
        set_scoreboard()
        screen.ontimer(countdown, 1000)  # 1초 후에 countdown 함수를 다시 호출
    else:
        game_over()

# 게임 종료 함수
def game_over():
    mole.clear()
    pen.clear()
    mole.goto(0, 0)
    mole.write("게임 종료\n최종 점수: " + str(score), align="center", font=("", 40))

# 그래픽 창 설정
def set_screen():
    screen.setup(600, 600)
    screen.bgcolor('green')

# 두더지가 나오는 구멍 그리기
def draw_holes():
    mole.speed("fastest")
    for position in circle_list:
        mole.penup()
        mole.goto(position)
        draw_oval()  # 타원 그리기

# 구멍의 좌표 리스트
circle_list = [(-200, 0), (100, 0), (-50, 0), (-200, 150), (100, 150), (-50, 150), (-200, -150), (-50, -150), (100, -150)]

# 실행 함수
def start_game():
    set_screen()
    set_scoreboard()
    draw_holes()
    turtle_move()
    countdown()  # 타이머 감소 시작
    mole.onclick(catch)

# 게임 시작
start_game()

# 터틀 메인 루프 실행
t.mainloop()
