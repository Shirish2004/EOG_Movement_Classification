import serial
arduino_data=serial.Serial('COM7',115200)
list1=[]#to store arduino values
list3=[]#to store cleansed arduino value
list4=[]  #to use this list when we have to append a specific state
while 1==1:
    while(arduino_data.inWaiting()==0):
        pass
    print("Type 1 for eye blink, 0 for eye open, 3 for up, and 4 for down after typing perform the action ")#storing the labels
    arduino_data.flushInput()
    target=float(input("Enter the target label  :"))
    arduino_signal = arduino_data.readline().decode('utf-8')#reading arduino data after mentioning the action 
    list1.append(arduino_signal)
    list4.append(target)
    print(list1)
    print(list4)
    if len(list1)>20000:
        break
for i in range(0,len(list1)):
    try:
        num,_=list1[i].split("\r")#splitting arduino data into float and strings
        list3.append(float(num))
    except ValueError:
            pass
    

 
import pandas as pd 
#Creating dataframes
df1=pd.DataFrame(list3,columns=['potential_difference'])
df2=pd.DataFrame(list4,columns=['Target'])
df3=pd.concat([df1,df2],axis=1)
print(df3)
df3.info()
df3.to_csv("name_state.csv")