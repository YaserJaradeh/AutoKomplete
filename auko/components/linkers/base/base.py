from typing import List, Tuple
from auko.discovery import AuKoClass


class BaseLinker(AuKoClass):
    """
    Base linker class, all other linkers will inherit from this
    entity, relation, or joint linkers will use this class
    """

    def __init__(self, name: str = 'Base Linker', **kwargs):
        self.name = name

    def get_links(self, text: str) -> List[Tuple[str, str, str]]:
        """
        gets the links in the text
        :param text: the text to search in
        :return: a list of tuples, each tuple contains the <URL, surface form, and type (entity, relation)>
        """
        pass


class DummyLinker(BaseLinker):
    """
    Dummy Linker used for testing purposes or to fill space in the pipeline
    """

    def __init__(self, **kwargs):
        super().__init__(name="Dummy Linker", **kwargs)

    def get_links(self, text: str) -> List[Tuple[str, str, str]]:
        return []
