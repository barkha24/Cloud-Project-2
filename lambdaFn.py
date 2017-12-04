from __future__ import print_function
from pprint import pprint
from contextlib import closing
import json 
import boto3

def lambda_handler(event, context):
    client = boto3.client('s3') 
    s3 = boto3.resource('s3', aws_access_key_id='****',aws_secret_access_key='****')
    #bucket = s3.Bucket('recipebucketv1')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    bucket2 = s3.Bucket('txtmp3bucketv1')
    
    obj = client.get_object(Bucket=bucket, Key=key)
    
    jdata=obj['Body'].read()
    
    parsed_json1 = json.loads(jdata)
    recipeTitle=parsed_json1['recipeTitle']
    recipeSleep=parsed_json1['recipeIns'][0]['sleep']
    recipeIns=parsed_json1['recipeIns']
    finalrecipe=''
    #finalrecipe1=''
    
    for ins in recipeIns:
        outSleep=ins['sleep']
        outIns=ins['instruction']
        pprint('{}<break time = "{}">'.format(outIns, outSleep))
        finalrecipe= finalrecipe + '{} <break time = "{}"/> '.format(outIns, outSleep)
        #finalrecipe='<speak>'+finalrecipe1+'</speak>'
        
    s3.Bucket('txtmp3bucketv1').put_object(Key='recipev2.txt', Body=finalrecipe)
    pprint('chips_recipe')
    pprint(finalrecipe)
    pprint('****** Get ready for POLLY ******')
   
    pollyclient = boto3.client('polly',aws_access_key_id='****', aws_secret_access_key='****')
    mp3key=recipeTitle+'.mp3'
    response = pollyclient.synthesize_speech(
    Text = '<speak>'+'Here we go with'+ recipeTitle + finalrecipe +'</speak>',
    TextType ='ssml',
    VoiceId='Joanna',
    OutputFormat='mp3')
    with closing(response["AudioStream"]) as stream:
                s3.Bucket('txtmp3bucketv1').put_object(Key=mp3key, Body=stream.read())
    pprint(response)

    return 'HiFi from Food Admin'
