import threading
import time

if __name__ == "__main__":
    running_event = threading.Event()
    running_event.set()
    a = True

    def worker(num, b):
        while 1:
            running_event.wait()
            print(f"Worker {num} working...", b)
            time.sleep(num + 1)

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i, a), daemon=True)
        threads.append(t)
        t.start()

    while 1:
        input("按 Enter 鍵退出...")
        a = not a
        # if running_event.is_set():
        #     running_event.clear()
        # else: 
        #     running_event.set()
