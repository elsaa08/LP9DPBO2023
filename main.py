from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Rumah("Agust ", 5, 2, 1))
hunians.append(Apartemen("Wonwoo", 3, 3, 3))
hunians.append(Apartemen("Elsa Nabilah", 4, 4, 1))
hunians.append(Indekos("Bp. eskup", "Dino", 1, 2, 3))
hunians.append(Indekos("hanbin", "yujin", 1, 1, 6))
hunians.append(Rumah("Gyuvin", 1, 4, 2))
hunians.append(Rumah("Nabiilah", 1, 1, 10))

root = Tk()
root.title("Praktikum DPBO Python")

judul = Label(root, text="Selamat Datang")
judul.pack(padx=10, pady=10)

pict = Image.open("pythonGUI/code/assets/rmh1.jpg").resize((200,200))
pict = ImageTk.PhotoImage(pict)

img = Label(root, image=pict)
img.pack(padx=10, pady=10)

btn = Button(root, text="Start", command=lambda: home(), padx=10, pady=10)
btn.pack()

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_detail()+hunians[index].get_lama() + hunians[index].get_summary() + hunians[index].get_dokumen() , anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")
    #d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_lama() + hunians[index].get_summary() + "\n" + hunians[index].get_sum() + hunians[index].get_unit() + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")
  #  d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_sum() + hunians[index].get_unit(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w") 
    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

def home():
    root.destroy()
    temp = Tk()
    temp.title("Daftar Residen")
    
    frame = LabelFrame(temp, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(temp, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=temp.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)



root.mainloop()
