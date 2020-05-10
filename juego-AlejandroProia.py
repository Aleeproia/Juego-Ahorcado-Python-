import hangman
import reversegam
import tictactoeModificado
import json
import PySimpleGUI as sg

archivo = 'Juego.txt'

dic = {}

with open(archivo,'w') as f:
         json.dump(dic,f)

#Utilizo un diccionario con listas,para que cada clave sea el nombre y el valor sea los juegos que jugó

def agregar_Juego(archivo,nombre,juego):  
    with open(archivo,'r') as f:          #Abro el archivo en modo lectura
        dic=json.load(f)                  #Cargo lo que tiene el archivo en el diccionario
        if nombre in dic.keys():          #Pregunto si el nombre existe en el diccionario
            dic[nombre]+=[juego]          #Agrego el juego en un mismo nombre
        else:                             
            lista=[]                      #De lo contraio agrego nombre de jugador y juego que jugó
            lista.append(juego)           
            dic.setdefault(nombre,lista)
    with open(archivo,'w') as f:
        json.dump(dic,f) #Almaceno lo del diccionario en el archivo txt
        print(dic)

# Utilizo json por que fue lo primero que conoci y me resulto mas facil manejarme con txts
def main(args):

    while True:

        layout=[[sg.Text('Ingrese su nombre'), sg.Text(size=(15,1))],
                [sg.Input(key='nombre')],
                [sg.Text('Ingrese que juego desea jugar'), sg.Text(size=(15,1))],
                [sg.Button('Ahorcado'),sg.Button('Ta-TE-TI'),sg.Button('Otello'),sg.Button('Exit')]]

        window= sg.Window('Modificar datos',layout)

        event, values = window.read()

        if event == 'Ahorcado':
            hangman.main()
            juego= 'Ahorcado'
        elif event == 'Ta-TE-TI':
            tictactoeModificado.main()
            juego= 'Ta-TE-TI'
        elif event == 'Otello':
            reversegam.main()
            juego= 'Otello'
        elif event == 'Exit':
            break
        nombre=values['nombre']
        agregar_Juego(archivo,nombre,juego)

        window.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))