corpus = {"play": [5, 5], "playing": 3, "played": 2, "plays": 1}

print("Corpus:", corpus)
print("Length of the corpus:", len(corpus))

for k, v in corpus.items():
    print(k, end=",")
    values = v if isinstance(v, (list, tuple)) else [v]
    for value in values:
        print(value, end=",")
    print()

for k, v in corpus.items():
    print(k, v)