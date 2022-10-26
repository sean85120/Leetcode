# 给定一个经过压缩的字符串，对它进行解压。
# 压缩规则为: k[str]，表示方括号内的str正好重复k次。此外str本身只包含字母。

# 样例：
# 输入"3[a]2[bc]"，解压结果为"aaabcbc"。

# 输入"3[a2[c]]"，解压结果为"accaccacc"。

# 输入"abc3[cd]xyz”，解压结果为"abccdcdcdxyz"

def contract(strs):
    stores = []

    for i in range(len(strs)):
        if strs[i] == "[":
            stores.append(i)
        if strs[i] == "]":
            stores.append(i)

    mid = round(len(stores)/2) -1

    midcol = stores[mid]
    midend = stores[mid+1]
    multi = strs[midcol-1]
    result = int(multi) * strs[midcol:midend+1]
    strs[midcol-1:midend+1] = []
    strs[midcol-1:midend+1] = result
    if stores != []:
        return contract(strs)

contract("3[a2[c]]")