import holdem_calc
import os
import streamlit as st
import testImage
import numpy as np
from PIL import Image
import pyscreenshot
import time
#x=holdem_calc.calculate(None, False, 10, None, ["Qd", "Qs", "?", "?"], True)
#print(x)

spades = ["2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","As"]
diamonds = ["2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","Ad"]
hearts = ["2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ah"]
clubs = ["2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc","Ac"]
carteTotal = spades+diamonds+hearts+clubs+["?"]

def main():
    with st.sidebar:
        choixMode = st.radio('Pick one', ['Calcul Manuel','Calcul Auto'])
    if choixMode == "Calcul Auto":
        modeAuto = st.selectbox('Mode',["Clic","Auto","Auto 10s"])
        mainJoueur, boardjoueur = testImage.TestChiffreCouleurMainBoard()
        time.sleep(1)
        if boardjoueur == ["?","?","?","?","?"]:
            st.write("Pas de jeu en cours")
        afficheMainBoard(mainJoueur,boardjoueur)
        calcul = calculProba(mainJoueur, boardjoueur)
        if calcul[0] != "Erreur":
            st.write("Pourcentage de gagner : "+str(int(calcul[1]*1000)/10))
            st.write("Pourcentage de perdre : "+str(int(calcul[2]*1000)/10))
            st.write("Pourcentage d'égalité : "+str(int(calcul[0]*1000)/10))
        
        if modeAuto == "Auto":
            time.sleep(1)
            st.experimental_rerun()
        if modeAuto == "Auto 10s":
            time.sleep(10)
            st.experimental_rerun()
        if modeAuto =="Clic":
            if st.button("Actualisé"):
                st.experimental_rerun()
    if choixMode == "Calcul Manuel":
        hand = st.multiselect('Cartes en main',spades+diamonds+hearts+clubs, ["As","Ad"])
        board = st.multiselect('Cartes du Board (3/4/5)',spades+diamonds+hearts+clubs)
        col1, col2, col3 = st.columns(3)
        if len(hand)==2:
            if col1.button("Calcul sans Board"):
                calcul = holdem_calc.calculate(None, False, 50, None, [hand[0], hand[1], "?", "?"], False)
                st.write("Cartes :",[hand[0], hand[1], "?", "?"])
                st.write("Pourcentage de gagner : "+str(int(calcul[1]*1000)/10))
                st.write("Pourcentage de perdre : "+str(int(calcul[2]*1000)/10))
                st.write("Pourcentage d'égalité : "+str(int(calcul[0]*1000)/10))
            if len(board) >= 3 and col2.button("Calcul avec Board"):
                calcul = holdem_calc.calculate(board, True, 1, None, [hand[0], hand[1], "?", "?"], False)
                st.write("Cartes :",board,[hand[0], hand[1], "?", "?"])
                st.write("Pourcentage de gagner : "+str(int(calcul[1]*1000)/10))
                st.write("Pourcentage de perdre : "+str(int(calcul[2]*1000)/10))
                st.write("Pourcentage d'égalité : "+str(int(calcul[0]*1000)/10))


def afficheMainBoard(mainJoueur,boardjoueur):
    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
    mainImage = []
    for i in range(2):
        if mainJoueur[i] != "?":
            mainImage.append(mainJoueur[i])
        else:
            mainImage.append("rien")
    col1.image('imageCarteTest/'+ mainImage[0] + '.png')
    col2.image('imageCarteTest/'+ mainImage[1] + '.png')
    boardImage = []
    for i in range(5):
        if boardjoueur[i] != "?":
            boardImage.append(boardjoueur[i])
        else:
            boardImage.append("rien")
    col4.image('imageCarteTest/'+ boardImage[0] + '.png')
    col5.image('imageCarteTest/'+ boardImage[1] + '.png')
    col6.image('imageCarteTest/'+ boardImage[2] + '.png')
    col7.image('imageCarteTest/'+ boardImage[3] + '.png')
    col8.image('imageCarteTest/'+ boardImage[4] + '.png')
@st.cache(suppress_st_warning=True)
def calculProba(mainJoueur, boardjoueur):
    if mainJoueur[1] != '?' and boardjoueur == ["?","?","?","?","?"]:
        return(holdem_calc.calculate(None, False, 50, None, [mainJoueur[0], mainJoueur[1], "?", "?"], False))
    if len(mainJoueur) == 2 and  mainJoueur[0] != '?' and mainJoueur[1] != '?' and boardjoueur != ["?","?","?","?","?"]:
        boardCalc = []
        for i in range(5):
            if boardjoueur[i] != "?":
                boardCalc.append(boardjoueur[i])
        return(holdem_calc.calculate(boardCalc, True, 1, None, [mainJoueur[0], mainJoueur[1], "?", "?"], False))
    return(["Erreur"])
main()
