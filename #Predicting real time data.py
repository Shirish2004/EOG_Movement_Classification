#Predicting real time data 
import serial 
import time 
import numpy as np 

#loading the model 
import pickle 
model_path="D:/data_D/Summer_Intern_Bhopal/rf_model_pkl"
with open(model_path,'rb') as f:
    model=pickle.load(f)
value=[]
prediction=[] 


arduino = serial.Serial(port='COM8', baudrate=115200,timeout=0.1)
arduino_data=serial.Serial('COM7',115200)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(1)
    data = arduino.readline()
    return data
time.sleep(5)
while True:
    while(arduino_data.inWaiting()==0):
       pass
    arduino_data.flushInput()
    arduino_signal = arduino_data.readline().decode('utf-8')
    try:
        num1,_=arduino_signal.split("\r")
        # time.sleep(1)
        print(num1)
        value.append(num1)
    except ValueError:
        pass
    # time.sleep(1)
    print(value)
    try:
        y_pred=model.predict(np.array(value).reshape(-1,1))
        prediction.append(y_pred)
        print(prediction)
        num2 =str(int(prediction[0]))
        v=arduino.write(bytes(num2,'utf-8'))
        # time.sleep(1)
        print(v)
        value.clear()
        prediction.clear()
    except ValueError:
        pass


