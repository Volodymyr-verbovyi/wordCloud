import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from googletrans import Translator

import os
from os import path

translator = Translator()

# input_text = input("Введите текст :")


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text2 = open(path.join(d, 'dataWord/VEED-subtitles_The2.txt')).read()

# f = open('text.txt', 'r')
# translator.detect(input_text)
result = translator.translate(text2, dest='ru')

text = [text2, result.text]

text1 = ' '.join(text)
print(text1)

x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)

wc = WordCloud(background_color="white", repeat=True, mask=mask)
wc.generate(text1)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()
