# -*- coding: utf-8 -*-

from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import time,random,sys,json,codecs,threading,glob,re,os,subprocess
from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
import requests
import datetime
import requests,urllib,json


#Khusus Login Qr
#ririn = LINE()
#ririn.log("Auth Token : " + str(ririn.authToken))
#ririn.log("Timeline Token : " + str(ririn.tl.channelAccessToken))

#Khusus Login Token (Chrome)
ririn = LINE('Es8F9rvfe5qWM1OyBUKd.UC8K+GXOvK/3A1WWSKmQRq.Ks5f57uNaBJYk8ZYbbM5KSJahM913pRZJI7AoATs9pQ=')
ririn.log("Auth Token : " + str(ririn.authToken))
ririn.log("Timeline Token : " + str(ririn.tl.channelAccessToken))

dna1 = LINE('Esn9u0ubtOSNbrvmZRj2.We7lj7PxgwBQ8O07ppSHuG.yZgTUBb0XWQeIuEeEcOTxrVcnWfEXOKs0ecytY8Ungk=')
dna1.log("Auth Token : " + str(dna1.authToken))
dna1.log("Timeline Token : " + str(dna1.tl.channelAccessToken))

dna2 = LINE('EswPaA5BOBJTsJYOn671.Sl2u8yHwWYZHMslzI9Bi8q.20nDyP69BtbKbjSH0g+Az8JIhjkvKDyF5cnu+TLbWJc=')
dna2.log("Auth Token : " + str(dna2.authToken))
dna2.log("Timeline Token : " + str(dna2.tl.channelAccessToken))

dna3 = LINE('EsEKNt02EJOcnTi6Xzx8.M53qiD/PJ1i6qsVfYwB7Ea.NaLIAwjUUJL6CgB0EDUFAPFuGYBt1Tfnu+Di90xex+w=')
dna3.log("Auth Token : " + str(dna3.authToken))
dna3.log("Timeline Token : " + str(dna3.tl.channelAccessToken))

dna4 = LINE('EsW1g9iNsbBlMKijNfg3.LTjIccO9HW0I2OLJ9e3wmW.mvP+mX2apHj/j8NBNUX/V2mNidEVhpOwAGUyCcNSSDI=')
dna4.log("Auth Token : " + str(dna4.authToken))
dna4.log("Timeline Token : " + str(dna4.tl.channelAccessToken))

dna5 = LINE('EsuIBccvd1yt4fKYcMua.i4cphH9h9VMs4DyAsZSSsG.6dh1FLhE4KKi6AS/yTbG5hYIAd2ZEn5SW2gaOUenUTs=')
dna5.log("Auth Token : " + str(dna5.authToken))
dna5.log("Timeline Token : " + str(dna5.tl.channelAccessToken))

dna6 = LINE('Esrt47QpyN5xDpEI9q7a.fW/HXK/P6ucyNSYHd42E2G.IfXCDZecGl9VI8YP70o5nXE+BVa1MPJ/RArJyIzm7fg=')
dna6.log("Auth Token : " + str(dna6.authToken))
dna6.log("Timeline Token : " + str(dna6.tl.channelAccessToken))

dna7 = LINE('EsUm82oDONrrROSjd0o3.GQe1F0FLgkB3suGK5WtUCW.H1Mt8JrAr6MOcF/Jey5dYH62txLV9EUeC7kpIy7xbI8=')
dna7.log("Auth Token : " + str(dna7.authToken))
dna7.log("Timeline Token : " + str(dna7.tl.channelAccessToken))

dna8 = LINE('EsxzQWuDsnqvc6umvf13.fOtS1/ZYrVfyY2wr74a3uW.5NYRTH6X2K+wXUVCetEqGUoqhqMZEZfh9iY/yY/NeH8=')
dna8.log("Auth Token : " + str(dna8.authToken))
dna8.log("Timeline Token : " + str(dna8.tl.channelAccessToken))

dna9 = LINE('EsCbkUtvMVAsXQ6h0Vj1./PGYhVVe4uDle5Q6kp48qq.QdI0wcEL/lGgxXLSRWgiHGqtblWKBVsv1pw+H+jnqoM=')
dna9.log("Auth Token : " + str(dna9.authToken))
dna9.log("Timeline Token : " + str(dna9.tl.channelAccessToken))

dna10 = LINE('Es0Dc6tTZLGHWLdjLoj5.qzjQVWZ0ZEOc9BUr4r9zrq.53ywR6urnzMdrRTfoFuFUXmX92L79AkrN/LPysGzdVg=') #Ghost
dna10.log("Auth Token : " + str(dna10.authToken))
dna10.log("Timeline Token : " + str(dna10.tl.channelAccessToken))


startBot = time.time()
elapsed_time = format_timespan(time.time()-startBot)


