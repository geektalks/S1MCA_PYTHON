n=int(input("Enter the number of elements in the list: "))
words=[]
max=0
for i in range(n):
    words.append(input("Enter the word: "))
    if len(words[i])>max:
        max=len(words[i])
        word=words[i]
print("Longest word is",word,"with length",max)
        
