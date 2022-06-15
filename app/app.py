from scraper import getDivContent

hash_old = ""
hash_new = ""

# check if hash.txt file already exists
try:
    with open("./hash.txt", "r") as f:
        hash_old = f.readline()
        
        hash_new = getDivContent()

        if hash_old == hash_new:
            print("no change")
        else:
            print("changed")

        f.write(hash_new)
        f.close()

# create if it doesnt already exist
except FileNotFoundError:
    with open("./hash.txt", "w") as f:
        f.write(getDivContent())

