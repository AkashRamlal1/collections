def divideAndDisplayLists():
    lijst1 = [1,2,3,4,5,6,7,8,9,10]
    lijst2 = [2,4,6,8,10,12,14,16,18,20]
    
    for x in range(1, 11): #in de range zullen alle 10 getallen uit de ijst gebruikt
        x -= 1

        print(lijst2[x], "/", lijst1[x],"=", lijst2[x] / lijst1[x])     
       
divideAndDisplayLists()