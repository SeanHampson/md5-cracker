import hashlib

md5_hash  = input("Please enter md5 hash: ")
pass_file = input("Please add password file: ")

counter = 0

try:
	file = open(pass_file, "r", encoding="utf8")
except:
	print("\nFile \" %s \" Not Found" % pass_file)
	exit()

for password in file:
	
	counter += 1
	hashed_pass = hashlib.md5(password.encode()).hexdigest()
	print("\rTrying Password #{0}: {1}".format(counter, password), end="")
	
	if hashed_pass == md5_hash:
		print("\nPassword Found: %s" % password)
		input()
		break

else:
	print("\nPassword Not Found!")
