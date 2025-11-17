# Merge the PDF files problem solving day-74

from pypdf import PdfMerger
import os

merger = PdfMerger()
files = sorted([f for f in os.listdir() if f.lower().endswith(".pdf")])

# Optional: print files that will be merged
print("Merging these files in order:")
for f in files:
    print(" -", f)

for pdf in files:
    with open(pdf, "rb") as fh:
        merger.append(fh)

with open("merged-pdf.pdf", "wb") as out:
    merger.write(out)

merger.close()
print("Done: merged-pdf.pdf created")
