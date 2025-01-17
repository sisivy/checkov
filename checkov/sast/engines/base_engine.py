from abc import abstractmethod, ABC
from typing import List, Set
from checkov.common.output.report import Report
from checkov.common.sast.consts import SastLanguages
from checkov.sast.checks_infra.base_registry import Registry


class SastEngine(ABC):
    @abstractmethod
    def get_reports(self, targets: List[str], registry: Registry, languages: Set[SastLanguages]) -> List[Report]:
        pass
