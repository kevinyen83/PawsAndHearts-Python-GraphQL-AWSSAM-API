import json
import boto3
from datetime import datetime
import graphene
from graphene import ObjectType, String, Int, Boolean, Field, List, ID, InputObjectType

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
table = dynamodb.Table('pet-and-paws-pet')

class PetInput(InputObjectType):
    petId = ID(required=True)
    organizationName = String(required=True)
    applicantName = String(required=True)
    contactEmail = String(required=True)
    contactPhone = String(required=True)
    name = String(required=True)
    category = String(required=True)
    age = Int(required=True)
    gender = String(required=True)
    color = String(required=True)
    size = String(required=True)
    location = String(required=True)
    vaccination = String(required=True)
    availability = String(required=True)
    image = String(required=True)
    description = String(required=True)

class PetType(ObjectType):
    petId = ID()
    organizationName = String()
    applicantName = String()
    contactEmail = String()
    contactPhone = String()
    name = String()
    category = String()
    age = Int()
    gender = String()
    color = String()
    size = String()
    location = String()
    vaccination = String()
    availability = String()
    image = String()
    description = String()

class Query(ObjectType):
    pet = Field(PetType, petId=ID(required=True))
    pets = List(PetType)

    def resolve_pet(root, info, petId):
        try:
            response = table.get_item(Key={'petId': petId})
            if 'Item' in response:
                return response['Item']
            else:
                return None
        except Exception as e:
            print(f"Error getting pet: {str(e)}")
            return None

    def resolve_pets(root, info):
        try:
            response = table.scan()
            if 'Items' in response:
                return response['Items']
            else:
                return []
        except Exception as e:
            print(f"Error getting pets: {str(e)}")
            return []

class CreatePetProfile(graphene.Mutation):
    class Arguments:
        petProfileData = PetInput(required=True)

    pet = Field(PetType)

    def mutate(root, info, petProfileData):
        if not validate_input(petProfileData):
            raise Exception('Missing required fields')
        pet_profile_data_dict = petProfileData.__dict__
        pet_profile_data_dict['uploadDate'] = datetime.utcnow().isoformat()
        try:
            table.put_item(Item=pet_profile_data_dict)
            return CreatePetProfile(pet=pet_profile_data_dict)
        except Exception as e:
            print(f"Error saving pet: {str(e)}")
            raise Exception('Error saving pet')

class Mutation(ObjectType):
    create_pet_profile = CreatePetProfile.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

def validate_input(input_data):
    required_fields = [
        'contactEmail', 'contactPhone', 'organizationName', 'applicantName',
        'petId', 'name', 'category', 'age', 'gender', 'color', 'size',
        'location', 'vaccination', 'availability', 'image', 'description'
    ]
    return all(hasattr(input_data, field) for field in required_fields)

# AWS Lambda handler
def lambda_handler(event, context):
    print('Request event:', event)
    body = event.get('body', '{}')
    if isinstance(body, dict):
        print('Body is already a dictionary.')
    else:
        print('Body is a string, converting to dictionary.')
        body = json.loads(body)
    print('Parsed body:', body)
    query = body.get('query')
    variables = body.get('variables')

    if query is None:
        print('No query provided in the request body')
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Query not provided'})
    }

    try:
        result = schema.execute(query, variable_values=variables)
        response_body = {}
        if result.errors:
            response_body['errors'] = [str(error) for error in result.errors]
        if result.data:
            response_body['data'] = result.data

        return {
            'statusCode': 200 if not result.errors else 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PATCH,DELETE',
                'Access-Control-Allow-Headers': 'Content-Type,X-Api-Key'
            },
            'body': json.dumps(response_body)
    }
    except Exception as e:
        print(f"Error executing query: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }