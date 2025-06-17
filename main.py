import os
import pty
import sys
import select

# ANSI color codes
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def spawn_shell():
    pid, fd = pty.fork() # <- this divides process in child and parent process
    #fd is a file descriptor It represents the pseudo-terminal master connected to the child process (which runs the shell like bash)

    if pid == 0:# this is child process and pid != 0 is parent process.
        # Child: replace with bash shell <- fake bash shell
        
        os.execvp("bash", ["bash"])
    else:
        try:
            os.write(sys.stdout.fileno(), f"{GREEN}Welcome to ColTerm! Type 'exit' to quit.{RESET}\n".encode()) #sys.stdout.fileno() -> integer file descriptor that points to where your program writes output — usually your terminal screen.
            #`str.encode()` converts a string into bytes.

            while True:
                os.write(sys.stdout.fileno(), f"{BLUE}>>> {RESET}".encode())

                rlist, _, _ = select.select([sys.stdin, fd], [], [])
#This line says "If the bash shell sent some output, let's read it."
#Wait until either the user types something or the shell sends output. 
#rlist, _, _ = ... We only care about the readable list We don’t care about the writable and error lists In Python, _ is a convention meaning: "I’m receiving this value, but I don’t care about it."

                if sys.stdin in rlist:
                    user_input = os.read(sys.stdin.fileno(), 1024)
                    if user_input.strip() == b"exit":
                        break
                    os.write(fd, user_input)
                    #checks if user wrote "exit" and then it ends session.

                if fd in rlist:
                    output = os.read(fd, 1024) #- Reads **up to 1024 bytes** of output from the shell.
                    os.write(sys.stdout.fileno(), f"{YELLOW}".encode() + output + f"{RESET}".encode())

        except KeyboardInterrupt:
            pass #- If user presses `Ctrl + C` (KeyboardInterrupt), just **ignore it**.#- Prevents crashing or showing traceback.
    
        finally:
            print(f"\n{RED}Session ended.{RESET}")

if __name__ == "__main__": #boilerplate
    spawn_shell()


#encode after colors is necessary - because the colours wont work without encode()
