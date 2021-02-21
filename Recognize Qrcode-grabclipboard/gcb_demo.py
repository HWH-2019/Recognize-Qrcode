import webbrowser
from PIL import ImageGrab
from pyzbar import pyzbar

if __name__ == "__main__":
    image = ImageGrab.grabclipboard()
    if image is None:
        print("未从剪切板读取到图片")
        results = ''
    else:
        results = pyzbar.decode(image, symbols=[pyzbar.ZBarSymbol.QRCODE])
    if len(results):
        if "http://" in results[0].data.decode("utf-8") or "https://" in results[0].data.decode("utf-8"):
            webbrowser.open(results[0].data.decode("utf-8"))
        print(results[0].data.decode("utf-8"))
    else:
        print("Can not recognize.")
