from .bases import Grime2TestBase
from ..enums import EnumItem

class TestOptionAddCutWeaponsTrue(Grime2TestBase):
    options = {"addcutweapons": 0}
    def test_cut_weapons_excluded(self) -> None:
        """Test cut weapons - false"""
        item_names = [i.name for i in self.multiworld.get_items()]

        self.assertTrue(EnumItem.W_ALLOYBARK_CLEAVERS.value not in item_names)
        self.assertTrue(EnumItem.W_BLADEROOT_JAVELIN.value not in item_names)
        # self.assertTrue(EnumItem.W_CODA_SCYTHESWORD.value not in item_names)

class TestOptionAddCutWeaponsFalse(Grime2TestBase):
    options = {"addcutweapons": 1}
    def test_cut_weapons_included(self) -> None:
        """Test cut weapons - true"""
        item_names = [i.name for i in self.multiworld.get_items()]

        self.assertTrue(EnumItem.W_ALLOYBARK_CLEAVERS.value in item_names)
        self.assertTrue(EnumItem.W_BLADEROOT_JAVELIN.value in item_names)
        # self.assertTrue(EnumItem.W_CODA_SCYTHESWORD.value in item_names)