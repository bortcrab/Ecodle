#WORDLE
import tkinter as tk
import english_words as ew
import random as ran

BG_COLOR = "#121213"
LB_COLOR = "#818384"
LT_COLOR = "#FFFFFF"
LBN_COLOR = "#3A3A3C"
LBI_COLOR = "#B59F3B"
LBC_COLOR = "#538D4E"
LBV_COLOR = "#FFFFFF"

atino = False
intentos = 0
letrukis = 0
palabra = ""
enJuego = True
adivinadas = []

tags = {}

tags["Q"] = ["letraQ", False, False, 0]
tags["W"] = ["letraW", False, False, 0]
tags["E"] = ["letraE", False, False, 0]
tags["R"] = ["letraR", False, False, 0]
tags["T"] = ["letraT", False, False, 0]
tags["Y"] = ["letraY", False, False, 0]
tags["U"] = ["letraU", False, False, 0]
tags["I"] = ["letraI", False, False, 0]
tags["O"] = ["letraO", False, False, 0]
tags["P"] = ["letraP", False, False, 0]
tags["A"] = ["letraA", False, False, 0]
tags["S"] = ["letraS", False, False, 0]
tags["D"] = ["letraD", False, False, 0]
tags["F"] = ["letraF", False, False, 0]
tags["G"] = ["letraG", False, False, 0]
tags["H"] = ["letraH", False, False, 0]
tags["J"] = ["letraJ", False, False, 0]
tags["K"] = ["letraK", False, False, 0]
tags["L"] = ["letraL", False, False, 0]
tags["Z"] = ["letraZ", False, False, 0]
tags["X"] = ["letraX", False, False, 0]
tags["C"] = ["letraC", False, False, 0]
tags["V"] = ["letraV", False, False, 0]
tags["B"] = ["letraB", False, False, 0]
tags["N"] = ["letraN", False, False, 0]
tags["M"] = ["letraM", False, False, 0]

def teclear(event):
    presBtn(event.char.upper())

def presBtn(letra):
    global letrukis, intentos, palabra, mensaje, enJuego
    try:
        if letrukis <= 5 and (letra.isalpha() or ord(letra) == 8) and intentos < 6 and enJuego == True:
            if ord(letra) == 8:
                if letrukis == 0:
                    pass
                else:
                    globals()[f"espacio{intentos}{letrukis-1}"].config(text=" ")
                    letrukis -= 1
                    palabra = palabra[:-1]
            elif letrukis != 5:
                globals()[f"espacio{intentos}{letrukis}"].config(text=letra)
                letrukis += 1
                palabra += letra
        elif letrukis == 5 and intentos < 6 and enJuego == True:
            respuesta = validarPalabra()
            if respuesta == 0: #La palabra no existe
                mensaje.config(text="That word doesn't exist.", bg="#FF5050")
                mensaje.pack(pady=(10, 0))
                root.after(3000, ocultarMensaje)
            elif respuesta == 1:
                mensaje.config(text="Already guessed that one.", bg="#FF5050")
                mensaje.pack(pady=(10, 0))
                root.after(3000, ocultarMensaje)
    except Exception as e:
        pass

def validarPalabra():
    global intentos, letrukis, palabra
    correctos = 0
    
    if palabra not in palabras:
        return 0
    
    if palabra in adivinadas:
        return 1
    
    for letra1 in secreta:
        tags[letra1][3] = secreta.count(letra1)
    
    adivinadas.insert(intentos, palabra)
    for pos1, letra1 in enumerate(palabra):
        letrita = tags[letra1][0]
        for pos2, letra2 in enumerate(secreta):
            if letra1 == letra2 and pos1 == pos2:
                globals()[f"espacio{intentos}{pos1}"].config(text=letra1, bg=LBC_COLOR)
                globals()[letrita].config(text=letra1, bg=LBC_COLOR)
                tags[letra1][1] = True
                tags[letra1][3] -= 1
                correctos += 1
                break
            elif letra1 == letra2 and tags[letra1][3] == 0:
                globals()[f"espacio{intentos}{pos1}"].config(text=letra1, bg=LBN_COLOR)
            elif letra1 == letra2:
                globals()[f"espacio{intentos}{pos1}"].config(text=letra1, bg=LBI_COLOR)
                if tags[letra1][1] == False:
                    globals()[letrita].config(text=letra1, bg=LBI_COLOR)
                    tags[letra1][2] = True
                    tags[letra1][3] -= 1
            elif tags[letra1][1] == False and tags[letra1][2] == False:
                globals()[f"espacio{intentos}{pos1}"].config(text=letra1, bg=LBN_COLOR)
                globals()[letrita].config(text=letra1, bg=LBN_COLOR)

    intentos += 1
    if correctos == 5:
        victoria()
        return
    if intentos == 6:
        derrota()
        return
    letrukis = 0
    palabra = ""

