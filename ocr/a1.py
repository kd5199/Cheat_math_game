try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from subprocess import call
from PIL import Image
from PIL import ImageGrab
import time
"""
image = ImageGrab.grab()
image.save('Q.png')
image = Image.open("Q.png")

left = 760
top = 234
right = 1160
bottom = 348

# Cropped image of above dimension
# (It will not change orginal image)#################..############
im1 = image.crop((left, top, right, bottom))#########..############
#####################################################..############
# Shows the image in image viewer
#im1.show()
im1.save('Q.png')
image = ImageGrab.grab()
image.save('Q.png')
image = Image.open("Q.png")

left = 760
top = 234
right = 1160
bottom = 520

im1 = image.crop((left, top, right, bottom))#########..############

im1.save('Q.png')"""





# Simple image to string
toeval2 = str(pytesseract.image_to_string(Image.open('Q.png')))
print("toeval:::"+toeval2)
toeval2 = str(toeval2.replace(" ", ""))
toeval2 = str(toeval2.replace("l", "1"))
toeval2 = str(toeval2.replace("\n", ""))
toeval2 = str(toeval2.replace("I", "1"))
toeval2 = str(toeval2.replace("]", "1"))
toeval2 = str(toeval2.replace("[", "1"))
toeval2 = str(toeval2.replace("><", "*"))
toeval2 = str(toeval2.replace("O", "0"))
toeval2 = str(toeval2.replace("x", "*"))
toeval2 = str(toeval2.replace("X", "*"))
toeval2 = str(toeval2.replace("/", "/"))
toeval2 = str(toeval2.replace("—", "-"))
toeval2 = str(toeval2.replace("H", "11"))
toeval2 = str(toeval2.replace("C", "0"))
toeval2 = str(toeval2.replace("=", ""))


"""text_file = open("sample.py", "w")
n = text_file.write("def A():return {}".format(toeval2)+"\n"+"A()")
text_file.close()
toeval2 = str(toeval2)


time.sleep(1)
op = call(["python", "sample.py"])
print("op::::")
print(op)"""
"""if str(op) == ans:
    print("YEAAAAA")"""
try:
    print("final::::"+eval("5+2==7"))

except:
    print("WENT Wrong")
