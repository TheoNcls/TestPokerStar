import cv2
import numpy as np
from PIL import Image
import pyscreenshot




def TestImageChiffre(imageTest):
    spades = ["2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","As"]
    diamonds = ["2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","Ad"]
    hearts = ["2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ah"]
    clubs = ["2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc","Ac"]
    carteTot = spades+diamonds+hearts+clubs
    for carteTest in carteTot:
        template = cv2.imread('imageCarte/'+carteTest+'.png')
        w, h = template.shape[:-1]

        res = cv2.matchTemplate(imageTest, template, cv2.TM_CCOEFF_NORMED)
        threshold = .8
        loc = np.where(res >= threshold)
        if loc[0].size >= 2:
            #print("Il y a un :"+carteTest)
            #print(loc[0])

        #for pt in zip(*loc[::-1]):  # Switch collumns and rows
        #    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        #cv2.imwrite('result'+carteTest+'.png', img_rgb)
    #print(result[-1], result[-2])
            return(carteTest)
def TestImageCouleur(image):
    color=[255,255,255]
    for y in range(5, 30, 3):
        for x in range(5, 30, 3):
            color = [image[x, y] [0],image[x, y] [1],image[x, y] [2]]
            if color != [255,255,255]:
                break
        if color != [255,255,255]:
                break
    if color[0]>color[1] and color[0]>color[2]:
        return('d')
    if color[1]>color[0] and color[1]>color[2]:
        return('c')
    if color[2]>color[0] and color[2]>color[1]:
        return('h')
    return('s')

def ChiffreCouleurCarte(image):
    ChiffreImage = TestImageChiffre(image)
    CouleurImage = TestImageCouleur(image)
    if ChiffreImage == None or CouleurImage == None:
        Carte = "?"
    else:
        Carte = ChiffreImage[0]+CouleurImage
    return(Carte)

def TestChiffreCouleurMainBoard():
    imageATest = pyscreenshot.grab()
    img_rgb = cv2.cvtColor(np.array(imageATest), cv2.COLOR_RGB2BGR)
    MainTrouve = []
    BoardTrouve = [] 
    MainTrouve.append(ChiffreCouleurCarte(img_rgb[440:478, 428:474])) #Carte Main 1
    MainTrouve.append(ChiffreCouleurCarte(img_rgb[440:478, 483:530])) #Carte Main 2
    BoardTrouve.append(ChiffreCouleurCarte(img_rgb[254:295, 342:386])) #Carte Board 1
    BoardTrouve.append(ChiffreCouleurCarte(img_rgb[254:295, 400:446])) #Carte Board 2
    BoardTrouve.append(ChiffreCouleurCarte(img_rgb[254:295, 456:502])) #Carte Board 3
    BoardTrouve.append(ChiffreCouleurCarte(img_rgb[254:295, 512:564])) #Carte Board 4
    BoardTrouve.append(ChiffreCouleurCarte(img_rgb[254:295, 572:623])) #Carte Board 5
    return(MainTrouve, BoardTrouve)

#imageATest=pyscreenshot.grab(bbox=(400,400,600,550))
"""
imageATest = pyscreenshot.grab(bbox=(428, 440, 474, 478))
imageATest.save("imageATest.png")
img_rgb = cv2.cvtColor(np.array(imageATest), cv2.COLOR_RGB2BGR)
#img_rgb = cv2.imread("imageATest.png")
MainTrouve = []
MainTrouve.append(TestImageChiffre(img_rgb)[0]+TestImageCouleur(imageATest))
imageATest = pyscreenshot.grab(bbox=(483, 440, 530, 478))
imageATest.save("imageATest.png")
img_rgb = cv2.imread("imageATest.png")
MainTrouve.append(TestImageChiffre(img_rgb)[0]+TestImageCouleur(imageATest))
print(MainTrouve)
"""
"""

import pyscreenshot
# Pour récupérer les cartes
# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
image1 = pyscreenshot.grab(bbox=(428, 440, 474, 478))
image2 = pyscreenshot.grab(bbox=(483, 440, 530, 478))

image1.save("imageCarteTest/2d.png")
image2.save("imageCarteTest/Ad.png")
"""
"""
from PIL import Image
for carteTest in carteTot:
    Image1 = Image.open('imageCarteTest/'+carteTest+'.png')
    croppedIm = Image1.crop((20, 2, 45, 37))
    croppedIm.save('imageCarte/'+carteTest+'.png')
"""

#import pyscreenshot
#im=pyscreenshot.grab()
#img_rgb = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
'''
img = cv2.imread('pierre.png')
print('Original Dimensions : ',img.shape)
 
scale_percent = 75 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
'''
#cv2.imshow("Resized image", resized)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#main1 = resized[440:478, 428:474]
#main2 = img_rgb[440:478, 483:530]
#cv2.imshow("cropped", main1)
#cv2.imshow("test",img_rgb)
#cv2.waitKey(0)
#cropped = img[y:y+h, x:x+w]
#board1 = img_rgb[254:295, 342:386]
#board2 = img_rgb[254:295, 400:446]
#board3 = img_rgb[254:295, 456:502]
#board4 = img_rgb[254:295, 512:564]
#board5 = img_rgb[254:295, 572:623]
