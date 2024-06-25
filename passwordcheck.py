import redis 
import numpy as np

SIGNUP = redis.StrictRedis(host='redis', port=6379, db=0)


username = "love"




 
p = "email"
p1  = "'{}'".format(p)
r1 =   str("b")+ p1

r  =   SIGNUP.hget(username, 'EMAIL')
print(r)
r2 = str(r)
print(r2)
print(r1)

if r2 == r1 :
 print('exits')
else:
 print('not exits')




  
