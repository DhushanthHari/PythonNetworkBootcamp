import hashlib

#print(hashlib.algorithms_available)

def crypt(): 

    text = "H.Dhushanth Sendhuran"
    textUtf8 = text.encode("utf-8")

    hash = hashlib.md5( textUtf8 )
    hexa = hash.hexdigest()

    print ( hexa )

    return

crypt()