"""
Main library
"""
import requests
import requirements
import re

from readsettings import ReadSettings
data = ReadSettings("pio.json")

try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain


def getVersionList(package):
    return list(
        requests.get("https://pypi.org/pypi/{}/json".format(package)).json()
        ["releases"].keys())


def add(cwd, args):
    for i in enumerate(args):
        latest = getLatestVersion(i[1])[-1]

        pipmain(["install", "{}~={}".format(i[1], latest)])

        data[i[1]] = latest


def remove(cwd, args):
    for i in enumerate(args):
        pipmain(["uninstall", i[1]])
        del data[i[1]]


def install(cwd, args):
    for key in data.json().keys():
        pair = (key, data.json()[key])
        pipmain(["install", "{}~={}".format(pair[0], pair[1])])


def update(cwd, args=False):
    if not args:
        args = data.json().keys()

    for i in enumerate(args):
        latest = getLatestVersion(i[1])[-1]

        pipmain(["install", "--update", "{}~={}".format(i[1], latest)])

        data[i[1]] = latest


def migrate(cwd, args):
    if not args[0]:
        args[0] = "requirements.txt"
    with open(args[0], "r") as f:
        for req in requirements.parse(f):
            print(req.name, req.specs)
