import boto3
from time import gmtime, strftime

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    order_table = dynamodb.Table('pizzaOrder')
    table_menu = dynamodb.Table('pizzaMenu')
    
    response = order_table.get_item(Key={'order_id':event['order_id']})
    order_info = response['Item']
    content = order_info['order_content']
    order_status = order_info['order_status']
    menu_id = order_table.get_item(Key={'order_id': event['order_id']}).get('Item').get('menu_id')
    selection = table_menu.get_item(Key={'menu_id':menu_id}).get('Item').get('selection')
    menu_info = table_menu.get_item(Key={'menu_id':menu_id})
  
    sizelist = table_menu.get_item(Key={'menu_id':menu_id}).get('Item').get('size')
    
    
    if order_status == "step1":
        index = int(event['input'])-1
        size = ""
        i = 1
        for k in sizelist:
            size += str(i) + "."
            size += k + " "
            i += 1
        sizeMessage = {"Message": "Which size do you want? " + size}
        order_table.update_item(
            Key={
                'order_id':event['order_id']
            },
            UpdateExpression="set order_content.selection =:s, order_status =:r",
            ExpressionAttributeValues={':s': selection[index],
                                        ':r':"step2"
                                    } 
        )
        return sizeMessage
        
    elif order_status == "step2":
        index2 = int(event['input'])-1
        order_table.update_item(
            Key={
                'order_id':event['order_id']
            },
            UpdateExpression="set order_content.size =:s, order_status =:r, order_content.order_time = :d",
            ExpressionAttributeValues={':s': sizelist[index2],
                                        ':r':"processing",
                                        ':d': strftime("%m-%d-%Y %H:%M:%S", gmtime())
                                        } 
        )

        menu_content = menu_info['Item']
        prices = menu_content['price']
        cost = prices[index2]
        
        costMessage = {"Message":"Your order costs " + cost + ". We will email you when the order is ready. Thank you!"}
        
        order_table.update_item(
            Key={
                'order_id':event['order_id']
            },
            UpdateExpression="set order_content.cost = :c",
            ExpressionAttributeValues={':c': cost}
        )
        return costMessage
