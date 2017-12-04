from __future__ import print_function
from pprint import pprint
from contextlib import closing
import json 
import boto3

def lambda_handler(event, context):
    
    client = boto3.client('s3') 
    s3 = boto3.resource('s3', aws_access_key_id='****',aws_secret_access_key='****')
 
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    obj = client.get_object(Bucket=bucket, Key=key)
    
    #get json data from s3 object
    jdata=obj['Body'].read()
    
    #parse json
    parsed_json1 = json.loads(jdata) 
    recipeTitle=parsed_json1['recipeTitle']
    recipeSleep=parsed_json1['recipeIns'][0]['sleep']
    recipeIns=parsed_json1['recipeIns']
    finalrecipe=''
   
    #loop over parsed data and create ssml for polly with breaks
    for ins in recipeIns:
        outSleep=ins['sleep']
        outIns=ins['instruction']
        pprint('{}<break time = "{}">'.format(outIns, outSleep))
        finalrecipe= finalrecipe + '{} <break time = "{}"/> '.format(outIns, outSleep)
       
    s3.Bucket('txtmp3bucketv1').put_object(Key='recipev2.txt', Body=finalrecipe)
    
    pprint(finalrecipe)
    pprint('****** Get ready for POLLY ******')
   
    pollyclient = boto3.client('polly',aws_access_key_id='****', aws_secret_access_key='****')
    mp3key=recipeTitle+'.mp3'
    
    #calling polly function to create mp3 for our recipes!!
    response = pollyclient.synthesize_speech(
    Text = '<speak>'+'Here we go with'+ recipeTitle + finalrecipe +'</speak>',
    TextType ='ssml',
    VoiceId='Joanna',
    OutputFormat='mp3')
    
    #putting polly mp3 file - streaming object to s3 bucket
    with closing(response["AudioStream"]) as stream:
                s3.Bucket('txtmp3bucketv1').put_object(Key=mp3key, Body=stream.read())
    
    return 'HiFi from Food Admin'
