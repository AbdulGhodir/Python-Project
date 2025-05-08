import tkinter as tk

window = tk.Tk()
window.geometry("900x480")

id_timer = None

def addleft():
    temp = angka1.cget("text")
    temp = int(temp)
    temp += 1
    
    if temp >= 10:
        angka1.place_configure(x=15)
        
    angka1.config(text=temp)

def minleft():
    temp = angka1.cget("text")
    temp = int(temp)
    temp -= 1
    
    if temp < 10:
        angka1.place_configure(x=40)
        
    angka1.config(text=temp)

def addright():
    temp = angka2.cget("text")
    temp = int(temp)
    temp += 1
    
    if temp >= 10:
        angka2.place_configure(x=465)
    
    angka2.config(text=temp)

def minright():
    temp = angka2.cget("text")
    temp = int(temp)
    temp -= 1
    
    if temp < 10:
        angka2.place_configure(x=490)
    
    angka2.config(text=temp)
    
def timer():
    global id_timer
    
    #Timer Kiri
    time = Timer1.cget("text")
    time = time.split(":")
    time[1] = int(time[1]) + 1
    time[0] = str(int(time[0]) + time[1] // 60)
    time[1] = str(int(time[1]) % 60)
    
    if int(time[1]) < 10:
        time[1] = "0" + time[1]
        
    time = time[0] + ":" + time[1]
    
    #Timer Kanan
    time = Timer2.cget("text")
    
    time = time.split(":")
    time[1] = int(time[1]) + 1
    time[0] = str(int(time[0]) + time[1] // 60)
    time[1] = str(int(time[1]) % 60)
    
    if int(time[1]) < 10:
        time[1] = "0" + time[1]
        
    time = time[0] + ":" + time[1]
    
    #Perbarui Waktu
    Timer1.config(text=time)
    Timer2.config(text=time)
    
    id_timer = window.after(1000, timer)
    
def start_stop():
    global id_timer
    if startop.cget("text") == "Start":
        startop.config(text="Stop")
        window.after(250)
        timer()
    elif startop.cget("text") == "Stop":
        window.after_cancel(id_timer)
        startop.config(text="Start")
        
def reset_timer():
    Timer1.config(text="0:00")
    Timer2.config(text="0:00")
    

#Garis Tengah
garis = tk.Frame(window, bg="black", width=2)
garis.place(x=300, y=0, relheight=1)

#Background
canvas = tk.Canvas(width=900, height=600, bg="white")
canvas.place(x=0, y=0)

canvas.create_rectangle(0, 0, 450, 480, fill="blue")
canvas.create_rectangle(450, 0, 900, 480, fill="red")

#Tulisan Angka Kiri
angka1 = tk.Label(window, text="0", font=("Comic Sans MS", 100), bg="blue", fg="white")
angka1.place(x=40, y=5)
#Tulisan Angka Kanan
angka2 = tk.Label(window, text="0", font=("Comic Sans MS", 100), bg="red", fg="white")
angka2.place(x=490, y=5)

#Tombol Kiri +
tombol1 = tk.Button(window, text="+1", width=3, font=("Comic Sans MS", 10, "bold"), command=addleft)
tombol1.place(x=35, y=165)
#Tombol Kiri -
tombol1 = tk.Button(window, text="-1", width=3, font=("Comic Sans MS", 10, "bold"), command=minleft)
tombol1.place(x=103, y=165)

#Tombol Kanan +
tombol2 = tk.Button(window, text="+1", width=3, font=("Comic Sans MS", 10, "bold"), command=addright)
tombol2.place(x=485, y=165)
#Tombol Kanan -
tombol2 = tk.Button(window, text="-1", width=3, font=("Comic Sans MS", 10, "bold"), command=minright)
tombol2.place(x=553, y=165)

#Gambar
gambar1 = tk.PhotoImage(file="merah.png")
gambar2 = tk.PhotoImage(file="biru.png")
gambar1 = gambar1.subsample(10, 10)
gambar2 = gambar2.subsample(10, 10)

#Letak Gambar 1
Gambar1 = tk.Label(window, image=gambar1, bg="white").place(x=640, y=20)
#Letak Gambar 2
Gambar2 = tk.Label(window, image=gambar2, bg="white").place(x=190, y=20)

#Timer Kiri
Timer1 = tk.Label(window, text="0:00", font=('digital-7', 90), bg="darkblue", fg="white", width=4)
Timer1.place(x=150, y=265)

#Timer Kanan
Timer2 = tk.Label(window, text="0:00", font=('digital-7', 90), bg="darkblue", fg="white", width=4)
Timer2.place(x=600, y=265)

#Tombol Start/Stop
startop = tk.Button(window, text="Start", fg="white", bg="green", font=("Comic Sans MS", 12, "bold"), command=start_stop)
startop.place(x=25, y=295)

#Reset Timer
reset = tk.Button(window, text="Reset", fg="white", bg="black", font=("Comic Sans MS", 12, "bold"), command=reset_timer)
reset.place(x=25, y=350)

window.mainloop()
