from __future__ import unicode_literals
from flask import Flask, request, abort, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage, StickerSendMessage
from linebot.models import TextMessage, ImageMessage, VideoMessage, AudioMessage, LocationMessage
from linebot.models import MessageEvent, FollowEvent, UnfollowEvent, JoinEvent
#import random, requests, os, re, mysql.connector
from config import channel_access_token, channel_secret
from linedestiny import drawStraws, divinationBlocks
from lineweather import weather, setweather
from linejob import job, update_job

app = Flask(__name__)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        print(body, signature)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# HTTP API
@app.route("/webapi", methods=['GET'])
def api():
    keyword = request.args.get("keyword")
    return jsonify(job(keyword,api=True))

@handler.add(JoinEvent)
def join_event(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='歡迎加我入群'))

@handler.add(FollowEvent)
def follow_event(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='歡迎加我好友'))


@handler.add(MessageEvent, message=TextMessage)
def text_request(event):
    user_text = event.message.text
    if '^' in user_text:
        return_text = update_job(user_text)
    elif '#' in user_text:
        return_text = job(user_text)
 
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=return_text))  

if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
