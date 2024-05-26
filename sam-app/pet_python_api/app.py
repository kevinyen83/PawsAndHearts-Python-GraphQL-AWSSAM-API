import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
table = dynamodb.Table('pet-and-paws-pet')

def validate_input(input_data):
    required_fields = [
        'contactEmail', 'contactPhone', 'organizationName', 'applicantName',
        'petId', 'name', 'category', 'age', 'gender', 'color', 'size',
        'location', 'vaccination', 'availability', 'image', 'description'
    ]
    return all(field in input_data for field in required_fields)

def get_pet(petId):
    try:
        response = table.get_item(Key={'petId': petId})
        if 'Item' in response:
            return build_response(200, response['Item'])
        else:
            return build_response(404, {'error': f'Pet not found for ID: {petId}'})
    except Exception as e:
        print(f"Error getting pet: {str(e)}")
        return build_response(500, {'error': f'Error retrieving pet: {str(e)}'})

def get_pets():
    try:
        response = table.scan()
        if 'Items' in response:
            return build_response(200, {'pets': response['Items']})
        else:
            return build_response(404, {'error': 'No pets found'})
    except Exception as e:
        print(f"Error getting pets: {str(e)}")
        return build_response(500, {'error': f'Error retrieving pets: {str(e)}'})

# 更新寵物可用性
def update_availability(data):
    petId = data.get('petId')
    if not petId:
        return build_response(400, {'error': 'petId is required'})

    try:
        response = table.update_item(
            Key={'petId': petId},
            UpdateExpression="set availability = :a",
            ExpressionAttributeValues={':a': 'No'},
            ReturnValues="ALL_NEW"
        )
        return build_response(200, response['Attributes'])
    except Exception as e:
        print(f"Error updating availability: {str(e)}")
        return build_response(500, {'error': f'Error updating availability: {str(e)}'})

def delete_pet(petId):
    try:
        table.delete_item(Key={'petId': petId})
        return build_response(204, '')
    except Exception as e:
        print(f"Error deleting pet: {str(e)}")
        return build_response(500, {'error': f'Error deleting pet: {str(e)}'})

def save_pet(pet):
    if not validate_input(pet):
        return build_response(400, {'error': 'Missing required fields'})
    
    pet['uploadDate'] = datetime.utcnow().isoformat()
    try:
        table.put_item(Item=pet)
        return build_response(200, 'Pet saved successfully')
    except Exception as e:
        print(f"Error saving pet: {str(e)}")
        return build_response(500, {'error': f'Error saving pet: {str(e)}'})

def build_response(status_code, body=None):
    response = {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PATCH,DELETE',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    }
    if body:
        response['body'] = json.dumps(body)
    return response

def lambda_handler(event, context):
    print('Request event:', event)
    http_method = event['httpMethod']
    path = event['path']
    if http_method == 'GET' and path == '/health':
        return build_response(200)
    elif http_method == 'GET' and path == '/pet':
        return get_pet(event['queryStringParameters']['petId'])
    elif http_method == 'GET' and path == '/pets':
        return get_pets()
    elif http_method == 'PATCH' and path == '/updateAvailability':
        return update_availability(json.loads(event['body']))
    elif http_method == 'DELETE' and path == '/pet':
        return delete_pet(json.loads(event['body'])['petId'])
    elif http_method == 'POST' and path == '/pet':
        return save_pet(json.loads(event['body']))
    else:
        return build_response(404, {'error': 'Not Found'})
