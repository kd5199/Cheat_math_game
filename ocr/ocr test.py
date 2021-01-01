try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from subprocess import call
from PIL import Image
import pyautogui

from PIL import ImageGrab
import time
import winsound
import goto
from goto import with_goto, _find_labels_and_gotos

imagecap = True

time.sleep(5)
def run():
    if imagecap == True:

        image = ImageGrab.grab()
        image.save('Q.png')
        image = Image.open("Q.png")

        left = 740
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

        time.sleep(0.5)
        image = ImageGrab.grab()
        image.save('A.png')
        image = Image.open("A.png")

        left = 760
        top = 355
        right = 1160
        bottom = 510

        # Cropped image of above dimension
        # (It will not change orginal image)#################..############
        im2 = image.crop((left, top, right, bottom))#########..############
        #####################################################..############
        # Shows the image in image viewer
        #im1.show()
        im2.save('A.png')

    # The crop method from the Image module takes four coordinates as input.
    # The right can also be represented as (left+width)
    # and lower can be represented as (upper+height).
    """(left, upper, right, lower) = (50, 50, 30, 10)
    
    # Here the image "im" is cropped and assigned to new variable im_crop
    im_crop = image.crop((left, upper, right, lower))
    im_crop.save('sc.png')"""


    # If you don't have tesseract executable in your PATH, include the following:
    #pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    # Simple image to string

    toeval2 = str(pytesseract.image_to_string(Image.open('Q.png')))
    toeval2 = str(toeval2.replace(" ", ""))
    toeval2 = str(toeval2.replace(" ", ""))
    toeval2 = str(toeval2.replace(" ", ""))
    toeval2 = str(toeval2.replace(" ", ""))
    toeval2 = str(toeval2.replace(" ", ""))
    toeval2 = str(toeval2.replace(" ", ""))
    toeval2 = str(toeval2.replace("\n", ""))
    toeval2 = str(toeval2.replace("l", "1"))
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
    toeval2 = str(toeval2.replace("{", "1"))
    toeval2 = str(toeval2.replace("}", "1"))
    print(toeval2)
    while len(toeval2) == 0:
        winsound.PlaySound("*", winsound.SND_ALIAS)
        image = ImageGrab.grab()
        image = Image.open("Q.png")

        left = 740
        top = 234
        right = 1160
        bottom = 348

        # Cropped image of above dimension
        # (It will not change orginal image)#################..############
        im1 = image.crop((left, top, right, bottom))  #########..############
        #####################################################..############
        # Shows the image in image viewer
        # im1.show()
        im1.save('Q.png')
        toeval2 = str(pytesseract.image_to_string(Image.open('Q.png')))
        print(toeval2)
        toeval2 = str(toeval2.replace(" ", ""))
        toeval2 = str(toeval2.replace(" ", ""))
        toeval2 = str(toeval2.replace(" ", ""))
        toeval2 = str(toeval2.replace(" ", ""))
        toeval2 = str(toeval2.replace(" ", ""))
        toeval2 = str(toeval2.replace(" ", ""))
        toeval2 = str(toeval2.replace("\n", ""))
        toeval2 = str(toeval2.replace("l", "1"))
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
        toeval2 = str(toeval2.replace("{", "1"))
        toeval2 = str(toeval2.replace("}", "1"))
        print(toeval2)



    ans = str(pytesseract.image_to_string(Image.open('A.png')))
    ans = str(ans.replace(" ", ""))
    ans = str(ans.replace("l", "1"))
    ans = str(ans.replace("I", "1"))
    ans = str(ans.replace("]", "1"))
    ans = str(ans.replace("[", "1"))
    ans = str(ans.replace("\n", ""))
    ans = str(ans.replace("><", "*"))
    ans = str(ans.replace("O", "0"))
    ans = str(ans.replace("x", "*"))
    ans = str(ans.replace("X", "*"))
    ans = str(ans.replace("/", "/"))
    ans = str(ans.replace("—", "-"))
    ans = str(ans.replace("H", "11"))
    ans = str(ans.replace("=", ""))
    ans = str(ans.replace("C", "0"))
    ans = str(ans.replace("{", "1"))
    ans = str(ans.replace("}", "1"))
    ans = str(ans.replace("!", "1"))
    print("2  " + ans)
    while len(ans) == 0:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        image = ImageGrab.grab()
        image = Image.open("A.png")

        left = 760
        top = 355
        right = 1160
        bottom = 510

        # Cropped image of above dimension
        # (It will not change orginal image)#################..############
        im2 = image.crop((left, top, right, bottom))  #########..############
        #####################################################..############
        # Shows the image in image viewer
        # im1.show()
        im2.save('A.png')
        ans = str(pytesseract.image_to_string(Image.open('A.png')))
        print("1  "+ans)
        ans = str(ans.replace(" ", ""))
        ans = str(ans.replace("l", "1"))
        ans = str(ans.replace("I", "1"))
        ans = str(ans.replace("]", "1"))
        ans = str(ans.replace("[", "1"))
        ans = str(ans.replace("\n", ""))
        ans = str(ans.replace("><", "*"))
        ans = str(ans.replace("O", "0"))
        ans = str(ans.replace("x", "*"))
        ans = str(ans.replace("X", "*"))
        ans = str(ans.replace("/", "/"))
        ans = str(ans.replace("—", "-"))
        ans = str(ans.replace("H", "11"))
        ans = str(ans.replace("=", ""))
        ans = str(ans.replace("C", "0"))
        ans = str(ans.replace("{", "1"))
        ans = str(ans.replace("}", "1"))
        ans = str(ans.replace("!", "1"))
        print("2  "+ans)




    text_file = open("sample.py", "a")
    n = text_file.write(toeval2)

    """time.sleep(0.5)
    if 1+2==3:
        from sample import A
    op = A()"""

    toeval2 ='"'+toeval2+'"'
    print(toeval2)
    try:
        print(int(eval(eval(toeval2))))
    except:
        print("WENT Wrong")
    try:
        if eval(eval(toeval2)) == int(ans):

            print("YEAAAAA")
            pyautogui.click(x=800, y=900)
        elif ans == "" or toeval2=="":
            run()

        elif eval(eval(toeval2)) != int(ans):
            pyautogui.click(x=1100, y=900)
    except:
        print("wrong")
        run()


run()