# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self,username,password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        #if data isnt empty it will try to add
        if data is not None:
            try:
                self.database.animals.insert_one(data)  # data should be dictionary 
                #this will return true if the item was added 
                print("TRUE")
             
            #this will return false if the item wasnt added to the database. 
            except Exception as e:
                print("FALSE")
                
        #if there was nothing in the data parameter it will return the exeption.         
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 
        
    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            results = list(self.database.animals.find(data)) # data in dictionary\
            return results
            
        #this will return false if the item wasnt found and return a empty list       
        else:
            self.database.animals.find({})
            print("none")
            return False
    
    # create method to implement the U in CRUD. 
    def update(self, data, update):
        #if data is not empty 
        if data is not None:
            #this will try to update and print the amount that it updated
            try:
                result = self.database.animals.update_one(data, update)  # data should be dictionary 
                print(result.modified_count)
                
            #this will return the exeption if it wasnt able to upated the item
            except Exception as e:
                print("FALSE")
                
        #this will return the exeption if there is nothing in the data item.
        else: 
            raise Exception("Nothing to update, because data parameter is empty")
    
    # create the delete method to implement the D in CRUD
    def delete(self, data):
        
        #this will delete the item if its the data is not empty
        if data is not None:
            try:
                #this will delete the item and return the count of deleted items. 
                result = self.database.animals.delete_one(data)  # data should be dictionary 
                print(result.deleted_count)
                
            #this is the exeption if the item wasnt deleted
            except Exception as e:
                print("FALSE")
            
        #this will return exeption if the data is empty
        else: 
            raise Exception("Nothing to delete, because data parameter is empty") 