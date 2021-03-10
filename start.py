# -*- coding: utf-8 -*-


#      WIR SIND HIER !!!
#  WAS MUSSEN WIR MACHEN ??
#     ERROR HANDLING
#         POPUPs
#      SAUBEREN CODE


import face_recognition as frc
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import *
import json
import time
from PIL import ImageFont
from PIL import ImageDraw
import argparse
loading = 0
limite = 0

time_tk = []

#Load the image

def load(path):
 global loading
 global input,face,face_l
 input = frc.load_image_file(path)
 face = frc.face_locations(input,model="hog")
 face_l = frc.face_landmarks(input,model="large")
 loading = loading + 20

def start(path):
 global loading
 face_errors = False

 for i in face_l:
   chin = i.get("chin")
   left_eyebrow = i.get("left_eyebrow")
   right_eyebrow = i.get("right_eyebrow")
   nose_bridge = i.get("nose_bridge")
   nose_tip = i.get("nose_tip")
   left_eye = i.get("left_eye")
   right_eye = i.get("right_eye")
   top_lip = i.get("top_lip")
   bottom_lip = i.get("bottom_lip")
   points1 = list()

   for points in chin,left_eyebrow,right_eyebrow,nose_bridge,nose_tip,left_eye,right_eye,top_lip,bottom_lip:
     for x in range(0,len(points)):
       x1,y1 = points[x]
       points1.append((x1,y1))

 for faces in face:
  (x,y,w,h) = faces

 loading = loading + 20

 if len(face) == 1 :

     back = Image.open(path)
     foreground = Image.open("./src/images/imageedit_1_2789986383(1).png").convert("RGBA")
     foreground = foreground.resize((int(w-x+(w-x)/3),int(w-x+(w-x)/3)))

     h1,w1=foreground.size
     back.paste(foreground, (int(h-h/55),int(x-h/55)), foreground)

     font = ImageFont.truetype("./src/fonts/neuropolitical rg.ttf", int(w/15))

     im = cv2.cvtColor(np.array(back),cv2.COLOR_RGB2BGR)

     #LANDMARKS_TRIANGLES
     loading = loading + 30
     def rect_contains(rect, point) :
        if point[0] < rect[0] :
            return False
        elif point[1] < rect[1] :
            return False
        elif point[0] > rect[2] :
            return False
        elif point[1] > rect[3] :
            return False
        return True

    # Draw a point
     if back.width < 800:
        lfont = 1
        rcircle = 2
     else:
        lfont = 2
        rcircle = 4
     def draw_point(img, p, color ) :

        cvc = cv2.circle( img, p,rcircle, color, cv2.FILLED, cv2.LINE_AA, 0 )




    # Draw delaunay triangles
     def draw_delaunay(img, subdiv, delaunay_color ) :

        triangleList = subdiv.getTriangleList();
        size = img.shape
        r = (0, 0, size[1], size[0])

        for t in triangleList :

            pt1 = (t[0], t[1])
            pt2 = (t[2], t[3])
            pt3 = (t[4], t[5])

            if rect_contains(r, pt1) and rect_contains(r, pt2) and rect_contains(r, pt3) :

                cv2.line(img, pt1, pt2, delaunay_color, lfont, cv2.LINE_AA, 0)
                cv2.line(img, pt2, pt3, delaunay_color, lfont, cv2.LINE_AA, 0)
                cv2.line(img, pt3, pt1, delaunay_color, lfont, cv2.LINE_AA, 0)


     animate = True

        # Define colors for drawin
     delaunay_color = (25,0,0)
     points_color = (0, 0, 255)


     img = im

        # Keep a copy around
     img_orig = img.copy();

        # Rectangle to be used with Subdiv2D
     size = img.shape
     rect = (0, 0, size[1], size[0])


     subdiv = cv2.Subdiv2D(rect);
     for p in points1 :
        subdiv.insert(p)
        if animate :
            img_copy = img_orig.copy()
            draw_delaunay( img_copy, subdiv, (255,219,0) );
            imw,imh,c = img_copy.shape


        # Draw points
     for p in points1 :
      draw_point(img_copy, p, (255,255,255))

     loading = loading + 30

     img_cop = cv2.cvtColor(img_copy,cv2.COLOR_BGR2RGB)
     cv2.imwrite("./src/images/id2_.png",img_copy)

 elif len(face) == 0:
     face_errors = None

 else:
     face_errors = True

 return face_errors


