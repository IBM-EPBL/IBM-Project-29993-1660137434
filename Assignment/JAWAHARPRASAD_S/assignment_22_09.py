import time 
import random   
i=0 
while (i<5):    
    i=i+1   
    time.sleep(1)   #1sec
    temp=random.randint(0,30)
    humid=random.randint(1,100)
    if temp<=15:
        print(temp,"Low Tempertature")
    elif temp<=25:
        print(temp,"Normal Temperature")
    else:
        print(temp,"High Temperature")
    if humid<=50:
        print(humid,"Low Humidity")
    elif humid<=80:
        print(humid,"Normal Humidity")
    else:
        print(humid,"High Humidity")