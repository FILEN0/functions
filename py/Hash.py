from hashlib import sha256
def convert(s:str):
    HASH = sha256()
    HASH.update(s.encode())    
    return HASH.hexdigest()
