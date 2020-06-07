# インストールした discord.py を読み込む
import discord

TOKEN = 'NzE4MjQ1NDg0NTA1ODU4MTA4.Xtmulw.zLo5__hS8dqOo0QhrUhkD8bn4t4'

# 接続に必要なオブジェクトを生成
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
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

@client.event
async def on_message(message):
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('塵一つ残らないね！')
        else:
            await message.channel.send('何様のつもり？')

ID_CHANNEL_WELCOME = 717718442341564507 # 入室用チャンネルのID(int)
ID_ROLE_WELCOME = 717624993155907625 # 付けたい役職のID(int)
EMOJI_WELCOME = '✅' # 対応する絵文字

# 役職を付与する非同期関数を定義
@client.event
async def grant_role(payload):
    # 絵文字が異なる場合は処理を打ち切る
    if payload.emoji.name != EMOJI_WELCOME: 
        return

    # チャンネルが異なる場合は処理を打ち切る
    channel = client.get_channel(payload.channel_id)
    if channel.id != ID_CHANNEL_README:
        return

    # Member オブジェクトと Role オブジェクトを取得して役職を付与
    member = channel.guild.get_member(payload.user_id)
    role = guild.get_role(ID_ROLE_WELCOME)
    await member.add_roles(role)
    return member

# リアクション追加時に実行されるイベントハンドラを定義
@client.event
async def on_raw_reaction_add(payload):
    # 役職を付与する非同期関数を実行して Optional[Member] オブジェクトを取得
    member = await grant_role(payload)
    if member is not None: # 役職を付与したメンバーがいる時
        text = f'{member.mention} ようこそ！'
        await message.channel.send(text)



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
