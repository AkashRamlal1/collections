def multiplyAndDisplayLists():
    lijst1 = [1,2,3,4,5,6,7,8,9,10]
    lijst2 = [2,4,6,8,10,12,14,16,18,20]
    
    for x in range(1, 11):
        x -= 1

        print(lijst1[x], "*", lijst2[x],"=", lijst1[x] * lijst2[x])
        
multiplyAndDisplayLists()