import hashlib

md5_hash  = input("Please enter md5 hash: ")
pass_file = input("Please add password file: ")

counter = 0

try:
        file = open(pass_file, "r", encoding="utf8", errors="ignore")
except:
        print("\nFile \" %s \" Not Found" % pass_file)
        exit()

for password in file:

        counter += 1
        hashed_pass = hashlib.md5(password.encode()).hexdigest()
        print("Trying Password: %s" % counter, end="\r")

        if hashed_pass == md5_hash:
                print("\nPassword Found: %s" % password)
                input()
                break
else:
        print("\nPassword Not Found!")
