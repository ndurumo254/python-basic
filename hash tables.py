#hash tables are types of data structures those maps keywords to their values


#dictionary

contacts={'john':10928,'mike':534653,'wayio':54775,'nick':73454}
print(contacts)


#cascanded dictionary

employee={'classa':{'john':{'salary':54514314,'id':3,'rank':'casual'},
                    'dave':{'salary':75479,'id':3,'rank':'permanent'}
                    }
          }
print(employee)


#accessing keys in dictionary

for items in employee.values():
    print(items)


#CONVERTING DICTIONARY INTO DATA FRAMES


import pandas as pd
df=pd.DataFrame(employee['classa'])#this will convert my data in tabular form
print(df)