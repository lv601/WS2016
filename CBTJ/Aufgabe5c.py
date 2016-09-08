

def codeprinter (mainstring,window):

    for i in range(0,len(mainstring)-(window-1)):
        substring = mainstring [i:i+window]
        print (substring)



rawdata= input ('input string:')
wlength = input ('windowlength: ')

codeprinter (rawdata,int(wlength))