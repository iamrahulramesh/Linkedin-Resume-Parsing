import cv2
from pdf2image import convert_from_path
import os
import sys
import time
import cv2
import numpy as np
import pytesseract
import threading
import glob
from pathlib import Path

address_list = []
outputDir = (r"C:\Users\Ramesh\Desktop\Parsing_Project\Resumes")


def convert(file, outputDir):
    outputDir = outputDir + str(round(time.time())) + '/'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    pages = convert_from_path(file, 500)
    counter = 1
    for page in pages:
        myfile = outputDir +'output' + str(counter) +'.jpg'
        counter = counter + 1
        page.save(myfile, "JPEG")
        return (myfile)



for file in glob.glob(r'C:\Users\Ramesh\Desktop\Parsing_Project\Resumes_pdf/**/*.pdf', recursive=True):

    address_list.append(file)
    
print(address_list)

for file in address_list:
    
    myfile = convert(file, outputDir)
    
    
    image = cv2.imread(myfile)
    image = cv2.resize(image,(800,740))

    gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = np.array([[-1,-1,-1], 
                       [-1, 9,-1],
                       [-1,-1,-1]])

    sharpened = cv2.filter2D(gray_image, -1, kernel)

    f = open(r'C:\Users\Ramesh\Desktop\Parsing_Project\parsed.txt', "a")

    def name(image):
        f.write('Name:')
        name_cropped = sharpened[30:70, 250:600]
        text = pytesseract.image_to_string(name_cropped).replace(',', ' ')
        print(text)
        f.write(text + '\n')
    
    

    def contact(image):
        f.write('Contact:')
        contact_cropped = sharpened[10:125, 10:200]
        text = pytesseract.image_to_string(contact_cropped).replace(',', ' ')
        print(text)
        f.write(text + '\n')
    

    def designation(image):
        f.write('Designation:')
        designation_cropped = sharpened[60:90, 250:600]
        text = pytesseract.image_to_string(designation_cropped).replace(',', ' ')
        print(text)
        f.write(text + '\n')
    


    def place(image):
        f.write('Place:')
        place_cropped = sharpened[85:100, 250:600]
        text = pytesseract.image_to_string(place_cropped).replace(',', ' ')
        print(text)
        f.write(text + '\n')
    


    def skills(image):
        f.write('Skills:')
        skills_cropped = sharpened[110:210, 10:220]
        text = pytesseract.image_to_string(skills_cropped).replace(',', ' ')
        print(text)
        f.write(text + '\n')
        f.close()
    

    threading.Thread(target =name(image)).start()
    threading.Thread(target =contact(image)).start()
    threading.Thread(target =designation(image)).start()
    threading.Thread(target =place(image)).start()
    threading.Thread(target =skills(image)).start()
