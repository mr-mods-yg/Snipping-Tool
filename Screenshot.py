from PIL import ImageGrab, ImageOps
from pynput import mouse
import pytesseract as tess

def click(x, y, button, pressed):
    global x1, y1, x2, y2,tpl
    if tpl ==None:
        if pressed:
            z = 'Pressed'
            print(f'{z} at {(x, y)}')
            x1, y1 = x, y
        else:
            z = 'Released'
            print(f'{z} at {(x, y)}')
            x2, y2 = x, y
            listener.stop()
            tpl = (x1,y1,x2,y2)
            m1 = ImageGrab.grab(bbox=tpl)
            # m1 = ImageOps.grayscale(m1)
            m1.save('Capture.png')
            print("Image Saved as Capture.png")
    else:
        listener.stop()
        m1 = ImageGrab.grab(bbox=tpl)
        # m1 = ImageOps.grayscale(m1)
        m1.save('Capture.png')
        print("Image Saved as Capture.png")


if __name__=='__main__':
    tpl = None          
    with mouse.Listener(on_click=click) as listener:
            listener.join()