import img2pdf
from PIL import Image

def convert_pdf(source,output):
    image = Image.open(source)
    pdf = img2pdf.convert(image.filename)
    with open(output,"wb") as img:
        img.write(pdf)
    img.close()
    print("Successfull")
#source and output is optional, you can replace it according to the needs in your directory
convert_pdf("image1.jpg","file.pdf")
