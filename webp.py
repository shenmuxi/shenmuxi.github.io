import glob
import os
import threading
import re

from PIL import Image

def get_file_name(path_string):
    """获取文件名称"""
    pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
    data = pattern.findall(path_string)
    if data:
        return data[0]

def create_image(infile, index):
 os.path.splitext(infile)
 im = Image.open(infile)
 im.save("webp/" + get_file_name(infile) + ".webp", "WEBP")


def start():
 index = 0
 for infile in glob.glob("img/*.png"):
  t = threading.Thread(target=create_image, args=(infile, index,))
  t.start()
  t.join()
  index += 1


if __name__ == "__main__":
 start()
