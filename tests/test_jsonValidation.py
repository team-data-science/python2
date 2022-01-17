import pytest
import json
# jsonschema is an implementation of the JSON Schema specification for Python.
from jsonschema import validate
from src.jsonValidation import validate_json
from src.jsonValidation import validate_json_schema

# > $ pytest
# ================================================================================= test session starts ==================================================================================
# platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
# rootdir: here it will be your path
# collected 4 items

# tests\test_jsonValidation.py ....                                                                                                                                                 [100%]

# ================================================================================== 4 passed in 0.11s ===================================================================================


class Test_JSONValidation:

    def test_validate_json_Should_return_True_when_valid_json_string(self):
        # Arrange
        json_string = '[{"InvoiceNo": 536370, "StockCode": 22492, "Description": "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45", "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}, {"InvoiceNo": 536372, "StockCode": 22632, "Description": "HAND WARMER RED POLKA DOT", "Quantity": 6, "InvoiceDate": "12/1/2010 9:01", "UnitPrice": 1.85, "CustomerID": 17850, "Country": "United Kingdom"}, {"InvoiceNo": 536389, "StockCode": 22727, "Description": "ALARM CLOCK BAKELIKE RED", "Quantity": 4, "InvoiceDate": "12/1/2010 10:03", "UnitPrice": 3.75, "CustomerID": 12431, "Country": "Australia"}, {"InvoiceNo": 562106, "StockCode": 22993, "Description":"SET OF 4 PANTRY JELLY MOULDS", "Quantity": 1, "InvoiceDate": "8/2/2011 15:19", "UnitPrice": 1.25, "CustomerID": 14076, "Country": "United Kingdom"}]'

        # Act
        is_valid_json = validate_json(json_string)

        # Assert
        assert is_valid_json == True

    def test_validate_json_Should_return_False_when_invalid_json_string(self):

        # Arrange
        invalid_json_string = '{"InvoiceNo": 536370 "StockCode": 22492, "Description":  "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45",   "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}'

        # Act
        is_valid_json = validate_json(invalid_json_string)

        # Assert
        assert is_valid_json == False

    def test_validate_json_schema_Should_return_False_when_invalid_json_schema(self):
        # Arrange
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

        # Act
        is_valid_json_schema, message = validate_json_schema(
            InvoiceNo_is_a_string,  schema=transaction_schema)
        # Assert
        assert is_valid_json_schema == False
        assert message == 'Given JSON data is not valid '

    def test_validate_json_schema_Should_return_True_when_valid_json_schema(self):
        # Arrange
        valid_json_schema = {
            "InvoiceNo": 536370,
            "StockCode": 22492,
            "Description": "MINI PAINT SET VINTAGE",
            "Quantity": 36,
            "InvoiceDate": "12/1/2010 8:45",
            "UnitPrice": 0.65,
            "CustomerID": 12583,
            "Country": "France",
            "CustomerID": 12583,
        }

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

        # Act
        is_valid_json_schema, message = validate_json_schema(
            valid_json_schema,  schema=transaction_schema)
        # Assert
        assert is_valid_json_schema == True
        assert message == "Given JSON is valid."
