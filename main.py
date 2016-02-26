import os

def child(cmd, args):
    os.execv(cmd, args)

def main():

    while(True):
        print(">", end=" ")
        cmd = input()

        if("exit" == cmd):
            exit()
        else:

            pieces = cmd.split()

            newpid = os.fork()

            if(0 == newpid):
            
                child(pieces[0], pieces[0:])
            else:
                cpid,s = os.wait()
                print("child died :( " + str(cpid) + " status: " + str(s))


if __name__ == "__main__":
    main()
