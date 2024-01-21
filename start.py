from os import system
import webbrowser
import subprocess


def main():
    """
    The basis of the functionality depends on 3 different work types
    1) Study
    2) Social
    3) Code:

    Depending on the work type the program will open firefox with specific links
    and vscode only if type 3 is chosen

    Also, it can be configured as per the current workflow. For example if I am learning
    Blockchain dev, it will open a learning resource, vscode and spotify

    IMPORTANT:
    wherever i have written CMD, it stand for `Command Might Differ`
    this was built for linux, so if you're on mac or windows, etc,
    those commands might differ on your os.

    In order to use this properly, please go through the entire code and
    make changes according to your requirements.
    """

    work_type = take_input()
    browser(work_type)
    vsc(work_type)

    # Extra: This part is not applicable to all workflows, but it is configured for very specific needs.
    
    if work_type == 3:
        subprocess.run('atril Documents/Mastering\ Ethereum.pdf', shell=True)
    
    exit()

def take_input():
    
    valid_choices = [1, 2, 3]
    
    while True:
        # subprocess.run("clear") # clears the screen, CMD

        print("Welcome user! What can I help you with?\n"
              "1) Study\n"
              "2) Social\n"
              "3) Code\n")
        
        choice = int(input())
        
        if choice not in valid_choices:
            print("Choice Invalid, retry!")
            input()
            continue

            """
            Blank input creates a sort of waiting function
            so like the user will hit enter and then the entire function will restart
            """

        break
    
    return choice


def browser(work_type):
    """
    Opens the broswer with specified links,
    change the arg in .run() to your fav browser and links
    shell=True runs it as a terminal command
    """
    
    if work_type == 1:
        subprocess.run('firefox --new-tab open.spotify.com --new-tab www.youtube.com', shell=True)

    if work_type == 2:
        subprocess.run('firefox --new-tab www.discord.com/app --new-tab open.spotify.com', shell=True)

    if work_type == 3:
        subprocess.run('firefox --new-tab chat.openai.com --new-tab open.spotify.com', shell=True)

    print("Opened Firefox!")


def vsc(work_type):
    
    if work_type == 3:
        subprocess.run("code-oss", shell=True) # CMD
        # You might want to use a different directory so just, code /path/to/dir

        print("opened vsc")

    return 0

if __name__ == '__main__':
    main()