def ocultarMensaje():
    mensaje.pack_forget()

def victoria():
    global enJuego
    mensaje.config(text="You win!", bg=LBC_COLOR)
    mensaje.pack(pady=(10, 0))
    enJuego = False
    root.after(5000, ocultarMensaje)
    root.after(5000, reiniciar_ventana)

def derrota():
    global enJuego
    mensaje.config(text=f"You lose! The word was '{secreta}'", bg="#FF5050")
    mensaje.pack(pady=(10, 0))
    enJuego = False
    root.after(5000, ocultarMensaje)
    root.after(5000, reiniciar_ventana)

def reiniciar_ventana():
    global intentos, letrukis, palabra, secreta, enJuego, adivinadas
    intentos = 0
    letrukis = 0
    palabra = ""
    enJuego = True
    adivinadas = []

    secreta = ran.choice(palabras).upper()

    for i in range(6):
        for j in range(5):
            globals()[f"espacio{i}{j}"].config(text=" ", bg=LBV_COLOR)

    for elemento in tags:
        globals()[tags[elemento][0]].config(bg=LB_COLOR)
        tags[elemento][1] = False
        tags[elemento][2] = False

palabras = ew.get_english_words_set(["web2"], lower=True)
palabras = list(filter(lambda palabra: len(palabra) == 5, palabras))
palabras = [palabra.upper() for palabra in palabras]

secreta = ran.choice(palabras).upper()

root = tk.Tk()
root.title("Ecodle!")
#root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.state('zoomed')

try:
    root.iconbitmap(r"C:\Users\Usuario\Desktop\Bort\Otras cosas\Programación\Python\Ecodle\logo.ico")
except Exception as e:
    pass

cont = tk.Frame(root, background=BG_COLOR)
cont.pack(expand=True, fill="both")

mensaje = tk.Label(cont, font=("Source Code Pro", 20), fg=LT_COLOR)

titulo = tk.Label(cont, text="WORDLE!", font=("Source Code Pro", 40, "bold"), bg=BG_COLOR, fg=LT_COLOR)
titulo.pack(pady=((root.winfo_reqheight()/2), 0))

#Parte para los aciertos
aciertos = tk.Frame(cont, background=BG_COLOR)
aciertos.columnconfigure(0, weight=1)
aciertos.columnconfigure(1, weight=1)
aciertos.columnconfigure(2, weight=1)
aciertos.columnconfigure(3, weight=1)
aciertos.columnconfigure(4, weight=1)

espacio00 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio00.grid(row=0, column=0, padx=2, pady=10, ipadx=10)
espacio01 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio01.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
espacio02 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio02.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
espacio03 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio03.grid(row=0, column=3, padx=2, pady=10, ipadx=10)
espacio04 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio04.grid(row=0, column=4, padx=2, pady=10, ipadx=10)

espacio10 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio10.grid(row=1, column=0, padx=2, pady=10, ipadx=10)
espacio11 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio11.grid(row=1, column=1, padx=2, pady=10, ipadx=10)
espacio12 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio12.grid(row=1, column=2, padx=2, pady=10, ipadx=10)
espacio13 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio13.grid(row=1, column=3, padx=2, pady=10, ipadx=10)
espacio14 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio14.grid(row=1, column=4, padx=2, pady=10, ipadx=10)

espacio20 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio20.grid(row=2, column=0, padx=2, pady=10, ipadx=10)
espacio21 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio21.grid(row=2, column=1, padx=2, pady=10, ipadx=10)
espacio22 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio22.grid(row=2, column=2, padx=2, pady=10, ipadx=10)
espacio23 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio23.grid(row=2, column=3, padx=2, pady=10, ipadx=10)
espacio24 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio24.grid(row=2, column=4, padx=2, pady=10, ipadx=10)

espacio30 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio30.grid(row=3, column=0, padx=2, pady=10, ipadx=10)
espacio31 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio31.grid(row=3, column=1, padx=2, pady=10, ipadx=10)
espacio32 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio32.grid(row=3, column=2, padx=2, pady=10, ipadx=10)
espacio33 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio33.grid(row=3, column=3, padx=2, pady=10, ipadx=10)
espacio34 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio34.grid(row=3, column=4, padx=2, pady=10, ipadx=10)

espacio40 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio40.grid(row=4, column=0, padx=2, pady=10, ipadx=10)
espacio41 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio41.grid(row=4, column=1, padx=2, pady=10, ipadx=10)
espacio42 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio42.grid(row=4, column=2, padx=2, pady=10, ipadx=10)
espacio43 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio43.grid(row=4, column=3, padx=2, pady=10, ipadx=10)
espacio44 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio44.grid(row=4, column=4, padx=2, pady=10, ipadx=10)

