import discord
from discord.ext import commands
import datetime
from zoneinfo import ZoneInfo

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
moscow_tz = ZoneInfo('Europe/Moscow')

user_voice_times = {}

VOICE_LOG_CHANNEL_ID = 1382921637976084500 
VOICE_CHANNEL_ID = 1382897566479552575     
ROLE_LOG_CHANNEL_ID =1382945119308746803
TARGET_ROLE_ID = 1382921497835995206

@bot.event
async def on_voice_state_update(member, before, after):
    channel = bot.get_channel(VOICE_LOG_CHANNEL_ID)
    role_log_channel = bot.get_channel(ROLE_LOG_CHANNEL_ID)
    if channel is None:
        print("Текстовый канал для логов не найден!")
        return
    if role_log_channel is None:
        print("Текстовый канал для логов по ролям не найден!")
        return


    def count_members_with_role(vc_channel, role_id):
        return sum(1 for m in vc_channel.members if any(r.id == role_id for r in m.roles))

    # Вход в указанный голосовой канал
    if (before.channel is None and 
        after.channel is not None and 
        after.channel.id == VOICE_CHANNEL_ID):
        user_voice_times[member.id] = datetime.datetime.now(moscow_tz)
        msg = (f"🔊 {member.display_name} зашел в голосовой канал "
               f"{after.channel.name} ({after.channel.mention}) в "
               f"{user_voice_times[member.id].strftime('%H:%M:%S')}")
        await channel.send(msg)

        # Логируем количество пользователей с ролью в отдельный канал
        if any(role.id == TARGET_ROLE_ID for role in member.roles):
            count = count_members_with_role(after.channel, TARGET_ROLE_ID)
            await role_log_channel.send(f"👥 Сейчас в голосовом канале {after.channel.name} {count} человек с ролью <@&{TARGET_ROLE_ID}>.")

    # Аналогично для перемещения между каналами
    elif (before.channel is not None and after.channel is not None and before.channel.id != after.channel.id):
        # ... (остальной код без изменений)

        if after.channel.id == VOICE_CHANNEL_ID:
            user_voice_times[member.id] = datetime.datetime.now(moscow_tz)
            msg = (f"🔊 {member.display_name} зашел в голосовой канал "
                   f"{after.channel.name} ({after.channel.mention}) в "
                   f"{user_voice_times[member.id].strftime('%H:%M:%S')}")
            await channel.send(msg)

            if any(role.id == TARGET_ROLE_ID for role in member.roles):
                count = count_members_with_role(after.channel, TARGET_ROLE_ID)
                await role_log_channel.send(f"👥 Сейчас в голосовом канале {after.channel.name} {count} человек с ролью <@&{TARGET_ROLE_ID}>.")

bot.run("MTM4MjkwNjI5MzA3Njg4NTUwNA.G4eBg5.whtbbF6iium7WCno4jl-MtZ-4f_nLOmVjEIURs")