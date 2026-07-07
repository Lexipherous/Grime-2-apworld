from __future__ import annotations
from typing import TYPE_CHECKING, Self
from rule_builder.rules import CanReachLocation, Has, CanReachRegion, HasAll, HasAny
from .enums import EnumItem, EnumLoc, EnumRegions

if TYPE_CHECKING:
    from .world import Grime2World


def set_all_rules(world: Grime2World) -> None:
    set_all_main_quest_rules(world)
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_main_quest_rules(world: Grime2World) -> None:
    # # # # # # # # # # 
    # Main Logic Rules
    # # # # # # # # # # 
    # Entrance to Kankan, requires Mountainborn Kill
    world.set_rule(world.get_entrance("Marah's Orchard to Kankan"),
                   CanReachLocation(EnumLoc.UNDERHEADS_MOUNTAINBORN.value))

    # Entrance to Palace, requires Breathsmith Info
    world.set_rule(world.get_entrance("Kankan Upper Before Palace to Kankan Upper Palace"),
                   Has(EnumItem.QI_BREATHSMITH_LOCATION_INFO.value))

    # Entrance to Palace Jail, requires Locked Sphere
    world.set_rule(world.get_entrance("Kankan Upper Palace to Kankan Upper Jail"),
                   Has("Locked Sphere") & CanReachLocation(EnumLoc.UNDERHEADS_MOUNTAINBORN.value))

    # Getting Manzil's Breathcrown, requires Yr'Gog being freed
    world.set_rule(world.get_location(EnumLoc.MUDFALLS_MANZIL_BREATHCROWN.value),
                   CanReachRegion(EnumRegions.KANKAN_UPPER_JAIL.value))

    # === Act 2 ===
    # Completing act 2 requires the 3 weapon parts
    world.set_rule(world.get_entrance("Mudfalls to Palladium"),
                   HasAll(EnumItem.QI_FORGED_ANVIL, EnumItem.QI_QUADRANT_BLADE, EnumItem.QI_FRAIL_HORN))

def set_all_entrance_rules(world: Grime2World) -> None:
    """
        Placeholder
    """
    # Mudfalls
    world.set_rule(world.get_entrance("Mudfalls to Mudfalls Spike Pit"), can_item_grasp())
    
    # Underheads
    world.set_rule(world.get_entrance("Underheads Lahav Knight to Nailglade Transition"), is_breathcrowned())
    world.set_rule(world.get_entrance("Underheads Left Lower to Dregbourg"), is_breathcrowned())
    
    # Kankan
    world.set_rule(world.get_entrance("Kankan Lower to Jagged Forest"), is_breathcrowned())
    world.set_rule(world.get_entrance("Kankan Upper Dropot to Kankan Upper Heod"), can_item_explode())
    
    # Connection rules
    world.set_rule(world.get_entrance("BG_Upper to BG_Middle"), can_air_dash())
    world.set_rule(world.get_entrance("BG_Middle to BG_Lower"), can_grasp_hook_slide())

def set_all_location_rules(world: Grime2World) -> None:
    """
        Placeholder
    """
    # Discarded Flesh requires Grasp
    world.set_rule(world.get_location(EnumLoc.KANKAN_DISCARDED_FLESH.value), can_grasp())
    world.set_rule(world.get_location(EnumLoc.MARAHS_DISCARDED_FLESH.value), can_grasp())
    world.set_rule(world.get_location(EnumLoc.DREGBOURG_DISCARDED_FLESH.value), can_grasp())
    world.set_rule(world.get_location(EnumLoc.REEF_DISCARDED_FLESH.value), can_grasp())
    world.set_rule(world.get_location(EnumLoc.NAILGLADE_DISCARDED_FLESH.value), can_grasp())
    
    
    # Temple of Hands
    world.set_rule(world.get_location(EnumLoc.BIRTHPLACE_UPPER_FORCE_CAPACITY.value),  can_climb_walls() & can_cross_spike_tunnels())

    # Jagged Forest
    world.set_rule(world.get_location(EnumLoc.JAGGED_FORCE.value), can_climb_walls() & (can_dash_slide() | can_item_grasp()) )
    world.set_rule(world.get_location(EnumLoc.JAGGED_CHAIN_JAVELIN_PIT.value), can_item_grasp())
    world.set_rule(world.get_location(EnumLoc.JAGGED_BLOODROOT_LEARNING.value), can_grasp() & can_climb_walls() & can_high_jump())
    world.set_rule(world.get_location(EnumLoc.JAGGED_MARAH_STRAND_LAHAV.value), can_high_jump())

    # Blade Garden
    world.set_rule(world.get_location(EnumLoc.GARDEN_MARAH_STRAND_SEAL_BELOW.value), can_air_dash())
    world.set_rule(world.get_location(EnumLoc.GARDEN_ATRIUM_GREATBLADE_LEGS.value), can_high_jump() | (can_item_grasp() | can_air_dash()))
    world.set_rule(world.get_location(EnumLoc.GARDEN_MARAH_STRAND_AXE.value), can_high_jump())
    world.set_rule(world.get_location(EnumLoc.GARDEN_ALVEOLI_TREE.value), can_high_jump())


def set_completion_condition(world: Grime2World) -> None:
    """
        Placeholder
    """
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
    
def can_cross_spike_tunnels() -> Has | HasAll:
    return Has(EnumItem.IM_EMBEDDING_NAIL.value) | HasAll(EnumItem.AM_HANDJUMP.value, EnumItem.AM_AIRDASH.value)

def can_climb_walls() -> Has:
    return Has(EnumItem.AM_WALLJUMP.value)

def can_burst_jump() -> Has:
    return Has(EnumItem.AM_BURSTJUMP.value)

def can_hand_jump() -> Has:
    return Has(EnumItem.AM_HANDJUMP.value)

def can_high_jump() -> HasAny:
    return HasAny(EnumItem.AM_BURSTJUMP.value, EnumItem.AM_HANDJUMP.value)

def can_grasp() -> Has:
    return Has(EnumItem.AC_GRASP.value)

def can_grasp_hook() -> Has:
    return Has(EnumItem.AC_GRASP.value) & Has(EnumItem.AM_GRASPHOOK.value)

def can_item_grasp() -> Has:
    return Has(EnumItem.AC_GRASP.value) & (Has(EnumItem.MI_THIRD_OF_FLESH.value, 3) | Has(EnumItem.AC_ITEM_GRASP.value))

def can_grasp_hook_slide() -> Has:
    return Has(EnumItem.AC_GRASP.value) & Has(EnumItem.AM_GRASPHOOK.value) & Has(EnumItem.AM_GRASPSLIDE.value)

def can_air_dash() -> Has:
    return Has(EnumItem.AM_AIRDASH.value)

def can_dash_slide() -> HasAll:
    return HasAll(EnumItem.AM_WALLJUMP.value, EnumItem.AM_DASHSLIDE.value)

def can_item_explode() -> HasAny:
    return HasAny(EnumItem.IM_VOLATILE_VASE.value, EnumItem.IM_OVERGROWN_BLOB.value)

def is_breathcrowned() -> HasAny:
    return HasAny(EnumItem.BC_MANZILS_BREATHCROWN)