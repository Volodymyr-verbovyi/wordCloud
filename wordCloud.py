import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from googletrans import Translator

import os
from os import path

translator = Translator()

# input_text = input("Введите текст :")


d = path.dirname(__file__) \
    if "__file__" in locals() \
    else os.getcwd()
subtitre = open(path.join(d, 'dataWord/VEED-subtitles_The3.txt')).read()


resultTranslate = translator.translate(subtitre, dest='ru')

text = [subtitre, resultTranslate.text]
#print(text)

textToString = ' '.join(text).split()


finallist = []
for element in textToString:
    if len(element) > 3:
        finallist.append(element)
#print(finallist)

finallistString = ' '.join(finallist)

chars = '.,!-?1234567890'

removeSymbols = finallistString.translate(str.maketrans(' ', ' ', chars))

x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)

wc = WordCloud(background_color="white", repeat=True, mask=mask)
wc.generate(finallistString)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()
