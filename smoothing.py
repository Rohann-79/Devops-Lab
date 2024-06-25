import numpy as np
from collections import defaultdict
import pandas as pd
bgc={'eos':{'eos':0,'I':300,'booked':0,'a':0,'flight':0,'took':300},
    'I':{'eos':0,'I':0,'booked':300,'a':0,'flight':0,'took':0},
'booked':{'eos':0,'I':0,'booked':0,'a':300,'flight':0,'took':0},
'a':{'eos':0,'I':0,'booked':0,'a':0,'flight':600,'took':0},
'flight':{'eos':0,'I':0,'booked':0,'a':300,'flight':0,'took':0}
}
vocab=list(bgc.keys())
vsize=len(vocab)
alpha=1
bgp=defaultdict(lambda:defaultdict(float))
for w1 in vocab:
  tc=sum(bgc[w1].values())
  for w2 in vocab:
    c=bgc[w1][w2]
    bgp[w1][w2]=(c+alpha)/(tc+alpha)
bgpm=np.zeros((vsize,vsize))
wti={word: i for i, word in enumerate(vocab)} 
for w1 in vocab:
  for w2 in vocab:
    bgpm[wti[w1],wti[w2]]=bgp[w1][w2] 
print("Before smoothing")
df1=pd.DataFrame(bgc,index=vocab,columns=vocab)
print(df1)
print("/n")
print("After smoothing")
df=pd.DataFrame(bgpm,index=vocab,columns=vocab)
print(df)
print("/n")
