from __future__ import print_function
from pprint import pprint
import json 
import boto3

def lambda_handler(event, context):
    client = boto3.client('s3') 
    s3 = boto3.resource('s3', aws_access_key_id='***',aws_secret_access_key='***')
    bucket = s3.Bucket('recipebucketv1')
    bucket2 = s3.Bucket('txtmp3bucketv1')
    
    obj = client.get_object(Bucket='recipebucketv1', Key='chips_recipe.json')
    
    jdata=obj['Body'].read()
    
    parsed_json1 = json.loads(jdata)
    recipeTitle=parsed_json1['recipeTitle']
    recipeSleep=parsed_json1['recipeIns'][0]['sleep']
    recipeIns=parsed_json1['recipeIns']
    finalrecipe=''
    
    for ins in recipeIns:
        outSleep=ins['sleep']
        outIns=ins['instruction']
        pprint('{}<break time = "{}">'.format(outIns, outSleep))
        finalrecipe= finalrecipe + '{}<break time = "{}">'.format(outIns, outSleep)
       
    s3.Bucket('txtmp3bucketv1').put_object(Key='recipev1.txt', Body=finalrecipe)
    
    
    return 'HiFi from Food Admin'  
