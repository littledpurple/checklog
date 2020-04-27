#!/bin/bash

cd /root/checklog/
python checklog.py > msg.txt

API="xxxxxxx" # Telegram bot API
chat="xxxxxxxx" # Telegram chat ID

[ ! -f "msg.txt" ] && { echo "Error: $0 file not found."; exit 2; }

if [ -s "msg.txt" ]
then
        message=`cat msg.txt`
        message="rsyslog report
${message}"
        curl -F $"text="$'\U0001F514'" $message" -F "parse_mode=html" "https://api.telegram.org/bot$API/sendMessage?chat_id=$chat"
fi

rm msg.txt
