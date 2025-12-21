import re, math, sys, io, json
import nltk

STOPWORDS = {"the","is","a","me","to","of","and","on","in","for","show","open"}
buffer = io.StringIO()
sys.stdout = buffer

# remove= True
def tokenize(text, remove=True):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    tokens = text.split()
    if remove:
        tokens = [t for t in tokens if t not in STOPWORDS]
    return tokens

def cosine_similarity(a,b):
    dot = sum(x*y for x,y in zip(a,b))
    ma = math.sqrt(sum(x*x for x in a))
    mb = math.sqrt(sum(x*x for x in b))
    return 0 if ma*mb==0 else dot/(ma*mb)
remove=True
sentences="""
Piyush cooks Maggi.
Piyush is making Maggi.

Piyush prepares Maggi noodles.

Piyush whips up a bowl of Maggi.

Piyush is busy cooking Maggi.

Piyush boils Maggi on the stove.

Piyush rustles up some Maggi.

Piyush is stirring Maggi in the pan.

Piyush gets the Maggi ready.

Piyush is serving freshly cooked Maggi.

Piyush makes a quick Maggi snack.
"""
S2="Piyush cooks Maggi."
sentences=sentences.split(".")
for S1 in sentences:
  S1=S1.strip()
  print(len(S1))
  if len(S1)<=1:
    continue

  t1 = tokenize(S1, remove)
  t2 = tokenize(S2, remove)

print("STEP 1: TOKENS")
print(t1)
print(t2)

vocab = sorted(set(t1)|set(t2))
A = [t1.count(w) for w in vocab]
B = [t2.count(w) for w in vocab]

print("\nSTEP 2: VOCAB")
print(vocab)

print("\nSTEP 3: VECTORS")
print("A =",A)
print("B =",B)
score = cosine_similarity(A,B)
print("\nSTEP 4: COSINE")
print(round(score,4))
score=int((10000*score))/100
print(score)
score=score/100
print(f"{S1},{S2},{score}%")
print("_DATA_"+json.dumps({"A":A,"B":B,"score":score}))
buffer.seek(0)
output = buffer.read()
sys.stdout = sys.__stdout__
print(output)