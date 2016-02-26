#! /usr/bin/python3

import os
import JSH

def main():

    jsh = JSH.JSH()

    while(True):
        jsh.prompt.PrintPrompt()
        cmd = input()

        if("exit" == cmd):
            exit()
        elif("" == cmd):
            pass
        elif(cmd.isspace()):
            pass
        else:
            jsh.Process(cmd)


if __name__ == "__main__":
    main()
