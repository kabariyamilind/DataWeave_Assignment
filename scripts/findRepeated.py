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
    def __init__(self,maximumVersions):
        self.exthashmapList = [None]*10000000
        self.todayRepetedList=[]
        self.maximumVersions=int(maximumVersions)
    
    
    #function to add the data in hash map
    #This function also count the number of time partcular link repeated in a day
    def ADD(self,key,value):
        hashkey = hashFunction(key)
        j=1
        while True:
            if self.exthashmapList[hashkey] == None:
                innerHash = innerHashMap(self.maximumVersions)
                innerHash.todayTimesOfOccurance=1
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
                    innerHash.todayTimesOfOccurance+=1
                    self.exthashmapList[hashkey] = innerHash
                    break
                else:
                    hashkey = hashkey+1
                    if hashkey >10000000:
                        hashkey=0
            j+=1
                
    #function for counting whether the link is in yesterday file or not.
    def check(self,key,version=0):
        hashkey = hashFunction(key)
        j=1
        while True:
            innerHash = self.exthashmapList[hashkey]
            if innerHash!=None and innerHash.hashList[self.maximumVersions-1-version] != None:
                keyobj = innerHash.hashList[self.maximumVersions-1-version]
                if keyobj.key == key:
                    if innerHash.todayRepeted ==0:
                        self.todayRepetedList.append(key)
                        innerHash.todayRepeted =1
                    self.exthashmapList[hashkey] = innerHash
                    break
                else:
                    hashkey = hashkey+1
                    if hashkey >10000000:
                        hashkey=0
            else:
                #value = "No value exist for given key and version"
                break
            j+=1
            
    # this function contains generators which is built for reading the both today and tomorrows file.
    def checkOccurance(self):       
        with open("../input/today_file2.txt") as today: #please mention today's crawled file path here
            line = self.readLine(today)
            while True :
                yieldedStr = next(line)
                if ("" == yieldedStr):
                    break
                self.ADD(yieldedStr.strip(),0)
                
        
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
    maximumVersions = raw_input("Please enter number of versions:\n")
    exthash = externalHashMap(maximumVersions)
    listOcuurance = exthash.checkOccurance()
    todayrepetedList = exthash.getRepetedList()
    with open("../output/Repeatedly_crawled.txt","wb") as rc:
        rc.write("Urlhs which are Repeatedly crawled\r\n")
        for repetedItem in todayrepetedList:
            rc.write(repetedItem+'\r\n')
    with open("../output/Stats_for_today.txt","wb") as rc:
        rc.write("Stats for today\r\n")
        rc.write("url\trepetation\r\n")
        for urls in listOcuurance:
            if urls!= None:
                rc.write(str(urls.hashList[int(maximumVersions)-1].key)+"\t")
                rc.write(str(urls.todayTimesOfOccurance)+"\r\n")