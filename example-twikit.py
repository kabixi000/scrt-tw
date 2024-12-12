import dotenv
import os
import asyncio
from twikit import Client

# ユーザー名とパスワードを環境変数から取得
dotenv.load_dotenv()
USERNAME = os.environ.get('TWITTER_USERNAME', 'your_username')
PASSWORD = os.environ.get('TWITTER_PASSWORD', 'your_password')
EMAIL = os.environ.get('TWITTER_EMAIL', 'your_email')

print('username:', USERNAME)

# Initialize client
client = Client('en-US')

async def main():
    # アカウントにログイン
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

asyncio.run(main())
