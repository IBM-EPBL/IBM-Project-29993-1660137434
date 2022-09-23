import time #importing the time lib
import random   #importing the random lib
i=0 #initiating with 0
while (i<5):    #iterating only for 5 times
    i=i+1   
    time.sleep(1)   #1sec
    temp=random.randint(0,30)
    humid=random.randint(1,100)
    if temp<=15:
        print(temp,"the temperature is low")
    elif temp<=25:
        print(temp,"the temperature is ok & normal")
    else:
        print(temp,"the temperature is absolutely high")
    if humid<=50:
        print(humid,"the humidity is low")
    elif humid<=80:
        print(humid,"the humidity is ok & normal")
    else:
        print(humid,"the humidity is definitely high")
