tokens = ["I", "love", "Learning", "Python"]

print("Tokens:", tokens)
print("Length of the tokens:", len(tokens))
print("First Token:", tokens[0])
print("Last Token:", tokens[-1])
print("Last Token:", tokens[len(tokens)-1])

print("First two tokens:", tokens[0:2])
print("Tokens in reverse order:", tokens[::-1])
print("Last two tokens:", tokens[-2:])
for token in tokens:
    print(token, end=",")