import boto3
import json


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('pizzaMenu')
    
    response = table.delete_item(
        Key={'menu_id': event['menu_id']}
    )
    
    return "Delete successfully"
