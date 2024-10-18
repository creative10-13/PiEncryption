def encode(message, key):
    message = [format(ord(x), 'b') for x in message]
    ogkey = key
    while len(message) > len(key): key += ogkey
    if len(message) < len(key): key = key[:len(message)]
    key = [format(ord(x), 'b').rjust(8) for x in key]
    
    Newlist = []
    for i in range(len(message)):
        binary = ""
        print(range(len(message[i])))
        print(key[i])
        
        for foo in range(len(message[i])):
            print(foo)
            if key[i][foo] == message[i][foo]:
                binary += "1"
            else:
                binary += "0"
        Newlist.append(format(int(binary, 2), "02x"))
    
    outstring = ""
    return "".join(Newlist)

def decode(message, key):
    messagelist = []
    for i in range(0, len(message), 2): messagelist.append(format(int(message[i:i+2], 16), '08b')[1:])         
    ogkey = key
    while len(message) > len(key): key += ogkey
    if len(message) < len(key): key = key[:len(message)]
    key = [format(ord(x), 'b') for x in key]
    Newlist = []
    for i in range(len(messagelist)):
        binary = ""
        for foo in range(len(messagelist[i])):
            if key[i][foo] == messagelist[i][foo]:
                binary += "1"
            else:
                binary += "0"
        Newlist.append(chr(int(binary, 2)))
    
    outstring = ""
    return "".join(Newlist)

def v(): print("Version 3") # Version Printer
# In built encoding interface
def Run():
    v()
    print("Choose an option: 1. Encode 2. Decode")
    try:
        inp = int(input())
    except ValueError:
        print("Invalid option")
        exit()

    if inp == 1:
        print("The message can only contain letters, numbers, spaces, and periods. All letters will be lowercased")
        inmsg = input("Message to encode: ")
        inkey = input("Key to encode: ")
        print("Encoded Message: "+encode(inmsg, inkey))
    elif inp == 2:
        outmsg = input("Message to decode: ")
        outkey = input("Key to decode: ")
        print("Decoded Message: "+decode(outmsg,outkey))