import pandas as pd
import sqlite3

conn = sqlite3.connect('ucimlrepo.db')
#cursor = conn.cursor()


#%%
#Select all columns and instances from a table
query="SELECT * FROM donated_datasets"
result=pd.read_sql(query, conn)
print(result)
#%%
#Join
query='''SELECT * 
        FROM donated_datasets a 
        LEFT JOIN descriptive_questions  b ON a.ID=b.datasetID'''

result=pd.read_sql(query, conn)

#%%
#Joins + Condition
query='''
        SELECT c.name as dataset_name, a.*, b.* 
        FROM dataset_keywords a 
        LEFT JOIN keywords  b ON a.keywordsID=b.id
        LEFT JOIN donated_datasets c on a.datasetID=c.ID
        WHERE c.name='Adult'
        '''

result=pd.read_sql(query, conn)


#%%
#List all tables
query='''
	SELECT name 
	FROM sqlite_master 
	WHERE type= "table"
	'''

result=pd.read_sql(query, conn)

#%%
#Count records
query="SELECT count(*) from foreign_papers"

result=pd.read_sql(query, conn)

conn.close()