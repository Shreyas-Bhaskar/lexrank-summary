import numpy as np
import pandas as pd
import nltk
from lexrank import STOPWORDS, LexRank
from path import Path
nltk.download('punkt') # one time execution
import re
df = pd.read_csv("news_summary_more.csv")
df.head()


from nltk.tokenize import sent_tokenize
sentences = []
for s in df['text']:
  sentences.append(sent_tokenize(s))

sentences = [y for x in sentences for y in x] 
#print(sentences[:5])

lxr = LexRank(sentences, stopwords=STOPWORDS['en'])
summary = lxr.get_summary(sentences[:10], summary_size=5, threshold=.1)
print(summary)
summary_cont = lxr.get_summary(sentences[:20], threshold=None)
print(summary_cont)

# ['The BBC understands that as chancellor, Mr Osborne, along with the Treasury '
#  'will retain responsibility for overseeing banks and financial regulation.']

# get LexRank scores for sentences
# 'fast_power_method' speeds up the calculation, but requires more RAM
scores_cont = lxr.rank_sentences(
    sentences[:20],
    threshold=None,
    fast_power_method=False,
)
print(scores_cont)
