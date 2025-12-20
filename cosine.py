import re
import math
from collections import Counter

# ---------- Tokenizer ----------
def tokenize(text: str):
    """
    Token = cleaned word
    Keeps English letters, numbers, and Devanagari
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\u0900-\u097F]", " ", text)
    return [t for t in text.split() if t]

# ---------- Vocabulary ----------
def make_vocab(tokens1, tokens2):
    return sorted(set(tokens1) | set(tokens2))

# ---------- Vectorization ----------
def vectorize(tokens, vocab):
    counts = Counter(tokens)
    return [counts[w] for w in vocab]

# ---------- Math helpers ----------
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def magnitude(v):
    return math.sqrt(sum(x * x for x in v))

def cosine_similarity(a, b):
    denom = magnitude(a) * magnitude(b)
    return 0.0 if denom == 0 else dot(a, b) / denom


# ---------- Input ----------
S1 = """मैं ठीक हूँ
मैं ठीक नहीं हूँ
मैं खुश हूँ
मैं खुश नहीं हूँ
मैं दयालु हूँ
मैं दयालु नहीं हूँ
मैं ठीक हूँ
मैं ठीक नहीं हूँ"""

S2 = "मैं दयालु नहीं हूँ"


# ---------- Sentence-level comparison ----------
sentences = S1.strip().split("\n")
target_tokens = tokenize(S2)

print("TARGET SENTENCE:", S2)
print("-" * 50)

for i, sent in enumerate(sentences, 1):
    tokens1 = tokenize(sent)
    vocab = make_vocab(tokens1, target_tokens)

    A = vectorize(tokens1, vocab)
    B = vectorize(target_tokens, vocab)

    score = cosine_similarity(A, B)

    label = (
        "✅ Very similar" if score > 0.8 else
        "🙂 Moderately similar" if score > 0.5 else
        "😕 Not similar"
    )

    print(f"Sentence {i}: {sent}")
    print(f"  Cosine Similarity = {score:.4f}  {label}")
    print()