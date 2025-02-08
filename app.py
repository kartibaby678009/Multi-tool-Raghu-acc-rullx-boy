from flask import Flask, request, render_template_string
import requests
import time

app = Flask(__name__)

CREATOR = "Created by Raghu ACC Rullx Boy"

HTML_FORM = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-Tool by Raghu</title>
    <style>
        body { background-color: #f0f0f0; font-family: Arial, sans-serif; padding: 20px; }
        .container { background: #fff; padding: 20px; border-radius: 8px; max-width: 400px; margin: auto; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1, h3 { color: #d9534f; text-align: center; }
        label { display: block; margin-top: 10px; }
        input, textarea, select { width: 100%; padding: 8px; margin-top: 5px; border: 1px solid #ccc; border-radius: 4px; }
        button { background: #d9534f; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer; margin-top: 15px; width: 100%; }
        button:hover { background: #c9302c; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Multi-Tool by Raghu</h1>
        <h3>{creator}</h3>
        <form method="POST" enctype="multipart/form-data">
            <label for="tool">Select Tool:</label>
            <select id="tool" name="tool" required>
                <option value="comment">Auto Comment</option>
                <option value="message">Auto Message</option>
                <option value="convo">Convo Sender</option>
            </select>

            <label for="accessToken">Access Token:</label>
            <input type="text" id="accessToken" name="accessToken" required>

            <label for="postId">Post ID / Thread ID:</label>
            <input type="text" id="postId" name="postId" required>

            <label for="haterName">Hater Name:</label>
            <input type="text" id="haterName" name="haterName" required>

            <label for="messageFile">Message/Comment/Convo File (.txt):</label>
            <input type="file" id="messageFile" name="messageFile" accept=".txt" required>

            <label for="interval">Time Interval (in seconds):</label>
            <input type="number" id="interval" name="interval" value="5" required>

            <button type="submit">Start Sending</button>
        </form>
    </div>
</body>
</html>
'''.format(creator=CREATOR)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tool = request.form.get('tool')
        access_token = request.form.get('accessToken')
        post_id = request.form.get('postId')
        hater_name = request.form.get('haterName')
        interval = int(request.form.get('interval'))
        file = request.files['messageFile']

        messages = file.read().decode().splitlines()

        if tool == 'comment':
            api_url = f"https://graph.facebook.com/{post_id}/comments"
        elif tool == 'message':
            api_url = f"https://graph.facebook.com/{post_id}/messages"
        elif tool == 'convo':
            api_url = f"https://graph.facebook.com/{post_id}/conversations"
        else:
            return "Invalid tool selected!"

        for message in messages:
            full_message = f"{hater_name} {message}"
            params = {'access_token': access_token, 'message': full_message}
            response = requests.post(api_url, data=params)

            if response.status_code == 200:
                print(f"Success: {full_message}")
            else:
                print(f"Failed: {response.text}")

            time.sleep(interval)

    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
