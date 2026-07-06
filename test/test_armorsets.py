from .bases import Grime2TestBase
from ..enums import EnumItem

class TestStartingArmorPieces(Grime2TestBase):
    options = {"armorsets": 0}
    def test_maul_pieces(self) -> None:
        """Test starting armorsets 0 - armor pieces"""
        item_names = [i.name for i in self.multiworld.get_items()]
        self.assertFalse(EnumItem.A_HANDCLOTH_CHEST.value in item_names)
        self.assertFalse(EnumItem.A_HANDCLOTH_LEGS.value in item_names)
        self.assertFalse(EnumItem.A_HANDCLOTH_HANDS.value in item_names)
        self.assertTrue(EnumItem.A_HANDCLOTH_SET.value in item_names)

class TestStartingArmorSet(Grime2TestBase):
    options = {"armorsets": 1}
    def test_maul_sets(self) -> None:
        """Test starting armorsets 1 - armorsets"""
        item_names = [i.name for i in self.multiworld.get_items()]
        print("Sets: ", item_names)
        self.assertTrue(EnumItem.A_HANDCLOTH_CHEST.value in item_names)
        self.assertTrue(EnumItem.A_HANDCLOTH_LEGS.value in item_names)
        self.assertTrue(EnumItem.A_HANDCLOTH_HANDS.value in item_names)
        self.assertFalse(EnumItem.A_HANDCLOTH_SET.value in item_names)