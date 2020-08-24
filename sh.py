from os import system
def show() :
    system("a.exe")
    with open('output.txt' , 'r') as f:
        print(f.read())
if __name__ == "__main__" : 
    show()
