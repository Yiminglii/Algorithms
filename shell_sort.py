def shell_sort(slist):
    gap = len(slist)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(slist)):
            for j in range(i % gap, i, gap):
                if slist[i] < slist[j]:
                    slist[i], slist[j] = slist[j], slist[i]
    return slist

a=[1,2,4,3,5,6,7,0,1]
a=shell_sort(a)
print (a)
