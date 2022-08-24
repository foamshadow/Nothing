#注释：
#a=原数
#s=原文
#s1,s2=凯撒改字符
#j1=一层加密个数
#j2=二层机密偏移量
#m=序改数
#m1,m2=19改数/字符
#l=混合步长
#d,i,b_1,b_2=既定变量
#q=自定19改

#输入区
a=list(input("输入9位数字："))  #数字
s=list(input("输入字母："))     #英文
if a == [] and s == [] :       #无原文则结束
    print("无效指令")
    import sys
    sys.e/xit()
j1=input("二层加密个数：")      #加密个数
j2=input("三层加密个数：")      #加密个数

print('\n')
#一层加密-数字序数
if a !=[] :                    #有数字
    m=[a[int(a[i])-1] for i in range(len(a))]
    print("一层加密结果:%s"%"".join(m))
    #二层加密-19改
    #定义19改
    q={'0': '_', '1': '%', '2': '~', '3': '$', '4': '^', '5': '#', '6': '|', '7': '!', '8': '<', '9': '>', '10': '=', '11': '-', '12': '.', '13': '&', '14': '@', '15': '：', '16': '+', '17': '/', '18': '\\', '19': '?'}
    print(j1)
    if j1!='' :
        j1=int(j1)
        if j1 > 9 :
            j1=4
    else:
        j1=4
    j=m[:j1]
    m1=list(m)
    for i in j:
        m1[int(i)-1]=q[str(m[int(i)-1])]
    print("二层加密结果：%s"%"".join(m1))
else :
    pass
#三层加密-凯撒 
if s != [] :                   #有英文
    if j2 == "" :              #没有赋值则为 5
        j2=5
    else :
        j2=int(j2)
    import string
    def kaisa(s, j2):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        before = string.ascii_letters
        after = lower[j2:] + lower[:j2] + upper[j2:] + upper[:j2]
        table = ''.maketrans(before, after)
        return s.translate(table) 
    s1=kaisa("".join(s),j2)
    print("三层加密结果：%s"%s1)
else :
    pass
#四层加密-混合
if a != [] and s != [] :       #有原文
    s2=list(s1)
    m2=list(m1)
    b_1=0
    b_2=0
    if len(s)>len(m):
        l=len(s)//len(m)
        while b_1<len(m) :
            s2[int(l+b_2):int(l+b_2)]=m2[0+b_1:1+b_1]
            b_1 +=1
            b_2 +=1+l
        print("四层加密结果:%s"%"".join(s2))
    elif len(s)<len(m):
        l=len(m)//len(s)
        while b_1<len(s):
            m2[int(l+b_2):int(l+b_2)]=s1[0+b_1:1+b_1]
            b_1 +=1
            b_2 +=1+l
        print("四层加密结果:%s"%"".join(m1))
    else :
        l=1
        while b_1<len(s):
            s2[int(l+b_2):int(l+b_2)]=m2[int(0+b_1):int(1+b_1)]
            b_1 +=1
            b_2 +=1+l
        print("四层加密结果:%s"%"".join(s2))
else :
    pass
input()
