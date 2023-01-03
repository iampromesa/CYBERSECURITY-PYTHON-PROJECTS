import psutil
import time 

update_delay = 1 

def get_size(bytes):
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

io = psutil.net_io_counters()

bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

while True:
    time.sleep(update_delay)
    io_2 = psutil.net_io_counters()
    upload_speed = io_2.bytes_sent - bytes_recv
    download_speed = io_2.bytes_recv - bytes_recv

    print(f"Upload: {get_size(io_2.bytes_sent)}   "
          f", Download: {get_size(io_2.bytes_recv)}   "
          f", Upload Speed: {get_size(upload_speed / update_delay)}/s   "
          f", Download Speed: {get_size(download_speed / update_delay)}/s      ", end="\r")
    # update the bytes_sent and bytes_recv for next iteration
    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv