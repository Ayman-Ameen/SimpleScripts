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
from PIL import Image


def insert_image_latex(image_path, caption="", extension='pdf'):
    return f"""
    \\begin{{figure}}[h]
    \\centering
    \\includegraphics[width=0.5\\textwidth]{{{image_path}.{extension}}}
    \\caption{{{caption}}}
    \\label{{fig:{image_path}}}
    \\end{{figure}}
    """


def get_files(folder='.'):
    files = []
    for file in os.listdir(folder):
        if not os.path.isdir(file):
            files.append(file)
    return files

def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size

def main(folder):
    files = get_files(folder)
    path_latex = os.path.join(folder, 'latex.txt')
    for file in files:
        file_path = os.path.join(folder, file)
        if file.endswith(('.png', '.jpg', '.jpeg')):
            size = get_image_size(file_path)
            pdf = FPDF(unit="pt", format=size)
            pdf.add_page()
            pdf.image(file_path, 0, 0, size[0], size[1])
            pdf.output(os.path.join(folder, file_path.replace('.png', '.pdf')), "F")
            file_path = file_path.split('/')[-1].replace('.png', '')
            with open(path_latex, 'a') as f:
                f.write(insert_image_latex(file_path, caption=""))
        else:
            print(f'Unsupported file type: {file}')
            

if __name__ == '__main__':
    folder = "path/to/folder"
    main(folder)