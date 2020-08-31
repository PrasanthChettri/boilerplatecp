#COMPILE THEM CODE
#GIT GUD AT DSA
from os import system

def main():
    if(system("g++ -std=c++11 this.cpp")):
        exit()
    print("compiled")
    system("a.exe")

if __name__ == "__main__" : 
    main()
