#!/usr/bin/python
import json
import httplib
try:
    apikey = "aaf6f597dc43f93115c5aa01079bdd20"
    conn = httplib.HTTPConnection("localhost:8080")
    conn.request("GET","/sabnzbd/api?mode=queue&output=json&apikey="+apikey)
    jsonstr = conn.getresponse().read()
    sabqueue = json.loads(jsonstr)["queue"]
    sabcurrent = sabqueue["slots"][0]
    

    
    print "SabNZB"
    print "Status: "+sabqueue["status"]
    print "Current Item:"
    print "-----------------"
    sabcurrent["mbdone"] = float(sabcurrent["mb"])-float(sabcurrent["mbleft"])
    print sabcurrent["filename"]
    print  "ETA: "+sabcurrent["timeleft"]+"@"+sabqueue["kbpersec"]+"KB/s"
    print "MB Left: "+str(sabcurrent["mbleft"])+"/"+str(sabcurrent["size"])
    print "-----------------"
    print ""+str(sabqueue["noofslots"])+" Items in Queue"
    print "ETA: "+sabqueue["timeleft"]
    print "MB Left: "+sabqueue["mbleft"]
    if sabqueue["speedlimit"] != "":
        print "Speedlimit: "+ sabqueue["speedlimit"]+"KB/s"
except:
    pass