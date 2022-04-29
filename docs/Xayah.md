# The `Xayah` module

> `Xayah` is a submodule of the **rakan package** intended to provide a low level access to the [Riot Developer API](https://developer.riotgames.com/apis) and the [What is my MMR API](https://dev.whatismymmr.com/).

The module uses the `requests` package to send requests to the [API](https://en.wikipedia.org/wiki/API)s in order to retrieve information from them.

Keep in mind that all the functions in this module will return a [JSON](https://www.json.org/) formatted string that will be always minified in one line:

```json
{"id": "6LeFnUOR-aMSdaRbWOi3iostlgD5dqfgTTNQ5FAEGJPlg2Y1","accountId": "Hm8-8MFC8f8tryWn2cl6yYfF4Q9AoGo-ygjHMWgO3Xkk_r1KEfWP1HSE","puuid": "NNbFVaY2SsfIzyo_yHHabJ2VVr6jpMCqW9b8T0DplTwb4bYT0Uz7KAiJSKksbz5aPJK1rRX1VssECQ","name": "G2 Jankos","profileIconId": 989,"revisionDate": 1580964425000,"summonerLevel": 31}
```

Xayah is composed by two classes:[ `Xayah.RiotAPI`](#`Xayah.RiotAPI`) and `Xayah.MMR_API`.

## `Xayah.RiotAPI`

> This class is a wrapper for the [Riot Developer API](https://developer.riotgames.com/apis) for the `Xayah` submodule.

 Before making requests you will need to make an instance of the class:

```python
from rakan import Xayah

riot_api = Xayah.RiotAPI('API token')
```

To obtain an **API token** you'll need to register at the [Riot Developer Portal](https://developer.riotgames.com/). Be sure to refresh your **development API token** every $24$ hours!

### `api_token`

`__api_token` (`str`): The *API token* that will be used to make requests to the  [Riot Developer API](https://developer.riotgames.com/apis).

---

### `get_matches_by_puuid(region, puuid, start_time, end_time, queque, type, start, count)`

> This function will search all of a *summoner*'s *matchlist* to find the *match ID*s that satisfies the search parameters and return them.

#### Parameters

- `region` (`str`): The *continent* region to execute the request against.

- `puuid` (`str`): The *PUUID* of the summoner.

- `start_time` (`int`): Epoch timestamp in seconds. 

  The *matchlist* started storing *timestamps* on June 16th, 2021. Any matches played before June 16th, 2021 won't be included in the results.

- `end_time` (`int`): Epoch timestamp in seconds.

- `queque` (`int`): Filter the list of match ids by a specific queue id. 

  This filter is mutually inclusive of the `type` filter meaning any *match ID*s returned must match both the `queue` and `type` parameters.

- `type` (`str`): Filter the list of match ids by the type of match. 

  This filter is mutually inclusive of the `queue` parameter meaning any match ids returned must match both the `queue` and `type` parameters.

- `start` (`int`): starting index of the list of *match ID*s. 

  - **default value**: `0`.

- `count` (`int`): maximum number of *match ID*s in the list.

  - **default value**: `20`.
  - **valid values**: only values between `0` and `100` are acceptable.

#### Returns

> This functions returns a [JSON](https://www.json.org/) formatted one line string containing a list of all the *match ID*s found by the search.

#### Example

```python
from rakan import Xayah

riot_api = Xayah.RiotAPI('API token')

matches = riot_api.get_matches_by_puuid(
    'EUROPE', 
    'ONLVZymFvyfRzVC9wWqlD5sYeQ_ehIL99WScZ3e2J83VmqbaLisCJ3tn6JOSPo4UI4j3P2FWHDyCNg', 
    0, 
    10000000000, 
    0, 
    'normal', 
    0, 
    3
)
```

Will return something that looks like this:

```json
["EUW1_5830028434","EUW1_5811242561","EUW1_5811242481"]
```

---

### `get_match_by_match_id(region, match_id)`

> This function will fetch all the available information for a specific *match ID*.

#### Parameters

- `region` (`str`): The *continent* region to execute the request against.
  
- `match_id` (`str`): The *match ID* of the match.

#### Returns

> This function will return a [JSON](https://www.json.org/) formatted one line string containing all the available information for the given *match ID*.

#### Example

```python
from rakan import Xayah

riot_api = Xayah.RiotAPI('API token')

match_info = riot_api.get_match_by_match_id('EUROPE', 'EUW1_5830028434') # I won't include the result because it would be too long.
```

---

### `get_match_timeline_by_match_id(region, match_id)`

> This function fetches the *API* for the *timeline* of a specific match.

#### Parameters

- `region` (`str`): The *continent* region to execute the request against.
  
- `match_id` (`str`): The *match ID* of the match.

#### Returns

> This function will return a [JSON](https://www.json.org/) formatted one line string containing the timeline of the given *match ID*.

#### Example

```python
from rakan import Xayah

riot_api = Xayah.RiotAPI('API token')

match_info = riot_api.get_match_timeline_by_match_id('EUROPE', 'EUW1_5830028434') # I won't include the result because it would be too long.
```

---

### `get_champion_mastery_by_summoner_id(summoner_id, region)`

> This function will fetch the API for all the available information about a summoner's mastery.

#### Parameters

- `summoner_id` (`string`): The *ID* of the summoner.
- `region` (`string`): The summoner's *region*.

#### Returns

> This function will return a [JSON](https://www.json.org/) formatted one line string containing a list of all champions paired with the mastery points the player has on each of them.

#### Example

```python
from rakan import Xayah

riot_api = Xayah.RiotAPI('API token')

cr4k3nv4gh3n_mastery = Xayah.RiotAPI.get_champion_mastery_by_summoner_id(
    'h8YDyi3NlgNt240EZE1AHkDnXmmlRbnmNLYpbhZo6f2xgXzQ', 
    `EUW1`
)
```

Will result in a string like this (the one here has been cut to just one champion in order to fit the space available.)

```json
[{"championId": 19,"championLevel": 7,"championPoints": 150621,"lastPlayTime": 1650544986000,"championPointsSinceLastLevel": 129021,"championPointsUntilNextLevel": 0,"chestGranted": false,"tokensEarned": 0,"summonerId":"h8YDyi3NlgNt240EZE1AHkDnXmmlRbnmNLYpbhZo6f2xgXzQ"}]
```

---

### `get_champion_mastery_by_summoner_id_and_champion_id(summoner_id, champion_id, region)`

#### Parameters

- `summoner_id` (`string`): The *ID* of the summoner.
- `champion_id` (`int`): The *ID* number associated to a certain champion.
- `region` (`string`): The summoner's *region*.

#### Returns

> This function will return a [JSON](https://www.json.org/) formatted one line string containing all the available information about the summoner's mastery of a certain champion.

#### Example

```python
from rakan import Xayah

riot_api = Xayah.RiotAPI('API token')

cr4k3nv4gh3n_mastery = Xayah.RiotAPI.get_champion_mastery_by_summoner_id_and_champion_id(
    'h8YDyi3NlgNt240EZE1AHkDnXmmlRbnmNLYpbhZo6f2xgXzQ', 
    19
    `EUW1`
)
```

Will result in this:

```json
[{"championId": 19,"championLevel": 7,"championPoints": 150621,"lastPlayTime": 1650544986000,"championPointsSinceLastLevel": 129021,"championPointsUntilNextLevel": 0,"chestGranted": false,"tokensEarned": 0,"summonerId":"h8YDyi3NlgNt240EZE1AHkDnXmmlRbnmNLYpbhZo6f2xgXzQ"}]
```

---

### `get_summoner_mastery_score(summoner_id, region)`

> This function will fetch a summoner's *mastery score*.

#### Parameters

- `summoner_id` (`string`): The *ID* of the summoner.
- `region` (`string`): The summoner's *region*.

#### Returns

> This function will return a [JSON](https://www.json.org/) formatted one line string containing the mastery score of a summoner.

#### Example

```python
from rakan import Xayah

riot_api = Xayah.RiotAPI('API token')

cr4k3nv4gh3n_mastery = Xayah.RiotAPI.get_summoner_mastery_score(
    'h8YDyi3NlgNt240EZE1AHkDnXmmlRbnmNLYpbhZo6f2xgXzQ',
    `EUW1`
)
```

Will result in this:

```python
425
```

---