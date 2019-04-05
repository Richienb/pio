import requests
from os import path
from distutils.version import StrictVersion
import requirements
import json
from readsettings import ReadSettings
data = ReadSettings("pio.json")

try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain


def getLatestVersion(package):
    releases = list(
        requests.get("https://pypi.org/pypi/{}/json".format(
            i[1])).json()["releases"].keys())
    releases.sort(key=StrictVersion)
    return releases[-1]


def add(args, cwd):
    for i in enumerate(args):
        latest = getLatestVersion(i[1])

        pipmain(['install', "{}~={}".format(i[1], latest)])

        data.set(i[1], latest)


def remove(args, cwd):
    for i in enumerate(args):
        pipmain(['uninstall', i[1]])
        data.rem(i[1])


def install(args, cwd):
    for key in data.raw().keys():
        pair = (key, data.raw()[key])
        pipmain(['install', "{}~={}".format(pair[0], pair[1])])


def update(cwd):
    pass


# TODO: Create updater
