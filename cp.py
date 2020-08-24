from sys import argv
from os import system
from sh import show

def main():
    a = argv[1:]
    if len(a)  == 1  : 
        f = a[0] 
    else : 
        f = "this.cpp"
    if(system("g++ -std=c++11 {}".format(f))):
        exit()
    print("compiled")
    show()

if __name__ == "__main__" : 
    main()
