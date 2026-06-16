from __future__ import annotations
from typing import TYPE_CHECKING, Self
from BaseClasses import CollectionState, Location
from rule_builder.rules import CanReachLocation, Has, CanReachRegion
from worlds.generic.Rules import add_rule, set_rule

from .options import ItemGrasp
from .enums import EnumItem, EnumLoc, EnumRegions

# from .locations import location_table, Grime2LocationData
# from .options import GRIME2Options

if TYPE_CHECKING:
    from .world import Grime2World


def set_all_rules(world: Grime2World) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: Grime2World) -> None:
    """
        Placeholder
    """
#     # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
#     dried_paint_from_overgrown_barrier = world.get_entrance("ToH Birthplace Lower to ToH Dried Paint")
#     set_rule(
#         dried_paint_from_overgrown_barrier, 
#         lambda state: state.has(LocTemple.BIRTHPLACE_LOWER_OVERGROWN_BARRIER.value, world.player),)

    
    
    
    
    

    # self._add_entrance_rule("Undead Settlement", lambda state: (
    #         state.has("Small Lothric Banner", self.player)
    #         and self._can_get(state, "HWL: Soul of Boreal Valley Vordt")
    
#         # overworld_to_top_left_room = world.get_entrance("Overworld to Top Left Room")
#         # right_room_to_final_boss_room = world.get_entrance("Right Room to Final Boss Room")
# 
#     # An access rule is a function. We can define this function like any other function.
#     # This function must accept exactly one parameter: A "CollectionState".
#     # A CollectionState describes the current progress of the players in the multiworld, i.e. what items they have,
#     # which regions they've reached, etc.
#     # In an access rule, we can ask whether the player has a collected a certain item.
#     # We can do this via the state.has(...) function.
#     # This function takes an item name, a player number, and an optional count parameter (more on that below)
#     # Since a rule only takes a CollectionState parameter, but we also need the player number in the state.has call,
#     # our function needs to be locally defined so that it has access to the player number from the outer scope.
#     # In our case, we are inside a function that has access to the "world" parameter, so we can use world.player.
#         # def can_destroy_bush(state: CollectionState) -> bool:
#         #     return state.has("Sword", world.player)
# 
#     # Now we can set our "can_destroy_bush" rule to our entrance which requires slashing a bush to clear the path.
#     # One way to set rules is via the set_rule() function, which works on both Entrances and Locations.
#         # set_rule(overworld_to_bottom_right_room, can_destroy_bush)
# 
#     # Because the function has to be defined locally, most worlds prefer the lambda syntax.
#         # set_rule(overworld_to_top_left_room, lambda state: state.has("Key", world.player))
# 
#     # Conditions can depend on event items.
#         # set_rule(right_room_to_final_boss_room, lambda state: state.has("Top Left Room Button Pressed", world.player))
# 
#     # Some entrance rules may only apply if the player enabled certain options.
#     # In our case, if the hammer option is enabled, we need to add the Hammer requirement to the Entrance from
#     # Overworld to the Top Middle Room.
#         # if world.options.hammer:
#         #     overworld_to_top_middle_room = world.get_entrance("Overworld to Top Middle Room")
#         #     set_rule(overworld_to_top_middle_room, lambda state: state.has("Hammer", world.player))


def set_all_location_rules(world: Grime2World) -> None:
    """
        Placeholder
    """
