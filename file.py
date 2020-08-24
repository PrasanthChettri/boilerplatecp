from sys import argv
def main() : 
    if argv[1:] :
        file_name = argv[-1]
    else :
        file_name = "this.cpp"
    with open("starting_code.txt" , "r") as fr , open("this.cpp" , "w") as fw:
        fw.write(fr.read())
if __name__ == "__main__" : 
    main()
