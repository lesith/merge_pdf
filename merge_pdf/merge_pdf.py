from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = []  # List for storing file paths
    directory = input('Input directory path to the PDF files to be merged: ')
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)
            paths.append(os.path.abspath(entry))
    merge_pdfs(paths, output='merged_output.pdf')
