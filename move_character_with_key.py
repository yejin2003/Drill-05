from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 700
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation.png')

def handle_events():
    global running
    global x, y
    global xdir, ydir
    global direction  # 새로운 변수 추가
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                xdir += 1
                direction = 1  # 오른쪽 (세 번째 행)
            elif event.key == SDLK_LEFT:
                xdir -= 1
                direction = 2  # 왼쪽 (두 번째 행)
            elif event.key == SDLK_UP:
                ydir += 1
                direction = 0  # 위쪽 (네 번째 행)
            elif event.key == SDLK_DOWN:
                ydir -= 1
                direction = 3  # 아래쪽 (첫 번째 행)
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                xdir -= 1
            elif event.key == SDLK_LEFT:
                xdir += 1
            elif event.key == SDLK_UP:
                ydir -= 1
            elif event.key == SDLK_DOWN:
                ydir += 1

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
xdir = 0
ydir = 0
direction = 0  # 기본적으로 아래쪽(첫 번째 행)으로 설정

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 64, 64 * direction, 64, 64, x, y,90,90)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 4

    x += xdir * 5
    if x > TUK_WIDTH:
        x = TUK_WIDTH
    if x < 0:
        x = 0
    y += ydir * 5
    if y > TUK_HEIGHT:
        y = TUK_HEIGHT
    if y < 0:
        y = 0
    delay(0.05)

close_canvas()
