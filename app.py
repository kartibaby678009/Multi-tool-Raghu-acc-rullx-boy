from flask import Flask, request
import requests
import time
import os

app = Flask(__name__)

# App Header
CREATOR = "Created by Raghu ACC Rullx Boy"

# Facebook API Headers
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

@app.route('/')
def home():
    return f"<h1>Welcome to Multi-Tool - {CREATOR}</h1><p>Go to /message for Auto Messaging or /comment for Auto Commenting.</p>"

# Auto Messaging Tool
@app.route('/message', methods=['POST'])
def send_message():
    data = request.json
    access_token = data.get('accessToken')
    thread_id = data.get('threadId')
    message = data.get('message')
    interval = int(data.get('interval', 5))  # Default interval is 5 seconds

    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
    parameters = {'access_token': access_token, 'message': message}

    try:
        while True:
            response = requests.post(api_url, data=parameters, headers=headers)
            if response.status_code == 200:
                print(f"Message sent: {message}")
            else:
                print(f"Failed to send message: {response.text}")
            time.sleep(interval)
    except Exception as e:
        return {"error": str(e)}
    
    return {"status": "Messaging Started!"}

# Auto Commenting Tool
@app.route('/comment', methods=['POST'])
def auto_comment():
    data = request.json
    access_token = data.get('accessToken')
    post_id = data.get('postId')
    comment = data.get('comment')
    interval = int(data.get('interval', 5))  # Default interval is 5 seconds

    api_url = f"https://graph.facebook.com/{post_id}/comments"
    parameters = {'access_token': access_token, 'message': comment}

    try:
        while True:
            response = requests.post(api_url, data=parameters, headers=headers)
            if response.status_code == 200:
                print(f"Comment posted: {comment}")
            else:
                print(f"Failed to post comment: {response.text}")
            time.sleep(interval)
    except Exception as e:
        return {"error": str(e)}
    
    return {"status": "Auto Commenting Started!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
