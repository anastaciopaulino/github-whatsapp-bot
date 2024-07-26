import pytest
from app.notification_sender import NotificationSender
from unittest.mock import patch

@patch('app.notification_sender.requests.post')
def test_send_whatsapp_message(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.text = 'Success'
    
    sender = NotificationSender()
    response = sender.send_whatsapp_message("Test message")
    
    assert response.status_code == 200
    assert response.text == 'Success'
    mock_post.assert_called_once()
