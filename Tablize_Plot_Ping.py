from tcp_latency import measure_latency
import xlsxwriter
import warnings
import matplotlib
from matplotlib import pyplot as plt
import datetime as dt
import matplotlib.animation as animation

warnings.filterwarnings("ignore")

############################CREATING EXCEL FILES#################################
PingBook = xlsxwriter.Workbook('C:/Users/BarisZorba/.spyder-py3/PingData.xlsx')

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

        #measure the ping
        #ping = measure_latency(host='81.95.107.155', port=50061, timeout=2.5)
        ping = measure_latency(host='8.8.8.8', timeout=2.5)
        print(ping, "ms")
        
        #write into excel
        sheet.write(row, column, dt.datetime.now().strftime('%H:%M:%S'))
        column += 1
        sheet.write(row, column, ping[0])
        column -= 1
        row += 1
        
        #draw graph
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
