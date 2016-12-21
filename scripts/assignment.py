# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:31:59 2016

@author: Milind Kabariya
"""
#class creating key value object
class keyValue:
    def __init__(self,key,value):
        self.key = key
        self.value = value
            
#hash function for caluclate the hash value for URLS
def hashFunction(key):
    i=0
    hashVal = 7
    while(i<len(key)):
        hashVal = (hashVal*3 + ord(key[i]))%10000000;
        i+=1
    return hashVal 

#class for second level hashing
class innerHashMap:
    def __init__(self,maximumVersions):
        self.hashList =[None]*int(maximumVersions)
        self.maximumVersions = int(maximumVersions)
    def innerHashMapAddValue(self,keyValObj):
        if len(self.hashList)<self.maximumVersions:
            self.hashList.append(keyValObj)
        else:
            self.hashList.pop(0)
            self.hashList.append(keyValObj)
    
#class for primary(first level) hashing      
class externalHashMap:
    #When the externalHashMap object create it will create one list and initialize the number of version requires per key
    #1.exthashmapList: to store the pointers of the innerhash
    #2.maximumVersions: Specify maximum versions
    def __init__(self,maximumVersions):
        self.exthashmapList = [None]*10000000
        self.maximumVersions = int(maximumVersions)
    
    #function to add the data in hash map
    def ADD(self,key,value):
        hashkey = hashFunction(key)
        j=1
        while True:
            if self.exthashmapList[hashkey] == None:
                innerHash = innerHashMap(self.maximumVersions)
                keyValueObj = keyValue(key,value)
                innerHash.innerHashMapAddValue(keyValueObj)
                self.exthashmapList[hashkey] = innerHash
                break
            else:
                innerHash = self.exthashmapList[hashkey]
                keyobj = innerHash.hashList[self.maximumVersions-1]
                keyValueObj = keyValue(key,value)
                if keyobj.key == key:
                    innerHash.innerHashMapAddValue(keyValueObj)
                    self.exthashmapList[hashkey] = innerHash
                    break
                else:
                    hashkey = hashkey+1
                    if hashkey >10000000:
                        hashkey=0
            j+=1
    # function for getting data from key value store       
    def get(self,key,version=0):
        hashkey = hashFunction(key)
        j=1
        while True:
            innerHash = self.exthashmapList[hashkey]
            if innerHash!=None and innerHash.hashList[self.maximumVersions-1-version] != None:
                keyobj = innerHash.hashList[self.maximumVersions-1-version]
                if keyobj.key == key:
                    value = keyobj.value
                    break
                else:
                    hashkey = hashkey+1
                    if hashkey >10000000:
                        hashkey=0
            else:
                value = "No value exist for given key and version"
                break
            j+=1
        return value
    
    #function for delete the data from key value data store
    def Delete(self,key):
        hashkey = hashFunction(key)
        j=1
        while True:
            innerHash = self.exthashmapList[hashkey]
            if innerHash.hashList[self.maximumVersions-1] != None:
                keyobj = innerHash.hashList[self.maximumVersions-1]
                if keyobj.key == key:
                    self.exthashmapList[hashkey]=None
                    break
                else:
                    hashkey = hashkey+1
                    if hashkey >10000000:
                        hashkey=0
            else:
                print "No key exist"
                break
            j+=1
    
    def readLine(self,yday):
        while True :
            line = yday.readline()
            #print line
            yield line
            
            
if __name__ == "__main__":     
    maximumVersions = raw_input("Please enter number of versions:\n")
    if maximumVersions =="":
       maximumVersions=3 
    
    exthash = externalHashMap(maximumVersions)
    with open("../input/Add_file.txt") as today: #please mention file path of file which contain key,value pair and needed to add into data store
            line = exthash.readLine(today)
            while True :
                yieldedStr = next(line).strip()
                if ("" == yieldedStr):
                    break
                listkeyvalue=yieldedStr.split(",")
                exthash.ADD(listkeyvalue[0],listkeyvalue[1])
                
                
    with open("../input/get_file.txt") as today: #please mention file path of file which contain key,version for which data need to extracted from data store
            line = exthash.readLine(today)
            with open("../output/get_outut_file.txt","wb") as op_get:
                while True :
                    yieldedStr = next(line).strip()
                    if ("" == yieldedStr):
                        break
                    listkeyvalue=yieldedStr.split(",")
                    if len(listkeyvalue)==1:
                        get_value = exthash.get(listkeyvalue[0])
                        op_get.write("key:"+listkeyvalue[0]+"\tversion:"+str(0)+"\tvalue:"+str(get_value)+"\r\n")
                    else:
                        get_value = exthash.get(listkeyvalue[0],int(listkeyvalue[1]))
                        op_get.write("key:"+listkeyvalue[0]+"\tversion:"+str(listkeyvalue[1])+"\tvalue:"+str(get_value)+"\r\n")
                        
                        
    with open("../input/Delete_file.txt") as today: #please mention file path of file which contain keys to delete the data from data store
            line = exthash.readLine(today)
            while True :
                yieldedStr = next(line).strip()
                if ("" == yieldedStr):
                    break
                exthash.Delete(yieldedStr)