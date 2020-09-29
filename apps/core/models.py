import os
from .opensubs import OpenSubs


open_subs = OpenSubs(
    os.getenv('OPENSUBS_USERNAME'),
    os.getenv('OPENSUBS_PASSWORD')
)
