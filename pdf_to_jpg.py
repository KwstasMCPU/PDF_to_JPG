from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import tempfile
import webbrowser, os
import glob

inputpath = "pdf"
outputpath = "jpg"

def turnPdftoImg(outputpath,inputpath):
    '''
    this function takes a directory as an input, find all the pdfs in it, and converts them into an image type
    (if a pdf has multiple pages, these are splited in relevant .jpg files)
    outputpath : folder directory where the image type will be stored
    inputpath  : directory where the pdf files are located
    '''
    with tempfile.TemporaryDirectory() as path:
        for pdf_file in (glob.glob1(inputpath,"*.pdf")):    #glob.glob1(outputpath,"*.pdf") returns a list of names of all .pdf files in a directory
            pdf_directory = inputpath + '\\' + pdf_file
            images_from_path =  convert_from_path(pdf_directory, dpi = 80, output_folder = outputpath, fmt = "jpeg")

def rename_img_in_a_dir(outputpath):
    '''
    renames multiple .jpg files in a given directory
    '''
    for count, filename in enumerate(glob.glob1(outputpath,"*.jpg")): #glob.glob1(outputpath,"*.jpg") returns a list of names of all .jpg files in a directory while os.listdir(‘Src’) returns all files
            dst ="Img" + str(count+1) + ".jpg"
            src = outputpath +'\\'+ filename
            dst = outputpath +'\\'+ dst
            # rename() functionto rename the files
            os.rename(src, dst)

#####

# calling the functions
turnPdftoImg(outputpath,inputpath)
rename_img_in_a_dir(outputpath)

# open the output folder
webbrowser.open(os.path.realpath(outputpath))











