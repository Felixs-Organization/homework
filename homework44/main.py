import pandas as pd
import jieba
import jieba.analyse
from wordcloud import WordCloud

# read the document
data = open('data.txt', 'r', encoding='utf-8').read()

wc = WordCloud(
    width=1000, height=1000, # set height and width to 1000px
    background_color=(200, 200, 255), # set background to a RGB color
    max_font_size=100, min_font_size=10, # set max font size to 100 and min to 10
    scale=2 # scale 2
)
wordlist = jieba.lcut_for_search(data)
print(type(wordlist))
result = str().join(wordlist)
print(result)

tag = jieba.analyse.extract_tags(sentence=result, topK=10, withWeight=True)

print(tag)
wc.generate(data)

wc.to_file('wordcloud.jpg')