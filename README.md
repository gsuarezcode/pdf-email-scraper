# pdf-email-scraper
A simple script to scrap emails from pdfs both offline and online

With this script you can choose which function do you need. If you have an OnlinePDF() or OfflinePDF()
It works just with the url of the pdf you want to scrape in Online, or the pdf file name in Offline.

The script just uses requests to get the pdf, then we save it to the disc for processing.
Then we just scrap it for mails and we export it to an excel file.

Its a work in progress but it works.

MODULES:
-io
-pdfminer3
-re
-pandas
-requests
