from steamwebapi.api import ISteamUser, IPlayerService, ISteamUserStats
from steamwebapi import profiles
import requests
steamuserinfo = ISteamUser(steam_api_key = '2680454F00E6FAE51F4AD8CE0F477AB8')
steamid = steamuserinfo.resolve_vanity_url("profileURL")['response']['steamid']
usersummary = steamuserinfo.get_player_summaries(steamid)['response']['players'][0]

response = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=2680454F00E6FAE51F4AD8CE0F477AB8&steamid=76561198124741242&format=json')

data = response.json()

print(data['response']['game_count'])


