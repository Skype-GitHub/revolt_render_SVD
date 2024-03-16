import revolt
import requests
import asyncio
import os

import always_on
import time


async def reconnect():
  while True:
    requests.get("https://ALSTL-R.ztttas11.repl.co/")
    await asyncio.sleep(60)



class Client(revolt.Client):
  
  async def on_ready(self):
    print('Run  ALSTL-R')
    await reconnect()
  


  async def on_message(self, message: revolt.Message):
    

    
      
    if message.content == ".!":
      await message.channel.send("botは正常です!")
    
    if message.content == "!svd":
      print('AL')
      for _ in range(50):
        await message.channel.send("https://autumn.revolt.chat/attachments/2PlNj2OIRXFulLko2A89x4s-cIRjlvjneldZyGIPt5/027cdc8e74424ea19922161c35befd5c_high.webp")
        await message.channel.send("https://autumn.revolt.chat/attachments/2PlNj2OIRXFulLko2A89x4s-cIRjlvjneldZyGIPt5/027cdc8e74424ea19922161c35befd5c_high.webp")
        await message.channel.send("https://autumn.revolt.chat/attachments/2PlNj2OIRXFulLko2A89x4s-cIRjlvjneldZyGIPt5/027cdc8e74424ea19922161c35befd5c_high.webp")
        await message.channel.send("https://autumn.revolt.chat/attachments/2PlNj2OIRXFulLko2A89x4s-cIRjlvjneldZyGIPt5/027cdc8e74424ea19922161c35befd5c_high.webp")
        await message.channel.send("https://autumn.revolt.chat/attachments/2PlNj2OIRXFulLko2A89x4s-cIRjlvjneldZyGIPt5/027cdc8e74424ea19922161c35befd5c_high.webp")

    
    



async def main():
  async with revolt.utils.client_session() as session:
    client = Client(session, os.environ['Revolt-TOKEN'])
    await client.start()
    





always_on.activate()

asyncio.run(main())
