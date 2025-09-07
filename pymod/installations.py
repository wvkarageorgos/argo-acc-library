from .metrics import InstallationMetrics
from .restresource import RestResourceItem, RestResourceList


class InstallationBase(RestResourceItem):
    """Base class for Installation related classes"""

    def __init__(self, parent, data: dict):
        self.id = None
        self.project = None
        self.organisation = None
        self.infrastructure = None
        self.installation = None
        self.resource = None
        self.unit_of_access = None
        super().__init__(parent, data)


class Installation(InstallationBase):
    """Class to represent an installation"""

    def _fetch_route(self):
        return "installation_entry"

    def _fetch_args(self):
        return [self.id]

    @property
    def metrics(self):
        return InstallationMetrics(self)


class Installations(RestResourceList):
    """Installation collection class"""
    def _fetch_route(self):
        return "installation_list"

    def _fetch_args(self) -> list:
        return []

    def _create_child(self, data):
        return Installation(self, data)


class ProjectInstallation(InstallationBase):
    """Class to represent an installation belonging to a project"""

    def _fetch_route(self):
        return ""

    def _fetch_args(self):
        return []

    @property
    def metrics(self):
        return InstallationMetrics(self)


class ProjectInstallations(RestResourceList):
    """Project installation collection class"""

    def _fetch_route(self):
        return "project_installations_list"

    def _fetch_args(self) -> list:
        return [self._parent.id]

    def _create_child(self, data):
        return ProjectInstallation(self, data)


class ProjectProviderInstallation(InstallationBase):
    """Class to represent an installation belonging to a project for a specific provider"""

    def _fetch_route(self):
        return ""

    def _fetch_args(self):
        return []

    @property
    def metrics(self):
        return InstallationMetrics(self)


class ProjectProviderInstallations(RestResourceList):
    """Project provider installation collection class"""

    def _fetch_route(self):
        return "project_provider_installations_list"

    def _fetch_args(self) -> list:
        return [self._parent._parent._parent.id, self._parent.id]

    def _create_child(self, data):
        return ProjectProviderInstallation(self, data)
