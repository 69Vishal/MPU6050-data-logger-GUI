from tkinter import * 
import serial
import csv, time

# Checking if serial connection is available or not 
try:
    ser = serial.Serial("COM4", 115200)
    ser.timeout = 10 # change your serial port with COM4
    serial_try = True
except:
    # gives failed to connect to serial port error if serial port is not available
    serial_try = False
    print('Failed to connect to serial port')
    time.sleep(2)
    exit()


# Creates a file to save raw data from serial input
f2 = open('data_gui.csv', 'w')
writer = csv.writer(f2)
writer.writerow(['time (ms)','acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y','gyro_z','temperature']) 


# variable's
status_of_window = True
row = 1
window = True

# Functions
def close_window():
    global status_of_window
    window = False
    ser.close()
    root.destroy()

# GUI section
root = Tk()
root.title("MPU6050")
root.geometry("500x400")
root.protocol("WM_DELETE_WINDOW", close_window)

# GUI variable
serial_info = StringVar()
time_serial = StringVar()
time_serial.set('0')
acc_x_serial = StringVar()
acc_x_serial.set('0')
acc_y_serial = StringVar()
acc_y_serial.set('0')
acc_z_serial = StringVar()
acc_z_serial.set('0')
gyro_x_serial = StringVar()
gyro_x_serial.set('0')
gyro_y_serial = StringVar()
gyro_y_serial.set('0')
gyro_z_serial = StringVar()
gyro_z_serial.set('0')
temperature_serial = StringVar()
temperature_serial.set('0')

# status of serial port
serial_status = Label(root, text='Serial Status: ')     
serial_status.grid(row = 0, column = 0)
serial_status_1 = Label(root, textvariable=serial_info, fg = 'green')     
serial_status_1.grid(row = 0, column = 1)

time_1=Label(root, text='Time (ms): ')
time_1.grid(row = row, column = 0)
acc_x_1=Label(root, text='acc_x: ')
acc_x_1.grid(row = row + 1, column = 0)
acc_y_1=Label(root, text='acc_y: ')
acc_y_1.grid(row = row + 2, column = 0)
acc_z_1=Label(root, text='acc_z: ')
acc_z_1.grid(row = row + 3, column = 0)
gyro_x_1=Label(root, text='gyro_x: ')
gyro_x_1.grid(row = row + 4, column = 0)
gyro_y_1=Label(root, text='gyro_y: ')
gyro_y_1.grid(row = row + 5, column = 0)
gyro_z_1=Label(root, text='gyro_z: ')
gyro_z_1.grid(row = row + 6, column = 0)
temperature_1=Label(root, text='temperature: ')
temperature_1.grid(row = row + 7, column = 0)


time_2=Label(root, textvariable=time_serial)
time_2.grid(row = row, column = 1, padx=10, pady=10)
acc_x_2=Label(root,textvariable=acc_x_serial)
acc_x_2.grid(row = row + 1, column = 1, padx=10, pady=10)
acc_y_2=Label(root, textvariable=acc_y_serial)
acc_y_2.grid(row = row + 2, column = 1, padx=10, pady=10)
acc_z_2=Label(root, textvariable=acc_z_serial)
acc_z_2.grid(row = row + 3, column = 1, padx=10, pady=10)
gyro_x_2=Label(root, textvariable=gyro_x_serial)
gyro_x_2.grid(row = row + 4, column = 1, padx=10, pady=10)
gyro_y_2=Label(root, textvariable=gyro_y_serial)
gyro_y_2.grid(row = row + 5, column = 1, padx=10, pady=10)
gyro_z_2=Label(root, textvariable=gyro_z_serial)
gyro_z_2.grid(row = row + 6, column = 1, padx=10, pady=10)
temperature_2=Label(root, textvariable=temperature_serial)
temperature_2.grid(row = row + 7, column = 1, padx=10, pady=10)

# Logs data to CSV file and show it on python terminal
while (window):
    try:
        raw_data = str(ser.readline())
        data = raw_data[2:-5]
        print(data)
        split_data = data.split(',')
        time1 = split_data[0]
        acc_x = split_data[1]
        acc_y = split_data[2]
        acc_z = split_data[3]
        gyro_x = split_data[4][1:]
        gyro_y = split_data[5]
        gyro_z = split_data[6]
        temperature = split_data[7]
        time_serial.set(time1)
        acc_x_serial.set(acc_x)
        acc_y_serial.set(acc_y)
        acc_z_serial.set(acc_z)
        gyro_x_serial.set(gyro_x)
        gyro_y_serial.set(gyro_y)
        gyro_z_serial.set(gyro_z)
        temperature_serial.set(temperature)
        root.update()
        writer.writerow([time1,acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z, temperature]) 
        stat = True
    except:
        stat = False    

    if stat:
        serial_info.set('OK')
        serial_status_1.config(fg='green')
        root.update()
    else:
        serial_info.set('Error')
        serial_status_1.config(fg='red')
        root.update()


root.mainloop()

