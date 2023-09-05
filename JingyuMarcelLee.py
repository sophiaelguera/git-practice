import threading

def terrible_threaded_loop():
    while True:
        print("very tight double CPU loop from thread {}".format(threading.currentThread().name))

def main():
    t1 = threading.Thread(target=terrible_threaded_loop)
    t2 = threading.Thread(target=terrible_threaded_loop)
    
    t1.start()
    t2.start()
    
    print("this statement will never be executed")
    
if __name__ == "__main__":
    main()