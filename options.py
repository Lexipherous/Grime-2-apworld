from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  APQuest doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md


class CompletionGoal(Choice):
    """
    Act 1 - Return to Manzil after Kankan.
    Act 2 - Complete the Weapon.
    Act 3 - Beat Goel.
    """
    display_name = "Goal"
    option_act_1 = 0
    option_act_2 = 1
    option_act_3 = 2
    option_test_bound_shell = 3
    default = 3

class StartWithWeapon(Toggle):
    """
    If yes, you will randomly be assigned a weapon
    """
    display_name = "Start with weapon"
    default = 0

class Armorsets(Toggle):
    """
    If yes, armor will be sent as a complete set, instead of 1 of the 3 pieces of the set.
    """
    display_name = "Armorsets"
    default = 0

class ItemMolds(Toggle):
    """
    If yes, a check will grant enough item molds to get the item mold to Tier 2, then Tier 3. As opposed to receiving each Item Mold seperately.
    """
    display_name = "Item Molds"
    default = 0

class ItemGrasp(Toggle):
    """
    If yes, Item Grasp will be its own item, otherwise you will need the three Thirds of Flesh.
    """
    display_name = "Item Grasp"
    default = 0

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [CompletionGoal, StartWithWeapon, Armorsets, ItemMolds, ItemGrasp],
    ),
]

@dataclass
class Grime2Options(PerGameCommonOptions):
    completion_goal: CompletionGoal
    start_with_weapon: StartWithWeapon
    armorsets: Armorsets
    itemmolds: ItemMolds
    itemgrasp: ItemGrasp

option_presets = {}