#     # Location rules work no differently from Entrance rules.
#     # Most of our locations are chests that can simply be opened by walking up to them.
#     # Thus, their logical requirements are covered by the Entrance rules of the Entrances that were required to
#     # reach the region that the chest sits in.
#     # However, our two enemies work differently.
#     # Entering the room with the enemy is not enough, you also need to have enough combat items to be able to defeat it.
#     # So, we need to set requirements on the Locations themselves.
#     # Since combat is a bit more complicated, we'll use this chance to cover some advanced access rule concepts.
# 
#     # Sometimes, you may want to have different rules depending on the player's chosen options.
#     # There is a wrong way to do this, and a right way to do this. Let's do the wrong way first.
#     right_room_enemy = world.get_location("Right Room Enemy Drop")
# 
#     # DON'T DO THIS!!!!
#     set_rule(
#         right_room_enemy,
#         lambda state: (
#             state.has("Sword", world.player)
#             and (not world.options.hard_mode or state.has_any(("Shield", "Health Upgrade"), world.player))
#         ),
#     )
#     # DON'T DO THIS!!!!
# 
#     # Now, what's actually wrong with this? It works perfectly fine, right?
#     # If hard mode disabled, Sword is enough. If hard mode is enabled, we also need a Shield or a Health Upgrade.
#     # The access rule we just wrote does this correctly, so what's the problem?
#     # The problem is performance.
#     # Most of your world code doesn't need to be perfectly performant, since it just runs once per slot.
#     # However, access rules in particular are by far the hottest code path in Archipelago.
#     # An access rule will potentially be called thousands or even millions of times over the course of one generation.
#     # As a result, access rules are the one place where it's really worth putting in some effort to optimize.
#     # What's the performance problem here?
#     # Every time our access rule is called, it has to evaluate whether world.options.hard_mode is True or False.
#     # Wouldn't it be better if in easy mode, the access rule only checked for Sword to begin with?
#     # Wouldn't it also be better if in hard mode, it already knew it had to check Shield and Health Upgrade as well?
#     # Well, we can achieve this by doing the "if world.options.hard_mode" check outside the set_rule call,
#     # and instead having two *different* set_rule calls depending on which case we're in.
# 
#     if world.options.hard_mode:
#         # If you have multiple conditions, you can obviously chain them via "or" or "and".
#         # However, there are also the nice helper functions "state.has_any" and "state.has_all".
#         set_rule(
#             right_room_enemy,
#             lambda state: (
#                 state.has("Sword", world.player) and state.has_any(("Shield", "Health Upgrade"), world.player)
#             ),
#         )
#     else:
#         set_rule(right_room_enemy, lambda state: state.has("Sword", world.player))
    set_rule(world.get_location(EnumLoc.BIRTHPLACE_UPPER_FORCE_CAPACITY.value),
             lambda state: canClimbWalls(world.player, state) and canCrossSpikeTunnels(world.player, state))
    
    # Discarded Flesh requires Grasp
    set_rule(world.get_location(EnumLoc.KANKAN_DISCARDED_FLESH.value), lambda state: canGrasp(world.player, state))
    set_rule(world.get_location(EnumLoc.MARAHS_DISCARDED_FLESH.value), lambda state: canGrasp(world.player, state))

    # Entrance to Kankan, requires Mountainborn Kill
    #set_rule(world.get_entrance("Marah's Orchard to Kankan"),lambda state: state.can_reach_location(EnumLoc.UNDERHEADS_MOUNTAINBORN.value, world.player))
    world.set_rule(
        world.get_entrance("Marah's Orchard to Kankan"), 
        CanReachLocation(EnumLoc.UNDERHEADS_MOUNTAINBORN.value))
    
    # Entrance to Palace, requires Tankawrd Warden kill
    #manzils_breathcrown = world.get_entrance("Marah's Orchard to Kankan")
    #manzils_breathcrown.access_rule =)
    
    # Entrance to Palace Jail, requires Locked Sphere
    world.set_rule(
        world.get_entrance("Kankan Upper Palace to Kankan Upper Jail"), 
        Has("Locked Sphere") & CanReachLocation(EnumLoc.UNDERHEADS_MOUNTAINBORN.value))

    
    # Getting Manzil's Breathcrown, requires Yr'Gog being freed
    # manzil_breathcrown = world.get_location(EnumLoc.MUDFALLS_MANZIL_BREATHCROWN.value)
    # manzil_breathcrown_rule_1 = world.has(EnumItem.QI_LOCKED_SPHERE.value)
    # manzil_breathcrown.set_rule(manzil_breathcrown_rule_1)
    # set_rule(
    #     world.get_location(EnumLoc.MUDFALLS_MANZIL_BREATHCROWN.value),
    #     lambda state: state.can_reach_region(EnumRegions.KANKAN_UPPER_JAIL.value, world.player)
    # )
    world.set_rule(
        world.get_location(EnumLoc.MUDFALLS_MANZIL_BREATHCROWN.value),
        CanReachRegion(EnumRegions.KANKAN_UPPER_JAIL.value))
    
    
    
    # birthplace_force_capacity = world.get_location(LocTemple.BIRTHPLACE_UPPER_FORCE_CAPACITY)
    # set_rule(
    #     birthplace_force_capacity,
    #     lambda state: canClimbWalls(world.player, state) and canCrossSpikeTunnels(world.player, state))
