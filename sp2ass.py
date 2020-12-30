import speech_recognition as sr
#from demo_utils import *
#import resemblyzer
from pydub import AudioSegment
import datetime
#from googletrans import Translator
#from google_trans_new import google_translator  
import os
#from uuid import getnode as get_mac
from getmac import get_mac_address as gma
import base64
import ntplib
import shutil

#now = datetime.datetime.now()
c = ntplib.NTPClient()
response = c.request('pool.ntp.org')
now=datetime.datetime.fromtimestamp(response.tx_time)




#f=open("licenza.bin","rb")
#licenza=f.read().decode('utf-8')
#licenza=base64.b85decode(licenza)
#licenza=base64.b64decode(licenza)
#licenza=licenza.decode("utf-8")

#f.close()
#lice=licenza.split("\n")

#for lic in lice:
#    if lic.find("|")!=-1:
#        #print (lic)
#        lingua,scadenza,mac_add=lic.split("|");
#        if lingua=="EN" and datetime.datetime.strptime(scadenza, '%Y-%m-%d %H:%M:%S') > now:
#            EN="EN"
#            print("OK INGLESE")
#        if lingua=="DE" and datetime.datetime.strptime(scadenza, '%Y-%m-%d %H:%M:%S') > now:
#            DE="DE"
#            print("OK TEDESCO")
#        if lingua=="ES" and datetime.datetime.strptime(scadenza, '%Y-%m-%d %H:%M:%S') > now:
#            print("OK SPAGNOLO")
#            ES="ES"
#        if lingua=="FR" and datetime.datetime.strptime(scadenza, '%Y-%m-%d %H:%M:%S') > now:
#            print("OK FRANCESE")
#            FR="FR"
#
#        mac=gma()
#        if str(mac) != mac_add:
#            file_out="OUTPUT/LEGGIMI.TXT"
#            File = open(file_out,"w")
#            File.write ("LA LICENZA NON E' VALIDA PER QUESTO PC "+str(mac))
#            exit(-1)



#if EN=="" and DE=="" and FR=="" and ES=="":
#    file_out="OUTPUT/LEGGIMI.TXT"
#    File = open(file_out,"w")
#    File.write ("LA LICENZA E' SCADUTA IN DATA "+str(scadenza))
#    exit(-1)


    

cartella_in="INPUT"
working_dir="PROCESSING"
cartella_out="OUTPUT"
ins = os.listdir(cartella_in) #cartella INPUT FILE FOTOGRAFICI

print(len(ins))
for video in ins:
    #salvo traccia audio del video
    input_audio = working_dir+"/"+video[:-4]+".wav"
    os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}'.format(cartella_in+"/"+video, input_audio))


    #calcolo la durata della traccia audio
    audioi = AudioSegment.from_file(input_audio)
    duration=audioi.duration_seconds
    print (audioi.duration_seconds)



    r = sr.Recognizer()
    
    #carico il file audio
    wav = sr.AudioFile(input_audio)

    file_en="OUTPUT/"+video[:-4]+".txt"
    File_EN = open(file_en,"w")


    i=0
    a=1
    b=0
    off=10
    inizio=datetime.datetime.now()
    inizio=inizio-inizio


    while i<=duration+off+off:
        with wav as source:
            audio = r.record(source,offset=b,duration=off+1)
        try:    
            text=(r.recognize_google(audio, language="it-IT"))
        except:
            text="--"
    
        start=inizio
        stop=inizio+datetime.timedelta(0,off)
        print (str(start)+" --> "+str(stop))
        File_EN.write (str(start)+" --> "+str(stop)+"              "+text+"\n")
        #print(text+"\n")
        print (text+"\n")
        a=a+1
        i=i+off
        b=b+off-1
        inizio=inizio+datetime.timedelta(0,off)


    shutil.move(cartella_in+'/'+video, cartella_out+'/'+video)
