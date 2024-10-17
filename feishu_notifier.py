import argparse
import os

import requests


def send_message(url, user_id):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "GitHub Action 自动推送",
                    "content": [
                        [{
                            "tag": "text",
                            "text": "你好 "
                        }, {
                            "tag": "at",
                            "user_id": user_id
                        }],
                        [{
                            "tag": "text",
                            "text": "我们的每日推送与团队研究相关的ArXiv最新论文机器人："
                        }, {
                            "tag": "a",
                            "text": "ArXiv Radar",
                            "href": "https://github.com/IAAR-Shanghai/ArxivBot"
                        }, {
                            "tag": "text",
                            "text": " 正在开发中"
                        }]
                    ]
                }
            }
        }
    }
    print("Sending message to Feishu...")
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        print(f"Message sent successfully: {response.status_code}")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a message using Feishu bot webhook")
    parser.add_argument("--url", required=False, help="Webhook URL")
    parser.add_argument("--user_id", required=False, help="User ID to mention")
    args = parser.parse_args()

    # Use GitHub Action secrets if not provided via arguments
    url = args.url or os.getenv("WEBHOOK_URL")
    user_id = args.user_id or os.getenv("USER_ID")

    if not url or not user_id:
        raise ValueError("Both webhook URL and user ID must be provided either as arguments or as environment variables.")

    send_message(url, user_id)
