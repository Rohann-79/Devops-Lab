import nltk
import matplotlib.pyplot as plt
nltk.download('punkt')
from nltk.probability import FreqDist
text="NLTK is leading platform for python"
to=nltk.word_tokenize(text)
fdist=FreqDist(to)
tc=fdist.N()
fc=fdist.B()
tl=len(text)
print("Tokens are:",to)
print("Total count:",tc)
print("Frequency count:",fc)
print("Orginal text length:",tl)
fdist.plot()
