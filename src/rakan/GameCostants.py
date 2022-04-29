from enum import Enum


class ServerRegion(Enum):
    """Enumation of all the server regions."""
    BR = 'br1'
    """Brazil server"""
    EUNE = 'eun1'
    """Nordic and Eastern European server."""
    EUW = 'euw1'
    """Western European server."""
    LAN = 'la1'
    """Latin America North."""
    LAS = 'la2'
    """Latin America South."""
    NA = 'na1'
    """North American server."""
    OCE = 'oc1'
    """Oceania."""
    RU = 'ru1'
    """Russian server."""
    TUR = 'tr1'
    """Turkey."""
    JAP = 'jp1'
    """Japanese server."""
    KR = 'kr'
    """Korean server."""


class ServerContinent(Enum):
    AMERICAS = 'americas'
    ASIA = 'asia'
    EUROPE = 'europe'


class Seasons(Enum):
    PRESEASON_3 = 0
    SEASON_3 = 1
    PRESEASON_4 = 2
    SEASON_4 = 3
    PRESEASON_5 = 4
    SEASON_5 = 5
    PRESEASON_6 = 6
    SEASON_6 = 7
    PRESEASON_7 = 8
    SEASON_7 = 9
    PRESEASON_8 = 10
    SEASON_8 = 11
    PRESEASON_9 = 12
    SEASON_9 = 13


class Tier(Enum):
    """Enumation of all the tiers in League of Legends"""
    IRON = 'IRON'
    BRONZE = 'BRONZE'
    SILVER = 'SILVER'
    GOLD = 'GOLD'
    PLATINUM = 'PLATINUM'
    DIAMON = 'DIAMOND'
    MASTER = 'MASTER'
    GANDMASTER = 'GRANDMASTER'
    CHALLENGER = 'CHALLENGER'


class Division(Enum):
    """Enumation of all the ranks in League of Legends"""
    I = 'I'
    """1"""
    II = 'II'
    """2"""
    III = 'III'
    """3"""
    IV = 'IV'
    """4"""


class Queque(Enum):
    SOLO = 'RANKED_SOLO_5x5'
    FLEX_SR = 'RANKED_FLEX_SR'
    FLEX_TT = 'RANKED_FLEX_TT'


class GameType(Enum):
    RANKED = 'ranked'
    NORMAL = 'normal'
    TOURNEY = 'tourney'
    TUTORIAL = 'tutorial'
