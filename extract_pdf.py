import PyPDF2

with open('Yiswa PDF.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    
    with open('pdf_content.txt', 'w', encoding='utf-8') as output:
        output.write(text)
    
    print("PDF content extracted successfully!")
    print("\n" + "="*50)
    print(text)
