from . import Xayah
from . import GameCostants
from . import Globals
import json


def set_riot_api_key(riot_api_key: str):
    Globals.riot_api_key = riot_api_key


class Summoner:
    __summoner_boring_info = {
        'name': None,
        'account_id': None,
        'summoner_id': None,
        'puuid': None,
        'region': None
    }

    def __init__(self, name: str, region: GameCostants.ServerRegion) -> None:
        riot_api = Xayah.RiotAPI(Globals.riot_api_key)
        boring_data = json.loads(riot_api.get_summoner_by_name(name, region))
        self.__summoner_boring_info['name'] = boring_data['name']
        self.__summoner_boring_info['account_id'] = boring_data['accountId']
        self.__summoner_boring_info['summoner_id'] = boring_data['id']
        self.__summoner_boring_info['puuid'] = boring_data['puuid']
        self.__summoner_boring_info['region'] = region
