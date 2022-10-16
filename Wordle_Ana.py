path = "/Users/User/Documents/School or Work/Coding/wordle_wordlist.txt"
file = open(path, 'r').read().split("\n")
first_half = 0
second_half = 0

for z in file:       
    if ord(z[0]) > 109:
        second_half+=1
    else :
        first_half+=1


print(first_half, second_half, first_half/len(file), second_half/len(file), 1*first_half/second_half, 1*second_half/first_half)