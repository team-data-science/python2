# Import the json module
import json

# JSON basics

# Below is an example of a json array of objects in ./data/data_subset.json file
# [
#     {
#         "InvoiceNo": 536370,
#         "StockCode": 22492,
#         "Description": "MINI PAINT SET VINTAGE",
#         "Quantity": 36,
#         "InvoiceDate": "12/1/2010 8:45",
#         "UnitPrice": 0.65,
#         "CustomerID": 12583,
#         "Country": "France"
#     },
#     {
#         "InvoiceNo": 536372,
#         "StockCode": 22632,
#         "Description": "HAND WARMER RED POLKA DOT",
#         "Quantity": 6,
#         "InvoiceDate": "12/1/2010 9:01",
#         "UnitPrice": 1.85,
#         "CustomerID": 17850,
#         "Country": "United Kingdom"
#     },
#     ...
#     ...
# ]

# Deserilization of JSON is the conversion of JSON objects into their respective Python objects.

# JSON OBJECT	PYTHON OBJECT
# object	    dict
# array	        list
# string	    str
# null	        None
# number(int)	int
# number(real)	float
# true	        True
# false	        False

# Load JSON from file

with open("./data/data_subset.json") as json_file:
    json_object = json.load(json_file)

# Create JSON string and pretty print of JSON string

json.dumps(json_object)

# '[{"InvoiceNo": 536370, "StockCode": 22492, "Description": "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45", "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}, {"InvoiceNo": 536372, "StockCode": 22632, "Description": "HAND WARMER RED POLKA
# DOT", "Quantity": 6, "InvoiceDate": "12/1/2010 9:01", "UnitPrice": 1.85, "CustomerID": 17850, "Country": "United Kingdom"}, {"InvoiceNo":
# 536389, "StockCode": 22727, "Description": "ALARM CLOCK BAKELIKE RED", "Quantity": 4, "InvoiceDate": "12/1/2010 10:03", "UnitPrice": 3.75, "CustomerID": 12431, "Country": "Australia"}, {"InvoiceNo": 562106, "StockCode": 22993, "Description": "SET OF 4 PANTRY JELLY MOULDS", "Quantity": 1, "InvoiceDate": "8/2/2011 15:19", "UnitPrice": 1.25, "CustomerID": 14076, "Country": "United Kingdom"}]'

json_formatted_string = json.dumps(
    json_object, indent=4)  # indent used for pretty print
print(json_formatted_string)

# [
#     {
#         "InvoiceNo": 536370,
#         "StockCode": 22492,
#         "Description": "MINI PAINT SET VINTAGE",
#         "Quantity": 36,
#         "InvoiceDate": "12/1/2010 8:45",
#         "UnitPrice": 0.65,
#         "CustomerID": 12583,
#         "Country": "France"
#     },
#     {
#         "InvoiceNo": 536372,
#         "StockCode": 22632,
#         "Description": "HAND WARMER RED POLKA DOT",
#         "Quantity": 6,
#         "InvoiceDate": "12/1/2010 9:01",
#         "UnitPrice": 1.85,
#         "CustomerID": 17850,
#         "Country": "United Kingdom"
#     },
#     ...
#     ...
# ]

# load JSON string

json_object = json.loads(json_formatted_string)

# [{'InvoiceNo': 536370, 'StockCode': 22492, 'Description': 'MINI PAINT SET VINTAGE', 'Quantity': 36, 'InvoiceDate': '12/1/2010 8:45', 'UnitPrice': 0.65, 'CustomerID': 12583, 'Country': 'France'}, {'InvoiceNo': 536372, 'StockCode': 22632, 'Description': 'HAND WARMER RED POLKA DOT', 'Quantity': 6, 'InvoiceDate': '12/1/2010 9:01', 'UnitPrice': 1.85, 'CustomerID': 17850, 'Country': 'United Kingdom'}, {'InvoiceNo': 536389, 'StockCode': 22727, 'Description': 'ALARM CLOCK BAKELIKE RED', 'Quantity': 4, 'InvoiceDate': '12/1/2010 10:03', 'UnitPrice': 3.75,
# 'CustomerID': 12431, 'Country': 'Australia'}, {'InvoiceNo': 562106, 'StockCode': 22993, 'Description': 'SET OF 4 PANTRY JELLY MOULDS', 'Quantity': 1, 'InvoiceDate': '8/2/2011 15:19', 'UnitPrice': 1.25, 'CustomerID': 14076, 'Country': 'United Kingdom'}]

# access individual attributes within the object

# loop through a list and
# access of values by using .get method and a name of the key
# in a python dictionary

# list of keys on the first level of a json tree
json_object[0].keys()

# dict_keys(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])

# Access all 'InvoiceNo' for each transaction
for transaction in json_object:
    print(transaction.get('InvoiceNo'))


# modify the object's attributes

# dump it back into a string
