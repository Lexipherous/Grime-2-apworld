from .bases import Grime2TestBase
from ..enums import EnumLoc, EnumItem
from ..items import populate_items_weapons

class TestStartingWeaponMaulAxe(Grime2TestBase):
    options = {"starting_weapon": 0}
    def test_maul_axe_start(self) -> None:
        """Test starting weapon option 0 - Maul Axe"""
        maul_axe_location = self.multiworld.get_location(EnumLoc.BIRTHPLACE_LOWER_MAUL_AXE.value, self.player)
        self.assertIsNotNone(maul_axe_location.item, f"No item placed at {maul_axe_location.name}")
        self.assertEqual(maul_axe_location.item.name, EnumItem.W_MAUL_AXE.value)

class TestStartingWeaponAnyStarter(Grime2TestBase):
    options = {"starting_weapon": 1}
    def test_option_any_usable_start(self) -> None:
        """Test starting weapon option 1 - option_any_usable"""
        maul_axe_location = self.multiworld.get_location(EnumLoc.BIRTHPLACE_LOWER_MAUL_AXE.value, self.player)
        self.assertIsNotNone(maul_axe_location.item, f"No item placed at {maul_axe_location.name}")
        print(maul_axe_location.item.name)
        self.assertTrue(maul_axe_location.item.name in [EnumItem.W_MAUL_AXE.value, EnumItem.W_THROWING_THUMBS.value, EnumItem.W_CLASPED_MACE.value, EnumItem.W_KNIFEHAND.value])

class TestStartingWeaponAnyStarterNotMaulAxe(Grime2TestBase):
    options = {"starting_weapon": 2}
    def test_option_any_usable_start(self) -> None:
        """Test starting weapon option 2 - option_any_starter_except_maul_axe"""
        maul_axe_location = self.multiworld.get_location(EnumLoc.BIRTHPLACE_LOWER_MAUL_AXE.value, self.player)
        self.assertIsNotNone(maul_axe_location.item, f"No item placed at {maul_axe_location.name}")
        print(maul_axe_location.item.name)
        self.assertTrue(maul_axe_location.item.name in [EnumItem.W_THROWING_THUMBS.value, EnumItem.W_CLASPED_MACE.value, EnumItem.W_KNIFEHAND.value])

class TestStartingWeaponAny(Grime2TestBase):
    options = {"starting_weapon": 3}
    def test_option_any_usable_start(self) -> None:
        """Test starting weapon option 3 - option_any"""
        maul_axe_location = self.multiworld.get_location(EnumLoc.BIRTHPLACE_LOWER_MAUL_AXE.value, self.player)
        self.assertIsNotNone(maul_axe_location.item, f"No item placed at {maul_axe_location.name}")
        print(maul_axe_location.item.name)

        starter_weapon = [EnumItem.W_ATTUNING_BOW.value, EnumItem.W_BARBED_SWORD.value, EnumItem.W_BEAK_FISTS.value, 
                          EnumItem.W_BEAST_BOW.value, EnumItem.W_BLADEROOT_GREATSWORD.value, EnumItem.W_BLADEROOT_SWORD.value, 
                          EnumItem.W_BLOODMETAL_SCYTHE.value, EnumItem.W_BOWBLADES.value, EnumItem.W_CLASPED_MACE.value, 
                          EnumItem.W_CLAWING_SCYTHE.value, EnumItem.W_FACELESS_SPEAR.value, EnumItem.W_FINGER_FISTS.value, 
                          EnumItem.W_FINGERCLUMP_MACE.value, EnumItem.W_FORGED_FISTS.value, EnumItem.W_FORGED_PICK.value, 
                          EnumItem.W_FORGED_STAKE.value, EnumItem.W_GOEL_GREATSWORD.value, EnumItem.W_GOZ_SICKLE.value, 
                          EnumItem.W_GRIPPING_GREATAXE.value, EnumItem.W_JAW_AXE.value, EnumItem.W_KNIFEHAND.value, 
                          EnumItem.W_MAMMOTH_AXE.value, EnumItem.W_MAUL_AXE.value, EnumItem.W_NAIL_BOW.value, 
                          EnumItem.W_PITCHER_SPEAR.value, EnumItem.W_RAKING_SWORD.value, EnumItem.W_RUST_FISTS.value, 
                          EnumItem.W_SPEARHAND.value, EnumItem.W_THROWING_NAILS.value, EnumItem.W_THROWING_STARS.value, 
                          EnumItem.W_THROWING_THUMBS.value, EnumItem.W_TOOTH_HAMMER.value, EnumItem.W_ZEV_BLADES.value]
        self.assertTrue(maul_axe_location.item.name in starter_weapon)
