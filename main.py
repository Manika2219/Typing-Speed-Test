from time import *
import random as r

print(time() )

def mistake(partest, usertest):
    error =0
    for i in range(len(partest)):
        try:
            if partest[i] !=usertest[i]:
                error =error + 1
        except Exception as e:
            error=error+1
    return error


def speed_time(time_s, time_e,userinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)

test=["Hello everyone how's you guys?. I hope you all are good",
      "The moon hung low in the indigo sky, casting a gentle glow over the silent town. The streets were deserted, with only the occasional flicker of a distant streetlamp. ",
      "My name is Manika Singh", "Welcome in python world"]
test1 = r.choice(test)
print("***** typing speed ******")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter: ")
time_2=time()

print('Speed:',speed_time(time_1,time_2, testinput),"w/sec")
print("error:",mistake(test1,testinput))