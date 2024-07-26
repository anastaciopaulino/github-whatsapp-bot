import pytest
from app.webhook_listener import app
from flask import json
from unittest.mock import patch

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@patch('app.webhook_listener.NotificationSender.send_whatsapp_message')
def test_webhook_push_event(mock_send_whatsapp_message, client):
    mock_send_whatsapp_message.return_value = None
    
    payload = {
        "repository": {"name": "test-repo"},
        "commits": [{"message": "Test commit"}]
    }
    
    response = client.post('/webhook', 
                           data=json.dumps(payload),
                           content_type='application/json',
                           headers={'X-GitHub-Event': 'push'})
    
    assert response.status_code == 200
    mock_send_whatsapp_message.assert_called_once_with(
        "New push to the repository:\n\n"
        "test-repo\n"
        "Commits: Test commit"
    )
