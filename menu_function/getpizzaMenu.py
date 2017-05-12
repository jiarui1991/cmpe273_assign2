import boto3
import json

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('pizzaMenu')
    response = table.get_item(Key={'menu_id':event['menu_id']})
    item =response['Item']
    return item
 
 
