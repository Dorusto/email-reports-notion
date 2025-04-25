from dotenv import load_dotenv
import os
from notion_api import NotionAPI
from data_processor import DataProcessor
from email_sender import EmailSender

# Load environment variables
load_dotenv()

# Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Step 1: Fetch data from Notion
notion = NotionAPI(NOTION_API_KEY, NOTION_DATABASE_ID)
notion_data = notion.fetch_data()

# Step 2: Process the data
processor = DataProcessor()
processed_data = processor.process_data(notion_data)

# Step 3: Prepare email content
email_body = """Hello,

Here is your report:

"""
for item in processed_data:
    email_body += f"- {item['name']} (Date: {item['date']})\n"

email_body += "\nBest regards,\nYour Automation Script"

# Step 4: Send the email
email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, EMAIL_USERNAME, EMAIL_PASSWORD)
email_sender.send_email(RECIPIENT_EMAIL, "Your Report", email_body)

print("Email sent successfully!")