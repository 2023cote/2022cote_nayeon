#baekjoon 17413
s = input().rstrip()
flag = False
word = ""
answer = ""

for i in s:
    if flag == False:
        if i == "<":
            flag = True
            word += i
        elif i == " ":
            word += i
            answer += word
            word = ""
        else:
            word = i + word

    else:
        word += i
        if i == ">":
            flag = False
            answer += word
            word = ""

print(answer + word)

#################################################
string = input().rstrip()
Flag = False
word = ""
tag = ""
for s in string:
    if s == "<":
        Flag = True
        if word != "":
            word = word.split()
            for i in range(len(word)):
                for j in range(len(word[i])):
                    word = word[i].rstrip()
                    print(word[i][len(word[i]) - j - 1])
            word
    if s == ">":
        Flag = False
    if Flag == True:
        word += s
    else:
        tag += s