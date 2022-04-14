def papershatrangi():
    n = int(input(" Enter Number Row: \n"))
    m = int(input(" Enter Number Col: \n"))

    for i in range (n):
        if i % 2 == 0:
            for j in range (m):
                if j %2 ==0:
                    print (" ",end = " ⬜")
                else:
                    print (" ",end = "⬛ ")
            print ("\n")
            
        else:
            for j in range (m):
                if j %2 ==0:
                    print (" ",end = "⬛ ")
                else:
                    print (" ",end = "⬜")
            print ("\n")
        
papershatrangi ()