from pkg_resources import get_distribution, DistributionNotFound

__project__ = 'onlinebrief24'

try:
    __version__ = get_distribution(__project__).version
except DistributionNotFound:
    __version__ = None


from onlinebrief24.client import Client
