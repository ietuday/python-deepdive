import boto3

bucket_name = 'kreedo-file-bulk-upload'

s3 = boto3.client('s3')

s3.download_file('kreedo-file-bulk-upload',
                 'Rapidera Test_Observation.xlsx', 'output.xlsx')
