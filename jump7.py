i=0
while i < 100:
    i+=1
    if i==3 or i%3==0 or i//10==3 or i%10==3:
        continue
    else:
        print(i)
