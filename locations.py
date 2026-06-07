from __future__ import annotations
from typing import TYPE_CHECKING
#from typing import cast, ClassVar, Optional, Dict, List, Set
from BaseClasses import ItemClassification as IC, Location, Region
from dataclasses import dataclass
from . import items
from .enums import LocTemple, EnumRegions

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
    temple_of_hands_birthplace_lower = world.get_region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value)
    temple_of_hands_birthplace_upper = world.get_region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_UPPER.value)
    temple_of_hands_dried_paint = world.get_region(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value)
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
    
location_data: list[Grime2LocationData] = [
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, LocTemple.BIRTHPLACE_LOWER_MAUL_AXE, 1),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, LocTemple.BIRTHPLACE_LOWER_ATRIUM_1, 2),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, LocTemple.BIRTHPLACE_LOWER_ATRIUM_2, 3),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, LocTemple.BIRTHPLACE_LOWER_LEFT, 4),
    #Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, LocTemple.BIRTHPLACE_LOWER_OVERGROWN_BARRIER, 5),
    
    #Grime2LocationData("Temple of Hands", LocTemple.HALL_SPIKE_GAP_FRAGMENTS, 6),
    #Grime2LocationData("Temple of Hands", LocTemple.SEALED_CHAMBER_BOUND_SHELL, 40),
]

LOCATION_NAME_TO_ID = {location.name.value: location.ap_id for location in location_data}


def create_events(world: Grime2World) -> None:
    """
    Placeholder
    """
    victory_zone = world.get_region(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT)
    victory_zone.add_event(
        LocTemple.BIRTHPLACE_LOWER_OVERGROWN_BARRIER, "Victory", location_type=Grime2Location, item_type=items.Grime2Item
    )
