from .installations import ProjectInstallations
from .metrics import ProjectMetrics
from .providers import ProjectProviders
from .restresource import RestResourceItem, RestResourceList


class Project(RestResourceItem):
    """Class to represent projects"""

    def __init__(self, parent, data: dict):
        self.id = None
        self.acronym = None
        self.title = None
        self.start_date = None
        self.end_date = None
        self.call_identifier = None
        self._providers = None
        super().__init__(parent, data)

    def _fetch_route(self):
        return "project_entry"

    def _fetch_args(self):
        return [self.id]

    @property
    def providers(self):
        return ProjectProviders(self)

    @providers.setter
    def providers(self, val):
        self._providers = val

    @property
    def metrics(self):
        return ProjectMetrics(self)

    @property
    def installations(self):
        return ProjectInstallations(self)


class Projects(RestResourceList):
    """Project collection class"""

    def _fetch_route(self):
        return "project_list"

    def _fetch_args(self) -> list:
        return []

    def _create_child(self, data):
        return Project(self, data)
