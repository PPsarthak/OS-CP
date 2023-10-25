import threading
import time
import random

# Initialize semaphores
pread = threading.Semaphore(1)
pwrite = threading.Semaphore(1)  # Changed to 1

# Shared data variables
seconds = 0
minutes = 0
hours = 0

# Reader process
def reader():
    global seconds, minutes, hours
    while True:
        pread.acquire()
        print(f"Reader: Time - {hours}:{minutes}:{seconds}")
        pread.release()
        time.sleep(1)

# Writer process
def writer():
    global seconds, minutes, hours
    while True:
        pwrite.acquire()
        seconds = random.randint(0, 59)
        minutes = random.randint(0, 59)
        hours = random.randint(0, 23)
        print(f"Writer: Updated Time - {hours}:{minutes}:{seconds}")
        pwrite.release()
        time.sleep(5)

# Create reader and writer threads
reader_thread = threading.Thread(target=reader)
writer_thread = threading.Thread(target=writer)

# Start the threads
reader_thread.start()
writer_thread.start()

# Wait for threads to finish (this program runs indefinitely)
reader_thread.join()
writer_thread.join()
