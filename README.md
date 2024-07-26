# WhatsApp GitHub Notification Bot

This project is a Python bot that sends notifications via WhatsApp whenever there are changes to a GitHub repository, including commits, pushes, and new issues.

## Features

- **Push Notifications:** Sends a message when there is a new commit in the repository.
- **Issue Notifications:** Sends a message when a new issue is created in the repository.

## Requirements

- Python 3.7 or higher
- [Twilio](https://www.twilio.com/) account for sending WhatsApp messages
- [GitHub](https://github.com/) account to set up webhooks

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/whatsapp-bot.git
    cd whatsapp-bot

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Configure environment variables:**
Create a .env file in the root directory of the project with the following content:
    ```bash
    TWILIO_AUTH_TOKEN=YOUR_TWILIO_AUTH_TOKEN
    TWILIO_ACCOUNT_SID=YOUR_TWILIO_ACCOUNT_SID
    WHATSAPP_FROM=whatsapp:YOUR_TWILIO_WHATSAPP_NUMBER
    WHATSAPP_TO=whatsapp:YOUR_PHONE_NUMBER

Replace YOUR_TWILIO_AUTH_TOKEN, YOUR_TWILIO_ACCOUNT_SID,YOUR_TWILIO_WHATSAPP_NUMBER, and YOUR_PHONE_NUMBER with your Twilio credentials.

5. **Start the Flask server:**
    ```bash
    python run.py

## Configure GitHub Webhook

1. Go to your repository on **GitHub**.
2. Navigate to **Settings > Webhooks > Add webhook**.
3. In the **Payload URL field**, enter the URL where your bot is running (e.g., http://yourdomain.com/webhook).
4. Under Content type, select **application/json**.
5. Choose the events you want to monitor, such as Pushes and Issues.
Click Add webhook.

## Testing
To run the unit tests, use:
    ```bash
    pytest
   
Tests are located in the tests/ directory and cover the main functionalities of the bot.

## Contributing

Feel free to contribute to this project. To do so:

  1. Fork the repository.
  2. Create a new branch (git checkout -b my-feature).
  3. Make your changes and test.
  4. Submit a pull request to the main branch.

## License
This project is licensed under the MIT License.


