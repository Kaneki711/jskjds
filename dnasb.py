# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

dee = LINE("EseCbkPVnm7ecMcVV2o6.7kqscP17dKQEF08Bg5AKnG.Df385DZh1hANY8s+tgpIvXyuLMgFQmUBel7Yxc7527E=")
#dee = LINE("TOKEN KAMU")
#dee = LINE("Email","Password")
dee.log("Auth Token : " + str(dee.authToken))
channelToken = dee.getChannelResult()
dee.log("Channel Token : " + str(channelToken))

deeMID = dee.profile.mid
deeProfile = dee.getProfile()
lineSettings = dee.getSettings()
oepoll = OEPoll(dee)
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)


myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = deeProfile.displayName
myProfile["statusMessage"] = deeProfile.statusMessage
myProfile["pictureStatus"] = deeProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
    
def logError(text):
    dee.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        dee.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "╔════════════════════╗" + "\n" + \
                  "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                  "╚════════════════════╝" + "\n" + \
                  "╔════════════════════╗" + "\n" + \
                  "                  ◄]·✪·Help·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Help" + "\n" + \
                  "╠❂➣ Translate" + "\n" + \
                  "╠❂➣ Texttospeech" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                ◄]·✪·Status·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Restart" + "\n" + \
                  "╠❂➣ Runtime" + "\n" + \
                  "╠❂➣ Speed" + "\n" + \
                  "╠❂➣ Status" + "\n" + \
                  "╠❂➣ About" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "              ◄]·✪·Settings·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ AutoAdd「On/Off」" + "\n" + \
                  "╠❂➣ AutoJoin「On/Off」" + "\n" + \
                  "╠❂➣ AutoLeave「On/Off」" + "\n" + \
                  "╠❂➣ AutoRead「On/Off」" + "\n" + \
                  "╠❂➣ CheckSticker「On/Off」" + "\n" + \
                  "╠❂➣ DetectMention「On/Off」" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                  ◄]·✪·Self·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Me" + "\n" + \
                  "╠❂➣ MyMid" + "\n" + \
                  "╠❂➣ MyName" + "\n" + \
                  "╠❂➣ MyBio" + "\n" + \
                  "╠❂➣ MyPicture" + "\n" + \
                  "╠❂➣ MyVideoProfile" + "\n" + \
                  "╠❂➣ MyCover" + "\n" + \
                  "╠❂➣ StealContact「Mention」" + "\n" + \
                  "╠❂➣ StealMid「Mention」" + "\n" + \
                  "╠❂➣ StealName「Mention」" + "\n" + \
                  "╠❂➣ StealBio「Mention」" + "\n" + \
                  "╠❂➣ StealPicture「Mention」" + "\n" + \
                  "╠❂➣ StealVideoProfile「Mention」" + "\n" + \
                  "╠❂➣ StealCover「Mention」" + "\n" + \
                  "╠❂➣ CloneProfile「Mention」" + "\n" + \
                  "╠❂➣ RestoreProfile" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                 ◄]·✪·Group·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ GroupCreator" + "\n" + \
                  "╠❂➣ GroupId" + "\n" + \
                  "╠❂➣ GroupName" + "\n" + \
                  "╠❂➣ GroupPicture" + "\n" + \
                  "╠❂➣ GroupTicket" + "\n" + \
                  "╠❂➣ GroupTicket「On/Off」" + "\n" + \
                  "╠❂➣ GroupList" + "\n" + \
                  "╠❂➣ GroupMemberList" + "\n" + \
                  "╠❂➣ GroupInfo" + "\n" + \
                  "╠❂➣ Kill「Mention」" + "\n" + \
                  "╠❂➣ KickAllMember" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                ◄]·✪·Special·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Mimic「On/Off」" + "\n" + \
                  "╠❂➣ MimicList" + "\n" + \
                  "╠❂➣ MimicAdd「Mention」" + "\n" + \
                  "╠❂➣ MimicDel「Mention」" + "\n" + \
                  "╠❂➣ Mention" + "\n" + \
                  "╠❂➣ Lurking「Oɴ/Off/Reset」" + "\n" + \
                  "╠❂➣ Lurking" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                ◄]·✪·Media·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Kalender" + "\n" + \
                  "╠❂➣ CheckDate「Date」" + "\n" + \
                  "╠❂➣ InstagramInfo「UserName」" + "\n" + \
                  "╠❂➣ InstagramPost「UserName」" + "\n" + \
                  "╠❂➣ SearchYoutube「Search」" + "\n" + \
                  "╠❂➣ SearchMusic「Search」" + "\n" + \
                  "╠❂➣ SearchLyric「Search」" + "\n" + \
                  "╠❂➣ SearchImage「Search」" + "\n" + \
                  "╠❂➣ ScreenshootWebsite「LinkUrl」" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "              Credits by : ©D̶e̶e̶ ✯" + "\n" + \
                  "╚════════════════════╝" + "\n" + \
                  "╔════════════════════╗" + "\n" + \
                  "                   ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                  "╚════════════════════╝"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "╔════════════════════╗" + "\n" + \
                         "               ✯ T̶e̶x̶t̶t̶o̶s̶p̶e̶e̶c̶h̶ ✯" + "\n" + \
                         "╠════════════════════╝" + "\n" + \
                         "╠❂➣ ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                         "╠❂➣ ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                         "╠❂➣ ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                         "╠❂➣ ᴢʜ : ᴄʜɪɴᴇsᴇ" + "\n" + \
                         "╠❂➣ ᴢʜ-ᴄɴ : ᴄʜɪɴᴇsᴇ (sɪᴍᴘʟɪғɪᴇᴅ)" + "\n" + \
                         "╠❂➣ ᴢʜ-ᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴛʀᴀᴅɪᴛɪᴏɴᴀʟ)" + "\n" + \
                         "╠❂➣ ᴢʜ-ʏᴜᴇ : ᴄʜɪɴᴇsᴇ ((ᴄᴀɴᴛᴏɴᴇsᴇ))" + "\n" + \
                         "╠❂➣ ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                         "╠❂➣ ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                         "╠❂➣ ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                         "╠❂➣ ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                         "╠❂➣ ᴇɴ-ᴀᴜ : ᴇɴɢʟɪsʜ (ᴀᴜsᴛʀᴀʟɪᴀ)" + "\ɴ" + \
                         "╠❂➣ ᴇɴ-ᴜᴋ : ᴇɴɢʟɪsʜ (ᴜɴɪᴛᴇᴅ ᴋɪɴɢᴅᴏᴍ)" + "\ɴ" + \
                         "╠❂➣ ᴇɴ-ᴜs : ᴇɴɢʟɪsʜ (ᴜɴɪᴛᴇᴅ sᴛᴀᴛᴇs)" + "\n" + \
                         "╠❂➣ ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                         "╠❂➣ ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                         "╠❂➣ ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                         "╠❂➣ ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                         "╠❂➣ ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                         "╠❂➣ ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                         "╠❂➣ ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                         "╠❂➣ ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                         "╠❂➣ ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                         "╠❂➣ ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                         "╠❂➣ ᴋᴍ : ᴋʜᴍᴇʀ" + "\n" + \
                         "╠❂➣ ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                         "╠❂➣ ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                         "╠❂➣ ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                         "╠❂➣ ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                         "╠❂➣ ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                         "╠❂➣ sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                         "╠❂➣ sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                         "╠❂➣ sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                         "╠❂➣ ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                         "╠❂➣ ᴇs : sᴘᴀɴɪsʜ(sᴘᴀɪɴ)" + "\n" + \
                         "╠❂➣ ᴇs : sᴘᴀɴɪsʜ(ᴜɴɪᴛᴇᴅ sᴛᴀᴛᴇs)" + "\n" + \
                         "╠❂➣ sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                         "╠❂➣ sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                         "╠❂➣ ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                         "╠❂➣ ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                         "╠❂➣ ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                         "╠❂➣ ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                         "╠❂➣ ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                         "╠════════════════════╗" + "\n" + \
                         "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                         "      ᴄᴏɴᴛᴏʜ : sᴀʏ-ɪᴅ ʀɪʀɪɴ ᴄᴀɴᴛɪᴋ" + "\n" + \
                         "╚════════════════════╝"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╔════════════════════╗" + "\n" + \
                         "                   ✯ T̶r̶a̶n̶s̶l̶a̶t̶e̶ ✯" + "\n" + \
                         "╠════════════════════╝" + "\n" + \
                         "╠❂➣ ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                         "╠❂➣ sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴀᴍ : ᴀᴍʜᴀʀɪᴄ" + "\n" + \
                         "╠❂➣ ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                         "╠❂➣ ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴀᴢ : ᴀᴢᴇʀʙᴀɪᴊᴀɴɪ" + "\n" + \
                         "╠❂➣ ᴇᴜ : ʙᴀsǫᴜᴇ" + "\n" + \
                         "╠❂➣ ʙᴇ : ʙᴇʟᴀʀᴜsɪᴀɴ" + "\n" + \
                         "╠❂➣ ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                         "╠❂➣ ʙs : ʙᴏsɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ʙɢ : ʙᴜʟɢᴀʀɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                         "╠❂➣ ᴄᴇʙ : ᴄᴇʙᴜᴀɴᴏ" + "\n" + \
                         "╠❂➣ ɴʏ : ᴄʜɪᴄʜᴇᴡᴀ" + "\n" + \
                         "╠❂➣ ᴢʜ-ᴄɴ : ᴄʜɪɴᴇsᴇ (sɪᴍᴘʟɪғɪᴇᴅ)" + "\n" + \
                         "╠❂➣ ᴢʜ-ᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴛʀᴀᴅɪᴛɪᴏɴᴀʟ)" + "\n" + \
                         "╠❂➣ ᴄᴏ : ᴄᴏʀsɪᴄᴀɴ" + "\n" + \
                         "╠❂➣ ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                         "╠❂➣ ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                         "╠❂➣ ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                         "╠❂➣ ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                         "╠❂➣ ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                         "╠❂➣ ᴇᴛ : ᴇsᴛᴏɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴛʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                         "╠❂➣ ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                         "╠❂➣ ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                         "╠❂➣ ғʏ : ғʀɪsɪᴀɴ" + "\n" + \
                         "╠❂➣ ɢʟ : ɢᴀʟɪᴄɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴋᴀ : ɢᴇᴏʀɢɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                         "╠❂➣ ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                         "╠❂➣ ɢᴜ : ɢᴜᴊᴀʀᴀᴛɪ" + "\n" + \
                         "╠❂➣ ʜᴛ : ʜᴀɪᴛɪᴀɴ ᴄʀᴇᴏʟᴇ" + "\n" + \
                         "╠❂➣ ʜᴀ : ʜᴀᴜsᴀ" + "\n" + \
                         "╠❂➣ ʜᴀᴡ : ʜᴀᴡᴀɪɪᴀɴ" + "\n" + \
                         "╠❂➣ ɪᴡ : ʜᴇʙʀᴇᴡ" + "\n" + \
                         "╠❂➣ ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                         "╠❂➣ ʜᴍɴ : ʜᴍᴏɴɢ" + "\n" + \
                         "╠❂➣ ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                         "╠❂➣ ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                         "╠❂➣ ɪɢ : ɪɢʙᴏ" + "\n" + \
                         "╠❂➣ ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                         "╠❂➣ ɢᴀ : ɪʀɪsʜ" + "\n" + \
                         "╠❂➣ ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                         "╠❂➣ ᴊᴡ : ᴊᴀᴠᴀɴᴇsᴇ" + "\n" + \
                         "╠❂➣ ᴋɴ : ᴋᴀɴɴᴀᴅᴀ" + "\n" + \
                         "╠❂➣ ᴋᴋ : ᴋᴀᴢᴀᴋʜ" + "\n" + \
                         "╠❂➣ ᴋᴍ : ᴋʜᴍᴇʀ" + "\n" + \
                         "╠❂➣ ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                         "╠❂➣ ᴋᴜ : ᴋᴜʀᴅɪsʜ (ᴋᴜʀᴍᴀɴᴊɪ)" + "\n" + \
                         "╠❂➣ ᴋʏ : ᴋʏʀɢʏᴢ" + "\n" + \
                         "╠❂➣ ʟᴏ : ʟᴀᴏ" + "\n" + \
                         "╠❂➣ ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                         "╠❂➣ ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                         "╠❂➣ ʟᴛ : ʟɪᴛʜᴜᴀɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ʟʙ : ʟᴜxᴇᴍʙᴏᴜʀɢɪsʜ" + "\n" + \
                         "╠❂➣ ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴍɢ : ᴍᴀʟᴀɢᴀsʏ" + "\n" + \
                         "╠❂➣ ᴍs : ᴍᴀʟᴀʏ" + "\n" + \
                         "╠❂➣ ᴍʟ : ᴍᴀʟᴀʏᴀʟᴀᴍ" + "\n" + \
                         "╠❂➣ ᴍᴛ : ᴍᴀʟᴛᴇsᴇ" + "\n" + \
                         "╠❂➣ ᴍɪ : ᴍᴀᴏʀɪ" + "\n" + \
                         "╠❂➣ ᴍʀ : ᴍᴀʀᴀᴛʜɪ" + "\n" + \
                         "╠❂➣ ᴍɴ : ᴍᴏɴɢᴏʟɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴍʏ : ᴍʏᴀɴᴍᴀʀ (ʙᴜʀᴍᴇsᴇ)" + "\n" + \
                         "╠❂➣ ɴᴇ : ɴᴇᴘᴀʟɪ" + "\n" + \
                         "╠❂➣ ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴘs : ᴘᴀsʜᴛᴏ" + "\n" + \
                         "╠❂➣ ғᴀ : ᴘᴇʀsɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                         "╠❂➣ ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                         "╠❂➣ ᴘᴀ : ᴘᴜɴᴊᴀʙɪ" + "\n" + \
                         "╠❂➣ ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                         "╠❂➣ sᴍ : sᴀᴍᴏᴀɴ" + "\n" + \
                         "╠❂➣ ɢᴅ : sᴄᴏᴛs ɢᴀᴇʟɪᴄ" + "\n" + \
                         "╠❂➣ sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                         "╠❂➣ sᴛ : sᴇsᴏᴛʜᴏ" + "\n" + \
                         "╠❂➣ sɴ : sʜᴏɴᴀ" + "\n" + \
                         "╠❂➣ sᴅ : sɪɴᴅʜɪ" + "\n" + \
                         "╠❂➣ sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                         "╠❂➣ sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                         "╠❂➣ sʟ : sʟᴏᴠᴇɴɪᴀɴ" + "\n" + \
                         "╠❂➣ sᴏ : sᴏᴍᴀʟɪ" + "\n" + \
                         "╠❂➣ ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                         "╠❂➣ sᴜ : sᴜɴᴅᴀɴᴇsᴇ" + "\n" + \
                         "╠❂➣ sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                         "╠❂➣ sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                         "╠❂➣ ᴛɢ : ᴛᴀᴊɪᴋ" + "\n" + \
                         "╠❂➣ ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                         "╠❂➣ ᴛᴇ : ᴛᴇʟᴜɢᴜ" + "\n" + \
                         "╠❂➣ ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                         "╠❂➣ ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                         "╠❂➣ ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                         "╠❂➣ ᴜʀ : ᴜʀᴅᴜ" + "\n" + \
                         "╠❂➣ ᴜᴢ : ᴜᴢʙᴇᴋ" + "\n" + \
                         "╠❂➣ ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                         "╠❂➣ ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                         "╠❂➣ xʜ : xʜᴏsᴀ" + "\n" + \
                         "╠❂➣ ʏɪ : ʏɪᴅᴅɪsʜ" + "\n" + \
                         "╠❂➣ ʏᴏ : ʏᴏʀᴜʙᴀ" + "\n" + \
                         "╠❂➣ ᴢᴜ : ᴢᴜʟᴜ" + "\n" + \
                         "╠❂➣ ғɪʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                         "╠❂➣ ʜᴇ : ʜᴇʙʀᴇᴡ" + "\n" + \
                         "╠════════════════════╗" + "\n" + \
                         "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                         "       ᴄᴏɴᴛᴏʜ : ᴛʀ-ɪᴅ ʀɪʀɪɴ ᴄᴀɴᴛɪᴋ" + "\n" + \
                         "╚════════════════════╝"
    return helpTranslate
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] Succes")
            return
        if op.type == 5:
            print ("[ 5 ] ADD CONTACT")
            if settings["autoAdd"] == True:
                dee.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(dee.getContact(op.param1).displayName)))
        if op.type == 13:
            print ("[ 13 ] INVITE GROUP")
            group = dee.getGroup(op.param1)
            if settings["autoJoin"] == True:
                dee.acceptGroupInvitation(op.param1)
        if op.type == 17:
        	dan = dee.getContact(op.param2)
        	tgb = dee.getGroup(op.param1)
        	dee.sendMessage(op.param1, "Hai {}, Selamat datang di grup {}\nJangan Lupa Check Note ya\nAwas kalau Baper😘😘😘".format(str(dan.displayName),str(tgb.name)))
        	dee.sendContact(op.param1, op.param2)
        	dee.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))                          
        if op.type == 24:
            print ("[ 24 ] LEAVE ROOM")
            if settings["autoLeave"] == True:
                dee.leaveRoom(op.param1)
        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != dee.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    dee.sendMessage(to, str(helpMessage))
                    dee.sendContact(to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
                elif text.lower() == 'texttospeech':
                    helpTextToSpeech = helptexttospeech()
                    dee.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'translate':
                    helpTranslate = helptranslate()
                    dee.sendMessage(to, str(helpTranslate))
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    dee.sendMessage(to, "Waiting....")
                    elapsed_time = time.time() - start
                    dee.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':
                    dee.sendMessage(to, "Restarting")
                    time.sleep(5)
                    dee.sendMessage(to, "Restart Sukses")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    dee.sendMessage(to, "Running in {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "ueca4120a9d7b0e4a9e7f4f1b1b96a436"
                        creator = dee.getContact(owner)
                        contact = dee.getContact(deeMID)
                        grouplist = dee.getGroupIdsJoined()
                        contactlist = dee.getAllContactIds()
                        blockedlist = dee.getBlockedContactIds()
                        ret_ = "╔══[ About Self ]"
                        ret_ += "\n╠❂➣ Line : {}".format(contact.displayName)
                        ret_ += "\n╠❂➣ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠❂➣ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠❂➣ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠❂➣══[ About Selfbot ]"
                        ret_ += "\n╠❂➣ Version : Beta Test"
                        ret_ += "\n╠❂➣ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚══[ Don't be Remake :P ]"
                        dee.sendMessage(to, str(ret_))
                    except Exception as e:
                        dee.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╔══[ Status ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠❂➣ Auto Add ✅"
                        else: ret_ += "\n╠❂➣ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠❂➣ Auto Join ✅"
                        else: ret_ += "\n╠❂➣ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠❂➣ Auto Leave ✅"
                        else: ret_ += "\n╠❂➣ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠❂➣ Auto Read ✅"
                        else: ret_ += "\n╠❂➣ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠❂➣ Check Sticker ✅"
                        else: ret_ += "\n╠❂➣ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠❂➣ Detect Mention ✅"
                        else: ret_ += "\n╠❂➣ Detect Mention ❌"
                        ret_ += "\n╚══[ Status ]"
                        dee.sendMessage(to, str(ret_))
                    except Exception as e:
                        dee.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    dee.sendMessage(to, "Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    dee.sendMessage(to, "Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    dee.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    dee.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    dee.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'autojoin off':
                    settings["autoLeave"] = False
                    dee.sendMessage(to, "Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    dee.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    dee.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    dee.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    dee.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    dee.sendMessage(to, "Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    dee.sendMessage(to, "Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'clonecontact':
                    settings["copy"] = True
                    dee.sendMessage(to, "Send Contact")
#==============================================================================#
                elif text.lower() == 'me':
                    sendMessageWithMention(to, deeMID)
                    dee.sendContact(to, deeMID)
                elif text.lower() == 'mymid':
                    dee.sendMessage(msg.to,"[MID]\n" +  deeMID)
                elif text.lower() == 'myname':
                    me = dee.getContact(deeMID)
                    dee.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = dee.getContact(deeMID)
                    dee.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = dee.getContact(deeMID)
                    dee.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = dee.getContact(deeMID)
                    dee.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = dee.getContact(deeMID)
                    cover = dee.getProfileCoverURL(deeMID)    
                    dee.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = dee.getContact(ls)
                            mi_d = contact.mid
                            dee.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("stealmid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        dee.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = dee.getContact(ls)
                            dee.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = dee.getContact(ls)
                            dee.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.dee.naver.jp/" + dee.getContact(ls).pictureStatus
                            dee.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.dee.naver.jp/" + dee.getContact(ls).pictureStatus + "/vp"
                            dee.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = dee.getProfileCoverURL(ls)
                                dee.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            dee.cloneContactProfile(contact)
                            dee.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            dee.sendMessage(msg.to, "Gagal clone member")
                            
                elif text.lower() == 'restoreprofile':
                    try:
                        deeProfile.displayName = str(myProfile["displayName"])
                        deeProfile.statusMessage = str(myProfile["statusMessage"])
                        deeProfile.pictureStatus = str(myProfile["pictureStatus"])
                        dee.updateProfileAttribute(8, deeProfile.pictureStatus)
                        dee.updateProfile(deeProfile)
                        dee.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        dee.sendMessage(msg.to, "Gagal restore profile")
                        
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            dee.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            dee.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            dee.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            dee.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        nadya.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠❂➣ "+dee.getContact(mi_d).displayName
                        dee.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            dee.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            dee.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = dee.getGroup(to)
                    GS = group.creator.mid
                    dee.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = dee.getGroup(to)
                    dee.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = dee.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    dee.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = dee.getGroup(to)
                    dee.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                    if msg.toType == 2:
                        group = dee.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = dee.reissueGroupTicket(to)
                            dee.sendMessage(to, "[ Group Ticket ]\nhttps://dee.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            dee.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'groupticket on':
                    if msg.toType == 2:
                        group = dee.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            dee.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            dee.updateGroup(group)
                            dee.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'groupticket off':
                    if msg.toType == 2:
                        group = dee.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            dee.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            dee.updateGroup(group)
                            dee.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = dee.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://dee.me/R/ti/g/{}".format(str(dee.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠❂➣ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠❂➣ ID Group : {}".format(group.id)
                    ret_ += "\n╠❂➣ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠❂➣ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠❂➣ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠❂➣ Group Qr : {}".format(gQr)
                    ret_ += "\n╠❂➣ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    dee.sendMessage(to, str(ret_))
                    dee.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = dee.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠❂➣ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        dee.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = dee.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = dee.getGroup(gid)
                            ret_ += "\n╠❂➣ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        dee.sendMessage(to, str(ret_))
#==============================================================================#          
                elif text.lower() == 'mention':
                    group = dee.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        dee.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        dee.sendMessage(to, "Total {} Mention".format(str(len(nama))))          
                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                dee.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            dee.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        dee.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        dee.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        dee.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        dee.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            dee.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = dee.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            dee.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        dee.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    dee.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    dee.sendMessage(msg.to, A)
#==============================================================================#   
                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    dee.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        dee.sendImageWithURL(to, data["result"])
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠❂➣ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠❂➣ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠❂➣ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠❂➣ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    dee.sendMessage(to, str(ret_))
                elif "instagraminfo" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠❂➣ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠❂➣ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠❂➣ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠❂➣ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠❂➣ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠❂➣ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠❂➣ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠❂➣ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠❂➣ Akun Pribadi : Tidak"
                            ret_ += "\n╠❂➣ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            dee.sendImageWithURL(to, str(path))
                            dee.sendMessage(to, str(ret_))
                        except:
                            dee.sendMessage(to, "Pengguna tidak ditemukan")
                elif "instagrampost" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1, 999):
                            print('PAGE: ', count)
                            r = x.get(profile, params={'max_id': end_cursor})
                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)
                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                if node['is_video']:
                                    page = 'https://www.instagram.com/p/' + node['code']
                                    r = x.get(page)
                                    url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                    print(url)
                                    dee.sendVideoWithURL(msg.to,url)
                                else:
                                    print (node['display_src'])
                                    dee.sendImageWithURL(msg.to,node['display_src'])
                            end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                elif "searchimage" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            dee.sendImageWithURL(to, str(path))
                elif "searchyoutube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠❂➣[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠❂➣ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        dee.sendMessage(to, str(ret_))
                elif "music" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                ret_ = "╔══[ Music ]"
                                ret_ += "\n╠❂➣ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠❂➣ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠❂➣ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ reading Audio ]"
                                dee.sendMessage(to, str(ret_))
                                dee.sendAudioWithURL(to, song[3])
                        except:
                            dee.sendMessage(to, "Musik tidak ditemukan")
                elif "smule " in msg.text.lower():
                    tob = msg.text.lower().replace("smule ","")
                    dee.sendText(msg.to,"Sedang Mencari...")
                    dee.sendText(msg.to,"Title : "+tob+"\nSource : Smule\nLink : https://www.smule.com/search?q=" + tob)
                    dee.sendText(msg.to,"Tuh Linknya Kak (^_^)")
                elif "lyric" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                songs = song[5]
                                lyric = songs.replace('ti:','Title - ')
                                lyric = lyric.replace('ar:','Artist - ')
                                lyric = lyric.replace('al:','Album - ')
                                removeString = "[1234567890.:]"
                                for char in removeString:
                                    lyric = lyric.replace(char,'')
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠❂➣ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠❂➣ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠❂➣ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                dee.sendMessage(to, str(ret_))
                        except:
                            dee.sendMessage(to, "Lirik tidak ditemukan")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠❂➣ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠❂➣ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠❂➣ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠❂➣ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    dee.sendMessage(to, str(ret_))
                    
            elif msg.contentType == 13:
                if settings["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = dee.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Copy")
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        dee.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                dee.cloneContactProfile(target)
                                dee.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                settings['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     settings["copy"] = False
                                     break                     
                    
                    
#==============================================================================#
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != dee.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    dee.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        dee.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in deeMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if deeMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = dee.getContact(sender)
                                    dee.sendMessage(to, "sundala nu")
                                    sendMessageWithMention(to, contact.mid)
                                break
#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
