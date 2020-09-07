import PyPDF2
pdffileobj=open('sample.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(x-1) # this is how to go to the next page 
text=pageobj.extractText()

file1=open(r"C:\laragon\www\How-to-Convert-PDF-To-Txt-Using-Python\1.txt","a")
file1.writelines(text)
file1.close()