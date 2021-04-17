import codecs
import re
import glob

if __name__ == "__main__":
    filename = glob.glob('./*.ipynb')
    f = codecs.open(''.join(filename), "r", "utf-8").read()
    command1 = re.compile("fit")
    assert len(command1.findall(f)) > 0
