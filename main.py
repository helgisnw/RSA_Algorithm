def decrypt(encrypted_string, n, e, d):
  decrypted_string = ""
  encrypted_string = str(encrypted_string)
  for c in encrypted_string:
    decrypted_string += chr(pow(ord(c), d, n))
  return decrypted_string
def modular_inverse(e, tot):
  for i in range(tot):
    if (i * e) % tot == 1:
      return i
  return -1

message = 89 
p1 = 53
p2 = 59
n = p1 * p2
e = 3
tot = (p1 - 1) * (p2 - 1)
d = modular_inverse(e, tot)

encrypted = (message ** e) % n
print(encrypted)

decrypted = decrypt(encrypted, n, e, d)

print (decrypted)
