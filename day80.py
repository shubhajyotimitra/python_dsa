# Merge the PDF files problem solving day-74

from PyPDF2 import PdfMerger
import os

merger = PdfMerger()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
