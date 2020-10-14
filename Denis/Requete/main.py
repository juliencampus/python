# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

def nbImage(html):

    html = html.split('\n')

    return len([el for el in html if '.jpg' in el or '.png' in el or '.gif' in el or '.jpeg' in el])

def main():
    r = requests.get('https://www.freeimages.com/fr')

    print(str(nbImage(r.text)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
