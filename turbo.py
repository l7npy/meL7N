from telethon.tl.functions.channels import JoinChannelRequest
from telethon import events
from new import *
from config import *
from fil import *


turbo.start()


@turbo.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@turbo.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    await turbo(JoinChannelRequest("𝐋7𝐍 «𓆩ᶠᵁᴿᵞ𓆪» ™ "))
    await turbo.send_file(event.chat.id, "https://t.me/yyyyyy3w/8", caption=f'''
•⌯ 𝐹𝑈𝑅𝑌 𝐶𝐻𝐸𝐶𝐾𝐸𝑅 𝐼𝑆 𝑊𝑂𝑅𝐾𝐼𝑁𝐺   
•⌯ 𝐷𝐸𝑉𝐸𝐿𝑂𝑃𝐸𝑅  ❲ @g_4_q ❳‌‌ - 
•⌯ 𝐶𝐻𝐴𝑁𝑁𝐸𝐿  ❲ @N1FURY ❳‌‌ -  
•⌯ 𝑅𝐸𝐿𝐸𝐴𝑆𝐸   :  ❲ 1.2 ❳‌‌ - 
•⌯ 𝑇𝐻𝐴𝑁𝐾 𝑌𝑂𝑈 𝐹𝑂𝑅 𝐴𝐶𝑇𝐼𝑉𝐴𝑇𝐼𝑂𝑁 
''')

@turbo.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف الصيد"))
async def update(event):
    await event.edit("جارِ ايقاف الصيد  ✿\n انتضࢪ 2 دقيقه Π \n @N1FURY - @g_4_q")
    await turbo.disconnect()
    await turbo.send_message("me", "`تم ايقاف الصيد !`")


turbo.run_until_disconnected()