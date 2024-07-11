# combine all images and pdf into one pdf
# usage: python3 combine.py
# get all images and pdfs in the current directory
# and combine them into one pdf
# the order is sorted by filename
# the output pdf is named output.pdf

import os
import sys
from PyPDF2 import PdfMerger 
from fpdf import FPDF


def get_files(folder='.'):
    files = []
    for file in os.listdir(folder):
        if not os.path.isdir(file):
            files.append(file)
    return files


def main(folder):
    files = get_files(folder)
    files.sort()
    merger = PdfMerger()
    for file in files:
        file_path = os.path.join(folder, file)
        if file.endswith('.pdf'):
            merger.append(file_path)
        elif file.endswith(('.png', '.jpg', '.jpeg')):
            pdf_temp_folder = os.path.join(folder, 'Single_PDFs')
            os.makedirs(pdf_temp_folder, exist_ok=True)
            pdf = FPDF()
            pdf.add_page()
            pdf.image(file_path, 0, 0, 210, 297)
            pdf.output(os.path.join(pdf_temp_folder, file_path.replace('.png', '.pdf')), "F")
            merger.append(os.path.join(pdf_temp_folder, file_path.replace('.png', '.pdf')))
        else:
            print(f'Unsupported file type: {file}')
            

    output = os.path.join(folder, 'output.pdf')
    merger.write(output)
    merger.close()

if __name__ == '__main__':
    folder = "path/to/folder"
    main(folder)