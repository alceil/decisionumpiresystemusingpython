import tkinder
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import imutils
stream = cv2.videoCapture("clip.mp4)
flag=true
def play(speed):
    print(f"You clicked on play.speed is {speed}")
  ``global flag
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1=speed)
    grabbed,frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame.PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(120,25,fill="green",font="Times 20 italic bold",text="Decision Pending")
    flag = not flag

def out():
    threading.Thread(target=pending,args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")
def not_out():
    threading.Thread(target=pending,args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")        
def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame=imutis.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk,PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image frame,anchor=tkinter.NW)
    
    time.sleep(1)

    
    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)
    frame=imutis.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk,PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image frame,anchor=tkinter.NW)

    time.sleep(1.5)

    if decision == 'out':
        decisionImg="out.png"
    else:
        decisionImg="not_out.png"    
    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)
    frame=imutis.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk,PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image frame,anchor=tkinter.NW)




SET_WIDTH = 650
SET_HEIGHT = 368
window = tkinter.Tk()
window.title("CodeWithHarry Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("welcome.png),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho tkinter.NW,image=photo)
canvas.pack()
btn = tkinter.Button(window,text="<<Previous (fast)",width=50,partial(play,-25))
btn.pack()
btn = tkinter.Button(window,text="<<Previous (slow)",width=50,partial(play,-2))
btn.pack()
btn = tkinter.Button(window,text="Next (slow)>>",width=50,partial(play,2))
btn.pack()
btn = tkinter.Button(window,text="Next (fast)>>",width=50,command=partial(play,25))
btn.pack()
btn = tkinter.Button(window,text="Give Out",width=50,command=out)
btn.pack()
btn = tkinter.Button(window,text="Give Not Out",width=50,command=not_out)
btn.pack()
window.mainloop()

