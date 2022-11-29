import pyautogui as auto
import pytesseract as tess
import time

tess.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

cardPos = (980,600)
fieldPos = (970,765)
defStartPos = (683,516)
defEndPos = (1278,547)

running = False

while True:
    while True:
        auto.click(cardPos[0], cardPos[1])
        time.sleep(1.3)
        textImg = auto.screenshot(region=(defStartPos[0], defStartPos[1], defEndPos[0] - defStartPos[0], defEndPos[1] - defStartPos[1]));
        text = tess.image_to_string(textImg)
        text = text.replace('\n', '');
        if(text != ''): break
    print(text)

    auto.click(cardPos[0], cardPos[1])
    time.sleep(.7)
    auto.click(fieldPos[0], fieldPos[1])
    time.sleep(0.1)
    auto.typewrite(text)
    time.sleep(0.1)
    auto.press('enter')
    time.sleep(0.3)
