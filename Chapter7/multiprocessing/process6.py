# process6.py to use Pipe to exchange data

from multiprocessing import Process, Pipe

def mysender (s_conn):
    s_conn.send({100: "Maths"})
    s_conn.send({200: "Science"})
    s_conn.send("BYE")
    s_conn.close()

def myreceiver(r_conn):
    while True:
        msg = r_conn.recv()
        if msg == "BYE":
            break
        print("Received message : ", msg)
    r_conn.close()
sender_conn, receiver_conn= Pipe()

p1 = Process(target=mysender, args=(sender_conn, ))
p2 = Process(target=myreceiver, args=(receiver_conn,))

p1.start()
p2.start()

p1.join()
p2.join()

print("Exiting the main process")
