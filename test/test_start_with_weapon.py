from .bases import Grime2TestBase
from ..options import StartingWeapon
from ..enums import EnumLoc, EnumItem

class TestStartingWeapon(Grime2TestBase):
    #options = {"start_with_weapon": StartingWeapon.option_maul_axe} # Maul Axe
    options = {"starting_weapon": 0} # Maul Axe

    def test_maul_axe_Start(self) -> None:
        """Test locations that require a sword"""
        maul_axe_location = self.world.get_location(EnumLoc.BIRTHPLACE_LOWER_MAUL_AXE.value)
        #maul_axe = self.world.create_item(EnumItem.W_MAUL_AXE.value)
        self.assertEqual(maul_axe_location.item.name, EnumItem.W_MAUL_AXE.value)
