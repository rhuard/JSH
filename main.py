import os
import JSH

def main():

    jsh = JSH.JSH()

    while(True):
        print(">", end=" ")
        cmd = input()

        if("exit" == cmd):
            exit()
        else:
            jsh.Process(cmd)


if __name__ == "__main__":
    main()
