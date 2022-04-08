from time import sleep
from telethon import TelegramClient, events
from threading import Thread

running = False

api_id = 14295855
api_hash = 'd7c97d558577a8633485c557a41174ef'
to = [-1001771051573]
From = -1001718455782

client = TelegramClient('session_name1', api_id, api_hash)


@client.on(events.NewMessage(pattern=r'\.stopmsg3'))
async def stophandler(event):
    global running
    running = False
    await client.edit_message(event.message, "STOPPED3")


# // bollywood
@client.on(events.NewMessage(pattern=r'\.getmsg3'))
async def runbollyhandler(event):
    global running
    running = True
    replied_msg = await event.get_reply_message()
    to_chat = to
    c = 0
#     chat = await event.get_chat()

    chat = From
    msg_id = replied_msg.id
    await client.delete_messages(chat, event.message)

    while running:
        allmsg = await client.get_messages(chat, None, reverse=True, min_id=msg_id, max_id=(msg_id + 5))
        for msg in allmsg:
            for i in to_chat:
                if running == True:
                    await client.send_message(i, msg)
                else:
                    return
            c = c + 1
            print(msg_id)
            if c == 5:
                c = 0
                msg_id = msg_id + 5
                sleep(3600)


client.start()
client.run_until_disconnected()
