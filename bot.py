import discord
import requests

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ip'):
        ip = message.content.split(' ')[1]
        ip_info = get_ip_info(ip)
        await message.channel.send(ip_info)

def get_ip_info(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}?fields=66846719')
    data = response.json()
    if data['status'] == 'fail':
        return 'Invalid IP address'
    
    ip_info = (
        f"IP: {data['query']}\n"
        f"Type: {'IPv4' if ':' not in data['query'] else 'IPv6'}\n"
        f"Continent Code: {data['continentCode']}\n"
        f"Continent Name: {data['continent']}\n"
        f"Country Code: {data['countryCode']}\n"
        f"Country Name: {data['country']}\n"
        f"Region Code: {data['region']}\n"
        f"Region Name: {data['regionName']}\n"
        f"City: {data['city']}\n"
        f"ZIP: {data['zip']}\n"
        f"Latitude: {data['lat']}\n"
        f"Longitude: {data['lon']}\n"
        f"Geoname ID: {data.get('geonameId', 'N/A')}\n"
        f"Capital: {data.get('capital', 'N/A')}\n"
        f"Languages: {data.get('languages', 'N/A')}\n"
        f"Country Flag: {data.get('countryFlag', 'N/A')}\n"
        f"Country Flag Emoji: {data.get('countryFlagEmoji', 'N/A')}\n"
        f"Calling Code: {data.get('callingCode', 'N/A')}\n"
        f"Is EU: {data.get('isEu', 'N/A')}\n"
        f"Time Zone: {data.get('timezone', 'N/A')}\n"
        f"Currency: {data.get('currency', 'N/A')}\n"
        f"Connection ASN: {data.get('as', 'N/A')}\n"
        f"ISP: {data['isp']}\n"
        f"Security - Proxy: {data.get('proxy', False)}\n"
        f"Security - Tor: {data.get('hosting', False)}\n"
        f"Security - Threat Level: {data.get('threat', {}).get('level', 'N/A')}\n"
        f"Security - Threat Types: {data.get('threat', {}).get('types', 'N/A')}\n"
    )
    return ip_info

client.run(TOKEN)
