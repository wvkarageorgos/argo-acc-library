from .installations import ProjectProviderInstallations
from .metrics import ProviderMetrics
from .restresource import RestResourceItem, RestResourceList


class Provider(RestResourceItem):
    """Class to represent providers"""

    def __init__(self, parent, data: dict):
        self.id = None
        self.acronym = None
        self.title = None
        self.start_date = None
        self.end_date = None
        self.call_identifier = None
        self.providers = None
        super().__init__(parent, data)

    def _fetch_route(self):
        return "provider_entry"

    def _fetch_args(self):
        return [self.id]

    @property
    def metrics(self):
        return ProviderMetrics(self)


class Providers(RestResourceList):
    """Provider collection class"""

    def _fetch_route(self):
        return "provider_list"

    def _fetch_args(self) -> list:
        return []

    def _create_child(self, data):
        return Provider(self, data)


class ProjectProvider(RestResourceItem):
    """Class to represent a provider under the context of a specific project"""

    def _fetch_route(self):
        return ""

    def _fetch_args(self):
        return []

    @property
    def metrics(self):
        return ProviderMetrics(self)

    @property
    def installations(self):
        return ProjectProviderInstallations(self)


class ProjectProviders(RestResourceList):
    """Project providers collection class"""

    def _fetch_route(self):
        return ""

    def _fetch_args(self):
        return []

    def __getitem__(self, key: str):
        return ProjectProvider(self, {"id": key})
