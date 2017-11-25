import boto3
import os

client = boto3.client('polly',aws_access_key_id=os.getenv( 'AWS_ACCESS_ID' ), aws_secret_access_key=os.getenv( 'AWS_SECRET_KEY' ),region_name='us-west-2' )
f = open('recipes.txt' , 'r')
txt = f.read()
response = client.synthesize_speech(
Text = "txt",
VoiceId='Joanna',
OutputFormat='mp3')

print(response)
