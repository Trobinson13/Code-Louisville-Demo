#Notes as I worked through the data1_project. 
#<Week>.<ModuleNumber>

#Function to print empty line, then a message wrapped in a character banner.
def banner(message, banner = "-"):
    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(line)

##
###Week 3 Data Structures 
##

#####
banner("Content for 3.1")
#####
a = [1,3,2,5,6]
print(a)

#####
banner("Content for 3.2")
#####

#don't over comment your code 
#don't write really complicated comments that 
#are overwhelming and don't do a good job of 
#explaining anything 
#for example this is slicing a list 
#but don't "undercomment" either

print(a[1:4])

#####
banner("Content for 3.3")
#####

text = ['this','is','a','list','of','text','values']
num = [1,5,6,2,4,4] # and this is a hand-typed list of integers

#note that this DOES NOT include the 3rd index item
print('this is how you slice a list from the 0 index to the 3rd index', text[0:3])

print('the same thing works for numbers',num[0:3]) #you can comment to the side or above, depends on your preference

#####
banner("Content for 3.4")
#####

data = {
    "make" : "Honda",
    "model": "Accord",
    "year" : 2015,
    "mileage":100250,
    "features" : ['leather seats', 'AC','Radio']
}
print(data)

#####
banner("Content for 3.5")
#####

#here's how we select a value from a dictionary 
#this will return a list!
data['features']
print(data['features'])

#####
banner("Content for 3.6")
#####

print(type(data))
print(type(data['features']))
print(type(1))

#####
banner("Content for 3.7")
#####

geo_data = (27.2839, 25.2030)
coordinates =(-10,5)

print("To select these values, use square brackets like this: coordinates[0] = ", coordinates[0])
print("Or, like this, geo_data[1] = ", geo_data[1])

###
### Week 4: Importing Data
###

#####
banner("Content for 4.1")
#####

print("Command to install pandas on Mac is: \"pip3 install pandas\"")
print("Command to install numpy on Mac is: \"pip3 install numpy\"")

#####
banner("Content for 4.2")
#####

print("Running imports for:\nnumpy\npandas")
import numpy as np 
import pandas as pd

#####
banner("Content for 4.3")
#####
test_data = pd.DataFrame([[1,4],[1,6], ['text', 'hello']],columns=['A','B'])
print(test_data)

#####
banner("Content for 4.4")
#####

spend_df = pd.read_csv("/Users/tre.robinson/Documents/GitHub/Code-Louisville-Demo/data1_project/Expenditures_FiscalYear2018.csv")
print(spend_df.head())

###
### Week 5: Exploring Data
###

#####
banner("Content for 5.1")
#####

print(spend_df.shape)
print(type(spend_df.shape))

#####
banner("Content for 5.2")
#####

n, num_columns = spend_df.shape
print("This is the number of rows: ", n)
print("This is the number of columns: ", num_columns)

#####
banner("Content for 5.3")
#####
agencies = list(spend_df['Agency_Name'].unique())
print(agencies)


