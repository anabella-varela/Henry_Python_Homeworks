import sys
import os
from datetime import datetime

time = datetime.now().strftime('%y/%m/%d %H:%M:%S') #datetime.now() function retrieves the current date and time. 
temp = input('Temperature in celcius: ')
hum = input('Humidity: ')
rain =input ('Did it rain today? writte True or False: ')

data_input = [time, temp, hum , rain]

file = open('clase10_ej2.csv', 'a' )

file.write('\t\t\t'.join(data_input) + '\n') #'\t'.join(data_input) joins the elements of data_input list using a tab character as the separator. The + '\n' adds a newline character at the end of each line to store the inputs in a new line.
file.close ()