def search(inp):
 global id_name
 id_name = []
 global time_tk
 time_tk = []
 global limite
 limite = len(os.listdir("./data/"))

 inp = frc.load_image_file(inp)
 face = frc.face_locations(inp,model="hog")
 enc1 = frc.face_encodings(inp,face)

 for files in os.listdir("./data/"):
  start = time.time()

  for np_enc in os.listdir(f"./data/{files}/"):
      #final = time.time() - start
      if np_enc == "enc.npy":

       enc2 = np.load(f"./data/{files}/enc.npy")
       predict = frc.compare_faces(enc1,enc2,0.6)

       if str(predict[0]) == "True":
        id_name.append(files)
  final = time.time() - start
  time_tk.append(final)


#Create id
def id_card():
 try:
  im1 = Image.open("./src/images/test.jpg")
  id = Image.open("./data/"+str(id_name[0])+"/"+str(id_name[0])+".jpg").convert("RGBA").resize((200,200))
  id_b = Image.open("./src/images/imageedit_3_5670490135.png")
  id_b = id_b.resize((132,142))
  id = id.resize((110,110))
  im2 = Image.open("./src/images/id3.png")
  w2,h2 = im2.size
  im2.paste(id,(int(w2/4.8),int(h2/4.5)),id)
  im2.paste(id_b,(int(w2/5.2),int(h2/5.5)),id_b)
  draw = ImageDraw.Draw(im2)
  font = ImageFont.truetype("./src/fonts/neuropolitical rg.ttf", 20)
  font2 = ImageFont.truetype("./src/fonts/neuropolitical rg.ttf", 19)
  with open(f"./data/{str(id_name[0])}/data.json","r") as read:
    data = json.load(read)
  draw.text((int(w2/2.35),int(h2/5)+15),"Full Name : " + str(data['name']),(153, 242, 255),font=font)
  draw.text((int(w2/2.35),int((h2/5)+45)),"D.O.B : "+str(data['dob']),(153, 242, 255),font=font)
  draw.text((int(w2/2.35),int((h2/5)+75)),"Country/City: "+str(data['cc']),(153, 242, 255),font=font)
  draw.text((int(w2/2.35),int((h2/5)+105)),"Gender : "+str(data['gen']) ,(153, 242, 255),font=font)
  draw.text((int(w2/5),int((h2/5)+145)),"Citizenship : "+str(data['cit']) ,(153, 242, 255),font=font2)
  draw.text((int(w2/5),int((h2/5)+170)),"Job : "+str(data['job']) ,(153, 242, 255),font=font2)
  draw.text((int(w2/5),int((h2/5)+195)),"Work location : "+str(data['job_loc']) ,(153, 242, 255),font=font2)
  draw.text((int(w2/5),int((h2/5)+220)),"Phone number 1 : "+str(data['phone_n1']) ,(153, 242, 255),font=font2)
  draw.text((int(w2/5),int((h2/5)+245)),"Phone number 2 : "+str(data['phone_n2']) ,(153, 242, 255),font=font2)
  draw.text((int(w2/5),int((h2/5)+270)),"Residence address : "+str(data['addr']) ,(153, 242, 255),font=font2)
  draw.text((int(w2/5),int((h2/5)+295)),"E-mail : "+str(data['email']) ,(153, 242, 255),font=font2)

  im2.save("./src/images/id2.png")
 except:
     return False
