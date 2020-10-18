from io import StringIO
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
import re
import pandas as pd
import requests

# OBTENEMOS LA PAGINA Y LA GUARDAMOS EN EL DISCO

def GetPDF(page):
    page = requests.get(page)

    archivo = open('pdf.pdf', 'wb')

    for line in page.iter_content(100000):
        archivo.write(line)


    archivo.close()

# CON ESTA FUNCION SE EXTRAEN LOS MAILS DEL PDF
def get_email(pdf):
    pagenums = set()
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(pdf, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    df = pd.DataFrame(email)
    df.to_excel('mails.xlsx', sheet_name='EMAILS', header=False, index=False,)


def OnlinePDF(page):

    GetPDF(page)
    get_email('pdf.pdf')

def OfflinePDF(pdf):
    get_email(pdf)

# OnlinePDF() for online pdfs with the url as an argument
# OfflinePDF() for offline pdfs with the pdf file name as an argument
