import customtkinter # importing customtkinter module
import tkinter as tk # importing tkinter module

host ='C:\Windows\System32\drivers\etc\hosts'
ip = '127.0.0.1'

# Functions
def block():
    urls = url.get('1.0', 'end')
    urlList = list(urls.split(','))
    
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

def unblock():
    urls = url.get('1.0', 'end')
    urlList = list(urls.split(','))

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

def setHost():
    global host
    
    val = radio_var.get()

    if val == 1:
        host = 'C:\Windows\System32\drivers\etc\hosts'
    else:
        host = '/etc/hosts'

# GUI Code
root = customtkinter.CTk()
root.geometry("600x430")
root.minsize(300, 240)
root.maxsize(600, 460)
root.title("Website Blocker")

header = customtkinter.CTkFrame(root, fg_color="transparent")
header.pack()

h1 = customtkinter.CTkLabel(header, text="Website Blocker", font=customtkinter.CTkFont(family="Helevetica", size=35, weight = 'bold'))
h1.pack(pady=15)

main = customtkinter.CTkFrame(root, fg_color="transparent")
main.pack(pady=30)


inputs = customtkinter.CTkFrame(main, fg_color='transparent')
inputs.grid(row=0)
lb = customtkinter.CTkLabel(inputs, text="Website URL", font=customtkinter.CTkFont(family="Helevetica", size=18))
lb.grid(row=0, padx=50, pady=20)

url = customtkinter.CTkTextbox(inputs, width=300, height=5, font=customtkinter.CTkFont(family="Helevetica", size=15))
url.grid(row=0, column=1)

lb = customtkinter.CTkLabel(inputs, text="Choose OS", font=customtkinter.CTkFont(family="Helevetica", size=18))
lb.grid(row=1, column=0, padx=15, pady=20)

radio_var = tk.IntVar()
radiobutton_1 = customtkinter.CTkRadioButton(master=inputs, text="Windows",
                                             command=setHost, variable= radio_var, value=1)
radiobutton_2 = customtkinter.CTkRadioButton(master=inputs, text="Linux",
                                             command=setHost, variable= radio_var, value=2)
radiobutton_1.grid(row = 1, column=1, pady=10)
radiobutton_2.grid(row = 2, column=1, pady=10)
radiobutton_1.select()


btns = customtkinter.CTkFrame(main, fg_color='transparent')
btns.grid(row=1, pady=20)
btn = customtkinter.CTkButton(btns, text="Block", fg_color="red", width=100, height=45, font=customtkinter.CTkFont(family="Helevetica", size=16, weight='bold'), command=block)
btn.grid(row=0, column=0, pady=20, padx=30)

btn = customtkinter.CTkButton(btns, text="Unblock", fg_color="green", width=100, height=45, font=customtkinter.CTkFont(family="Helevetica", size=16, weight='bold'), command=unblock)
btn.grid(row=0, column=1, pady=20, padx=30)

root.mainloop()