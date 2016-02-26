import os

def child(cmd, args):
    os.execv(cmd, args)

def main():

    print(">", end=" ")
    cmd = input()
    pieces = cmd.split()

    newpid = os.fork()

    if(0 == newpid):
        
        child(pieces[0], pieces[0:])
    else:
        cpid,s = os.wait()
        print("child died :( " + str(cpid) + " status: " + str(s))


if __name__ == "__main__":
    main()
