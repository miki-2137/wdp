def choinka(h):
    gw = 1
    for i in range(h):
        print((' '*(h-i))+('*'*gw))
        gw += 2
    print(' '*h+'*')

print(choinka(5))
