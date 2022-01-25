import discord
import requests
import os
from keep_alive import keep_alive
from datetime import datetime
client = discord.Client()
response = requests.get("https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-by-provinces")
data = response.json()
now = datetime.today()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  i = 0
  while message.content != data[i]["province"]:
    i=i+1
    if i == 77:
        pass
  a = i
  while str(data[i]["update_date"][0:10]) != str(now.date()) or data[a]["province"] != data[i]["province"]:
    i=i+1
    if i == len(data):
        i=i-77
        break
  while data[a]["province"] != data[i]["province"]:
    i = i+1
  if data[i]["province"] == message.content and data[i]["txn_date"] == data[i]["update_date"][0:10]:
    await message.channel.send("วันที่ update ล่าสุด: "+ data[i]["update_date"]+"\nจังหวัด: "+ data[i]["province"]+"\nผู้ติดเชื้อรายใหม่: "+str(data[i]["new_case"])+"\ncase โดยรวม: "+ str(data[i]["total_case"])+"\nผู้ติดเชื้อรายใหม่ที่ไม่ใช่จากต่างประเทศ: " + str(data[i]["new_case_excludeabroad"])+"\ncase โดยรวมที่ไม่ใช่จากต่างประเทศ: "+ str(data[i]["total_case_excludeabroad"])+"\nจำนวนผู้เสียชีวิตรายใหม่: "+ str(data[i]["new_death"])+"\nจำนวนผู้เสียชีวิตโดยรวม: " + str(data[i]["total_death"]))


  else:
    pass
 

keep_alive()
client.run(os.getenv('Token'))