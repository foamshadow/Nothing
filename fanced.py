def fanc(a):
    k,s,s1=[],'',''
    for i in range(0,len(a),2):
        k.append((list(a[i:i+2])))
    for i in range(len(k)):
        s+=k[i][0]
        try :
            s1+=k[i][1]   
        except :
            pass
    return s+s1
def defanc(a):
    smaple=[]
    smaple.append(list(a[:len(a)-len(a)//2]))
    smaple.append(list(a[len(a)-len(a)//2:]))
    s,n='',0
    for i in range(len(smaple[1])+1):
        try :
            s+=smaple[0][n]
            s+=smaple[1][n]
            print(s+s1)
        except :pass
        n+=1
    return s
a=str(input('fanc_data:'))
print(fanc(a))
a=fanc(a)
print(defanc(a))
