'''
Created on 17-Feb-2013

@author: Sai Gopal
'''
from Query.Process_Query import Rec_Query
from DB.Database import Create_Rand_DB
from DB import DB

if __name__ == '__main__':
    DB=Create_Rand_DB() 
    Rec_Query(raw_input('Enter A Query::'),DB)