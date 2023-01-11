#baekjoon 12933
string = input()
quack = ['q', 'u', 'a', 'c', 'k']

duck = []
wrong = False
if len(string) % 5 != 0 or string[-1] != 'k':
    print(-1)
    exit(0)
for i in range(len(string)):
    tmp = ''
    wrong = True
    if string[i] == 'q' :
        for j in range(len(duck)):
            if duck[j][-1] == 'k':
                duck[j].append(string[i])
                wrong = False
                break
        if wrong == True:
            duck.append(['q'])
            wrong = False
    else:
        for k in range(1, 5):
            if quack[k] == string[i]:
                tmp = quack[k - 1]
                break
        for j in range(len(duck)):
            if duck[j][-1] == tmp:
                duck[j].append(string[i])
                wrong = False
                break
        if wrong == True:
            print(-1)
            exit(0)

print(len(duck))