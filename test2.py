# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams


class PDFUtils():

    def __init__(self):
        pass

    def pdf2txt(self, path):
        with open(path, 'rb') as f:
            praser = PDFParser(f)

            doc = PDFDocument(praser)

            if not doc.is_extractable:
                raise PDFTextExtractionNotAllowed

            pdfrm = PDFResourceManager()

            laparams = LAParams()

            device = PDFPageAggregator(pdfrm, laparams=laparams)

            interpreter = PDFPageInterpreter(pdfrm, device)
            file = '/Users/zbx/Desktop/demo.txt'
            with open(file, 'a') as file_handle:
                for page in PDFPage.create_pages(doc):
                    interpreter.process_page(page)
                    layout = device.get_result()
                    for x in layout:
                        if hasattr(x, "get_text"):
                            content = x.get_text()
                            file_handle.write(content)

        return content


if __name__ == '__main__':
    path = '/Users/zbx/Desktop/mksc.2020.1230.pdf'
    pdf_utils = PDFUtils()
    print (pdf_utils.pdf2txt(path))