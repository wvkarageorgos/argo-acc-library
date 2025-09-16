from typing import Optional

from .httprequests import HttpRequests
from .installations import Installations
from .projects import Projects
from .providers import Providers


class ArgoAccountingService(object):
    """Module main class, to access the REST API"""

    def __init__(self, endpoint, token):
        self._endpoint = endpoint
        self._conn = HttpRequests(token)
        self._installations: Optional[Installations] = None
        self._projects: Optional[Projects] = None
        self._providers: Optional[Providers] = None

    @property
    def installations(self):
        self._installations = self._installations or Installations(self)
        return self._installations

    @property
    def projects(self):
        self._projects = self._projects or Projects(self)
        return self._projects

    @property
    def providers(self):
        self._providers = self._providers or Providers(self)
        return self._providers

    @property
    def connection(self):
        return self._conn

    @property
    def endpoint(self):
        return self._endpoint
