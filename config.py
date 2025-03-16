import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")

# Admin Credentials
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")  # Default Admin Username
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "your_admin_password")  # Default Admin Password

# Database File (SQLite)
DB_FILE = os.getenv("DB_FILE", "admin.db")

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_telegram_bot_token")

# API Keys
FIVESIM_API_KEY = os.getenv("FIVESIM_API_KEY", "your_fivesim_api_key")  # 5Sim API Key
SMSACTIVATE_API_KEY = os.getenv("SMSACTIVATE_API_KEY", "your_smsactivate_api_key")  # Alternative API Key

# Payment Gateway (Razorpay & BharatPe)
RAZORPAY_KEY = os.getenv("RAZORPAY_KEY", "your_razorpay_key")
RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET", "your_razorpay_secret")
BHARATPE_WEBHOOK_SECRET = os.getenv("BHARATPE_WEBHOOK_SECRET", "your_bharatpe_webhook_secret")

# Webhook URLs
BOT_WEBHOOK_URL = os.getenv("BOT_WEBHOOK_URL", "https://your-bot-webhook-url.com")
BHARATPE_WEBHOOK_URL = os.getenv("BHARATPE_WEBHOOK_URL", "https://your-bharatpe-webhook-url.com")
