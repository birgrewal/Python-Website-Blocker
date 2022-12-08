from tkinter import * # importing tkinter module

host ='C:\Windows\System32\drivers\etc\hosts'
ip = '127.0.0.1'

# Functions
def block():
    urls = url.get(1.0, END)
    urlList = list(urls.split(','))
    
    for u in urlList:
        hostFile = open('hosts.txt', 'r+')
        hosts = hostFile.read()
        hostFile.close()

        if (ip+'\t'+u) in hosts:
            print(u,' is already blocked')
        else:
            hostFile = open('hosts.txt', 'w+')
            hostFile.write(hosts+'\n'+ip+'\t'+u)
            hostFile.close()

            print(u,' has been blocked!')

def unblock():
    urls = url.get(1.0, END)
    urlList = list(urls.split(','))

    hostFile = open('hosts.txt', 'r+')
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

            hostFile = open('hosts.txt', 'w+')
            hostFile.write(hosts)
            hostFile.close()
        else:
            print(u,' is already Unblocked')

# GUI Code
root = Tk()
root.geometry("655x545")
root.minsize(500, 445)
root.maxsize(955, 755)
root.title("Website Blocker")

header = Frame(root)
header.pack()

h1 = Label(header, text="Website Blocker", font="Helevetica 30 bold")
h1.pack(pady=15)

main = Frame(root)
main.pack(pady=30)

lb = Label(main, text="Website URL", font="Helevetica 15 bold")
lb.grid(row=0, padx=30)

url = Text(main, width='30', height='1.5', font="Helevetica 13")
url.grid(row=0, column=1)

Button(main, text="Block", bg="red", fg="white", width=15, height=2, font="Helevetica 13 bold", command=block).grid(pady=20)
Button(main, text="Unblock", bg="green", fg="white", width=15, height=2, font="Helevetica 13 bold", command=unblock).grid(row=1, column=1, pady=20)

root.mainloop()