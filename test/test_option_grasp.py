from .bases import Grime2TestBase
from ..enums import EnumItem

class TestOptionGrasp(Grime2TestBase):
    options = {"itemgrasp": 0}
    def test_maul_pieces(self) -> None:
        """Test starting itemgrasp 0 - ability"""
        item_names = [i.name for i in self.multiworld.get_items()]
        print("Ability:", item_names)
        self.assertTrue(EnumItem.MI_THIRD_OF_FLESH.value not in item_names, "Flesh incorrectly in item pool.")
        self.assertTrue(EnumItem.AC_ITEM_GRASP.value in item_names, "Grasp correctly in item pool")

class TestOptionThirdsOfFlesh(Grime2TestBase):
    options = {"itemgrasp": 1}
    def test_maul_pieces(self) -> None:
        """Test starting itemgrasp 1 - Third of Flesh"""
        item_names = [i.name for i in self.multiworld.get_items()]
        print("Flesh:", item_names)
        self.assertTrue(EnumItem.MI_THIRD_OF_FLESH.value in item_names, "Flesh correctly in item pool.")
        self.assertTrue(EnumItem.AC_ITEM_GRASP.value not in item_names, "Grasp incorrectly in item pool")