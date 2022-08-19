from tcp_latency import measure_latency
import xlsxwriter
import warnings
import matplotlib
from matplotlib import pyplot as plt
import datetime as dt
import matplotlib.animation as animation

warnings.filterwarnings("ignore")

############################CREATING EXCEL FILES#################################
#Do not forget to write your PC's username on the path below
PingBook = xlsxwriter.Workbook('C:/Users/WRITEYOURPCSUSERNAMEHERE/.spyder-py3/PingData.xlsx')

sheet = PingBook.add_worksheet()

#################################################################################

#Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs = []
ys = []


#write the headers to the excel
row = 0
column = 0
sheet.write(row, column, "Real Time")
column += 1
sheet.write(row, column, "Ping (ms)")
column -= 1
row += 1

while(True):   
    try:
        
        i = 10

        #give your IP address and port number to measure the ping
        ping = measure_latency(host='192.168.188.29', port=8086, timeout=2.5)
        print(ping, "ms")
        
        #writing into an excel book
        sheet.write(row, column, dt.datetime.now().strftime('%H:%M:%S'))
        column += 1
        sheet.write(row, column, ping[0])
        column -= 1
        row += 1
        
        #drawing the graph
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        ys.append(ping[0])
        ax.clear()
        ax.plot(xs, ys)
        
    except KeyboardInterrupt:
        PingBook.close()
        break

#set the plot ranges and labels
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
ax.set_ylim(0, 150)
plt.xlabel("Real Time")
plt.ylabel("Ping (ms)")
plt.title('Ping Data')
