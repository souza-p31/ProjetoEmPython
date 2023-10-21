import discord
from dados import *

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.content == '?bot':
            await message.channel.send(f'Olá {message.author.name}, eu sou um Bot que envia promoções!')

        if message.content == '?promoções de hoje':
            try:
                await message.channel.send(f'Preciso de um minuto, estou verificando as promoções do dia...')
                promocao = promocoeshoje()
                await message.channel.send(f'-'*60)
                for p in promocao:
                    await message.channel.send(f'🔥 {p[0]}\n💸 {p[1]}\n✅ Vendido por: {p[2]}\n')
                    await message.channel.send(f'-'*60)
                await message.channel.send(f'Essas são as promoções de hoje até o momento! 😉')
            except Exception:
                await message.channel.send(f'Tive um problema durante a verificação, tente novamente')

        if message.content == '?promoções da semana':
            try:
                await message.channel.send(f'Preciso de um minuto, estou verificando as promoções da semana...')
                promocao = promocoessemana()
                await message.channel.send(f'-'*60)
                for p in promocao:
                    await message.channel.send(f'🔥 {p[0]}\n💸 {p[1]}\n✅ Vendido por: {p[2]}\n')
                    await message.channel.send(f'-'*60)
                await message.channel.send(f'Essas são as promoções da semana até o momento! 😉')
            except Exception:
                await message.channel.send(f'Tive um problema durante a verificação, tente novamente')

        if message.content == '?promoções do mês':
            try:
                await message.channel.send(f'Preciso de um minuto, estou verificando as promoções do mês...')
                promocao = promocoessemana()
                await message.channel.send(f'-'*60)
                for p in promocao:
                    await message.channel.send(f'🔥 {p[0]}\n💸 {p[1]}\n✅ Vendido por: {p[2]}\n')
                    await message.channel.send(f'-'*60)
                await message.channel.send(f'Essas são as promoções do mês até o momento! 😉')
            except Exception:
                await message.channel.send(f'Tive um problema durante a verificação, tente novamente')

        if message.content == '?comandos':
                    try:
                        await message.channel.send(f'Até o momento meus comandos são:\n?promoções de hoje\n?promoções da semana\n?promoções do mês')
                    except Exception:
                        await message.channel.send(f'Tive um problema durante a verificação, tente novamente')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('#aqui entra a chave do bot')