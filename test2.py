# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
import os


class PDFUtils():

    def __init__(self):
        pass

    def pdf2txt(self, path, save):
        with open(path, 'rb') as f:
            praser = PDFParser(f)

            doc = PDFDocument(praser)

            if not doc.is_extractable:
                raise PDFTextExtractionNotAllowed

            pdfrm = PDFResourceManager()

            laparams = LAParams()

            device = PDFPageAggregator(pdfrm, laparams=laparams)

            interpreter = PDFPageInterpreter(pdfrm, device)
            file = save
            with open(file, 'a') as file_handle:
                for page in PDFPage.create_pages(doc):
                    interpreter.process_page(page)
                    layout = device.get_result()
                    for x in layout:
                        if hasattr(x, "get_text"):
                            content = x.get_text()
                            file_handle.write(content)

Location='/Users/zbx/Desktop/Summer/MS'
if __name__ == '__main__':
    k=0
    pdf_utils = PDFUtils()
    files = os.listdir(Location + '/Passage')
    for file in files:
        if file == '.DS_Store' : continue
        print(file)
        path = Location + '/Passage/'+file
        save = Location + '/Passage2/'+file[:-4]+'.txt'
        try:
            os.remove(save)
        except:
            print('fuck ')
        pdf_utils.pdf2txt(path,save)
        os.remove(path)
        k=k+1
        print(k)

