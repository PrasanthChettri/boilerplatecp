from sys import argv

def main() : 
    with open("boilerplate.cpp" , "r") as fr , open("this.cpp" , "w") as fw:
        try : 
            fw.write(fr.read())
        except Exception as e: 
            print("Exception : {}.".format(str(e)))

if __name__ == "__main__" : 
    main()
