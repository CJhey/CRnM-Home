import os
from PyPDF2 import PdfMerger

# Specify the directory containing the PDF files
pdf_directory = 'C:/Users/tetsu/Documents/GitHub/crnm-home/assets/slides/no_disclaimer/'

# Specify the file to merge with each individual PDF
merge_file = 'C:/Users/tetsu/Documents/GitHub/crnm-home/assets/slides/no_disclaimer/logodisc.pdf'

# Get all PDF files in the directory
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

# Loop through each PDF file and merge it with the common file
for pdf_file in pdf_files:
    # Create a PDF merger instance for each file
    merger = PdfMerger()

    # Open the PDF file
    pdf_path = os.path.join(pdf_directory, pdf_file)
    merger.append(pdf_path)

    # Append the merge file as the last page
    merger.append(merge_file)

    # Specify the path for the merged PDF file
    merged_pdf_path = os.path.splitext(pdf_path)[0] + '.merged.pdf'

    # Write the merged PDF to the output file
    with open(merged_pdf_path, 'wb') as output_pdf:
        merger.write(output_pdf)

    # Close the merger
    merger.close()
