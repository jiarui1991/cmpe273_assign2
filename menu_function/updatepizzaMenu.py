import boto3


def lambda_handler(event, context):
    table = boto3.resource('dynamodb', region_name='us-west-1').Table('pizzaMenu')
    table.update_item(
      Key={'menu_id': event['menu_id']},
      UpdateExpression="SET selection = :a",
      ExpressionAttributeValues={':a':event['selection'] }
      )
    response = {}
    return response