helpMessage ="""
╔════════════════════╗
                    ✰ ᴅɴᴀ ʙᴏᴛ ✰
╚════════════════════╝
╔════════════════════╗
                ◄]·✪·Public·✪·[►
╠════════════════════╝
╠❂➣ ɪᴅ
╠❂➣ ᴍᴇ
╠❂➣ ᴍʏ ᴍɪᴅ
╠❂➣ ᴛᴀɢᴀʟʟ
╠❂➣ ᴀʙᴏᴜᴛ
╠❂➣ ᴏᴡɴᴇʀʟɪsᴛ
╠❂➣ ᴀᴅᴍɪɴʟɪsᴛ
╠❂➣ ʀᴇsᴘᴏɴ
╠❂➣ ᴀʙsᴇɴ
╠❂➣ ᴅɴᴀ
╠❂➣ sᴘᴇᴇᴅ
╠❂➣ sᴘ
╠❂➣ ɢɪɴғᴏ
╠════════════════════╗
                ◄]·✪·Admin·✪·[►
╠════════════════════╝
╠❂➣ ʙᴜᴋᴀ ǫʀ
╠❂➣ ᴛᴜᴛᴜᴘ ǫʀ
╠❂➣ ᴄᴏɴᴛᴀᴄᴛ 「ᴏɴ/ᴏғғ」
╠❂➣ sᴇᴛ/sᴛᴀᴛᴜs
╠❂➣ ɢɴ 「ᴛᴇxᴛ」
╠❂➣ ɪɴᴠɪᴛᴇ 「ᴍɪᴅ」
╠❂➣ ɪɴᴠɪᴛᴇ 「ᴄᴏɴᴛᴀᴄᴛ」
╠❂➣ ᴘʀᴏᴄᴀɴᴄᴇʟ 「ᴏɴ/ᴏғғ」
╠❂➣ ᴘʀᴏɪɴᴠɪᴛᴇ 「ᴏɴ/ᴏғғ」
╠❂➣ ᴘʀᴏᴊᴏɪɴ 「ᴏɴ/ᴏғғ」
╠❂➣ ᴘʀᴏǫʀ 「ᴏɴ/ᴏғғ」
╠❂➣ ᴄᴀɴᴄᴇʟᴀʟʟ
╠❂➣ ʙʏᴇ ᴅɴᴀ
╠❂➣ ʙʏᴇ ᴀʟʟ
╠❂➣ sᴛᴇᴀʟ 「ᴍᴇɴᴛɪᴏɴ」
╠❂➣ ɴᴋ 「ᴍᴇɴᴛɪᴏɴ」
╠❂➣ ʙᴀɴ 「ᴍᴇɴᴛɪᴏɴ」
╠❂➣ ᴜɴʙᴀɴ 「ᴍᴇɴᴛɪᴏɴ」
╠❂➣ ʙᴀɴ 「ᴄᴏɴᴛᴀᴄᴛ」
╠❂➣ ᴜɴʙᴀɴ 「ᴄᴏɴᴛᴀᴄᴛ」
╠❂➣ ᴄʟᴇᴀʀ ʙᴀɴ
╠❂➣ ʙᴀɴʟɪsᴛ
╠❂➣ ᴋɪʟʟ ʙᴀɴ
╠❂➣ sɪᴅᴇʀ 「ᴏɴ/ᴏғғ」
╠════════════════════╗
                ◄]·✪·Owner·✪·[►
╠════════════════════╝
╠❂➣ ɢʟɪsᴛ
╠❂➣ ɢʀᴏᴜᴘ ɪᴅ
╠❂➣ ʀᴇsᴛᴀʀᴛ
╠❂➣ ᴀᴜᴛᴏ ᴊᴏɪɴ:「ᴏɴ/ᴏғғ」
╠❂➣ ɢᴄᴀɴᴄᴇʟ
╠❂➣ ʟᴇᴀᴠᴇ 「ᴏɴ/ᴏғғ」
╠❂➣ sʜᴀʀᴇ 「ᴏɴ/ᴏғғ」
╠❂➣ ᴀᴜᴛᴏ ᴀᴅᴅ:「ᴏɴ/ᴏғғ」
╠❂➣ ᴄᴏᴍᴇ ᴅɴᴀ
╠❂➣ ɢʀᴏᴜᴘ ʙᴄ 「ᴛᴇxᴛ」
╠❂➣ ʀᴜɴᴛɪᴍᴇ
╠❂➣ ᴀᴅᴍɪɴ ᴀᴅᴅ 「ᴍᴇɴᴛɪᴏɴ」
╠❂➣ ᴀᴅᴍɪɴ ʀᴇᴍᴏᴠᴇ 「ᴍᴇɴᴛɪᴏɴ」
╠❂➣ ʀᴇsᴘᴏɴᴛᴀɢ 「ᴏɴ/ᴏғғ」
╠❂➣  ᴋɪᴄᴋ ᴛᴀɢ 「ᴏɴ/ᴏғғ」
╠════════════════════╗
                Credits by : D̶e̶e̶ ✯
╚════════════════════╝
╔════════════════════╗
                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰
╚════════════════════╝
"""
oepoll = OEPoll(ririn)
KAC=[ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
mid = ririn.getProfile().mid
Amid = dna1.getProfile().mid
Bmid = dna2.getProfile().mid
Cmid = dna3.getProfile().mid
Dmid = dna4.getProfile().mid
Emid = dna5.getProfile().mid
Fmid = dna6.getProfile().mid
Gmid = dna7.getProfile().mid
Hmid = dna8.getProfile().mid
Imid = dna9.getProfile().mid
Jmid = dna10.getProfile().mid

responsename = ririn.getProfile().displayName
responsename2 = dna1.getProfile().displayName
responsename3 = dna2.getProfile().displayName
responsename4 = dna3.getProfile().displayName
responsename5 = dna4.getProfile().displayName
responsename6 = dna5.getProfile().displayName
responsename7 = dna6.getProfile().displayName
responsename8 = dna7.getProfile().displayName
responsename9 = dna8.getProfile().displayName
responsename10 = dna9.getProfile().displayName
responsename11 = dna10.getProfile().displayName

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]
admin=["ueca4120a9d7b0e4a9e7f4f1b1b96a436","u40d66b1f1c5ce30fdce9507a73247ef1","uc2d366327a79c98701b0b8bd9e08c0c9","ubcce0f23f428d75703fb33ee06c083b6","ubd3c3fa2c0128918d5b484caa42f9fee","u6fc2dc5f5f0d0fc6a4d2e92626afb742"]
Owner=["ueca4120a9d7b0e4a9e7f4f1b1b96a436"]
creator=["ueca4120a9d7b0e4a9e7f4f1b1b96a436"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'detectMention':True,
    'kickMention':False,
    'message':"ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ \nᴅɴᴀ ʙᴏᴛ \nᴏᴘᴇɴ ᴏʀᴅᴇʀ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ᴘʏᴛʜᴏɴ 3 \nᴍɪɴᴀᴛ ᴘᴄ ᴀᴋᴜɴ ᴅɪ ʙᴀᴡᴀʜ \nᴄʀᴇᴀᴛᴏʀ line.me/ti/p/ppgIZ0JLDW",
    "lang":"JP",
    "comment":"ᴀᴜᴛᴏ ʟɪᴋᴇ ʙʏ : \nᴅɴᴀ ʙᴏᴛ \nᴏᴘᴇɴ ᴏʀᴅᴇʀ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ᴘʏᴛʜᴏɴ 3 \nᴍɪɴᴀᴛ ᴘᴄ ᴀᴋᴜɴ ᴅɪ ʙᴀᴡᴀʜ \nᴄʀᴇᴀᴛᴏʀ line.me/ti/p/ppgIZ0JLDW",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "wcOn":True,
    "leftOn":True,
    "cName":"✰ ᴅɴᴀ ʙᴏᴛ ✰",
    "cName2":"✰ ᴅɴᴀ ʙᴏᴛ ✰ ",
    "cName3":"✰ ᴅɴᴀ ʙᴏᴛ ✰ ",
    "cName4":"✰ ᴅɴᴀ ʙᴏᴛ ✰ ",
    "cName5":"✰ ᴅɴᴀ ʙᴏᴛ ✰ ",
    "cName6":"✰ ᴅɴᴀ ʙᴏᴛ ✰",
    "cName7":"✰ ᴅɴᴀ ʙᴏᴛ ✰ ",
    "cName8":"✰ ᴅɴᴀ ʙᴏᴛ ✰ ",
    "cName9":"✰ ᴅɴᴀ ʙᴏᴛ ✰ ",
    "cName10":"✰ ᴅɴᴀ ʙᴏᴛ ✰ ",
    "likeOn":{},
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":True,
    "ProtectJoin":False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "Sider":{},
    "spamer":{},
    "CloseQR":True,
    "ProtectInvite":True,
    "Protectcancel":True,
    "protectionOn":True,
    "alwaysRead":False, 
    "atjointicket":True,
    "invite":{},
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']

#-------------------------------------=Kumpulan Def=-------------------------------------#

#-----------------Read Message-----------------#
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = ririn.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass
#-----------------------Restart-----------------------#
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
#-----------------------Mention----------------------#
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        ririn.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#------------------Detect Mention-----------------#
        if 'MENTION' in msg.contentMetadata.keys() != None:
        	if wait["detectMention"] == True:
        		contact = ririn.getContact(msg._from)
        		cName = contact.displayName
        		balas = ["sᴇᴋᴀʟɪ ʟᴀɢɪ ɴɢᴇ ᴛᴀɢ ɢᴡ sᴜᴍᴘᴀʜɪɴ ᴊᴏᴍʙʟᴏ sᴇᴜᴍᴜʀ ʜɪᴅᴜᴘ!","ᴅᴏɴᴛ ᴛᴀɢ!! ʟᴀɢɪ sɪʙᴜᴋ",cName + " ɴɢᴀᴘᴀɪɴ ɴɢᴇᴛᴀɢ?",cName + " ɴɢɢᴀᴋ ᴜsᴀʜ ᴛᴀɢ-ᴛᴀɢ! ᴋᴀʟᴏ ᴘᴇɴᴛɪɴɢ ʟᴀɴɢsᴜɴɢ ᴘᴄ ᴀᴊᴀ","ᴛᴀɢ ᴍᴜʟᴜ ʟᴏ ᴀɴᴊɪʀʀ!","ᴅɪᴀ ʟᴀɢɪ ᴏғғ", cName + " ᴋᴇɴᴀᴘᴀ ᴛᴀɢ? ᴋᴀɴɢᴇɴ?","ᴅɪᴀ ʟᴀɢɪ ᴛɪᴅᴜʀ\nᴊᴀɴɢᴀɴ ᴅɪ ᴛᴀɢ " + cName, "ᴊᴀɴɢᴀɴ sᴜᴋᴀ ᴛᴀɢ ɢᴜᴀ " + cName, "ᴋᴀᴍᴜ sɪᴀᴘᴀ " + cName + "?", "ᴀᴅᴀ ᴘᴇʀʟᴜ ᴀᴘᴀ " + cName + "?","ᴡᴏɪɪ " + cName + " ᴊᴀɴɢᴀɴ ɴɢᴇᴛᴀɢ, ʀɪɪʙᴜᴛ!"]
        		ret_ = random.choice(balas)
        		name = re.findall(r'@(\w+)', msg.text)
        		mention = ast.literal_eval(msg.contentMetadata['MENTION'])
        		mentionees = mention['MENTIONEES']
        		for mention in mentionees:
        			if mention['M'] in admin:
        				ririn.sendText(msg.to,ret_)
        				break                                  
        			if mention['M'] in Bots:
        				ririn.sendText(msg.to,ret_)
        				break
#--------------------Kick Mention-------------------#
        if 'MENTION' in msg.contentMetadata.keys() != None:
        	if wait["kickMention"] == True:
        		contact = ririn.getContact(msg._from)
        		cName = contact.displayName
        		balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
        		ret_ = random.choice(balas)                     
        		name = re.findall(r'@(\w+)', msg.text)
        		mention = ast.literal_eval(msg.contentMetadata['MENTION'])
        		mentionees = mention['MENTIONEES']
        		for mention in mentionees:
        			if mention['M'] in admin:
        				ririn.sendText(msg.to,ret_)
        				random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
        				break                                  
        			if mention['M'] in Bots:
        				ririn.sendText(msg.to,ret_)
        				random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
        				break         				
#------End Operation & Add Contact-------#
def bot(op):
    try:
        if op.type == 0:
        	return
        if op.type == 5:
            if wait["autoAdd"] == True:
                ririn.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    ririn.sendText(op.param1,str(wait["message"]))
#--------------Notif Update Group--------------#
        if op.type == 11:
            if wait["ProtectGroup"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                 	X = ririn.getGroup(op.param1)
                 	X.preventedJoinByTicket = False
                 	ririn.updateGroup(X)
                 	Ticket = ririn.reissueGroupTicket(op.param1)
                 	dna10.acceptGroupInvitationByTicket(op.param1,Ticket)
                 	dna10.kickoutFromGroup(op.param1,[op.param2])
                 	dna10.leaveGroup(op.param1)
                 	X = dna1.getGroup(op.param1)
                 	X.preventedJoinByTicket = True
                 	dna1.updateGroup(X)
#-------------Induk Invite to Group-------------#
        if op.type == 13:
            if mid in op.param2:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots:
                       G = ririn.getGroup(op.param1)
                       ririn.acceptGroupInvitation(op.param1)
#---------------Invite User Protect---------------#
        if op.type == 13:
           if wait["ProtectInvite"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).sendText(op.param1, "ᴍᴀᴜ ɴɢᴜɴᴅᴀɴɢ sɪᴀᴘᴀ ᴋᴀ?\nᴋᴋ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ\nᴊᴀᴅɪ ᴀᴋᴜ ᴄᴀɴᴄᴇʟ😛")
#----------------------Invite Bot------------------------#
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = dna1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        dna1.updateGroup(G)
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ririn.updateGroup(G)
                        Ticket = ririn.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = dna2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna2.updateGroup(X)
                        Ti = dna2.reissueGroupTicket(op.param1)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna1.updateGroup(X)
                        Ti = dna1.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = dna3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna3.updateGroup(X)
                        Ti = dna3.reissueGroupTicket(op.param1)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna2.updateGroup(X)
                        Ti = dna2.reissueGroupTicket(op.param1)
                        
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = dna4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna4.updateGroup(X)
                        Ti = dna4.reissueGroupTicket(op.param1)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna3.updateGroup(X)
                        Ti = dna3.reissueGroupTicket(op.param1)

                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = dna5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna5.updateGroup(X)
                        Ti = dna5.reissueGroupTicket(op.param1)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna4.updateGroup(X)
                        Ti = dna4.reissueGroupTicket(op.param1)
                        
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        G = dna6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        dna6.updateGroup(G)
                        Ticket = dna6.reissueGroupTicket(op.param1)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        dna5.updateGroup(G)
                        Ticket = dna5.reissueGroupTicket(op.param1)

                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = dna7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna7.updateGroup(X)
                        Ti = dna7.reissueGroupTicket(op.param1)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna6.updateGroup(X)
                        Ti = dna6.reissueGroupTicket(op.param1)

                if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = dna8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna8.updateGroup(X)
                        Ti = dna8.reissueGroupTicket(op.param1)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna7.updateGroup(X)
                        Ti = dna7.reissueGroupTicket(op.param1)
                        
                if op.param3 in Hmid:
                    if op.param2 in Imid:
                        X = dna9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna9.updateGroup(X)
                        Ti = dna9.reissueGroupTicket(op.param1)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna8.updateGroup(X)
                        Ti = dna8.reissueGroupTicket(op.param1)

                if op.param3 in Imid:
                    if op.param2 in mid:
                        X = ririn.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ririn.updateGroup(X)
                        Ti = ririn.reissueGroupTicket(op.param1)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna9.updateGroup(X)
                        Ti = dna9.reissueGroupTicket(op.param1)
                                        
        if op.type == 13:
            print(op.param1)
            print(op.param2)
            print(op.param3)
            if mid in op.param3:
                G = ririn.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ririn.rejectGroupInvitation(op.param1)
                        else:
                            ririn.acceptGroupInvitation(op.param1)
                    else:
                        ririn.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ririn.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ririn.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 13:
            if mid in op.param3:
                G = ririn.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ririn.rejectGroupInvitation(op.param1)
                        else:
                            ririn.acceptGroupInvitation(op.param1)
                    else:
                        ririn.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ririn.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ririn.cancelGroupInvitation(op.param1, matched_list)    
#-------------Invite User By Contact-------------#
            if msg.contentType == 13:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = ririn.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            ririn.sendText(msg.to, _name + " sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ririn.findAndAddContactsByMid(target)
                                ririn.inviteIntoGroup(msg.to,[target])
                                ririn.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    ririn.sendText(msg.to,'ᴇʀʀᴏʀ')
                                    wait["invite"] = False
                                    break
            else:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = dna1.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            dna1.sendText(msg.to, _name + "sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                dna1.findAndAddContactsByMid(target)
                                dna1.inviteIntoGroup(msg.to,[target])
                                dna1.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    dna1.sendText(msg.to,'ᴇʀʀᴏʀ')
                                    wait["invite"] = False
                                    break
#----------------Notif Leave Group----------------#
        if op.type == 15:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	ririn.sendMessage(op.param1, "ɴᴀʜ ᴋᴀɴ ʙᴀᴘᴇʀ {}, ɢᴀᴋ ᴜsᴀʜ ʙᴀʟɪᴋ ᴅɪ {} ʟᴀɢɪ ʏᴀ\nsᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴅᴀɴ sᴇᴍᴏɢᴀʜ ᴛᴇɴᴀɴɢ ᴅɪʟᴜᴀʀ sᴀɴᴀ 😘😘😘".format(str(dan.displayName),str(tgb.name)))
        	ririn.sendContact(op.param1, op.param2)
        	ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
#------------------Comment Like-------------------#

#-----------------Notif Join Group------------------#
        if op.type == 17:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	ririn.sendMessage(op.param1, "ʜᴏʟᴀ @!{} \nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ {} \nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴄʜᴇᴄᴋ ɴᴏᴛᴇ ʏᴀ \nᴀᴡᴀs ᴋᴀʟᴀᴜ ʙᴀᴘᴇʀᴀɴ😘😘😘".format(str(dan.displayName),str(tgb.name)))
        	ririn.sendContact(op.param1, op.param2)
        	ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
#-----------------User Join Kicked-----------------#
        if op.type == 17:
            if wait["ProtectJoin"] == True:
                if op.param2 not in admin:
                    try:
                        contact = ririn.getContact(op.param2)
                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)
#--------------Blacklist Join Kicked---------------#
        if op.type == 17:
           if op.param2 in wait["blacklist"]:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#----------------Blacklist Auto Kick----------------#
        if op.type == 19:
           if op.param2 not in admin:
              if op.param2 not in Bots:
                 if op.param2 not in wait["whitelist"]:
                    wait["blacklist"][op.param2] = True
                    print("kicker kicked")
                 else:
                    pass
#---------------------User Kicked---------------------#
        if op.type == 19:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                  try:
                   ririn.kickoutFromGroup(op.param1,[op.param2])
                  except:
                      try:
                          random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                          random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      except:
                          print ("User Kick")
#-------------------Admin Kicked--------------------#
        if op.type == 19:
           if op.param3 in admin:
               try:
                   ririn.kickoutFromGroup(op.param1,[op.param2])
                   ririn.inviteIntoGroup(op.param1,admin)
               except:
                   try:
                       random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                       random.choice(KAC).inviteIntoGroup(op.param1,admin)
                   except:
                       print ("Admin Kicked")
#----------------------Bot Kicked----------------------#
        if op.type == 19:
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna9.getGroup(op.param1)
                  dna9.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna9.updateGroup(G)
                  Ticket = dna9.reissueGroupTicket(op.param1)
                  ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ririn.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Amid:
              if op.param2 not in Bots or admin:
                try:
                  G = ririn.getGroup(op.param1)
                  ririn.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ririn.updateGroup(G)
                  Ticket = ririn.reissueGroupTicket(op.param1)
                  dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna1.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Bmid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna1.getGroup(op.param1)
                  dna1.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna1.updateGroup(G)
                  Ticket = dna1.reissueGroupTicket(op.param1)
                  dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna2.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Cmid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna2.getGroup(op.param1)
                  dna2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna2.updateGroup(G)
                  Ticket = dna2.reissueGroupTicket(op.param1)
                  dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna3.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Dmid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna3.getGroup(op.param1)
                  dna3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna3.updateGroup(G)
                  Ticket = dna3.reissueGroupTicket(op.param1)
                  dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna4.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Emid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna4.getGroup(op.param1)
                  dna4.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna4.updateGroup(G)
                  Ticket = dna4.reissueGroupTicket(op.param1)
                  dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna5.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Fmid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna5.getGroup(op.param1)
                  dna5.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna5.updateGroup(G)
                  Ticket = dna5.reissueGroupTicket(op.param1)
                  dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna6.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Gmid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna6.getGroup(op.param1)
                  dna6.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna6.updateGroup(G)
                  Ticket = dna6.reissueGroupTicket(op.param1)
                  dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna7.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Hmid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna7.getGroup(op.param1)
                  dna7.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna7.updateGroup(G)
                  Ticket = dna7.reissueGroupTicket(op.param1)
                  dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna8.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in Imid:
              if op.param2 not in Bots or admin:
                try:
                  G = dna8.getGroup(op.param1)
                  dna8.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  dna8.updateGroup(G)
                  Ticket = dna8.reissueGroupTicket(op.param1)
                  dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  dna9.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------Notif Invite Room----------------#
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)
#-----------------Notif Leave Room-----------------#                
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)
#------------------Receive Message-----------------#   
        if op.type == 26:
            msg = op.message



            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    ririn.sendChatChecked(msg._from,msg.id)
                else:
                    ririn.sendChatChecked(msg.to,msg.id)
                    
        if msg.contentType == 16:
        	if wait["likeOn"] == True:
        		url = msg.contentMetadata["postEndUrl"]
        		ririn.like(url[25:58], url[66:], likeType=1005)
        		dna1.like(url[25:58], url[66:], likeType=1002)
        		dna2.like(url[25:58], url[66:], likeType=1004)
        		dna3.like(url[25:58], url[66:], likeType=1003)
        		dna4.like(url[25:58], url[66:], likeType=1001)
        		dna5.like(url[25:58], url[66:], likeType=1005)
        		dna6.like(url[25:58], url[66:], likeType=1002)
        		dna7.like(url[25:58], url[66:], likeType=1004)
        		dna8.like(url[25:58], url[66:], likeType=1003)
        		dna9.like(url[25:58], url[66:], likeType=1001)
        		ririn.comment(url[25:58], url[66:], wait["comment"])
        		dna1.comment(url[25:58], url[66:], wait["comment"])
        		dna2.comment(url[25:58], url[66:], wait["comment"])
        		dna3.comment(url[25:58], url[66:], wait["comment"])
        		dna4.comment(url[25:58], url[66:], wait["comment"])
        		dna5.comment(url[25:58], url[66:], wait["comment"])
        		dna6.comment(url[25:58], url[66:], wait["comment"])
        		dna7.comment(url[25:58], url[66:], wait["comment"])
        		dna8.comment(url[25:58], url[66:], wait["comment"])
        		dna9.comment(url[25:58], url[66:], wait["comment"])
        		ririn.sendText(msg.to,"Like Success")
        		wait['likeOn'] = False
#------------------Receive Come Bye---------------#
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg._from
                if msg._from == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ririn.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = ririn.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            ririn.updateGroup(X)
                        except:
                            ririn.sendText(msg.to,"ᴇʀʀᴏʀ")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ririn.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ririn.like(url[25:58], url[66:], likeType=1001)
#---------------------Blacklist User--------------------#
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ririn.sendText(msg.to,"ᴅᴇᴄɪᴅᴇᴅ ɴᴏᴛ ᴛᴏ ᴄᴏᴍᴍᴇɴᴛ")
                        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ririn.sendText(msg.to,"ᴅᴇʟᴇᴛᴇᴅ")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        ririn.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ririn.sendText(msg.to,"ᴀᴅᴅᴇᴅ")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ririn.sendText(msg.to,"ᴅᴇʟᴇᴛᴇᴅ")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        ririn.sendText(msg.to,"ɪᴛ ɪs ɴᴏᴛ ɪɴ ᴛʜᴇ ʙʟᴀᴄᴋ ʟɪsᴛ")
#------------------------------------------=Contact=----------------------------------------#
               elif wait["contact"] == True:
                    msg.contentType = 0
                    ririn.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = ririn.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ririn.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ririn.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = ririn.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ririn.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ririn.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    ririn.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#----------------------------------------------------=Keyword=----------------------------------------------------#
#----------------------------------------------------=Keyword=----------------------------------------------------#
#----------------------------------------------------=Keyword=----------------------------------------------------#
#------------------------Key Public----------------------#
            elif msg.text in ["Key","key","help","Help"]:
                if wait["lang"] == "JP":
                    ririn.sendText(msg.to,helpMessage)
                else:
                    ririn.sendText(msg.to,helpt)
            elif "Id" == msg.text:
                ririn.sendText(msg.to,msg.to)
            elif msg.text in ["Mid ku","mid ku","My mid","Mid saya"]:
                ririn.sendText(msg.to,msg._from)
            elif msg.text in ["Me"]:
                ririn.sendContact(msg.to,msg._from)
            elif msg.text in ["Tagall","tagall"]:
                group = ririn.getGroup(msg.to)
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
                    ririn.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    ririn.sendMessage(msg.to, "ᴛᴏᴛᴀʟ {} ᴍᴇɴᴛɪᴏɴ".format(str(len(nama))))
                    
            elif msg.text in ["About","about"]:
                try:
                    arr = []
                    owner = "ueca4120a9d7b0e4a9e7f4f1b1b96a436"
                    creator = ririn.getContact(owner)
                    contact = ririn.getContact(mid)
                    grouplist = ririn.getGroupIdsJoined()
                    contactlist = ririn.getAllContactIds()
                    blockedlist = ririn.getBlockedContactIds()
                    ret_ = "╔══[ ᴀʙᴏᴜᴛ ʙᴏᴛ ]"
                    ret_ += "\n╠✪ ʟɪɴᴇ : {}".format(contact.displayName)
                    ret_ += "\n╠✪ ɢʀᴏᴜᴘ : {}".format(str(len(grouplist)))
                    ret_ += "\n╠✪ ғʀɪᴇɴᴅ : {}".format(str(len(contactlist)))
                    ret_ += "\n╠✪ ʙʟᴏᴄᴋᴇᴅ : {}".format(str(len(blockedlist)))
                    ret_ += "\n╠══[ ᴀʙᴏᴜᴛ ᴅɴᴀ ʙᴏᴛ ]"
                    ret_ += "\n╠✪ ᴠᴇʀsɪᴏɴ : ᴘʀᴇᴍɪᴜᴍ"
                    ret_ += "\n╠✪ ᴄʀᴇᴀᴛᴏʀ : {}".format(creator.displayName)
                    ret_ += "\n╚══[ ᴅᴏɴ'ᴛ ʙᴇ ʀᴇᴍᴀᴋᴇ 😝 ]"
                    ririn.sendContact(msg.to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
                    ririn.sendMessage(msg.to, str(ret_))
                except Exception as e:
                    ririn.sendMessage(msg.to, str(e))                    

            elif msg.text in ["Ownerlist","ownerlist"]:
                try:
                    arr = []
                    owner = "ueca4120a9d7b0e4a9e7f4f1b1b96a436"
                    creator = ririn.getContact(owner)
                    ret_ = "╔════════════════\n╠✪➣  ✰ ᴅɴᴀ ʙᴏᴛ ✰"
                    ret_ += "\n╠══✪〘ᴏᴡɴᴇʀ ʟɪsᴛ〙✪═══"
                    ret_ += "\n╠✪ ᴏᴡɴᴇʀʟɪsᴛ : : {}".format(creator.displayName)
                    ret_ += "\n╠════════════════"
                    ret_ += "\n╠✪〘 line.me/ti/p/ppgIZ0JLDW 〙"
                    ret_ += "\n╚════════════════"
                    ririn.sendContact(msg.to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
                    ririn.sendMessage(msg.to,"ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴏᴡɴᴇʀʟɪsᴛ...")
                    ririn.sendMessage(msg.to, str(ret_))
                except Exception as e:
                    ririn.sendMessage(msg.to, str(e))

            elif msg.text in ["Adminlist","adminlist"]:
            	if admin == []:
            		ririn.sendMessage(msg.to,"ᴛʜᴇ ᴀᴅᴍɪɴʟɪsᴛ ɪs ᴇᴍᴘᴛʏ")
            	else:
            		ririn.sendMessage(msg.to,"ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀᴅᴍɪɴʟɪsᴛ...")
            		mc = "╔════════════════\n╠✪➣  ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╠══✪〘 ᴀᴅᴍɪɴʟɪsᴛ 〙✪═══\n"
            		for mi_d in admin:
            			mc += "╠✪ " +ririn.getContact(mi_d).displayName + "\n"
            		ririn.sendMessage(msg.to,mc + "╠════════════════\n╠✪〘 line.me/ti/p/ppgIZ0JLDW 〙\n╚════════════════")
                        
            elif msg.text in ["Respon","respon"]:
                ririn.sendMessage(msg.to,responsename)
                dna1.sendMessage(msg.to,responsename2)
                dna2.sendMessage(msg.to,responsename3)
                dna3.sendMessage(msg.to,responsename4)
                dna4.sendMessage(msg.to,responsename5)
                dna5.sendMessage(msg.to,responsename6)
                dna6.sendMessage(msg.to,responsename7)
                dna7.sendMessage(msg.to,responsename8)
                dna8.sendMessage(msg.to,responsename9)
                dna9.sendMessage(msg.to,responsename10)
                random.choice(KAC).sendText(msg.to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                    
            elif msg.text in ["Dna","dna"]:
            	ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	dna1.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	dna2.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	dna3.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	dna4.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	dna5.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	dna6.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	dna7.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	dna8.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	dna9.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
            	random.choice(KAC).sendText(msg.to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")

            elif msg.text in ["Absen","absen"]:
                ririn.sendContact(msg.to, mid)
                dna1.sendContact(msg.to, Amid)
                dna2.sendContact(msg.to, Bmid)
                dna3.sendContact(msg.to, Cmid)
                dna4.sendContact(msg.to, Dmid)
                dna5.sendContact(msg.to, Emid)
                dna6.sendContact(msg.to, Fmid)
                dna7.sendContact(msg.to, Gmid)
                dna8.sendContact(msg.to, Hmid)
                dna9.sendContact(msg.to, Imid)
                random.choice(KAC).sendText(msg.to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                    
            elif msg.text in ["Sp","sp"]:
                ririn.sendText(msg.to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                sp = int(round(time.time() *1000))
                ririn.sendText(msg.to,"ᴍʏ sᴘᴇᴇᴅ : %sms" % (sp - op.createdTime))

            elif msg.text in ["Speed","speed"]:
                start = time.time()
                ririn.sendText(msg.to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                elapsed_time = time.time() - start
                ririn.sendText(msg.to, "ᴍʏ sᴘᴇᴇᴅ : %sms" % (elapsed_time))
                
            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                ririn.sendText(msg.to,"sᴇɴᴅ ᴜʀ ᴘᴏsᴛ")
                
            elif msg.text == "Ginfo":
               if msg._from in Owner:
                if msg.toType == 2:
                    ginfo = ririn.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventedJoinByTicket == True:
                            u = "ᴄʟᴏsᴇ "
                        else:
                            u = "ᴏᴘᴇɴ "
                        ririn.sendText(msg.to,"[ɢʀᴏᴜᴘ ɴᴀᴍᴇ]\n" + str(ginfo.name) + "\n[ɢɪᴅ]\n" + msg.to + "\n[ɢʀᴏᴜᴘ ᴄʀᴇᴀᴛᴏʀ]\n" + gCreator + "\n[ᴘʀᴏғɪʟᴇ sᴛᴀᴛᴜs]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nᴍᴇᴍʙᴇʀs:" + str(len(ginfo.members)) + "ᴍᴇᴍʙᴇʀs\nᴘᴇɴᴅɪɴɢ:" + sinvitee + "ᴘᴇᴏᴘʟᴇ\nᴜʀʟ:" + u + "ɪᴛ ɪs ɪɴsɪᴅᴇ")
                    else:
                        ririn.sendText(msg.to,"[ɢʀᴏᴜᴘ ɴᴀᴍᴇ]\n" + str(ginfo.name) + "\n[ɢɪᴅ]\n" + msg.to + "\n[ɢʀᴏᴜᴘ ᴄʀᴇᴀᴛᴏʀ]\n" + gCreator + "\n[ᴘʀᴏғɪʟᴇ sᴛᴀᴛᴜs]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴄᴀɴ ɴᴏᴛ ʙᴇ ᴜsᴇᴅ ᴏᴜᴛsɪᴅᴇ ᴛʜᴇ ɢʀᴏᴜᴘ")
                    else:
                        ririn.sendText(msg.to,"ɴᴏᴛ ғᴏʀ ᴜsᴇ ʟᴇss ᴛʜᴀɴ ɢʀᴏᴜᴘ")
                         
#------------------------Key Admin----------------------#

            elif msg.text in ["Ourl","ourl"]:
               if msg._from in admin:
               	if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                    else:
                        ririn.sendText(msg.to,"ǫʀ ᴀʟʀᴇᴀᴅʏ ᴏᴘᴇɴ")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ᴏᴜᴛsɪᴅᴇ ᴛʜᴇ ɢʀᴏᴜᴘ")
                    else:
                        ririn.sendText(msg.to,"ɴᴏᴛ ғᴏʀ ᴜsᴇ ʟᴇss ᴛʜᴀɴ ɢʀᴏᴜᴘ")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventedJoinByTicket = True
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ǫʀ ᴄᴏᴅᴇ ʜᴀs ʙᴇᴇɴ ᴄʟᴏsᴇᴅ")
                    else:
                        ririn.sendText(msg.to,"ʜᴀs ʙᴇᴇɴ ᴄʟᴏsᴇᴅ")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ɴᴏᴛ ғᴏʀ ᴜsᴇ ʟᴇss ᴛʜᴀɴ ɢʀᴏᴜᴘ")
                    else:
                        ririn.sendText(msg.to,"ɴᴏᴛ ғᴏʀ ᴜsᴇ ʟᴇss ᴛʜᴀɴ ɢʀᴏᴜᴘ")
              else:
                  ririn.sendText(msg.to,"ᴀᴄᴄᴇs ᴅᴇɴɪᴇᴅ.")
                  ririn.sendText(msg.to,"ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴀᴄᴄᴇssᴇᴅ ʙʏ ᴀᴅᴍɪɴ.")
            elif msg.text in ["Buka qr","Open qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ǫʀ ᴀʟʀᴇᴀᴅʏ ᴏᴘᴇɴ")
                    else:
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏᴘᴇɴ")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴄᴀɴ ɴᴏᴛ ʙᴇ ᴜsᴇᴅ ᴏᴜᴛsɪᴅᴇ ᴛʜᴇ ɢʀᴏᴜᴘ")
                    else:
                        ririn.sendText(msg.to,"ɴᴏᴛ ғᴏʀ ᴜsᴇ ʟᴇss ᴛʜᴀɴ ɢʀᴏᴜᴘ")
              else:
                  ririn.sendText(msg.to,"ᴀᴄᴄᴇs ᴅᴇɴɪᴇᴅ.")
                  ririn.sendText(msg.to,"ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴀᴄᴄᴇssᴇᴅ ʙʏ ᴀᴅᴍɪɴ.")
            elif msg.text in ["Crash"]:
              if msg._from in admin:
              	ririn.sendContact(to, "ub621484bd88d2486744123db00551d5e',")
            elif msg.text in ["CloseQR On","closeqr on"]:
               if msg._from in admin:
                if wait["CloseQR"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴄʟᴏsᴇ ǫʀ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["CloseQR"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴄʟᴏsᴇ ǫʀ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["CloseQR Off","closeqr off","Closeqr off"]:
               if msg._from in admin:
                if wait["CloseQR"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴄʟᴏsᴇ ǫʀ ᴏғғ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["CloseQR"] = False
                    if wait["lang"] == "JP":
                        dna1.sendText(msg.to,"ᴄʟᴏsᴇ ǫʀ ᴏғғ")
                    else:
                        dna1.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
               if msg._from in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
               if msg._from in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴏғғ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                        
            elif "Sider on" in msg.text:
            	if msg._from in admin:
            		try:
            			del cctv['point'][msg.to]
            			del cctv['sidermem'][msg.to]
            			del cctv['cyduk'][msg.to]
            		except:
            			pass
            		cctv['point'][msg.to] = msg.id
            		cctv['sidermem'][msg.to] = ""
            		cctv['cyduk'][msg.to]=True
            		wait["Sider"] = True
            		ririn.sendText(msg.to,"sɪᴀᴘ ᴏɴ ᴄᴇᴋ sɪᴅᴇʀ")
                
            elif "Sider off" in msg.text:
            	if msg._from in admin:
            		if msg.to in cctv['point']:
            			cctv['cyduk'][msg.to]=False
            			wait["Sider"] = False
            			ririn.sendText(msg.to, "ᴄᴇᴋ sɪᴅᴇʀ ᴏғғ")                        
                        
            elif msg.text in ["Set","Status"]:
               if msg._from in admin:
                md = "╔═════[ ·✪·sᴛᴀᴛᴜs·✪· ]═════╗\n"
                if wait["Protectcancel"] == True: md+="╠❂➣ ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ : ᴏɴ [🔵]\n"
                else: md+="╠❂➣ ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ : ᴏғғ [🔴]\n"
                if wait["ProtectQR"] == True: md+="╠❂➣ ᴘʀᴏᴛᴇᴄᴛ ǫʀ : ᴏɴ [🔵]\n"
                else: md+="╠❂➣ ᴘʀᴏᴛᴇᴄᴛ ǫʀ : ᴏғғ [🔴]\n"
                if wait["CloseQR"] == True: md+="╠❂➣ ᴄʟᴏsᴇᴅ ǫʀ : ᴏɴ [🔵]\n"
                else: md+="╠❂➣ ᴄʟᴏsᴇᴅ ǫʀ : ᴏғғ[🔴]\n"
                if wait["ProtectInvite"] == True: md+="╠❂➣ ʙʟᴏᴄᴋ ɪɴᴠɪᴛᴇ : ᴏɴ [🔵]\n"
                else: md+="╠❂➣ ʙʟᴏᴄᴋ ɪɴᴠɪᴛᴇ : ᴏғғ[🔴]\n"
                if wait["contact"] == True: md+="╠❂➣ ᴄᴏɴᴛᴀᴄᴛ : ᴏɴ [🔵]\n"
                else: md+="╠❂➣ ᴄᴏɴᴛᴀᴄᴛ : ᴏғғ [🔴]\n"
                if wait["autoJoin"] == True: md+="╠❂➣ ᴀᴜᴛᴏ ᴊᴏɪɴ : ᴏɴ [🔵]\n"
                else: md +="╠❂➣ ᴀᴜᴛᴏ ᴊᴏɪɴ : ᴏғғ [🔴]\n"
                if wait["autoCancel"]["on"] == True:md+="╠❂➣ ɢʀᴏᴜᴘ ᴄᴀɴᴄᴇʟ :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "╠❂➣ ɢʀᴏᴜᴘ ᴄᴀɴᴄᴇʟ ᴏғғ [🔴]\n"
                if wait["leaveRoom"] == True: md+="╠❂➣ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ : ᴏɴ [🔵]\n"
                else: md+="╠❂➣ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ : ᴏғғ [🔴]\n"
                if wait["timeline"] == True: md+="╠❂➣ sʜᴀʀᴇ : ᴏɴ [🔵]\n"
                else:md+="╠❂➣ sʜᴀʀᴇ : ᴏғғ [🔴]\n"
                if wait["autoAdd"] == True: md+="╠❂➣ ᴀᴜᴛᴏ ᴀᴅᴅ : ᴏɴ [🔵]\n"
                else:md+="╠❂➣ ᴀᴜᴛᴏ ᴀᴅᴅ : ᴏғғ [🔴]\n"
                if wait["commentOn"] == True: md+="╠❂➣ ᴄᴏᴍᴍᴇɴᴛ : ᴏɴ [🔵]\n"
                else:md+="╠❂➣ ᴄᴏᴍᴍᴇɴᴛ : ᴏɴ ᴏғғ [🔴]\n╚═════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                ririn.sendText(msg.to,md)

            elif ("Gn " in msg.text):
               if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    ririn.updateGroup(X)
                else:
                    ririn.sendText(msg.to,"ɪᴛ ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ʙᴇsɪᴅᴇs ᴛʜᴇ ɢʀᴏᴜᴘ.")
            elif "Invitemid " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Invitemid ","")
                ririn.findAndAddContactsByMid(midd)
                ririn.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Invite","invite"]:
               if msg._from in admin:
                wait["invite"] = True
                ririn.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                
            elif msg.text in ["Procancel On","Procancel on","procancel on","Pc on"]:
               if msg._from in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Procancel Off","procancel off","Procancel off","Pc off"]:
               if msg._from in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏғғ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                         ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ ᴏғғ")
                    else:
                         ririn.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Proinvite on","proinvite on","Proinvite On","Pi on"]:
               if msg._from in admin:
                if wait["ProtectInvite"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["ProtectInvite"] = True
                    if wait["lang"] == "JP":
                        dna1.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏɴ")
                    else:
                        dna1.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Proinvite Off","proinvite off","Proinvite off","Pi off"]:
               if msg._from in admin:
                if wait["ProtectInvite"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏғғ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["ProtectInvite"] = False
                    if wait["lang"] == "JP":
                         dna1.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ ᴏғғ")
                    else:
                         dna1.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Projoin on","projoin on","ProJoin On","Pj on"]:
               if msg._from in admin:
                if wait["ProtectJoin"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["ProtectJoin"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀɴᴛɪ ᴊᴏɪɴ ᴍᴏᴅᴇ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Projoin off","projoin off","Projoin Off","Pj off"]:
               if msg._from in admin:
                if wait["ProtectJoin"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["ProtectJoin"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀɴᴛɪ ᴊᴏɪɴ ᴍᴏᴅᴇ ᴏғғ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Proqr On","proqr on","ProQR On","Pqr on"]:
               if msg._from in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏɴ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Proqr Off","proqr off","ProQR Off","Pqr off"]:
               if msg._from in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏғғ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴘʀᴏᴛᴇᴄᴛ ǫʀ ᴏғғ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")

            elif msg.text in ["Cancelall"]:
               if msg._from in admin:
                gid = ririn.getGroupIdsInvited()
                for i in gid:
                    ririn.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ririn.sendText(msg.to,"ᴀʟʟ ɪɴᴠɪᴛᴀᴛɪᴏɴs ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇғᴜsᴇᴅ")
                else:
                    ririn.sendText(msg.to,"sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                    
#----------------Semua Bot Ninggalin Group Kecuali Bot Induk----------------------------#
            elif msg.text in ["Bye dna"]:
              if msg._from in admin:
                if msg.toType == 2:
                    ginfo = ririn.getGroup(msg.to)
                    try:
                        dna1.leaveGroup(msg.to)
                        dna2.leaveGroup(msg.to)
                        dna3.leaveGroup(msg.to)
                        dna4.leaveGroup(msg.to)
                        dna5.leaveGroup(msg.to)
                        dna6.leaveGroup(msg.to)
                        dna7.leaveGroup(msg.to)
                        dna8.leaveGroup(msg.to)
                        dna9.leaveGroup(msg.to)
                    except:
                        pass
#--------------------------Bot Ninggalin Group termasuk Bot Induk----------------------------#
            elif msg.text in ["Bye all","bye all"]:
              if msg._from in admin:
                if msg.toType == 2:
                    ginfo = ririn.getGroup(msg.to)
                    try:
                        dna1.leaveGroup(msg.to)
                        dna2.leaveGroup(msg.to)
                        dna3.leaveGroup(msg.to)
                        dna4.leaveGroup(msg.to)
                        dna5.leaveGroup(msg.to)
                        dna6.leaveGroup(msg.to)
                        dna7.leaveGroup(msg.to)
                        dna8.leaveGroup(msg.to)
                        dna9.leaveGroup(msg.to)
                        ririn.leaveGroup(msg.to)
                    except:
                        pass
            elif "Steal " in msg.text:
                  if msg._from in admin:
                       nk0 = msg.text.replace("Steal ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ririn.getGroup(msg.to)
                       ginfo = ririn.getGroup(msg.to)
                       gs.preventedJoinByTicket = False
                       ririn.updateGroup(gs)
                       invsend = 0
                       Ticket = ririn.reissueGroupTicket(msg.to)
                       dna10.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                          sendMessage(msg.to,"ᴜsᴇʀ ᴅᴏᴇs ɴᴏᴛ ᴇxɪsᴛ")
                          pass
                       else:
                          for target in targets:
                             try:
                               dna9.sendText(msg.to,"sᴇᴍᴏɢᴀ ᴋᴀᴜ ʙᴀʜᴀɢɪᴀ ᴅɪ ɴᴇʀᴀᴋᴀ 👹👹")
                               dna10.kickoutFromGroup(msg.to,[target])
                               print (msg.to,[g.mid])
                             except:
                               dna10.leaveGroup(msg.to)
                               gs = dna1.getGroup(msg.to)
                               gs.preventedJoinByTicket = True
                               dna1.updateGroup(gs)
                               gs.preventedJoinByTicket(gs)
                               dna1.updateGroup(gs)             
            elif "Nk " in msg.text:
                  if msg._from in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ririn.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ᴜsᴇʀ ᴅᴏᴇs ɴᴏᴛ ᴇxɪsᴛ")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    dna1.sendText(msg.to,"sᴇᴇ ʏᴀ...")
            elif "Blacklist @ " in msg.text:
               if msg._from in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = dna12.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            ririn.sendText(msg.to,"ɴᴏᴛ ғᴏᴜɴᴅ")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ririn.sendText(msg.to,"sᴜᴄᴄᴇs")
                                except:
                                    ririn.sendText(msg.to,"ᴇʀʀᴏʀ")
            elif "Ban @" in msg.text:
               if msg._from in admin:
                if msg.toType == 2:
                    print("[Ban]ok")
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ririn.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ririn.sendText(msg.to,"ᴛᴀʀɢᴇᴛ ɴᴏᴛ ғᴏᴜɴᴅ")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendText(msg.to,"ᴛᴀʀɢᴇᴛ ʀᴇᴀᴅʏ")
                            except:
                                ririn.sendText(msg.to,"sᴜᴄᴄᴇs")
            elif "Unban @" in msg.text:
               if msg._from in admin:
                if msg.toType == 2:
                    print("[Unban]ok")
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ririn.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ririn.sendText(msg.to,"ᴛᴀʀɢᴇᴛ ɴᴏᴛ ғᴏᴜɴᴅ")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendText(msg.to,"sᴜᴄᴄᴇs")
                            except:
                                ririn.sendText(msg.to,"sᴜᴄᴄᴇs")
            elif msg.text in ["Kill ban"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ririn.sendText(msg.to,"ᴛʜᴇʀᴇ ᴡᴀs ɴᴏ ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")
                        return
                    for jj in matched_list:
                        ririn.kickoutFromGroup(msg.to,[jj])
                    ririn.sendText(msg.to,"ᴜʀ ғᴠᴄᴋɪɴɢ ʙɪᴛɔʜ")
            elif msg.text in ["Ban"]:
               if msg._from in admin:
                wait["wblacklist"] = True
                ririn.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Unban"]:
               if msg._from in admin:
                wait["dblacklist"] = True
                ririn.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
            elif msg.text in ["Banlist"]:
               if msg._from in admin:
                if wait["blacklist"] == {}:
                    ririn.sendText(msg.to,"ɴᴏᴛʜɪɴɢ")
                else:
                    ririn.sendText(msg.to,"ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ'")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ririn.getContact(mi_d).displayName + "\n"
                    ririn.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    ririn.sendText(msg.to,cocoa + "")
#-----------------------Key Owner-----------------------#
            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                ririn.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                ririn.sendText(msg.to,"Always Read Sudah Di Nonaktifkan") 

            elif msg.text in ["Glist"]:
               if msg._from in Owner:
                  dna1.sendText(msg.to,"「ɢʀᴏᴜᴘ」\nᴡᴀɪᴛɪɴɢ ғᴏʀ : ɢʀᴏᴜᴘ ʟɪsᴛ")
                  gid = ririn.getGroupIdsJoined()
                  h = ""
                  for i in gid:
                      h += "║○%s\n" % (ririn.getGroup(i).name+"\n║ᴍᴇᴍʙᴇʀs: "+str(len(ririn.getGroup(i).members)))
                  ririn.sendText(msg.to,"╔════[]·✪·ɢʀᴏᴜᴘ ʟɪsᴛ·✪·[]════\n" + h + "╠══════[ ✰ ᴛᴏᴛᴀʟ ✰ ]══════\n║" + str(len(gid)) + "\n╚═════[] ✯ ᴅɴᴀ ʙᴏᴛ ✯ []═════")
            elif msg.text in ["Restart"]:
               if msg._from in Owner:
                  ririn.sendText(msg.to, "ʙᴏᴛ ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇsᴛᴀʀt")
                  restart_program()
                  print ("Restart")
            elif msg.text in ["cancelinvite","Cancelinvite"]:
               if msg._from in Owner:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ririn.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,"ɴᴏ ᴏɴᴇ ɪs ɪɴᴠɪᴛɪɴɢ")
                        else:
                            ririn.sendText(msg.to,"sᴏʀʀʏ, ɴᴏʙᴏᴅʏ ᴀʙsᴇɴᴛ")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴄᴀɴ'ᴛ ʙᴇ ᴜsᴇᴅ ᴏᴜᴛsɪᴅᴇ ᴛʜᴇ ɢʀᴏᴜᴘ")
                    else:
                        ririn.sendText(msg.to,"ɴᴏᴛ ғᴏʀ ᴜsᴇ ʟᴇss ᴛʜᴀɴ ɢʀᴏᴜᴘ")
            elif msg.text in ["TL:"]:
               if msg._from in Owner:
               	tl_text = msg.text.replace("TL:","")
               	ririn.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ririn.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])                        

            elif "Cn " in msg.text:
               if msg._from in Owner:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ririn.getProfile()
                    profile.displayName = string
                    ririn.updateProfile(profile)
                    ririn.sendText(msg.to,"ᴜᴘᴅᴀᴛᴇ ɴᴀᴍᴇs" + string)
            elif "Mybio " in msg.text:
               if msg._from in Owner:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 100000000000000:
                    profile = ririn.getProfile()
                    profile.statusMessage = string
                    ririn.updateProfile(profile)
                    ririn.sendText(msg.to,"()ᴜᴘᴅᴀᴛᴇ ʙɪᴏ→" + string + "←")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
               if msg._from in Owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
               if msg._from in Owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Gcancel:"]:
               if msg._from in Owner:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,"ɪɴᴠɪᴛᴀᴛɪᴏɴ ʀᴇғᴜsᴇᴅ ᴛᴜʀɴᴇᴅ ᴏғғ\ɪɴᴛᴏ ᴛᴜʀɴ ᴏɴ ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ᴘᴇᴏᴘʟᴇ ᴀɴᴅ sᴇɴᴅ")
                        else:
                            ririn.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,strnum + "ᴛʜᴇ ɢʀᴏᴜᴘ ᴏғ ᴘᴇᴏᴘʟᴇ ᴀɴᴅ ʙᴇʟᴏᴡ ᴅᴇᴄɪᴅᴇᴅ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʀᴇғᴜsᴇ ɪɴᴠɪᴛᴀᴛɪᴏɴ")
                        else:
                            ririn.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴠᴀʟᴜᴇ ɪs ᴡʀᴏɴɢ")
                    else:
                        ririn.sendText(msg.to,"ʙɪᴢᴀʀʀᴇ ʀᴀᴛɪɴɢs")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
               if msg._from in Owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
               if msg._from in Owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
               if msg._from in Owner:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
               if msg._from in Owner:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
               if msg._from in Owner:
                gid = ririn.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ririn.getGroup(i).name,i)
                ririn.sendText(msg.to,h)
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
               if msg._from in Owner:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
               if msg._from in Owner:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
                    else:
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"ᴅᴏɴᴇ")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Come dna"]: 
              if msg._from in Owner:
                G = ririn.getGroup(msg.to)
                ginfo = ririn.getGroup(msg.to)
                G.preventedJoinByTicket = False
                ririn.updateGroup(G)
                invsend = 0
                Ticket = ririn.reissueGroupTicket(msg.to)
                dna1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna2.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna3.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna4.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna5.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna6.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna7.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna8.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                dna9.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = ririn.getGroup(msg.to)
                ginfo = ririn.getGroup(msg.to)
                G.preventedJoinByTicket = True
                ririn.updateGroup(G)
#--------------------------Group Bc Start-------------------------------------#
            elif "Group bc " in msg.text:
               if msg._from in Owner:
                  bctxt = msg.text.replace("Group bc ", "")
                  a = ririn.getGroupIdsJoined()
                  for manusia in a:
                    ririn.sendText(manusia, (bctxt))
#--------------------------Group Bc Finish------------------------------------#                      
            elif msg.text in ["Runtime"]:
               if msg._from in Owner:
                runtime = time.time()-startBot
                elapsed_time = format_timespan(time.time()-startBot)
                ririn.sendText(msg.to,"ʀᴜɴɴɪɴɢ ɪɴ %s" % (elapsed_time))
            elif msg.text in ["Clear ban"]:
                if msg._from in Owner:
                    wait["blacklist"] = {}
                    ririn.sendText(msg.to,"ᴅᴏɴᴇ")
            elif msg.text in ["Clear"]:
               if msg._from in Owner:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ririn.cancelGroupInvitation(msg.to,[_mid])
                    ririn.sendText(msg.to,"ɪ ᴘʀᴇᴛᴇɴᴅᴇᴅ ᴛᴏ ᴄᴀɴᴄᴇʟ ᴀɴᴅ ᴄᴀɴᴄᴇʟᴇᴅ.")
                    
            elif msg.text in ["Respontag on","Autorespon on","Respon on","respon on"]:
            	if msg._from in Owner:
            		wait['detectMention'] = True
            		ririn.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴛᴀɢ ᴏɴ")
                
            elif msg.text in ["Respontag off","Autorespon off","Respon off","respon off"]:
            	if msg._from in Owner:
                    wait['detectMention'] = False
                    ririn.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴛᴀɢ ᴏғғ")
            
            elif msg.text in ["Kicktag on","kicktag on","Responkick on","responkick on"]:
            	if msg._from in Owner:
                    wait['kickMention'] = True
                    ririn.sendText(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴛᴀɢ ᴏɴ")
                
            elif msg.text in ["Kicktag off","kicktag off","Responkick off","responkick off"]:
            	if msg._from in Owner:
                    wait['kickMention'] = False
                    ririn.sendText(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴛᴀɢ ᴏғғ")
                    
            elif msg.text in ["Admin add @"]:
              if msg._from in Owner:
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = ririn.getGroup(msg.to)
                gs = dna1.getGroup(msg.to)
                gs = dna2.getGroup(msg.to)
                gs = dna3.getGroup(msg.to)
                gs = dna4.getGroup(msg.to)
                gs = dna5.getGroup(msg.to)
                gs = dna6.getGroup(msg.to)
                gs = dna7.getGroup(msg.to)
                gs = dna8.getGroup(msg.to)
                gs = dna9.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ᴛɪᴅᴀᴋ ᴅɪ ᴛᴇᴍᴜᴋᴀɴ")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            ririn.sendText(msg.to,"ᴀᴅᴍɪɴ ᴅɴᴀ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ")
                        except:
                            pass
              else:
              	ririn.sendText(msg.to,"ᴄᴏᴍᴍᴀɴᴅ ᴅᴇɴɪᴇᴅ.")
              	ririn.sendText(msg.to,"ᴏᴡɴᴇʀ ᴘᴇʀᴍɪssɪᴏɴ ʀᴇǫᴜɪʀᴇᴅ.")
                
            elif msg.text in ["Admin remove @"]:
              if msg._from in Owner:
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ririn.getGroup(msg.to)
                gs = dna1.getGroup(msg.to)
                gs = dna2.getGroup(msg.to)
                gs = dna3.getGroup(msg.to)
                gs = dna4.getGroup(msg.to)
                gs = dna5.getGroup(msg.to)
                gs = dna6.getGroup(msg.to)
                gs = dna7.getGroup(msg.to)
                gs = dna8.getGroup(msg.to)
                gs = dna9.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ᴛɪᴅᴀᴋ ᴅɪ ᴛᴇᴍᴜᴋᴀɴ")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            ririn.sendText(msg.to,"ᴀᴅᴍɪɴ ᴅɴᴀ ᴅɪʜᴀᴘᴜs")
                        except:
                            pass
              else:
              	ririn.sendText(msg.to,"ᴄᴏᴍᴍᴀɴᴅ ᴅᴇɴɪᴇᴅ.")
              	ririn.sendText(msg.to,"ᴏᴡɴᴇʀ ᴘᴇʀᴍɪssɪᴏɴ ʀᴇǫᴜɪʀᴇᴅ.")
#----------------Fungsi Cek Sider-------------------#
        if op.type == 55:
        	try:
        		group_id = op.param1
        		user_id=op.param2
        		subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
        	except Exception as e:
        		print(e)
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ririn.getContact(op.param2).displayName
                            Name = dna1.getContact(op.param2).displayName
                            Name = dna2.getContact(op.param2).displayName
                            Name = dna3.getContact(op.param2).displayName
                            Name = dna4.getContact(op.param2).displayName
                            Name = dna5.getContact(op.param2).displayName
                            Name = dna6.getContact(op.param2).displayName
                            Name = dna7.getContact(op.param2).displayName
                            Name = dna8.getContact(op.param2).displayName
                            Name = dna9.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        random.choice(KAC).sendText(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                    else:
                                        random.choice(KAC).sendText(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                                else:
                                    random.choice(KAC).sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass      
#----------------Fungsi Cek Sider-------------------#
        if op.type == 59:
            print(op)


    except Exception as error:
        print(error)


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = ririn.getProfile()
                profile.displayName = wait["cName"]
                ririn.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)