a = ["jhgj",1, "jh",4,7,['вот тут что-то нужно вытащить',5]]
for x in a:
    if type(x) == list:
        for l in x:
            print(l)
    else:
        print(x)
