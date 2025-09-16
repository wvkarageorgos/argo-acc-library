from .restresource import RestResourceItem, RestResourceList


class MetricBase(RestResourceItem):
    """Base class for metric related classes"""

    def __init__(self, parent, data: dict):
        self.id = None
        self.time_period_start = None
        self.time_period_end = None
        self.value = None
        self.project = None
        self.provider = None
        self.installation_id = None
        self.project_id = None
        self.resource = None
        self.group_id = None
        self.user_id = None
        self.metric_definition_id = None
        super().__init__(parent, data)
        if data.get("metric_definition"):
            self.metric_definition = MetricDefinition(self, data["metric_definition"])


class MetricDefinition(RestResourceItem):
    """Class to represent a metric definition"""

    def __init__(self, parent, data: dict):
        self.metric_definition_id = None
        self.metric_name = None
        self.metric_description = None
        self.unit_type = None
        self.metric_type = None
        self.creator_id = None
        super().__init__(parent, data)

    def _fetch_route(self):
        return ""

    def _fetch_args(self):
        return []


class Metrics(RestResourceList):
    """Base class for all metric collection subclasses"""

    pass


class InstallationMetric(MetricBase):
    """Class to represent a metric for a specific installation"""

    def _fetch_route(self):
        return "installation_metrics_entry"

    def _fetch_args(self):
        return [self._parent._parent.id, self.id]


class InstallationMetrics(Metrics):
    """Installation metrics collection class"""

    def _fetch_route(self):
        return "installation_metrics_list"

    def _fetch_args(self):
        return [self._parent.id]

    def _add_route(self):
        return "installation_metrics_add"

    def _add_args(self):
        return [self._parent.id]

    def _create_child(self, data):
        return InstallationMetric(self, data)


class ProjectMetric(MetricBase):
    """Class to represent a metric for a specific project"""

    def _fetch_route(self):
        return ""

    def _fetch_args(self):
        return []


class ProjectMetrics(Metrics):
    """Project metrics collection class"""

    def _fetch_route(self):
        return "project_metrics_list"

    def _fetch_args(self):
        return [self._parent.id]

    def _create_child(self, data):
        return ProjectMetric(self, data)


class ProviderMetric(MetricBase):
    """Class to represent a metric for a specific provider"""
    def _fetch_route(self):
        return ""

    def _fetch_args(self):
        return []


class ProviderMetrics(Metrics):
    """Project metrics collection class"""
    def _fetch_route(self):
        return "project_provider_metric_list"

    def _fetch_args(self):
        return [self._parent._parent._parent.id, self._parent.id]

    def _create_child(self, data):
        return ProviderMetric(self, data)
