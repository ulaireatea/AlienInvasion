from tkinter import *

class janela:
    def __init__(self, raiz):

        self.img = PhotoImage(file='Python-Logo.png')

        self.fr1 = Frame(raiz, background='#ffffff', highlightbackground='gray', highlightthickness=3)
        self.fr1.pack()

        self.lb1 = Label(self.fr1, text='Olá mundo!', background='#ffffff', font=('liberation serif', 25, 'bold', 'italic'), width=10, height=1)
        self.lb1.pack(side=LEFT)

        self.fr2 = Frame(raiz, background='#ffffff')
        self.fr2.pack()

        self.bt1 = Button(self.fr2, text='Clique Aqui', background='yellow', font=('liberation serif', 30, 'bold', 'italic'), command=self.muda_label)
        self.bt1['relief'] = SUNKEN
        # outros reliefs possíveis ( FLAT, RAISED, SUNKEN, GROOVE, RIDGE)
        self.bt1['border'] = 5
        self.bt1.bind('<Return>', self.muda_label2)
        self.bt1.pack(side=LEFT)

        # self.lb2 = Label(self.fr1, background='#ffffff', text='     ', width=40)
        # self.lb2.pack()

        # self.lb2 = Label(self.fr2, background='#ffffff', text='     ', width=40)
        # self.lb2.pack()

    def muda_label(self):
        self.lb1['text'] = 'Deu certo'
        self.lb_img = Label(raiz, image=self.img)
        self.lb_img.pack()

    def muda_label2(self, event):
        self.lb1['text'] = 'Deu certo'
        self.lb_img = Label(raiz, image=self.img)
        self.lb_img.pack()

raiz = Tk()
janela(raiz)
raiz.geometry('600x400+600+200') #Defini o tamanho da janela, e os valores adicionados ao lado é a posição xy da janela.(não é Obrigatório)
raiz.title('Aula 50')
# raiz.iconbitmap('Python-Logo.ico')
# raiz.overrideredirect(True)
raiz['bg'] = '#ffffff'
raiz['relief'] = RAISED
raiz['border'] = 10




raiz.mainloop()
