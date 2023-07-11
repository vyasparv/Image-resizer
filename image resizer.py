# image resizer 

from PIL import Image 

def resize_image(size1, size2):

image = image.open('beatles.jpg')

print(f"Current size : {image.size}")

resized_image = image.resize( (size1, size2))

resized_image.save('beatles-'+ str(size1) +''.jpeg') 
                   
size 1 = int(input('Enter Width:'))
size 2 = int(input('Enter Length:'))
resize_image(size1, size2)