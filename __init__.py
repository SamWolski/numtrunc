from sys import version_info

## Verify python version
if version_info >= (3,):
    ## Version info for package
    from .src._version import version as __version__
    ## Classes
    from .src.TruncNum import TruncNum

## numtrunc does not support Python 2
else:
    raise ImportError('numtrunc does not support Python2. Please upgrade!')