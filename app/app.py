from scraper import getDivContent

hash_old = ""
hash_new = ""

# check if hash.txt file already exists
try:
    with open("./hash.txt", "r") as f:
        hash_old = f.readline("./hash.txt", "r")

        f.close()

except FileNotFoundError:
    with open("./hash.txt", "w") as f:
        f.writeline(getDivContent())

