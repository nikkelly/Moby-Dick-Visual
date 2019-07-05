from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from bs4 import BeautifulSoup
import requests 
import os 

#sGet Directory for Picture
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

#Get Moby Dick
r = requests.get('https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm')
r.encoding = 'utf-8'
html = r.text
soup = BeautifulSoup(html, 'htlp.parser')
text = soup.text

#read the image
whale_picture = np.array(Image.open(path.join(d, 'whale.png')))

stopwords = set(STOPWORDS)

#Initialize WordCloud
wc = WordCloud(backgroud_color='white', max_words=2000, mask=whale_picture, stopwords=stopwords, contour_width=3, contour_color='steelblue')

wc.generate(text )

#Store to file
wc.to_file(path.join(d, 'whale.png'))

#show
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.figure()
plt.imshow(whale_picture, cmap='gray', interpolation='bilinear')
plt.axis('off')
plt.show()