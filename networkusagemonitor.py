from tkinter import *

import psutil
import time 

update_delay = 1

def get_size(bytes):
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

#creating a window
window = Tk()

#window size
window.geometry("400x400+400+400")

#window title
window.title("Network Usage Scanner")

#window resize
window.resizable(height=False, width=False)

#colours for windows
secondary = "081f4d"
primary = "#0083ff"
white = "#ffffff"

label_bytes_sent_header = Label(text="Bytes Sent:", font="Poppins 10 bold")
label_bytes_recv_header = Label(text="Bytes Recv:", font="Poppins 10 bold")
label_upload_speed_header = Label(text="Upload Speed:", font="Poppins 10 bold")
label_download_speed_header = Label(text="Download Speed:", font="Poppins 10 bold")

#attribution 
attribution = Label(text="\n...Promesa...", font="Poppins 10 italic")

io = psutil.net_io_counters()

bytes_sent = io.bytes_sent
bytes_recv = io.bytes_recv

while True:
    time.sleep(update_delay)
    io_2 = psutil.net_io_counters()
    upload_speed = io_2.bytes_sent - bytes_recv
    download_speed = io_2.bytes_recv - bytes_recv

    label_bytes_sent = f"{get_size(io_2.bytes_sent)}"
    label_bytes_recv = f"{get_size(io_2.bytes_recv)}"

    label_upload_speed = f"{get_size(upload_speed / update_delay)}/s"
    label_download_speed = f"{get_size(download_speed / update_delay)}/s\n"

    # update the bytes_sent and bytes_recv for next iteration
    bytes_sent = io_2.bytes_sent
    bytes_recv = io_2.bytes_recv

    window.after(update_delay)
      
    window.after(update_delay)
    window.mainloop()