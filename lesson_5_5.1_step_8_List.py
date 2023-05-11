lst_in = input().split() # "1 -5.6 2 abc 0 False 22.5 hello world"

total = 0
for i in range(len(lst_in)):
    try:
        lst_in[i] = int(lst_in[i])
        total += lst_in[i]
    except:
        pass

print(total)
