import boto3
import json



def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('pizzaMenu')
    
    table.put_item(Item=event)
    response = {}
   

    print("AddItem successfully!")
    return response
