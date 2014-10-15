#1*2-3+4*5-6+7

n = int(input())
operator = "*"
for i in range(1,n+1):
    if i==n:
        operator = ""
    if i%2==0:
        operator = "-"
    elif i%3==0:
        operator = "+"
    elif i%4==0:
        operator = "*"
    print(str(i)+operator,end="")