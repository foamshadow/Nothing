import string
def kaisa(s, k): #定义函数 接受一个字符串s 和 一个偏移量k
 
    lower = string.ascii_lowercase #小写字母
 
    upper = string.ascii_uppercase #大写字母
 
    before = string.ascii_letters #无偏移的字母顺序 小写+大写
 
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]#偏移后的字母顺序 还是小写+大写
    #分别把小写字母和大写字母偏移后再加到一起 
 
    table = ''.maketrans(before, after)  #创建映射表
 
    return s.translate(table) #对s进行偏移 即加密
 
s = input('请输入一个字符串：')
 
k = int(input('请输入一个整数密钥：'))
 
l=kaisa(s, k)
print(l)
