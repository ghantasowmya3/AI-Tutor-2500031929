#Word Level Tokenization
text=input("Enter a Sentence:") or "I love Learning Python"
print("Text:",text)
tokens = text.split()
print("Length of Tokens:",len(tokens))
print("Tokens:", tokens)