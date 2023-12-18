def choinka(h):
    gw = 1
    for i in range(h):
        print((' '*(h-i))+('*'*gw))
        gw += 2
    print(' '*h+'*')

print(choinka(5))


def choinka(h):
    for i in range(h):
        print((' '*(h-i-1))+('*'*(2*i+1)))
    print((' '*(h-1))+'*')

print(choinka(5))
