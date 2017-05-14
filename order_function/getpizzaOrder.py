import boto3
import json

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('pizzaOrder')
    response = table.get_item(Key={'order_id':event['order_id']})
    item =response['Item']
    return item
 
