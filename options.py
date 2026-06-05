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


class Goal(Choice):
    """
    Set what base game conditions need to be met to complete the game
    Goel: The standard intended ending for the game.
    """
    display_name = "Goal"
    option_goel = 0
    
    default = option_goel

@dataclass
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
    default = 0

@dataclass
class StartWithWeapon(Toggle):
    """
    Start with a random weapon.
    """
    display_name = "Goal"
    option_act_1 = 0
    option_act_2 = 1
    option_act_3 = 2
    default = 0
    
# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [Goal],
    ),
]

option_presets = {}