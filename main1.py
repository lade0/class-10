# activity 1: character occurence
some=input("enter a word")
thing=input("enter the letter you nwant to see how many times it appears")
i=0
n=0
while(i<len(some)):
    if(some[i]==thing):
        n=n+1
    i=i+1
print("the number of times the character",thing,"is repeated is",n)