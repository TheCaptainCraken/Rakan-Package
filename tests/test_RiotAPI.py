from src.rakan import Xayah
import os

account = 'cr4k3nv4gh3n'
region = 'EUW1'
summoner_id = 'h8YDyi3NlgNt240EZE1AHkDnXmmlRbnmNLYpbhZo6f2xgXzQ'
account_id = 'ay2ebiNZ5Z4NAs0jzdb9-wh3w506-TF6G4F2Gmly1-pSPfgh-pH2zuif'
puuid = 'ONLVZymFvyfRzVC9wWqlD5sYeQ_ehIL99WScZ3e2J83VmqbaLisCJ3tn6JOSPo4UI4j3P2FWHDyCNg'


def get_api_key():
    return os.environ.get('RIOT_API_KEY')


def test_get_champion_mastery_by_summoner_id():
    riot = Xayah.RiotAPI(get_api_key())
    response = riot.get_champion_mastery_by_summoner_id(summoner_id, region)
    assert response[0]['summonerId'] == summoner_id


def test_get_summoner_by_account_id():
    riot = Xayah.RiotAPI(get_api_key())
    response = riot.get_summoner_by_account_id(account_id, region)
    print(response)
    assert response['id'] == summoner_id


def test_get_summoner_by_puuid():
    riot = Xayah.RiotAPI(get_api_key())
    response = riot.get_summoner_by_puuid(puuid, region)
    print(response)
    assert response['id'] == summoner_id


def test_get_summoner_by_name():
    riot = Xayah.RiotAPI(get_api_key())
    response = riot.get_summoner_by_name(account, region)
    print(response)
    assert response['id'] == summoner_id


def test_get_summoner_by_summoner_id():
    riot = Xayah.RiotAPI(get_api_key())
    response = riot.get_summoner_by_summoner_id(summoner_id, region)
    print(response)
    assert response['id'] == summoner_id


def test_get_server_status():
    riot = Xayah.RiotAPI(get_api_key())
    response = riot.get_server_status(region)
    assert response['id'] == region
