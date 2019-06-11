result = []
for i in range(1,101):
    # 除去7的倍数
    if i%7 : 
        # 除去十位7
        if i//10%10 != 7: 
        #if ((i//10)+1)%(7+1): 
            # 哪位道友能把这句改为只进行逻辑真假判断而不进行比较
            # 除去个位7
            if (i%10) != 7 : 
                result.append(i)

#list(result)
#len(result)
for i in result:
    print(i)
