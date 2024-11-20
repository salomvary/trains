"""
ELVIRA API sends a cookie with an invalid key, which causes aiohttp
to log a warning every time a response is processed:
"Can not load response cookies: Illegal key 'BIGipServerus3QLq/ahQ21JjLqHgGlBA'"

There seems to be no way to suppress this warning, the current solution is to
monkeypatch Python's http.cookies module:
https://github.com/aio-libs/aiohttp/issues/2683#issuecomment-924559912
"""

# Not sure if this is necessary, but definitely hard to achieve.
# import sys
# if "http" in sys.modules:
#     raise ImportError("elvira_api must be imported before http module")

import http.cookies

_original_is_legal_key = http.cookies._is_legal_key


def _patched_is_legal_key(key):
    if "BIGipServerus" in key:
        return True
    return _original_is_legal_key(key)


http.cookies._is_legal_key = _patched_is_legal_key
