import sys
import re


def hashtag_extractor(file):
    with open(file, 'r') as f:
        text = f.read()
    hashtags = re.findall(r"#(\w+)", text)

    return hashtags


if __name__ == '__main__':
    try:
        if sys.argv[1] is not None:
            address = sys.argv[1]
            hashtags = hashtag_extractor(address)
    except:
        print("please enter the correct address :) ")
