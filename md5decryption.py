import pyfiglet    
import sys                              
import hashlib

def disp():
    print("\n"+"*"*70) 
    print(pyfiglet.figlet_format("          Shacks-Md5"))
    print("*\t\t\t Steve_Shacker\t")
    print("*\t\t    ojsteve01@gmail.com\t")
    print("*\t      https://github.com/Shacker01")
    print("*"*70)
    print("\nDecrypt MD5 Hashes with wordlist")
    print("\n"+"-"*50)
    args()

def usage():
    print("\nplease specify md5hash and wordlist correctly!")
    print("\nUSAGE:")
    print("\tpython crackmd5hash.py md5hash wordlistpath")
    print("EXAMPLE\n\tPython crackmd5hash.py d69403e2673e611d4cbd3fad6fd1788e /home/worldist.txt\n")
    print("\tPython crackmd5hash.py d69403e2673e611d4cbd3fad6fd1788e S:\\myfiles\welcome.txt\n")
    sys.exit(0)

def args():
    try:
        n = len(sys.argv)
        if n < 1:
            usage()
        elif n > 2:
            work(sys.argv[1], sys.argv[2])
        else:
            usage()
    except KeyboardInterrupt:
        print("\nKeyboard interrupted. \nExiting...")
        sys.exit(0)

def work(phash, wlist):
    f = False
    try:
        passfile = open (wlist, "r")
    except:
        print("Wordlist Not Found !!")
        usage()
        sys.exit(0) 
    print("working....")
    for word in passfile:
        enc_wrd = word.encode('utf-8')
        digest  = hashlib.md5(enc_wrd.strip()).hexdigest()
        if digest == phash:
            print(f"\nFound A Match for '{digest}'")
            print("The Plaintext Is: " +word)
            f = True
            break
    if f == False:
        print("\nPlaintext Not Found In Wordlist,\nTry A Different List\n")
    
if __name__ == "__main__":
    disp()