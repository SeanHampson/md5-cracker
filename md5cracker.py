import hashlib

def main(hashi, file_i):
        count = 0
        try:
            file = open(file_i, "r", encoding="utf8", errors="ignore")
        except:
            print("\nFile \" %s \" Not Found" % file_i)
            exit()

        for password in file:
            count += 1
                
            hashed_pass = hashlib.md5(password.encode()).hexdigest()
            status = str("Trying Password: %s" % count)
                
            print(status, end="\r")
            if hashed_pass == hashi:
                    print("\nPassword Found: %s" % password)
                    input()
                    break
        else:
            print("\nPassword Not Found!")

if __name__ == "__main__":
    md5_hash  = input("Please enter md5 hash: ")
    pass_file = input("Please add password file: ")
    main(md5_hash, pass_file)
