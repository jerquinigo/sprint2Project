from flask import Flask, render_template, request, redirect
#from werkzeug.utils import secure_filename
from werkzeug.utils import secure_filename
import boto3
from helpers import *

UPLOAD_FOLDER = '/Users/Administrator/Desktop/testingSubmit/pictureFolder'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config.from_object("config")

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
    #if request.method == "POST":
        #if request.files:
           # print(request.files['image'])
 
            # data = open(request.files['file'], 'rb')
            # s3.Bucket('jonie1').put_object(Key="request.files['file']", Body=data)

        return render_template('index.html')
    elif request.method == "POST":
        return upload_file()


def upload_file():

	# A
    if "user_file" not in request.files:
        return "No user_file key in request.files"

	# B
    file = request.files["user_file"]

    """
        These attributes are also available

        file.filename               # The actual name of the file
        file.content_type
        file.content_length
        file.mimetype

    """

	# C.
    if file.filename == "":
        return "Please select a file"

	# D.
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output   	  = upload_file_to_s3(file, app.config["S3_BUCKET"])
        return str(output)

    else:
        return redirect("/")



if __name__ == "__main__":
    app.run()


