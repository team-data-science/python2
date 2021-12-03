import json
# jsonschema is an implementation of the JSON Schema specification for Python.
import jsonschema
from jsonschema import validate

# JSON validation

with open("./data/data_subset.json") as json_file:
    data = json.load(json_file)

# Below is an example of a json array of objects in ./data/data_subset.json file

# First dictionary in the list of dictionaries:
#     {
#         "InvoiceNo": 536370,
#         "StockCode": 22492,
#         "Description": "MINI PAINT SET VINTAGE",
#         "Quantity": 36,
#         "InvoiceDate": "12/1/2010 8:45",
#         "UnitPrice": 0.65,
#         "CustomerID": 12583,
#         "Country": "France"
#     }

valid_transaction_dict = data[0]
valid_transaction_dict
# > { 'Country': 'France',
# >   'CustomerID': 12583,
# >   'Description': 'MINI PAINT SET VINTAGE',
# >   'InvoiceDate': '12/1/2010 8:45',
# >   'InvoiceNo': 536370,
# >   'Quantity': 36,
# >   'StockCode': 22492,
# >   'UnitPrice': 0.65}

# create JSON schema with attributes and types

transaction_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "InvoiceNo": {
            "type": "integer"
        },
        "StockCode": {
            "type": "integer"
        },
        "Description": {
            "type": "string"
        },
        "Quantity": {
            "type": "integer",
        },
        "InvoiceDate": {
            "type": "string"
        },
        "UnitPrice": {
            "type": "number"
        },
        "CustomerID": {
            "type": "integer"
        },
        "Country": {
            "type": "string"
        }
    },
    "required": [
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "CustomerID",
        "InvoiceDate",
        "UnitPrice"

    ]
}

validate(instance=valid_transaction_dict, schema=transaction_schema)
# > None
customer_id_missing_dict = {
    "InvoiceNo": 536370,
    "StockCode": 22492,
    "Description": "MINI PAINT SET VINTAGE",
    "Quantity": 36,
    "InvoiceDate": "12/1/2010 8:45",
    "UnitPrice": 0.65,
    "Country": "France"
}

validate(instance=customer_id_missing_dict, schema=transaction_schema)
# > Traceback (most recent call last):
# >   File "<string>", line 1, in <module>
# >   File "C:\Users\kbaka\_projects_python\2021-12-03_python2_teamdatascience\python2\venv\lib\site-packages\jsonschema\validators.py", line 967, in validate
# >     raise error
# > ValidationError: 'CustomerID' is a required property
# >
# > Failed validating 'required' in schema:
# >     {'$schema': 'http://json-schema.org/draft-04/schema#',
# >      'properties': {'Country': {'type': 'string'},
# >                     'CustomerID': {'type': 'integer'},
# >                     'Description': {'type': 'string'},
# >                     'InvoiceDate': {'type': 'string'},
# >                     'InvoiceNo': {'type': 'integer'},
# >                     'Quantity': {'type': 'integer'},
# >                     'StockCode': {'type': 'integer'},
# >                     'UnitPrice': {'type': 'number'}},
# >      'required': ['InvoiceNo',
# >                   'StockCode',
# >                   'Quantity',
# >                   'CustomerID',
# >                   'InvoiceDate',
# >                   'UnitPrice'],
# >      'type': 'object'}
# >
# > On instance:
# >     {'Country': 'France',
# >      'Description': 'MINI PAINT SET VINTAGE',
# >      'InvoiceDate': '12/1/2010 8:45',
# >      'InvoiceNo': 536370,
# >      'Quantity': 36,
# >      'StockCode': 22492,
# >      'UnitPrice': 0.65}

InvoiceNo_is_a_string = {
    "InvoiceNo": "536370",
    "StockCode": 22492,
    "Description": "MINI PAINT SET VINTAGE",
    "Quantity": 36,
    "InvoiceDate": "12/1/2010 8:45",
    "UnitPrice": 0.65,
    "CustomerID": 12583,
    "Country": "France",
    "CustomerID": 12583,
}
validate(instance=InvoiceNo_is_a_string, schema=transaction_schema)
# > Traceback (most recent call last):
# >   File "<string>", line 1, in <module>
# >   File "C:\Users\kbaka\_projects_python\2021-12-03_python2_teamdatascience\python2\venv\lib\site-packages\jsonschema\validators.py", line 967, in validate
# >     raise error
# > ValidationError: '536370' is not of type 'integer'
# >
# > Failed validating 'type' in schema['properties']['InvoiceNo']:
# >     {'type': 'integer'}
# >
# > On instance['InvoiceNo']:
# >     '536370'

# Valid JSON string
valid_json_string = json.dumps(valid_transaction_dict)

# Invalid JSON string - missing ',' delimiter
invalid_json_string = '{"InvoiceNo": 536370 "StockCode": 22492, "Description": "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45", "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}'

json.loads(invalid_json_string)
# > Traceback (most recent call last):
# >   File "<string>", line 1, in <module>
# >   File "C:\Users\kbaka\AppData\Local\Programs\Python\Python39\lib\json\__init__.py", line 346, in loads
# >     return _default_decoder.decode(s)
# >   File "C:\Users\kbaka\AppData\Local\Programs\Python\Python39\lib\json\decoder.py", line 337, in decode
# >     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
# >   File "C:\Users\kbaka\AppData\Local\Programs\Python\Python39\lib\json\decoder.py", line 353, in raw_decode
# >     obj, end = self.scan_once(s, idx)
# > JSONDecodeError: Expecting ',' delimiter: line 1 column 22 (char 21)


# create a validation function

def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True


def validate_json_schema(json_data):
    """REF: https://json-schema.org/ """

    schema = transaction_schema

    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is not valid"
        return False, err

    error_message = "Given JSON is valid."
    return True, error_message


# validate valid json string
validate_json()

# validate INVALID json string
validate_json(invalid_json_string)


# validate data with valid schema
validate_json_schema(valid_transaction_dict)
# > (True, 'Given JSON data is Valid')

# validate data with invalid schema
validate_json_schema(InvoiceNo_is_a_string)
# > '536370' is not of type 'integer'
# >
# > Failed validating 'type' in schema['properties']['InvoiceNo']:
# >     {'type': 'integer'}
# >
# > On instance['InvoiceNo']:
# >     '536370'
# > (False, 'Given JSON data is not valid')
