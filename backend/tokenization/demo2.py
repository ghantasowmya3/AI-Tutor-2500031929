text = input("Enter a Sentence:") or "I love Learning Python"

print("length of the text:",len(text))
print("Characters in the text are:")
for ch in text:
    print(ch,end=",")
    
