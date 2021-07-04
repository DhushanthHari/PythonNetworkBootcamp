import hashlib
str = "H.Dhushanth Sendhuran"
  

result = hashlib.sha1(str.encode())
  

print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())