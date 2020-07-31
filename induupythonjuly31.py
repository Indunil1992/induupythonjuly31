import boto3
ddb = boto3.client("dynamodb")

def handler(event, context):
    try:
        data = ddb.get_item(
            TableName="indu-testPwith_july31CLI",
            Key={
                'induddbP': {
                    'S': "dresscodeN"
                },
                'induddbS': {
                    'S': "typeoftheD"
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
