from flask import Flask, request, redirect, Response, render_template
import cgi, cgitb, validators, sys, redis,  pymongo





#myclient = pymongo.MongoClient("mongodb://172.18.0.4:27017/")
#mydb = myclient["customers"]






SIGNUP = redis.Redis(host='redis', port=6379, db=0)


username = "mongo100"
password = ("mongo100")



r = SIGNUP.hget(username , 'PASSWORD')
#r1  =   SIGNUP.hget('mongo9', 'EMAIL')


p = password
p1 = "'{}'".format(p)
r1 =   str("b")+ p1
r2 = str(r)







print(r)
print(r2)
