#!/usr/bin/python3
# coding=utf-8

import android
import json
import time

from urllib import urlencode
from urllib2 import urlopen

hello_msg = "welcome to coache kelly's timeing app"
list_title = "here is you list of athletes:"
quit_msg = "Quitting coach kelly's app."

web_server = 'http://192.168.0.107:8080'

get_names_cgi = '/cgi-bin/generate_names.py'
get_data_cgi = '/cgi-bin/generate_data.py'

def send_to_server(url, post_data=None):
    if post_data:
        page = urlopen(url, urlencode(post_data))
        status_update(str(page))
    else:
        page = urlopen(url)
    return (page.read().decode("utf8"))


#create Android APP
app = android.Android()

#display short msg on the phone
def status_update(msg, how_long = 0.01):
    #app.makeToast(msg)
    time.sleep(how_long)

#say hello
status_update(hello_msg)

#send the web request to web server, load the data
athlete_names = sorted(json.loads(send_to_server(web_server + get_names_cgi)))

#create two button 
app.dialogCreateAlert(list_title)
app.dialogSetSingleChoiceItems(athlete_names)
app.dialogSetPositiveButtonText("Select")
app.dialogSetNegativeButtonText("Quit")
app.dialogShow()

#waiting for the user to tap 
resp = app.dialogGetResponse().result

#say bye 
status_update("Select")
if resp['which'] in ('positive'):
    status_update("Enter")
    selectd_athlete = app.dialogGetSelectedItems().result[0]
    which_athlete = athlete_names[selectd_athlete]
    status_update(str(which_athlete))
    athlete = json.loads(send_to_server(web_server + get_data_cgi, post_data = {'which_athlete': which_athlete}))
    status_update(str(athlete))

    athlete_title = athlete["Name"] + '(' + athlete['DOB'] +') , Top 3 times:'
    app.dialogCreateAlert(athlete_title)
    app.dialogSetItems(athlete["Top3"])
    app.dialogSetPositiveButtonText('ok')
    app.dialogShow()
    resp = app.dialogGetResponse().result
    
#say bye 
# status_update(quit_msg)


















