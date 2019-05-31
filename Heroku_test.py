import discord
import asyncio
import ffmpeg
import glob




client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')






# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    user_report_channel = 583172383792431105
    send_report_channel = 583668837623267344
    role_channel = 583924369374445589

                      #Scald Bot test's test
    if message.channel.id == int(user_report_channel):
        #print("^^")
        messeezi = message.content
        channel = client.get_channel(int(send_report_channel))
        await channel.send(str(messeezi))
        await message.channel.purge()

    if message.channel.id == int(role_channel):
        if message.content == 'pc':
             role = discord.utils.get(message.guild.roles, name='pc')
             await message.author.add_roles(role)
             await message.channel.purge()
             await message.channel.send('使用デバイスを役職としてつけたい場合はこちらに使用デバイス名を**すべて小文字で**入力してください。※スマホの場合は**スマホ**で大丈夫です\n例：\npc')
        if message.content == 'ps4':
             role = discord.utils.get(message.guild.roles, name='ps4')
             await message.author.add_roles(role)
             await message.channel.purge()
             await message.channel.send('使用デバイスを役職としてつけたい場合はこちらに使用デバイス名を**すべて小文字で**入力してください。※スマホの場合は**スマホ**で大丈夫です\n例：\npc')
        if message.content == 'スマホ':
             role = discord.utils.get(message.guild.roles, name='スマホ')
             await message.author.add_roles(role)
             await message.channel.purge()
             await message.channel.send('使用デバイスを役職としてつけたい場合はこちらに使用デバイス名を**すべて小文字で**入力してください。※スマホの場合は**スマホ**で大丈夫です\n例：\npc')
        if message.content == 'switch':
             role = discord.utils.get(message.guild.roles, name='switch')
             await message.author.add_roles(role)
             await message.channel.purge()
             await message.channel.send('使用デバイスを役職としてつけたい場合はこちらに使用デバイス名を**すべて小文字で**入力してください。※スマホの場合は**スマホ**で大丈夫です\n例：\npc')
        if message.content != 'pc' or 'ps4' or 'スマホ' or 'switch':
            await message.channel.purge()
            await message.channel.send('使用デバイスを役職としてつけたい場合はこちらに使用デバイス名を**すべて小文字で**入力してください。※スマホの場合は**スマホ**で大丈夫です\n例：\npc')



client.run("NTgzMTM4NzExMTA1OTYxOTg3.XO4AYg.BBz3YCty-r8wRxmaj3LzcZEYR9M")
