import os
import subprocess
import sys
import webbrowser
from PIL import Image
from pyzbar import pyzbar


def decode_qr_code(code_img_path):
    if not os.path.exists(code_img_path):
        raise FileExistsError(code_img_path)
    return pyzbar.decode(Image.open(code_img_path), symbols=[pyzbar.ZBarSymbol.QRCODE])


if __name__ == "__main__":
    # 添加此处将获取到的文件路径发送到剪切板
    cmd = 'echo ' + sys.argv[1].strip().replace('"', '') + '|clip'
    subprocess.check_call(cmd, shell=True)
    # 修改此处直接从系统得到了路径
    src = sys.argv[1].replace('\\', '/').replace('"', '')
    results = decode_qr_code(src)
    if len(results):
        if "http://" in results[0].data.decode("utf-8") or "https://" in results[0].data.decode("utf-8"):
            webbrowser.open(results[0].data.decode("utf-8"))
        print(results[0].data.decode("utf-8"))
    else:
        print("Can not recognize.")