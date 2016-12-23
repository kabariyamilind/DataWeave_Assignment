Problem-1:Building key value store

	Python file name:
		assignment.py

	Procedure to execute the code:
		In this program basically Three functionality was covered.
		1.	Adding the record to key value store.
			Function Name:	ADD(key,value)
		2.	Get the record value from the key value store by passing a record key and record version to function.
			Function Name:	get(key,version) or get(key)
		3.	Delete the record from the key value store.
			Function Name:	Delete(key)
		4.	In main function it need to add three different file for three different operation ADD,get and Delete
			Add_file.txt : This file contain all the key value pair that need to be added in key value data store.
				Format of data inside input file : key,value
			get_file.txt : This file contain the key,version pair with respect to which we need to fetch data from key value data store.
				Format of data inside input file : key,version(optional)
			get_op_file.txt : This file contains result from get.It has three fields key,version and value.
				Format of data inside output file : key,version,value
			Delete_file.txt : This file contains keys with respect to which we need to delete the data from key value store
				Format of data inside input file : key
			
			
 
	Major Design Decision:
		Here the number of records can be in Millions as per the program requirement.
		So adding data won't be an difficult task,But Searching a particular key and retrieve the data base on that key is a complicated task.
		In order to take care all that complication below are the points implemented.
			1. Here the heart of design is two level Hashing.
				-> External hashing is for storing the pointers of internal hashing
				-> Internal Hash store the key value pair object.
				-> For External hash to avoid the collision linear probing used.
			2. Here we have assumed per file there will be 10 million record so we have created Hash function base on that assumption.
			3. Number of version that requires to store per key is upto the user.User will be asked to enter the number of version need to maintain per
			   key at the time of execution of program.
			4. Key can be string value.So in hash function we are converting each and every character to ascii equivalent in order to calculate value
			   from hash function.
			   
Problem-2:Finding common entries between two files

	Python file name:
		findRepeated.py

	Procedure to execute the code:
		In this program basically two functionality was covered.
		1.	Adding the record to key value store.
			Function Name:	ADD(key,value)
		2.	Check many urlhs have we repeatedly scraped today from yesterday's scrap
			Function Name:	check(key)
		3.	In main function it need to add two different file for two different operation ADD and check
			today_file.txt : This file contains today's scrapped urls
				Format of data inside file : url
			yday_file.txt : This file contains yesterday's scrapped urls
				Format of data inside file : url
			Repeatedly_crawled.txt : This file contain the all the urls which is repeatedly scraped today by comparing with yesterday's scraped urls
				Format of data inside file : url
			Stats_for_today.txt : This file contains the url and its count,how many time each and every url is scraped repeatedly today.
				Format of data inside file : key
			
			
 
	Major Design Decision:
		Here the number of records can be in Millions as per the program requirement.
		So adding data won't be an difficult task,But Searching a particular key and retrieve the data base on that key is a complicated task.
		In order to take care all that complication below are the points implemented.
			1. Here the heart of design is two level Hashing.
				-> External hashing is for storing the key object
			2. Here we have assumed per file there will be 10 million record so we have created Hash function base on that assumption.
			3. Here url stores as a key.So in hash function we are converting each and every character to ascii equivalent in order to calculate value
			   from hash function.
			4. Here occurrence is calculated at the time of calling the ADD functionality.
			   
Problem-3: Web Scraping
	
	Python file name:
		scrappin.py

	Procedure to execute the code:
		In this program basically Two functionality was covered.
		1.	Scrap the basic information(url,title,price) from the main url
			Function Name:	getbasicInformation_mainURL(tree) #here tree means html tree object
		2.	Scrap the specification information with title from the internal 10 urls
			Function Name:	getInternalUrlScraped(url) #here url means all the internal urls
		3.	In main function it need to mention main url which need to scrap.
			basic_info.json : This json file basic information from main url
				Format of data inside file : {'monitor1':['title','url','price']}
			item_specification.json : This file contains specification information with title from the internal 10 urls
				Format of data inside file : {'title':{<specification information directory>}}
			

			
