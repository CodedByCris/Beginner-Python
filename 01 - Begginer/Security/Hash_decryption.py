import hashlib

def hash_crack(hash, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            line = line.strip()
            if hashlib.md5(line.encode()).hexdigest() == hash:
                return line
    return "Not found"
