from flask import Flask, request, jsonify
from .notification_sender import NotificationSender

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    
    notification_sender = NotificationSender()
    
    if event_type == 'push':
        message = f"New push to the repository:\n\n{data['repository']['name']}\nCommits: {data['commits'][0]['message']}"
    elif event_type == 'issues':
        message = f"New issue created:\n\n{data['issue']['title']}\n{data['issue']['body']}"
    else:
        message = f"Received event: {event_type}"
    
    notification_sender.send_whatsapp_message(message)
    return jsonify({'status': 'success'})
