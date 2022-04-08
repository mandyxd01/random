from time import sleep
from telethon import TelegramClient, events
from random import randint



api_id= 12149457
api_hash = "575877fb0c8586be1e91b618d44f07c5"

print("Starting Deployment..!")



client = TelegramClient('main_session', api_id, api_hash)


@client.on(events.NewMessage(pattern=r'\.for'))
async def runbollyhandler(event):
    messages_toSend = []
    dict = {

        -1001142224290: {},
        -1001782270836: {},
        -1001477756331: {},
        -1001198221154: {},
    }
    replied_msg = await event.get_reply_message()
    ran = 0
    chat = await event.get_chat()

    msg_id = replied_msg.id
    await client.delete_messages(chat, event.message)

    allmsg = await client.get_messages(chat, None, reverse=True, min_id=(msg_id-1))

    for msg in allmsg:
        messages_toSend.append(msg)
    messages_sent = 0

    while messages_sent < len(messages_toSend):
        #print("in loop 1 while message sent  = ",
              #messages_sent, len(messages_toSend))
        for ch in dict:
            print("loop2")
            c = 0
            while c < 10:
                if len(dict[ch].values()) == len(messages_toSend):
                    break
                ran = randint(0, len(messages_toSend) - 1)
                if not ran in dict[ch].values():
                    await client.send_message(ch, messages_toSend[ran])
                    c += 1
                    dict[ch][len(dict[ch].values())] = ran
        messages_sent = messages_sent + 10
        print("sleeping")
        sleep(200)
        print("wake")

    await client.send_message("@m3nd7", "All message sent")


          
print("Bot has been deployed.!")
client.start()
client.run_until_disconnected()
