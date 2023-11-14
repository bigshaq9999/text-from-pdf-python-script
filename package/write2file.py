import pdftotext

print("Thank you for using this script! Which pdf file would you like to extract text from?")

file_name = input("File name (with .pdf): ")

with open(file_name, "rb") as f:
    pdf = pdftotext.PDF(f)

output_file = "CONTENT_OF_" + file_name + ".txt" 
    
content_file = open(output_file, "w")

for page in pdf:
    content_file.write(page)
