from test.bases import Grime2TestBase


class TestChestAccess(Grime2TestBase):
    options = {
        "start_with_weapon": "true",
        "completion_goal": "act_3",
    }

    def test_sword_chests(self) -> None:
        """Test locations that require a sword"""
        locations = ["ToH-Birthplace: Maul Axe"]
        items = ["Clasped Mace", "Knifehand", "Maul Axe", "Throwing Thumbs"]
        # This tests that the provided locations aren't accessible without the provided items, but can be accessed once
        # the items are obtained.
        # This will also check that any locations not provided don't have the same dependency requirement.
        # Optionally, passing only_check_listed=True to the method will only check the locations provided.
        self.assertAccessDependency(locations, items)