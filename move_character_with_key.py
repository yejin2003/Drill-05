from pico2d import *


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running,x
    # fill here
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                x+=10
            elif event.key==SDLK_LEFT:
                x-=10
            elif event.key==SDLK_ESCAPE:
                running=False


running = True
x = 800 // 2
frame = 0

# fill here
while running:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,100,100,100,x,90)
    update_canvas()
    handle_events()
    frame=(frame+1)%8
    delay(0.05)


close_canvas()

