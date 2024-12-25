from os import _exit

def generateErrorLog():
    from datetime import datetime
    from sys import exc_info
    now = datetime.now()
    filename = f"venom_error_{now.strftime('%Y%m%d%H%M%S')}.txt"
    with open(filename, "w") as venomErrorLog:
        venomErrorLog.write(str(exc_info()))
    return filename

def venom():
    from telethon import TelegramClient, events

    apiId   = "" # Ваши данные
    apiHash = "" # Ваши данные

    client = TelegramClient("venom", apiId, apiHash)

    @client.on(events.NewMessage)
    async def handler(event):
        me = await client.get_me()
        if event.is_private and event.sender_id != me.id: # Триггер только если сообщение в лс и оно входящее
            await event.reply("venom")
            await client.send_file(event.chat_id, "venom.gif")
            
    with client:
        client.run_until_disconnected()

if __name__ == "__main__":
    try:
        venom()
    except KeyboardInterrupt:
        _exit(0)
    except Exception as e:
        print(f"Ошибка: {e}")
        print(f"Подробнее в {generateErrorLog()}") 
        _exit(1)
