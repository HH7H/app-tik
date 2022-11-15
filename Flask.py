from Naked.toolshed.shell import muterun_js
import requests,json,os.path
from flask import Flask,request
import random
import string

app = Flask(__name__)

@app.route('/',methods=['GET'])
def Root():
    return 'Hello from Flask'
    

@app.route('/api/tiktok/sign-request/',methods=['POST'])
def Api():
    url = str(request.form['url'])
    XApiKey = str(request.form['X-Api-Key'])
    if XApiKey == 'Pass@api':
        response = muterun_js(' '.join([os.path.abspath('browser.js'), "\""+url+"\""]))
        return response
    else:
        return json.dump({"status": "error", "error_type": "incorrect password"})
        

        
        
        
        