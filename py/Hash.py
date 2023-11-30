from hashlib import sha256
def toHASH(s:str):
    HASH = sha256()
    HASH.update(s.encode())    
    return HASH.hexdigest()
