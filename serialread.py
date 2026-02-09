import serial
import numpy as np

ser = serial.Serial(
    port='COM8',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
buffers=[]
count=0
file=open('ADC_sinewace_50Hz.csv', 'a', newline ='')
try:    
    while(True):
        data = ser.readline()
        buffers.append(int(data.decode().rstrip()))
        count=count+1
        if(len(buffers)>=5000):
            #print(f"big array is :{big_array[0]}")
            # Write all at once 
            np.savetxt(file, buffers,fmt="%u")
            buffers.clear()
except KeyboardInterrupt:
    print(f"length of buffer{len(buffers)}")
    print(f"Count variable{count}")
    np.savetxt(file, buffers,fmt="%u")

ser.close()