import os

S3_BUCKET                 = "jonie1"
S3_KEY                    = 
S3_SECRET                 = 
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000

#plug in jonathan.e aws secret id and secret password