espacio50 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio50.grid(row=5, column=0, padx=2, pady=10, ipadx=10)
espacio51 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio51.grid(row=5, column=1, padx=2, pady=10, ipadx=10)
espacio52 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio52.grid(row=5, column=2, padx=2, pady=10, ipadx=10)
espacio53 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio53.grid(row=5, column=3, padx=2, pady=10, ipadx=10)
espacio54 = tk.Label(aciertos, text=" ", font=("Source Code Pro", 30), borderwidth=2, relief="solid", bg=LBV_COLOR)
espacio54.grid(row=5, column=4, padx=2, pady=10, ipadx=10)

aciertos.pack()


#Parte para las letras de arriba
letras1 = tk.Frame(cont, background=BG_COLOR)
letras1.rowconfigure(0, weight=1)

letraQ = tk.Button(letras1, text="Q", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("Q"))
letraQ.grid(row=0, column=0, padx=4, pady=4)
letraW = tk.Button(letras1, text="W", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("W"))
letraW.grid(row=0, column=1, padx=4, pady=4)
letraE = tk.Button(letras1, text="E", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("E"))
letraE.grid(row=0, column=2, padx=4, pady=4)
letraR = tk.Button(letras1, text="R", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("R"))
letraR.grid(row=0, column=3, padx=4, pady=4)
letraT = tk.Button(letras1, text="T", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("T"))
letraT.grid(row=0, column=4, padx=4, pady=4)
letraY = tk.Button(letras1, text="Y", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("Y"))
letraY.grid(row=0, column=5, padx=4, pady=4)
letraU = tk.Button(letras1, text="U", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("U"))
letraU.grid(row=0, column=6, padx=4, pady=4)
letraI = tk.Button(letras1, text="I", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("I"))
letraI.grid(row=0, column=7, padx=4, pady=4)
letraO = tk.Button(letras1, text="O", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("O"))
letraO.grid(row=0, column=8, padx=4, pady=4)
letraP = tk.Button(letras1, text="P", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("P"))
letraP.grid(row=0, column=9, padx=4, pady=4)

letras1.pack()

#Parte para las letras de en medio
letras2 = tk.Frame(cont, background=BG_COLOR)
letras2.rowconfigure(0, weight=1)

letraA = tk.Button(letras2, text="A", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("A"))
letraA.grid(row=0, column=0, padx=4, pady=4)
letraS = tk.Button(letras2, text="S", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("S"))
letraS.grid(row=0, column=1, padx=4, pady=4)
letraD = tk.Button(letras2, text="D", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("D"))
letraD.grid(row=0, column=2, padx=4, pady=4)
letraF = tk.Button(letras2, text="F", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("F"))
letraF.grid(row=0, column=3, padx=4, pady=4)
letraG = tk.Button(letras2, text="G", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("G"))
letraG.grid(row=0, column=4, padx=4, pady=4)
letraH = tk.Button(letras2, text="H", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("H"))
letraH.grid(row=0, column=5, padx=4, pady=4)
letraJ = tk.Button(letras2, text="J", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("J"))
letraJ.grid(row=0, column=6, padx=4, pady=4)
letraK = tk.Button(letras2, text="K", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("K"))
letraK.grid(row=0, column=7, padx=4, pady=4)
letraL = tk.Button(letras2, text="L", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("L"))
letraL.grid(row=0, column=8, padx=4, pady=4)

letras2.pack()

#Parte para las letras de en medio
letras3 = tk.Frame(cont, background=BG_COLOR)
letras3.rowconfigure(0, weight=1)

letraZ = tk.Button(letras3, text="Z", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("Z"))
letraZ.grid(row=0, column=0, padx=4, pady=4)
letraX = tk.Button(letras3, text="X", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("X"))
letraX.grid(row=0, column=1, padx=4, pady=4)
letraC = tk.Button(letras3, text="C", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("C"))
letraC.grid(row=0, column=2, padx=4, pady=4)
letraV = tk.Button(letras3, text="V", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("V"))
letraV.grid(row=0, column=3, padx=4, pady=4)
letraB = tk.Button(letras3, text="B", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("B"))
letraB.grid(row=0, column=4, padx=4, pady=4)
letraN = tk.Button(letras3, text="N", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("N"))
letraN.grid(row=0, column=5, padx=4, pady=4)
letraM = tk.Button(letras3, text="M", font=("Source Code Pro", 25), relief="flat", fg=LT_COLOR, bg=LB_COLOR, command=lambda: presBtn("M"))
letraM.grid(row=0, column=6, padx=4, pady=4)

letras3.pack()

root.bind("<Key>", teclear)

#Pa que jale
root.mainloop()