inp = input()
inp = int(inp)
out = 0
zhishus = []
for zhishu in range(2, inp + 1, 1):
    for i in range(2, zhishu + 1, 1):
        if zhishu % i != 0:
            continue
        if i == zhishu:
            zhishus.append(zhishu)
        else:
            break

l = []
for j in zhishus:
    if inp % j == 0:
        out = out + 1
        l.append(j)
print(zhishus, out, l)
