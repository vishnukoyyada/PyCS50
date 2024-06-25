def fun(ul:int) -> list[int]:
    a,b,c=0,1,0
    list =[]
    while(c<n):
        list.append(a)
        print(a,end =",")
        a,b = b,a+b
        c+=1
    return list

if __name__ == "__main__":
    n= int(input())
    fun(n)

