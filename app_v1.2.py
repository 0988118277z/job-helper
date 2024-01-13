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

@handler.add(UnfollowEvent)
def unfollow_event(event):
    user_id = "Ub2401597f9f5813e94c70b9bbb3cb5c6"
    line_bot_api.push_message(user_id, TextSendMessage(text='被封鎖了'))


@handler.add(MessageEvent, message=TextMessage)
def text_request(event):
    user_text = event.message.text
    if '天氣' in user_text:
        return_text = weather(user_text)
    elif '擲筊' in user_text:
        return_text = divinationBlocks()
    elif '抽' in user_text:
        return_text = drawStraws()
    elif '^' in user_text:
        return_text = update_job(user_text)
    elif '#' in user_text:
        return_text = job(user_text)
    elif '讚' in user_text:
        line_bot_api.reply_message(event.reply_token, StickerSendMessage(
                package_id = '11537',
                sticker_id = '52002735'
                ))
        return 0
            
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=return_text))  
    return 0


@handler.add(MessageEvent, message=ImageMessage)
def text_request(event):
    #image_url = ''
    #line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
    sendString = '這是圖片'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))
    
@handler.add(MessageEvent, message=VideoMessage)
def text_request(event):
    #video_url = ''
    #image_url = ''
    #line_bot_api.reply_message(event.reply_token, VideoSendMessage(original_content_url=video_url, preview_image_url=image_url))
    sendString = '這是影片'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))
    
@handler.add(MessageEvent, message=AudioMessage)
def text_request(event):
    #audio_url = ''
    #line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url=audio_url, duration = 60000))
    sendString = '這是聲音'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))
    
@handler.add(MessageEvent, message=LocationMessage)
def text_request(event):
    #line_bot_api.reply_message(event.reply_token, LocationSendMessage(title='名稱', address='地址', latitude=緯度, longitude=經度))
    sendString = '這是地址'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))
    
if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
