from __future__ import annotations
from typing import TYPE_CHECKING
#from typing import cast, ClassVar, Optional, Dict, List, Set
from BaseClasses import ItemClassification, Location, Region
from dataclasses import dataclass
from . import items
from .enums import LocTemple

if TYPE_CHECKING:
    from .world import Grime2World

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
#location_name_to_id = {name.value: data for name, data in temple_location_table.items()}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class Grime2Location(Location):
    game = "Grime 2"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: Grime2World) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: Grime2World) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    menu = world.get_region("Menu")
    temple_of_hands = world.get_region("Temple of Hands")
    mudfalls = world.get_region("Mudfalls")
    faceless_mountains = world.get_region("Faceless Mountains")
    marahs_orchard = world.get_region("Marah's Orchard")
    underheads = world.get_region("Underheads")
    kankan = world.get_region("Kankan")
    jagged_forest = world.get_region("Jagged Forest")
    blade_garden = world.get_region("Blade Garden")
    nailglade = world.get_region("Nailglade")
    tree_roots = world.get_region("Tree Roots")
    dregbourg = world.get_region("Dregbourg")
    paint_reef = world.get_region("Paint Reef")
    palladium = world.get_region("Palladium")
    fallen_path = world.get_region("Fallen Path")
    mudpits = world.get_region("Mudpits")
    skyrise = world.get_region("Skyrise")
    starmire = world.get_region("Starmire")
    wanting_tree = world.get_region("Wanting Tree")

    for location in location_data:
        region = world.get_region(location.region)
        region.locations.append(Grime2Location(world.player, location.name.value, location.ap_id, region))

@dataclass
class Grime2LocationData:
    region: str
    name: LocTemple
    ap_id: int
    needGrasp: bool = False
    needBurstJump: bool = False
    needHandJump: bool = False
    needAirDash: bool = False
    
    

# A way to do this is by using the region.add_locations helper.
# For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
# Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
# You also need to pass your overridden Location class.
location_data: list[Grime2LocationData] = [
    Grime2LocationData("Temple of Hands", LocTemple.BIRTHPLACE_MAUL_AXE, 1),
    Grime2LocationData("Temple of Hands", LocTemple.BIRTHPLACE_ATRIUM_1, 2),
    Grime2LocationData("Temple of Hands", LocTemple.BIRTHPLACE_ATRIUM_2, 3),
    Grime2LocationData("Temple of Hands", LocTemple.OVERGROWN_BARRIER, 4),
    Grime2LocationData("Temple of Hands", LocTemple.HANDCLOTH_CHEST, 5),
]

LOCATION_NAME_TO_ID = {location.name.value: location.ap_id for location in location_data}


def create_events(world: Grime2World) -> None:
    """
    Placeholder
    """
#     # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
#     # In our case, the player must press a button in the top left room to open the final boss door.
#     # AP has something for this purpose: "Event locations" and "Event items".
#     # An event location is no different than a regular location, except it has the address "None".
#     # It is treated during generation like any other location, but then it is discarded.
#     # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
#     # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
#         # top_left_room = world.get_region("Top Left Room")
#         # final_boss_room = world.get_region("Final Boss Room")
# 
#     # One way to create an event is simply to use one of the normal methods of creating a location.
#         # button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
#         # top_left_room.locations.append(button_in_top_left_room)
# 
#     # We then need to put an event item onto the location.
#     # An event item is an item whose code is "None" (same as the event location's address),
#     # and whose classification is "progression". Item creation will be discussed more in items.py.
#     # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
#     # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
#     # it is common practice to create the item when creating the location.
#     # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
#     # we'll create both the event location and the event item in our locations.py code.
#         # button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
#         # button_in_top_left_room.place_locked_item(button_item)
# 
#     # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
#     # Luckily, we have another event we want to create: The Victory event.
#     # We will use this event to track whether the player can win the game.
#     # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
#         # final_boss_room.add_event(
#         #     "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
#         # )
# 
#     # If you create all your regions and locations line-by-line like this,
#     # the length of your create_regions might get out of hand.
#     # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
#     # However, it is worth understanding how the actual creation of regions and locations works,
#     # That way, we're not just mindlessly copy-pasting! :)le.items()}
