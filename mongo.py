import pymongo

myclient = pymongo.MongoClient("mongodb://172.18.0.4:27017/")
#mydb = myclient["customers"]I
mydb1 = myclient["eMAIL"]
#print(myclient.list_database_names())

#imycol = mydb1["Emailcollection"]
#mydict = { "EMAIL": "yogeshnirwan567@gmail.com" }
#x = mycol.insert_one(mydict)
my=  "yogeshnirwan567@gmail.com"
my1 = mydb1.Emailcollection
#find_one({"Branch":"CSE"})
mydoc = my1.find_one({ "EMAIL": my })
#print (my)
#print  (str(my))
#print(mydoc)
#mydoc4 = my1.find_one({"EMAIL": my })


#print(mydoc)
#print(mydoc4)

d = None
if mydoc == d : 
 print ("no found")

else : 

 print ("found")





print({ "EMAIL": my }) 




