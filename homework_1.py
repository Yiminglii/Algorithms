def findm_maiority(list):
    a=[]
    b=0
    list_len=len(list)
    for i in range(0,list_len-1):
        a.append(0)
    for i in range(0,list_len-1):
        for j in range(0,list_len-1):
            if list[i]==list[j]:
                a[i]=a[i]+1
    for i in range(0,list_len-1):
        if a[i]>list_len/2:
            print (list[i]) 
            b=1
            break
    if b==1:
        print ("majority element is"+list[i])
    else:
        print ("there is no majority element")
    return b
list=[1,2,4,4,4,2,4,3]
findm_maiority(list)
