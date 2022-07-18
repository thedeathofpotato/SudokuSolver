from colorama import Fore, Back, Style

def printField(values:list[list]):
    for i in range(9):
        if(i%3==0):
            print(Back.BLUE, end="")
        print(Fore.BLUE +"-"*37, end="")
        print(Back.RESET)
        for j in range(9):
            if(j%3==0):
                print(Back.BLUE, end="")
            print("|"+Back.RESET, end="")
            print(" "+Fore.WHITE+values[i][j]+" "+Fore.BLUE, end="")
           
        print(Back.BLUE+"|"+Back.RESET)

    print(Back.BLUE+"-"*37+Back.RESET)
        