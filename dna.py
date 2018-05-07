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

#Khusus Login Token
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
╠❂➣ Id
╠❂➣ Mid
╠════════════════════╗
                ◄]·✪·Admin·✪·[►
╠════════════════════╝
╠❂➣ Tutup qr
╠❂➣ Buka qr
╠❂➣ Invite 「mid」
╠❂➣ Ginfo
╠❂➣ White 「mention」
╠❂➣ Restart
╠❂➣ Guest 「On/Off」
╠❂➣ Qr 「On/Off」
╠❂➣ Lurking 「On/Off/Reset」
╠❂➣ Read
╠❂➣ View
╠❂➣ Kill
╠❂➣ Group bc 「text」
╠❂➣ Contact bc 「text」
╠❂➣ List group
╠❂➣ Speed
╠❂➣ Runtime
╠❂➣ Tagall
╠════════════════════╗
                ◄]·✪·Owner·✪·[►
╠════════════════════╝
╠❂➣ Kiss 「mention」
╠❂➣ Kick 「mid」
╠❂➣ Bye dna
╠❂➣ Come dna
╠❂➣ Bye all
╠❂➣ Kill ban
╠❂➣ Ban 「mention」
╠❂➣ Unban 「mention」
╠❂➣ Banlist
╠❂➣ Clearban
╠❂➣ Respon/Absen
╠❂➣ Clear
╠❂➣ About
╠❂➣ Adminlist
╠❂➣ Ownerlist
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
    'joingc':"WELCOME",
    'leftgc':"Baper Njink... 😂😂😂",
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add me \n Creator line.me/ti/p/ppgIZ0JLDW",
    "lang":"JP",
    "comment":"Thanks for add me \n Creator line.me/ti/p/ppgIZ0JLDW",
    "commentOn":False,
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
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":True,
    "acck":False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "spamer":{},
    "CloseQR":True,
    "Protectguest":True,
    "Protectcancel":True,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

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

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        ririn.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

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

	#--------Open Qr Kick Start--------------#
        if op.type == 11:
            if wait["ProtectQR"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                      G = ririn.getGroup(op.param1)
                      ririn.updateGroup(G)
                      Ticket = ririn.reissueGroupTicket(op.param1)
                      random.choice(KAC).sendText(op.param1, "Jangan buka Qr Anjenk 😡😡😡")
                      dna10.acceptGroupInvitationByTicket(op.param1,Ticket)
                      dna10.kickoutFromGroup(op.param1,[op.param2])
                      dna10.leaveGroup(op.param1)
                      G = ririn.getGroup(op.param1)
                      G.preventedJoinByTicket = True
                      ririn.updateGroup(G)
	#--------Open Qr Kick Finish--------------#
	#--------Open Qr Auto Close---------------#
        if op.type == 11:
            if not op.param2 in Bots:
                if wait["CloseQR"] == True:
                  try:
                      kpist=[ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
                      puck=random.choice(kpist)
                      G = puck.getGroup(op.param1)
                      G.preventJoinByTicket = True
                      puck.updateGroup(G)
                  except Exception as e:
                      print(e)
	#--------Open Qr Auto Close---------------#
        if op.type == 13:
            if mid in op.param2:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots:
                       G = ririn.getGroup(op.param1)
                       ririn.acceptGroupInvitation(op.param1)
	#--------Invite User Kick Start-----------#
        if op.type == 13:
           if wait["Protectguest"] == True:
              if op.param2 not in admin:
                 if op.param2 not in Bots:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).sendText(op.param1, "Mau Ngundang Siapa Ka?\nKk Bukan Admin\nJadi Aku Cancel😛")
	#------Invite User Kick Finish------------#
	#------Join Kicked start------------------#
        if op.type == 17:
            if wait["acck"] == True:
                if op.param2 not in admin:
                    try:
                        contact = ririn.getContact(op.param2)
                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)
        #-------Join Kicked Finish----------------# 
	#-------Blacklist Join Kick Start---------#
        if op.type == 17:
           if op.param2 in wait["blacklist"]:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Kick Auto BL------------------------#
        if op.type == 19:
           if op.param2 not in admin:
              if op.param2 not in Bots:
                 if op.param2 not in wait["whitelist"]:
                    wait["blacklist"][op.param2] = True
                    print("kicker kicked")
                 else:
                    pass
        #--------------------Kick Auto Bl-------#
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
                    if op.param2 in mid:
                        X = dna5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna5.updateGroup(X)
                        Ti = dna5.reissueGroupTicket(op.param1)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna4.updateGroup(X)
                        Ti = dna4.reissueGroupTicket(op.param1)
                        
                if op.param3 in Emid:
                    if op.param2 in Amid:
                        G = dna6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        dna6.updateGroup(G)
                        Ticket = dna6.reissueGroupTicket(op.param1)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        dna5.updateGroup(G)
                        Ticket = dna5.reissueGroupTicket(op.param1)

                if op.param3 in Fmid:
                    if op.param2 in Bmid:
                        X = dna7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna7.updateGroup(X)
                        Ti = dna7.reissueGroupTicket(op.param1)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna6.updateGroup(X)
                        Ti = dna6.reissueGroupTicket(op.param1)

                if op.param3 in Gmid:
                    if op.param2 in Cmid:
                        X = dna8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna8.updateGroup(X)
                        Ti = dna8.reissueGroupTicket(op.param1)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna7.updateGroup(X)
                        Ti = dna7.reissueGroupTicket(op.param1)
                        
                if op.param3 in Hmid:
                    if op.param2 in Dmid:
                        X = dna9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        dna9.updateGroup(X)
                        Ti = dna9.reissueGroupTicket(op.param1)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        dna8.updateGroup(X)
                        Ti = dna8.reissueGroupTicket(op.param1)

                if op.param3 in Dmid:
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

        if op.type == 19:
           if op.param2 not in Bots:
               try:
                   ririn.kickoutFromGroup(op.param1,[op.param2])
               except:
                   try:
                       random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                       random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                   except:
                       print ("bot Aktif")

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
                       print ("bot bekerja")

        if op.type == 19: #bot Ke Kick
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
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
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
	#-------------------------------------#
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
                            ririn.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ririn.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ririn.like(url[25:58], url[66:], likeType=1001)
#============================================================#
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ririn.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ririn.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ririn.sendText(msg.to,"deleted")
                        dna1.sendText(msg.to,"deleted")
                        dna2.sendText(msg.to,"deleted")
                        dna3.sendText(msg.to,"deleted")
                        dna4.sendText(msg.to,"deleted")
                        dna5.sendText(msg.to,"deleted")
                        dna6.sendText(msg.to,"deleted")
                        dna7.sendText(msg.to,"deleted")
                        dna8.sendText(msg.to,"deleted")
                        dna9.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        ririn.sendText(msg.to,"It is not in the black list")
                        dna1.sendText(msg.to,"It is not in the black list")
                        dna2.sendText(msg.to,"It is not in the black list")
                        dna3.sendText(msg.to,"It is not in the black list")
                        dna4.sendText(msg.to,"It is not in the black list")
                        dna5.sendText(msg.to,"It is not in the black list")
                        dna6.sendText(msg.to,"It is not in the black list")
                        dna7.sendText(msg.to,"It is not in the black list")
                        dna8.sendText(msg.to,"It is not in the black list")
                        dna9.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ririn.sendText(msg.to,"already")
                        dna1.sendText(msg.to,"already")
                        dna2.sendText(msg.to,"already")
                        dna3.sendText(msg.to,"already")
                        dna4.sendText(msg.to,"already")
                        dna5.sendText(msg.to,"already")
                        dna6.sendText(msg.to,"already")
                        dna7.sendText(msg.to,"already")
                        dna8.sendText(msg.to,"already")
                        dna9.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ririn.sendText(msg.to,"aded")
                        dna1.sendText(msg.to,"aded")
                        dna2.sendText(msg.to,"aded")
                        dna3.sendText(msg.to,"aded")
                        dna4.sendText(msg.to,"aded")
                        dna5.sendText(msg.to,"aded")
                        dna6.sendText(msg.to,"aded")
                        dna7.sendText(msg.to,"aded")
                        dna8.sendText(msg.to,"aded")
                        dna9.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ririn.sendText(msg.to,"deleted")
                        dna1.sendText(msg.to,"deleted")
                        dna2.sendText(msg.to,"deleted")
                        dna3.sendText(msg.to,"deleted")
                        dna4.sendText(msg.to,"deleted")
                        dna5.sendText(msg.to,"deleted")
                        dna6.sendText(msg.to,"deleted")
                        dna7.sendText(msg.to,"deleted")
                        dna8.sendText(msg.to,"deleted")
                        dna9.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        ririn.sendText(msg.to,"It is not in the black list")
                        dna1.sendText(msg.to,"It is not in the black list")
                        dna2.sendText(msg.to,"It is not in the black list")
                        dna3.sendText(msg.to,"It is not in the black list")
                        dna4.sendText(msg.to,"It is not in the black list")
                        dna5.sendText(msg.to,"It is not in the black list")
                        dna6.sendText(msg.to,"It is not in the black list")
                        dna7.sendText(msg.to,"It is not in the black list")
                        dna8.sendText(msg.to,"It is not in the black list")
                        dna9.sendText(msg.to,"It is not in the black list")
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
            elif msg.text in ["Keyword","help","Help"]:
                if wait["lang"] == "JP":
                    ririn.sendText(msg.to,helpMessage)
                else:
                    ririn.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
               if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    ririn.updateGroup(X)
                else:
                    ririn.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Kick ","")
                ririn.kickoutFromGroup(msg.to,[midd])
            elif "Kick2 " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Kick2 ","")
                dna1.kickoutFromGroup(msg.to,[midd])
            elif "Kick3 " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Kick3 ","")
                dna2.kickoutFromGroup(msg.to,[midd])
            elif "Kick4 " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Kick4 ","")
                dna3.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Invite ","")
                ririn.findAndAddContactsByMid(midd)
                ririn.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["List grup","List group","list grup","list group"]:
               if msg._from in Owner:
                  dna1.sendText(msg.to,"「Group」\n\nWaiting for : Group List")
                  gid = ririn.getGroupIdsJoined()
                  h = ""
                  for i in gid:
                      h += "║○%s\n" % (ririn.getGroup(i).name+"\n║Members: "+str(len(ririn.getGroup(i).members)))
                  ririn.sendText(msg.to,"╔═════¤|{ List Grup }|¤═════\n" + h + "╠═══════[  Total  ]════════\n║" + str(len(gid)) + "\n╚════════════════════")
            elif msg.text in ["Restart"]:
               if msg._from in Owner:
                  ririn.sendText(msg.to, "Bot Have Been Restart")
                  restart_program()
                  print ("Restart")
            elif msg.text in ["cancelinvite","Cancelinvite"]:
               if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ririn.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,"No one is inviting")
                        else:
                            ririn.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print ririn.getGroup(msg.to)
                ##ririn.sendMessage(msg)
            elif msg.text in ["Ourl","ourl"]:
               if msg._from in admin:
               	if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Done")
                    else:
                        ririn.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventedJoinByTicket = True
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        ririn.sendText(msg.to,"Sudah Tertutup")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
              else:
                  ririn.sendText(msg.to,"Perintah Ditolak.")
                  ririn.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif msg.text == "Ginfo":
               if msg._from in admin:
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
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        ririn.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        ririn.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                ririn.sendText(msg.to,msg.to)
            elif msg.text in ["Mid ku","mid ku","My mid","Mid saya"]:
                ririn.sendText(msg.to,msg._from)
            elif msg.text in ["Me"]:
                ririn.sendContact(msg.to,msg._from)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                ririn.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ririn.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Cn " in msg.text:
               if msg._from in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ririn.getProfile()
                    profile.displayName = string
                    ririn.updateProfile(profile)
                    ririn.sendText(msg.to,"Update Names " + string)
            elif "Mybio " in msg.text:
               if msg._from in admin:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 100000000000000:
                    profile = ririn.getProfile()
                    profile.statusMessage = string
                    ririn.updateProfile(profile)
                    ririn.sendText(msg.to,"()Update Bio→" + string + "←")
            elif msg.text in ["Pc On","pc on"]:
               if msg._from in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect Cancel On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"protect cancel On")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Pc Off","pc off"]:
               if msg._from in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect Cancel Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                         ririn.sendText(msg.to,"protect cancel  Off")
                    else:
                         ririn.sendText(msg.to,"done")
            elif msg.text in ["Guest on","guest on"]:
               if msg._from in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Guest Stranger On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Guest Stranger On")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
               if msg._from in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Guest Stranger Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                         ririn.sendText(msg.to,"Guest Stranger Off")
                    else:
                         ririn.sendText(msg.to,"done")
            elif msg.text in ["CloseQR On","closeqr on"]:
               if msg._from in admin:
                if wait["CloseQR"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["CloseQR"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR ON")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["CloseQR Off","closeqr off"]:
               if msg._from in admin:
                if wait["CloseQR"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["CloseQR"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Acc on","acc on","A on","a on"]:
               if msg._from in admin:
                if wait["acck"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Udah aktif kak")
                    else:
                        ririn.sendText(msg.to,"Done")
                else:
                    wait["acck"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Anti Join Mode on")
                    else:
                        ririn.sendText(msg.to,"Done")
            elif msg.text in ["Acc off","acc off","A off","a off"]:
               if msg._from in admin:
                if wait["acck"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Sudah off kak")
                    else:
                        ririn.sendText(msg.to,"Done")
                else:
                    wait["acck"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Anti Join Mode off")
                    else:
                        ririn.sendText(msg.to,"Done")
            elif msg.text in ["Qr On","qr on"]:
               if msg._from in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect QR On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect QR ON")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Qr Off","qr off"]:
               if msg._from in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
               if msg._from in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
               if msg._from in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
               if msg._from in Owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
               if msg._from in Owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
               if msg._from in Owner:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            ririn.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            ririn.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Value is wrong")
                    else:
                        ririn.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
               if msg._from in Owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
               if msg._from in Owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
               if msg._from in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
               if msg._from in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set","Status"]:
               if msg._from in admin:
                md = ""
                if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                else: md+=" Protect Cancel : off\n"
                if wait["ProtectQR"] == True: md+=" Protect QR	    : on\n"
                else: md+=" Protect QR	 : off\n"
                if wait["CloseQR"] == True: md+=" Closed QR : on\n"
                else: md+=" CloseQR   : off\n"
                if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                else: md+=" Block Invite : off\n"
                if wait["contact"] == True: md+=" Contact : on\n"
                else: md+=" Contact : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share : on\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                ririn.sendText(msg.to,md)
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
               if msg._from in admin:
                gid = ririn.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ririn.getGroup(i).name,i)
                ririn.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
               if msg._from in admin:
                gid = ririn.getGroupIdsInvited()
                for i in gid:
                    ririn.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ririn.sendText(msg.to,"All invitations have been refused")
                else:
                    ririn.sendText(msg.to,"Semua grup sudah dibatalkan")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
               if msg._from in Owner:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
               if msg._from in Owner:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Buka qr","Open qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        ririn.sendText(msg.to,"Sudah Terbuka")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
              else:
                  ririn.sendText(msg.to,"Perintah Ditolak.")
                  ririn.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
#-----------------------#-----------------------#-----------------------#-----------------------#
            elif msg.text in ["Cloneprofile"]:
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        contact = mention["M"]
                        break
                    try:
                        ririn.cloneContactProfile(contact)
                        dna1.cloneContactProfile(contact)
                        dna2.cloneContactProfile(contact)
                        dna3.cloneContactProfile(contact)
                        dna4.cloneContactProfile(contact)
                        dna5.cloneContactProfile(contact)
                        dna6.cloneContactProfile(contact)
                        dna7.cloneContactProfile(contact)
                        dna8.cloneContactProfile(contact)
                        dna9.cloneContactProfile(contact)
                        ririn.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                    except:
                        boteater.sendMessage(msg.to, "Gagal clone member")
#-----------------------#-----------------------#-----------------------#-----------------------#                 
            elif msg.text in ["Clonecontact"]:
                wait["copy"] = True
                ririn.sendMessage(msg.to, "SEND CONTACT TO CLONE!!!")
#-------------------------------- Change Picture ---------------------------------#
            elif msg.text in ["Changepp"]:
                wait["changePictureProfile"] = True
                ririn.sendMessage(msg.to, "Silahkan kirim gambarnya")
            elif msg.text in ["Changegpp"]:
                if msg.toType == 2:
                    if to not in settings["changeGroupPicture"]:
                        wait["changeGroupPicture"].append(to)
                    ririn.sendMessage(msg.to, "Silahkan kirim gambarnya")
#-----------------------------------------------------------------#                    
            elif msg.toType == 1:
                if wait["changePictureProfile"] == True:
                    path = ririn.downloadObjectMsg(msg_id)
                    path = dna1.downloadObjectMsg(msg_id)
                    path = dna2.downloadObjectMsg(msg_id)
                    path = dna3.downloadObjectMsg(msg_id)
                    path = dna4.downloadObjectMsg(msg_id)
                    path = dna5.downloadObjectMsg(msg_id)
                    path = dna6.downloadObjectMsg(msg_id)
                    path = dna7.downloadObjectMsg(msg_id)
                    path = dna8.downloadObjectMsg(msg_id)
                    path = dna9.downloadObjectMsg(msg_id)
                    wait["changePictureProfile"] = False
                    irene.updateProfilePicture(path)
                    dna1.updateProfilePicture(path)
                    dna2.updateProfilePicture(path)
                    dna3.updateProfilePicture(path)
                    dna4.updateProfilePicture(path)
                    dna5.updateProfilePicture(path)
                    dna6.updateProfilePicture(path)
                    dna7.updateProfilePicture(path)
                    dna8.updateProfilePicture(path)
                    dna9.updateProfilePicture(path)
                    irene.sendMessage(msg.to, "Berhasil mengubah foto profile")
                if msg.toType == 2:
                    if to in wait["changeGroupPicture"]:
                        path = irene.downloadObjectMsg(msg_id)
                        wait["changeGroupPicture"].remove(msg.to)
                        irene.updateGroupPicture(msg.to, path)
                        irene.sendMessage(msg.to, "Berhasil mengubah foto group")           
#-------------------------------- Lurking ---------------------------------#
            elif msg.text in ["Lurking on"]:
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
                if receiver in read['readPoint']:
                    try:
                        del read['readPoint'][receiver]
                        del read['readMember'][receiver]
                        del read['setTime'][receiver]
                    except:
                        pass
                    read['readPoint'][receiver] = msg_id
                    read['readMember'][receiver] = ""
                    read['setTime'][receiver] = readTime
                    read['ROM'][receiver] = {}
                    ririn.sendMessage(receiver,"Lurking telah diaktifkan")
                else:
                    try:
                        del read['readPoint'][receiver]
                        del read['readMember'][receiver]
                        del read['setTime'][receiver]
                    except:
                        pass
                    read['readPoint'][receiver] = msg_id
                    read['readMember'][receiver] = ""
                    read['setTime'][receiver] = readTime
                    read['ROM'][receiver] = {}
                    ririn.sendMessage(receiver,"Set reading point : \n" + readTime)
                    
            elif msg.text in ["Lurking off"]:
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
                if receiver not in read['readPoint']:
                    ririn.sendMessage(receiver,"Lurking telah dinonaktifkan")
                else:
                    try:
                        del read['readPoint'][receiver]
                        del read['readMember'][receiver]
                        del read['setTime'][receiver]
                    except:
                        pass
                    ririn.sendMessage(receiver,"Delete reading point : \n" + readTime)
        
            elif msg.text in ["Lurking reset"]:
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
                if msg.to in read["readPoint"]:
                    try:
                        del read["readPoint"][msg.to]
                        del read["readMember"][msg.to]
                        del read["setTime"][msg.to]
                        del read["ROM"][msg.to]
                    except:
                        pass
                    read['readPoint'][receiver] = msg_id
                    read['readMember'][receiver] = ""
                    read['setTime'][receiver] = readTime
                    read['ROM'][receiver] = {}
                    ririn.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                else:
                    ririn.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
#-----------------------------------------------
            elif msg.text in ["Read On","read on","Read on"]:
                if msg._from in admin:
                    if msg.to in wait2['readPoint']:
                            try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                                del wait2['setTime'][msg.to]
                            except:
                                pass
                            wait2['readPoint'][msg.to] = msg.id
                            wait2['readMember'][msg.to] = ""
                            wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            wait2['ROM'][msg.to] = {}
                            with open('sider.json', 'w') as fp:
                             json.dump(wait2, fp, sort_keys=True, indent=4)
                             ririn.sendText(msg.to,"Setpoint already on")
                    else:
                        try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                                del wait2['setTime'][msg.to]
                        except:
                              pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         ririn.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
    
                        
            elif msg.text in ["Read Off","read off","Read off"]:
                if msg._from in admin:
                    if msg.to not in wait2['readPoint']:
                        ririn.sendText(msg.to,"Setpoint already off")
                    else:
                        try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                                del wait2['setTime'][msg.to]
                        except:
                              pass
                        ririn.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                                             
              
            elif msg.text in ["View","view"]:
                if msg._from in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                             ririn.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])                       
                            cmem = ririn.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={"MENTION":str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        msg.contentMetadata = lol
                        try:
                          ririn.sendMessage(msg)
                        except Exception as error:
                          pass
                        else:
                            ririn.sendText(msg.to, "Lurking has not been set.")
#-----------------------------------------------
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
                    ririn.sendMessage(msg.to, "Total {} Mention".format(str(len(nama))))
                    
#----------------------------------Office dna bot------------------------------#
            elif msg.text in ["About","about"]:
                try:
                    arr = []
                    owner = "ueca4120a9d7b0e4a9e7f4f1b1b96a436"
                    creator = ririn.getContact(owner)
                    contact = ririn.getContact(mid)
                    grouplist = ririn.getGroupIdsJoined()
                    contactlist = ririn.getAllContactIds()
                    blockedlist = ririn.getBlockedContactIds()
                    ret_ = "╔══[ About Bot ]"
                    ret_ += "\n╠ Line : {}".format(contact.displayName)
                    ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                    ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                    ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                    ret_ += "\n╠══[ About Dna Bot ]"
                    ret_ += "\n╠ Version : Premium"
                    ret_ += "\n╠ Creator : {}".format(creator.displayName)
                    ret_ += "\n╚══[ Don't be Remake :P ]"
                    ririn.sendContact(msg.to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
                    ririn.sendMessage(msg.to, str(ret_))
                except Exception as e:
                    ririn.sendMessage(msg.to, str(e))                    
#-------------------------------------------------------------------------------      
            elif msg.text in ["Ownerlist","ownerlist"]:
                try:
                    arr = []
                    owner = "ueca4120a9d7b0e4a9e7f4f1b1b96a436"
                    creator = ririn.getContact(owner)
                    ret_ = "╔════════════════\n╠✪➣  ✰ ᴅɴᴀ ʙᴏᴛ ✰"
                    ret_ += "\n╠══✪〘Owner  List〙✪═══"
                    ret_ += "\n╠✪ Ownerlist : {}".format(creator.displayName)
                    ret_ += "\n╠════════════════"
                    ret_ += "\n╠✪〘 line.me/ti/p/ppgIZ0JLDW 〙"
                    ret_ += "\n╚════════════════"
                    ririn.sendContact(msg.to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
                    ririn.sendMessage(msg.to,"Loading...")
                    ririn.sendMessage(msg.to, str(ret_))
                except Exception as e:
                    ririn.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
            elif msg.text in ["Adminlist","adminlist"]:
                if msg._from in Owner:
                    if admin == []:
                        ririn.sendMessage(msg.to,"The Adminlist is empty")
                    else:
                        ririn.sendMessage(msg.to,"Loading...")
                        mc = "╔════════════════\n╠✪➣  ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╠══✪〘Admin  List〙✪═══\n"
                        for mi_d in admin:
                            mc += "╠✪ " +ririn.getContact(mi_d).displayName + "\n"
                        ririn.sendMessage(msg.to,mc + "╠════════════════\n╠✪〘 line.me/ti/p/ppgIZ0JLDW 〙\n╚════════════════")
                    
#----------------------------------Panggil Semua Bot------------------------------#
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
#-----------------------Leave Group Bot---------------------------------------#
            elif msg.text in ["Kill"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = dna1.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ririn.sendText(msg.to,"Fvck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#--------------------------Group Bc Start-------------------------------------#
            elif "Group bc " in msg.text:
               if msg._from in Owner:
                  bctxt = msg.text.replace("Group bc ", "")
                  a = ririn.getGroupIdsJoined()
                  for manusia in a:
                    ririn.sendText(manusia, (bctxt))
#--------------------------------#
            elif ".call " in msg.text:
               if msg._from in Owner:
                try:
                    _name = msg.text.replace(".call ","")                	
                    r = requests.get('https://farzain.xyz/api/prank().php?apikey=&id='+call+'&type=2')
                    sendMention(receiver, "@! Sukses melakukan panggilan ke nomor  "+call,[sender])
                except Exception as e:
                    ririn.sendMessage(receiver, str(e))
                    logError(e)

            elif ".sms " in msg.text:
               if msg._from in Owner:            	
                try:
                    _name = msg.text.replace(".sms ","")                	
                    r = requests.get('https://farzain.xyz/api/prank().php?apikey=&id='+sms+'&type=1')
                    sendMention(receiver, "@! Sukses mengirim pesan ke nomor  "+sms,[sender])
                except Exception as e:
                    ririn.sendMessage(receiver, str(e))
                    logError(e)
#--------------------------Group Bc Finish------------------------------------#
            elif "Kick all" in msg.text:
               if msg._from in owner:
                if msg.toType == 2:
                    print("ok")
                    _name = msg.text.replace("Salken Ya","")
                    gs = dna1.getGroup(msg.to)
                    gs = dna2.getGroup(msg.to)
                    gs = dna3.getGroup(msg.to)
                    ririn.sendText(msg.to,"⚠DENG DENG DENG DENG !⚠")
                    ririn.sendText(msg.to,"JANGAN PANIK SEMUA PINTU KELUAR ADA DI POJOK KANAN🔫")
                    ririn.sendText(msg.to,"CEPET TANGKIS GOBLOK JANGAN DILIATIN NTAR GRUP LU RATA GOBLOK")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ririn.sendText(msg.to,"Tidak Ditemukan.")
                    else:
                        for target in targets:
                          if not target in admin and Bots:
                            try:
                                klist=[ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ririn.sendText(msg.to,"Grup Bersih")                                     
                                
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
                          sendMessage(msg.to,"user does not exist")
                          pass
                       else:
                          for target in targets:
                             try:
                               dna1.sendText(msg.to,"Semoga kau bahagia di Neraka 👹👹")
                               dna10.kickoutFromGroup(msg.to,[target])
                               print (msg.to,[g.mid])
                             except:
                               dna10.leaveGroup(msg.to)
                               gs = ririn.getGroup(msg.to)
                               gs.preventedJoinByTicket = True
                               ririn.updateGroup(gs)
                               gs.preventedJoinByTicket(gs)
                               ririn.updateGroup(gs)             
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
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    dna1.sendText(msg.to,"Bye")
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
                            ririn.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ririn.sendText(msg.to,"Succes Cv")
                                except:
                                    ririn.sendText(msg.to,"error")
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
                        ririn.sendText(msg.to,"Target Tidak Djtemukan")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendText(msg.to,"Target Siap")
                            except:
                                ririn.sendText(msg.to,"Berhasil")
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
                        ririn.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendText(msg.to,"Succes Cv")
                            except:
                                ririn.sendText(msg.to,"Succes Cv")
#----------------------------------------------------------------------------#
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
#----------------------------------------------------------------------------#
            elif msg.text in ["Absen","absen"]:
                if msg._from in admin:
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
#-----------------------------------------------------------------------------
            elif msg.text in ["Sp","sp"]:
                ririn.sendText(msg.to, "Process Waiting...")
                sp = int(round(time.time() *1000))
                ririn.sendText(msg.to,"my speed : %sms" % (sp - op.createdTime))
#---------------------------------------------------------------------
            elif msg.text in ["Speed","speed"]:
                start = time.time()
                ririn.sendText(msg.to, "Proccess...")
                elapsed_time = time.time() - start
                ririn.sendText(msg.to, "Kecepatan mengirim pesan: %sms" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Runtime"]:
               if msg._from in admin:
                runtime = time.time()-startBot
                elapsed_time = format_timespan(time.time()-startBot)
                ririn.sendText(msg.to,"Running in %s" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
               if msg._from in admin:
                wait["wblacklist"] = True
                ririn.sendText(msg.to,"Kirim Kontak")
            elif msg.text in ["Unban"]:
               if msg._from in admin:
                wait["dblacklist"] = True
                ririn.sendText(msg.to,"Kirim Kontak")
            elif msg.text in ["Banlist"]:
               if msg._from in admin:
                if wait["blacklist"] == {}:
                    ririn.sendText(msg.to,"nothing")
                else:
                    ririn.sendText(msg.to,"Blacklist user")
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
            elif msg.text in ["Clear ban"]:
                if msg._from in admin:
                    wait["blacklist"] = {}
                    ririn.sendText(msg.to,"Done")
            elif msg.text in ["Kill ban"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ririn.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ririn.kickoutFromGroup(msg.to,[jj])
                    ririn.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ririn.cancelGroupInvitation(msg.to,[_mid])
                    ririn.sendText(msg.to,"I pretended to cancel and canceled.")
#------------------------------------------------------------#
        if op.type == 17:
          if op.param2 in Bots:
              gmasok = ririn.getGroup(op.param1)
              contact = ririn.getContact(op.param2)
              image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
              ririn.sendImageWithURL(op.param1, image)
              ririn.sendMessage(msg.to, "WELCOME  " + ririn.getContact(op.param1).displayName + "\n Welcome to"+"\nGroup" + str(gmasok.name))
              randhom.choice(KAC).sendText(op.param1,"Jangan Lupa Check Note ya\nAwas kalau Baper😘😘😘")
        if op.type == 15:
          if op.param2 in Bots:
             return
          random.choice(KAC).sendText(op.param1, "Baper dia njink 🤣🤣🤣")
#----------------Fungsi Cek Sider-------------------#
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = ririn.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              ririn.sendText
          except:
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
