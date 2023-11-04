def make_ruler(n):
    try:
        if(n<0):
            raise ValueError
        temp=[]

        for i in range(n):
            temp.append("|")
            temp.append("....")
            if i==n-1:
                temp.append("|")

        blankNumber=4


        temp.append("\n")
        for i in range(n+1):
            
            temp.append(str(i))
            if (i+1)%10==0 and (i)%9==0:
            
                blankNumber=blankNumber-1
            spaceList = []
            
            for i in range(blankNumber):
                spaceList.append(" ")
            if i!=n:
                if(blankNumber!=0):
                    tempBlank="".join(spaceList)
                    temp.append(tempBlank)
                    
        
        measuringTape="".join(temp)
        
        return measuringTape
    except ValueError:
        print("Zle dane,Spróbuj ponownie.")
        
        
        
print(make_ruler(12))