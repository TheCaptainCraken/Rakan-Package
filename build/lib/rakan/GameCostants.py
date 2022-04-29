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


class Queques(Enum):
    SNOWDOWN_SHOWDOWN_1VS1_GAMES = 72

    SNOWDOWN_SHOWDOWN_2VS2_GAMES = 73

    HEXAKILL_GAMES = 75
