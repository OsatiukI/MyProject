import string
answer = "hdfrfg kghrjkngkr rgnmr %$%&$w wwe-.!efrv" #статика
#answer = str(input("enetr: ")) # выриант для ввода
result = ""
for item in answer:
    if item not in string.punctuation:
        result += item
words = result.split()
big_letter = ""
for word in words:
    big_letter += word.capitalize()
big_letter = "#" + big_letter
big_letter = big_letter[:140]
print(big_letter)