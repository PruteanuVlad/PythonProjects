import _thread
import msvcrt


def prime(n):
    if n==2:
        return 1
    if n%2==0:
        return 0
    for i in range(3,n-1,2):
        if n%i==0:
            return 0
    return 1


def input_thread(a_list):
    msvcrt.getche()
    a_list.append(True)


def do_stuff():
    a_list = []
    _thread.start_new_thread(input_thread, (a_list,))
    n=2
    while not a_list:
        if prime(n):
            print(n,end=' ')
        n=n+1

print("The program will display the prime numbers. Press any key to exit")
do_stuff()