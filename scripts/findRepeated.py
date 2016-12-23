# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:31:59 2016

@author: Milind Kabariya
"""

#class creating key value object
class keyValue:
    def __init__(self,key):
        self.key = key
	    self.count = 1
	    self.repeated=0
            
#hash function for caluclate the hash value for URLS
def hashFunction(key):
    i=0
    hashVal = 7
    while(i<len(key)):
        hashVal = (hashVal*13 + ord(key[i]))%10000000;
        i+=1
    return hashVal 

#class for second level hashing
class innerHashMap:
    def __init__(self,maximumVersions):
        self.hashList =[None]*int(maximumVersions)
        self.todayTimesOfOccurance =0
        self.todayRepeted=0
        self.maximumVersions=int(maximumVersions)
    def innerHashMapAddValue(self,keyValObj):
        if len(self.hashList)<self.maximumVersions:
            self.hashList.append(keyValObj)
        else:
            self.hashList.pop(0)
            self.hashList.append(keyValObj)
    
#class for primary(first level) hashing
class externalHashMap:
    #When the externalHashMap object create it will create two list
    #1.exthashmapList: to store the pointers of the innerhash
    #2.store number of times url particular url got repeated
    def __init__(self):
        self.exthashmapList = [None]*10000000
        self.todayRepetedList=[]
        #self.maximumVersions=int(maximumVersions)
    
    
    #function to add the data in hash map
    #This function also count the number of time partcular link repeated in a day
    def ADD(self,key):
        hashkey = hashFunction(key)
        j=1
        while True:
            if self.exthashmapList[hashkey] == None:
                #innerHash = innerHashMap(self.maximumVersions)
                #innerHash.todayTimesOfOccurance=1
                keyValueObj = keyValue(key)
                #innerHash.innerHashMapAddValue(keyValueObj)
                self.exthashmapList[hashkey] = keyValueObj
                break
            else:
                #innerHash = self.exthashmapList[hashkey]
                keyobj = self.exthashmapList[hashkey]
                #keyValueObj = keyValue(key,value)
                if keyobj.key == key:
                    #innerHash.innerHashMapAddValue(keyValueObj)
                    #innerHash.todayTimesOfOccurance+=1
		            keyobj.count +=1
                    self.exthashmapList[hashkey] = keyobj
                    break
                else:
                    hashkey = hashkey+pow(j,2)
		            remain = hashkey%100
                    if hashkey >10000000:
                        hashkey=remain+0
			j=0
            j+=1
                
    #function for counting whether the link is in yesterday file or not.
    def check(self,key,version=0):
        hashkey = hashFunction(key)
        j=1
        while True:
            keyobj = self.exthashmapList[hashkey]
            if keyobj!=None:
                if keyobj.key == key:
                    if keyobj.repeated ==0:
                        keyobj.repeated==1
                    self.exthashmapList[hashkey] = keyobj
                    break
                else:
                    hashkey = hashkey+pow(j,2)
                    remain = hashkey%100
                    if hashkey >10000000:
                        hashkey=remain+0
			j=0
            else:
                #value = "No value exist for given key and version"
                break
            j+=1
            
    # this function contains generators which is built for reading the both today and tomorrows file.
    def checkOccurance(self):       
	k=0
        with open("../input/today_file.txt") as today: #please mention today's crawled file path here
            line = self.readLine(today)
            while True :
                yieldedStr = next(line)
                if ("" == yieldedStr):
                    break
                self.ADD(yieldedStr.strip())
                
        
        with open("../input/yday_file.txt") as yday: #please mention yesterday's crawled file path here
            line = self.readLine(yday)
            while True :
                yieldedStr = next(line)
                if ("" == yieldedStr):
                    break
                self.check(yieldedStr.strip())
        return self.exthashmapList
        
    def readLine(self,yday):
        while True :
            line = yday.readline()
            #print line
            yield line
        
        
    def getRepetedList(self):
        return self.todayRepetedList

if __name__ == "__main__": 
    #maximumVersions = raw_input("Please enter number of versions:\n")
    #if maximumVersions =="":
    #   maximumVersions=3
    exthash = externalHashMap()
    listOcuurance = exthash.checkOccurance()
    with open("../output/Repeatedly_crawled.txt","wb") as rc:
        rc.write("Urlhs which are Repeatedly crawled\r\n")
        for urls in listOcuurance:
	        if urls!= None:
                	rc.write(str(urls.key)+'\r\n')
            
    with open("../output/Stats_for_today.txt","wb") as rc:
        rc.write("Stats for today\r\n")
        rc.write("url\trepetation\r\n")
        for urls in listOcuurance:
            if urls!= None:
                rc.write(str(urls.key)+"\t")
                rc.write(str(urls.count)+"\r\n")
