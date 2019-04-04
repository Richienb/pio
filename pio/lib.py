import requests
from os import path
from distutils.version import StrictVersion

try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain

def getLatestVersion(package):
    releases = list(requests.get("https://pypi.org/pypi/{}/json".format(i[1])).json()["releases"].keys())
    releases.sort(key=StrictVersion)
    return releases[-1]
    
def add(arguments, cwd):
    for i in enumerate(arguments):
        content = "{}~={}".format(i[1], getLatestVersion(i[1]))
        pipmain(['install', content])
        # TODO: Check if already appended
        with open(path.join(cwd, "requirements.txt"), "a") as f:
            f.write("\n" + content)
            
def remove(arguments, cwd):
    for i in enumerate(arguments):
        pipmain(['uninstall', i[1]])
        # TODO: Remove entry
        
def install(cwd):
    pass
	# TODO: Create installer
    
def update(cwd):
    pass
	# TODO: Create updater