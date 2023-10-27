#!/usr/bin/env python3
from PyPDF2 import PdfReader, PdfWriter, Transformation
from PyPDF2 import PageObject
from tqdm import tqdm
import argparse
import os

def get_info(path, margin=30):
    with open(path, 'rb') as f:
        p = PdfReader(f)
        info = p.metadata
        print(f"width: {p.pages[0].mediabox.width}")
        number_of_pages = len(p.pages)

        writer = PdfWriter()
        
        print(f'margin: {margin}')
        for i in tqdm(range(number_of_pages)):
            page = p.pages[i]
            new_page = PageObject.create_blank_page(
                width=page.mediabox.width + 2 * margin,
                height=page.mediabox.height + 2 * margin
            )
            #new_page.mergeScaledTranslatedPage(page, 1, margin, margin)
            new_page.merge_page(page)
            new_page.add_transformation(Transformation().scale(1).translate(margin, margin))
            writer.add_page(new_page)
            ## new_page is the writer
        writename = path.replace(".pdf", "_margin.pdf")
        with open(writename, 'wb') as f:
            writer.write(f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", help="file to process")
    parser.add_argument("-m", "--margin", help="margins of pdf to add")
    args = parser.parse_args()
    path = os.getcwd()
    margin = int(args.margin)
    fullpath = path + '/' + args.file

    get_info(fullpath, margin=margin)