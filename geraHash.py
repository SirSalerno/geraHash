from hashlib import sha1
import string
import random

def id_generator(size, chars=string.ascii_letters + string.digits + string.punctuation):
 return ''.join(random.choice(chars) for _ in range(size))
 
while (True):
  numero_da_sorte=random.randint(10,50)	
  s=id_generator(numero_da_sorte)
  obj = sha1(s)
  aux=obj.hexdigest()
  if (aux.endswith('0'*8)):
    break
print "Hash: " + aux + " Entrada: " + s