from pdf2image import convert_from_path
import os
import sys
import time

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


file = (r'C:\Users\Ramesh\Desktop\Parsing_Project\Resumes_pdf\Sakshi Dixit.pdf')
convert(file, outputDir)


