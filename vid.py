import cv2
from TkinterDnD2 import TkinterDnD, DND_FILES
from tkinter import *

check = 'on'

vid = TkinterDnD.Tk()
vt = 12.31666666666667
w = 800
h = 500
vid.geometry('800x500')
vid.config(bg='#333')
vid.wm_attributes('-transparentcolor', 'green')
vid.attributes('-alpha', 0.80)
vid.overrideredirect(1)
vid.title('green screen')

def file__(e=''):
    from tkinter.messagebox import showinfo
    showinfo('File', 'ABout, Settings, Add')
menu_file = Button(bg="#fff", fg="#810", text="File", border=0, width=8, command=file__)
def settings__(e=''):
    from tkinter.messagebox import showinfo
    showinfo('Settings', 'Click ON ADD...')
menu_settings = Button(bg="orange", fg="#810", text="Settings", border=0, width=8, command=settings__)
def about__(e=''):
    from tkinter.messagebox import showinfo
    showinfo('About', 'IT Is Made By Python...')
menu_about = Button(bg="#cc007d", fg="#000", text="About", border=0, width=8, command=about__)
def add__(e=''):
    # global menu_text
    menu_text1 = Entry(bg="#fff", fg="#cc007d", border=0, width=70)
    menu__ = Button(bg="orange", fg="#810", text="bro", border=0, width=8)
    menu_text1.place(x=250, y=0)
    menu__.place(x=683, y=0)
    menu_text1.focus()
    def er(e=''):
        menu_text1.place(x=9000)
        menu__.place(x=9000)
        global path
        try:
            path = int(menu_text1.get())
        except:
            path = str(menu_text1.get()).replace(' ', '')
    def browze(e=''):
        from tkinter.filedialog import askopenfilename
        path__ = askopenfilename(filetypes=(('.mp4', '.mp4'), ('all', '*')))
        menu_text1.delete(0, END)
        menu_text1.insert('end', path__)
        er()
    menu_text1.bind('<Return>', er)
    menu__.bind('<Button-1>', browze)
menu_add = Button(bg="#0095ff", fg="#810", text="Add", border=0, width=8, command=add__)
menu_text = Button(bg="#fff", fg="#00d4fa", text="No File", border=0, width=70)
def ecx():
    vid.destroy()
menu_exit = Button(bg="#cc007d", fg="#feb600", text="exit", border=0, width=8, command=ecx)
# vide_player_img = PhotoImage(file='imk.png')
video_player = Label(width=800, bg="#777", height=350, image=None)
img1 = PhotoImage(file="play.png")
img2 = PhotoImage(file="stop.png")
img3 = PhotoImage(file="left.png")
img4 = PhotoImage(file="right.png")
img5 = PhotoImage(file="progracebar.png")
img6 = PhotoImage(file="red.png")
play = Button(bg="#333", image=img1)
stop = Button(bg="#333", image=img2)
left = Button(bg="#333", image=img3)
right = Button(bg="#333", image=img4)
pro = Button(bg="#333", image=img5, border=0)
pro_red = Button(bg="#333", image=img6, border=0, width=50)
def vid_fr(e):
    global vt
    if e.x + 0 < 769:
        pro_red['width'] = e.x + 0
        vt = e.x
def vid_fr_l(e):
    global vt
    if pro_red['width'] > 50:
        pro_red['width'] = pro_red['width'] - 10
        vt -= 10
def vid_fr_r(e):
    global vt
    if pro_red['width'] > 769:
        pass
    else:
        pro_red['width'] = pro_red['width'] + 10
        vt += 10
def on_n(e=''):
    global check
    if check == 'on':
        check = 'off'
    else:
        check = 'on'
def off_n(e=''):
    global check
    if check == 'off':
        check = 'on'
    else:
        check = 'off'
right.bind('<Button-1>', vid_fr_r)
pro_red.bind('<B1-Motion>', vid_fr)
left.bind('<Button-1>', vid_fr_l)
menu_text_time = Button(bg="#0095ff", fg="#00d4fa", text="0.00", border=0, width=8)
menu_file.grid(row=0, column=0)
menu_settings.grid(row=0, column=1)
menu_about.grid(row=0, column=2)
menu_add.grid(row=0, column=3)
menu_text.grid(row=0, column=4)
menu_exit.grid(row=0, column=5)
video_player.place(x=10, y=30)
play.place(x=300, y=400)
play.bind('<Button-1>', on_n)
stop.bind('<Button-1>', off_n)
stop.place(x=400, y=400)
left.place(x=200, y=400)
right.place(x=500, y=400)
pro.place(x=10, y=360)
pro_red.place(x=10, y=360)
menu_text_time.place(x=700, y=330)

path = 'D:\\videos\\Football\\(SabWap.CoM)_10_Impossible_Goals_Scored_By_Lionel_Messi_That_Cristiano_Ronal.mp4'
path_ch = 'D:\\videos\\Football\\(SabWap.CoM)_10_Impossible_Goals_Scored_By_Lionel_Messi_That_Cristiano_Ronal.mp4'
cam = cv2.VideoCapture(path)

def mov(e):
    vid.geometry(f'{w}x{h}+{e.x+1}+{e.y+10}')

menu_text.bind('<B1-Motion>', mov)

# req 12.31666666666667

while True:
    vid.update_idletasks()
    vid.update()
    menu_text_time['text'] = vt
    if path == path_ch:
        pass
    else:
        cam = cv2.VideoCapture(path)
        path_ch = path
    try:
        vid.attributes('-alpha', float('0.'+f'{str(vt).replace(".", "")}'))
    except:
        pass
    if check == 'on':
        try:
            fra, frame = cam.read()
            cv2.imwrite('imk.png', frame)
            vide_player_img = PhotoImage(file="imk.png")
            video_player['image'] = vide_player_img
        except:
            cam = cv2.VideoCapture(path)