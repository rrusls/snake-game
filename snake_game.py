import sdl3
import sdl3.SDL_events
import ctypes
import random

WIDTH = 600
HEIGHT = 500
window = sdl3.SDL_CreateWindow("Test Rects".encode(),WIDTH, HEIGHT,0)
renderer = sdl3.SDL_CreateRenderer(window,None)
wsurface = sdl3.SDL_GetWindowSurface(window)

running = 1
event = sdl3.SDL_Event()

interval = 0.2
keyFrameTime, lastTime = 0, 0
head = sdl3.SDL_FRect(WIDTH//2, HEIGHT//2, 20,20)
tail = sdl3.SDL_FRect(WIDTH//2-50, HEIGHT//2,20,20)
prev_head_cords = [(int(head.x), int(head.y)),(int(tail.x), int(tail.y))]
applerect = sdl3.SDL_FRect()
applerect.w = 20
applerect.h = 20
MAX_TAIL_LENGTH = 3
APPLES = []
score = MAX_TAIL_LENGTH

def directions(dx,dy):
    if event.key.scancode == sdl3.SDL_SCANCODE_D and dx == 0:
            dx, dy = 1, 0
    elif event.key.scancode == sdl3.SDL_SCANCODE_A and dx == 0:
            dx, dy = -1, 0
    elif event.key.scancode == sdl3.SDL_SCANCODE_W and dy == 0:
            dx, dy = 0, -1
    elif event.key.scancode == sdl3.SDL_SCANCODE_S and dy == 0:
            dx, dy = 0, 1
    return dx,dy
dx,dy = 1,0

def spawn_food():
    apple = random.randint(0,20)
    if apple == 0:
        apple_x = random.randint(0,int(WIDTH/20 - 1)) * 20
        apple_y = random.randint(0,int(HEIGHT/20 - 1)) * 20
        APPLES.append((apple_x, apple_y))
        print("spawn food: ", apple_x, apple_y)

while running:
    while sdl3.SDL_PollEvent(ctypes.byref(event)) !=0:
        if event.type == sdl3.SDL_EVENT_QUIT:
            running = 0
        elif event.type == sdl3.SDL_EVENT_KEY_DOWN:
            dx,dy = directions(dx,dy)
    #sdl3.SDL_RenderClear(renderer)
    sdl3.SDL_SetRenderDrawColor(renderer, 0, 0, 0, sdl3.SDL_ALPHA_OPAQUE)
    sdl3.SDL_RenderClear(renderer)
    sdl3.SDL_SetRenderDrawColor(renderer,255,255,255,sdl3.SDL_ALPHA_OPAQUE)
    #dx,dy = directions(dx,dy)
    
    head.x += dx * 20
    head.y += dy * 20
    prev_head_cords.insert(0,(int(head.x),int(head.y)))
    if len(prev_head_cords) > MAX_TAIL_LENGTH:
        prev_head_cords.pop()
    
    currentTime = sdl3.SDL_GetTicks()
    deltaTime = (currentTime - lastTime) / 1000
    lastTime = currentTime

    for i in prev_head_cords:
        x,y = i
        rect = sdl3.SDL_FRect(int(x),int(y),20,20)
        sdl3.SDL_RenderFillRect(renderer,rect)

    (head_x,head_y) = prev_head_cords[0]
    for x,y in APPLES:
        if abs(head.x - x) < 20 and abs(head.y - y) < 20:
            prev_head_cords.append((x,y))
            APPLES.remove((x,y))
            score +=1
            print(f"Current score: {len(prev_head_cords)}")
    #sdl3.SDL_RenderFillRect(renderer,tail)
    #sdl3.SDL_SetRenderDrawColor(renderer,128,128,255,sdl3.SDL_ALPHA_OPAQUE)
    keyFrameTime += deltaTime
    if keyFrameTime >= interval:
        spawn_food()
        keyFrameTime = 0
    sdl3.SDL_SetRenderDrawColor(renderer,128,128,255,sdl3.SDL_ALPHA_OPAQUE)
    for x,y in APPLES:
        applerect.x = int(x)
        applerect.y = int(y)
        sdl3.SDL_RenderFillRect(renderer,applerect)
        

          
    sdl3.SDL_RenderPresent(renderer)
    
    sdl3.SDL_Delay(95)