# 
#     # Another way to chain multiple conditions is via the add_rule function.
#     # This makes the access rules a bit slower though, so it should only be used if your structure justifies it.
#     # In our case, it's pretty useful because hard mode and easy mode have different requirements.
#     final_boss = world.get_location("Final Boss Defeated")
# 
#     # For the "known" requirements, it's still better to chain them using a normal "and" condition.
#     add_rule(final_boss, lambda state: state.has_all(("Sword", "Shield"), world.player))
# 
#     if world.options.hard_mode:
#         # You can check for multiple copies of an item by using the optional count parameter of state.has().
#         add_rule(final_boss, lambda state: state.has("Health Upgrade", world.player, 2))


def set_completion_condition(world: Grime2World) -> None:
    """
        Placeholder
    """
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
    
def canCrossSpikeTunnels(player: int, state: CollectionState) -> bool:
    return lambda state: (
        state.has(EnumItem.IM_EMBEDDING_NAIL.value, player)
        or state.has_all([EnumItem.AM_HANDJUMP.value, EnumItem.AM_AIRDASH.value], player)
    )

def canClimbWalls(player, state: CollectionState) -> bool:
    return lambda state: state.has(EnumItem.AM_WALLJUMP.value, player)

def canBurstJump(player, state: CollectionState) -> bool:
    return lambda state: state.has(EnumItem.AM_BURSTJUMP.value, player)

def canHandJump(player, state: CollectionState) -> bool:
    return lambda state: state.has(EnumItem.AM_HANDJUMP.value, player)

def canHighJump(player, state: CollectionState) -> bool:
    return lambda state: state.has_any([EnumItem.AM_BURSTJUMP.value, EnumItem.AM_HANDJUMP.value], player)

def canGrasp(player, state: CollectionState) -> bool:
    return lambda state: state.has(EnumItem.AC_GRASP.value, player)

def canGraspHook(player, state: CollectionState) -> bool:
    return lambda state: state.has_all([EnumItem.AC_GRASP.value, EnumItem.AM_GRASPHOOK.value], player)

def canItemGrasp(player, state: CollectionState) -> bool:
    if ItemGrasp:
        return lambda state: state.has_all([EnumItem.AC_GRASP.value, EnumItem.AC_ITEM_GRASP.value], player)
    else:
        return lambda state: state.has(EnumItem.MI_THIRD_OF_FLESH.value, player, 3)

def canGraspHookSlide(player, state: CollectionState) -> bool:
    return lambda state: state.has_all([EnumItem.AC_GRASP.value, EnumItem.AM_GRASPHOOK.value, EnumItem.AM_GRASPSLIDE.value], player)

def canAirDash(player, state: CollectionState) -> bool:
    return lambda state: state.has(EnumItem.AM_AIRDASH.value, player)

def canItemExplode(player, state: CollectionState) -> bool:
    return lambda state: state.has_any([EnumItem.IM_VOLATILE_VASE.value, EnumItem.IM_OVERGROWN_BLOB.value], player)

def isBreathcrowned(player, state: CollectionState) -> bool:
    return lambda state: state.has_any(EnumItem.BC_MANZILS_BREATHCROWN, player)
    

# def set_dredge_rule(world_location: Location, location: DREDGELocationData, player: int) -> None:
#     add_rule(world_location, lambda state: state.has("Dredge Crane", player))
#     match location.requirement:
#         case "explosives":
#             add_rule(world_location, lambda state: state.has("Packed Explosives", player))
#         case "icebreaker":
#             add_rule(world_location, lambda state: state.has("Icebreaker", player))
#         case "":
#             return
#         case _:
#             #maybe log here
#             return
#     return