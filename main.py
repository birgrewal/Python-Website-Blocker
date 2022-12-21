import customtkinter # importing customtkinter module
from sys import platform # importing platform from sys module

host ='C:\Windows\System32\drivers\etc\hosts'
ip = '127.0.0.1'

# Functions
def block(): # For blocking the urls
    urls = url.get('1.0', 'end')
    urlList = list(urls.split(','))
    
    # Working: Takes urls that user entered, then adds them to the hosts file by redirecting them to localhost ip

    for u in urlList:
        hostFile = open(host, 'r+')
        hosts = hostFile.read()
        hostFile.close()

        if (ip+'\t'+u) in hosts:
            print(u,' is already blocked')
        else:
            hostFile = open(host, 'w+')
            hostFile.write(hosts+'\n'+ip+'\t'+u)
            hostFile.close()

            print(u,' has been blocked!')

def unblock(): # For unblocking urls
    urls = url.get('1.0', 'end')
    urlList = list(urls.split(','))

    # Working: Takes urls that user entered, then checks if they are present in hosts file (and redirected to localhost ip), and then removes them from the file

    hostFile = open(host, 'r+')
    hosts = hostFile.read()
    hostFile.close()
    
    for u in urlList:
        u = list(u.split('\n'))[0]
        if (ip+'\t'+u) in hosts:
            hostList = list(hosts.split('\n'))
            hosts = ""
            for i in hostList:
                if (ip+'\t'+u) in i:
                    print(u,' has been Unblocked!')
                else:
                    hosts += i+'\n'

            hostFile = open(host, 'w+')
            hostFile.write(hosts)
            hostFile.close()
        else:
            print(u,' is already Unblocked')

def setHost(): # To check the system platform and editing hosts file path accordingly
    global host
    
    if platform == 'win32':
        host = 'C:\Windows\System32\drivers\etc\hosts'
    elif platform == 'linux' or platform == 'linux2':
        host = '/etc/hosts'
    elif platform == 'darwin':
        host = '/private/etc/hosts'
    else:
        print('System Not Compatible!')
        quit()
    
    print(host)

# GUI Code
root = customtkinter.CTk()
root.geometry("600x430")
root.minsize(300, 240)
root.maxsize(600, 460)
root.title("Website Blocker")

# Fonts
bg = customtkinter.CTkFont(family="Helevetica", size=35, weight = 'bold')
md = customtkinter.CTkFont(family="Helevetica", size=18)
sm = customtkinter.CTkFont(family="Helevetica", size=15)

# Heading
header = customtkinter.CTkFrame(root, fg_color="transparent")
header.pack()

h1 = customtkinter.CTkLabel(header, text="Website Blocker", font=bg)
h1.pack(pady=15)

# Main - Textbox and buttons for submission
main = customtkinter.CTkFrame(root, fg_color="transparent")
main.pack(pady=30)

inputs = customtkinter.CTkFrame(main, fg_color='transparent')
inputs.grid(row=0)
lb = customtkinter.CTkLabel(inputs, text="Website URL", font=md)
lb.grid(row=0, padx=50, pady=20)

url = customtkinter.CTkTextbox(inputs, width=300, height=8, font=sm)
url.grid(row=0, column=1)

setHost() # Calling setHost function to change hosts file path

btns = customtkinter.CTkFrame(main, fg_color='transparent')
btns.grid(row=1, pady=20)
btn = customtkinter.CTkButton(btns, text="Block", fg_color="red", width=100, height=50, font=customtkinter.CTkFont(family="Helevetica", size=16, weight='bold'), command=block)
btn.grid(row=0, column=0, pady=20, padx=30)

btn = customtkinter.CTkButton(btns, text="Unblock", fg_color="green", width=100, height=50, font=customtkinter.CTkFont(family="Helevetica", size=16, weight='bold'), command=unblock)
btn.grid(row=0, column=1, pady=20, padx=30)

root.mainloop()