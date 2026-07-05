from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List, Callable, NamedTuple
#from typing import cast, ClassVar, Optional, Dict, List, Set
from BaseClasses import ItemClassification as IC, Location, Region, CollectionState
from dataclasses import dataclass
from . import items
from .enums import EnumLoc, EnumRegions, EnumItem, GRIME_GAME_NAME

if TYPE_CHECKING:
    from .world import Grime2World
location_base_id = 6942013371314159

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
#location_name_to_id = {name.value: data for name, data in temple_location_table.items()}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class Grime2Location(Location):
    game = GRIME_GAME_NAME


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
    
    faceless_mountains_mudfalls = world.get_region(EnumRegions.FACELESS_MOUNTAINS_MUDFALLS.value)
    faceless_mountains_dropot = world.get_region(EnumRegions.FACELESS_MOUNTAINS_DROPOT.value)
    faceless_mountains_melded = world.get_region(EnumRegions.FACELESS_MOUNTAINS_MELDED.value)
    faceless_mountains_main = world.get_region(EnumRegions.FACELESS_MOUNTAINS.value)
    faceless_mountains_wanting_atrium = world.get_region(EnumRegions.FACELESS_MOUNTAINS_WANTING_ATRIUM.value)
    faceless_mountains_wanting_bloodroots = world.get_region(EnumRegions.FACELESS_MOUNTAINS_WANTING_BLOODROOTS.value)
    faceless_mountains_darsh = world.get_region(EnumRegions.FACELESS_MOUNTAINS_DARSH.value)
    
    marahs_orchard_entrance = world.get_region("Marah's Orchard Entrance")
    marahs_orchard_faceblob = world.get_region("Marah's Orchard Faceblob")
    marahs_orchard_main = world.get_region("Marah's Orchard Main")
    marahs_orchard_prime_above = world.get_region("Marah's Orchard Above Prime Pitcher")
    marahs_orchard_prime_dropot = world.get_region("Marah's Orchard Above Prime Pitcher Dropot")
    marahs_orchard_prime = world.get_region("Marah's Orchard Prime Pitcher")
    
    underheads_left_upper = world.get_region(EnumRegions.UNDERHEADS_LEFT_UPPER.value)
    underheads_left_middle = world.get_region(EnumRegions.UNDERHEADS_LEFT_MIDDLE.value)
    underheads_left_lower = world.get_region(EnumRegions.UNDERHEADS_LEFT_LOWER.value)
    underheads_surrogate_left = world.get_region(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value)
    underheads_lower_hunt = world.get_region(EnumRegions.UNDERHEADS_LOWER_HUNT.value)
    underheads_before_mountainborn = world.get_region(EnumRegions.UNDERHEADS_BEFORE_MOUNTAINBORN.value)
    underheads_mountainborn = world.get_region(EnumRegions.UNDERHEADS_MOUNTAINBORN.value)
    underheads_lahav_knight = world.get_region(EnumRegions.UNDERHEADS_LAHAV_KNIGHT.value)
    underheads_nailglade_transition = world.get_region(EnumRegions.UNDERHEADS_NAILGLADE_TRANSITION.value)
    underheads_right = world.get_region(EnumRegions.UNDERHEADS_RIGHT.value)
    underheads_forged_little = world.get_region(EnumRegions.UNDERHEADS_FORGED_LITTLE.value)
    underheads_boulder_hands = world.get_region(EnumRegions.UNDERHEADS_BOULDER_HANDS.value)
    underheads_forged_pick = world.get_region(EnumRegions.UNDERHEADS_FORGED_PICK.value)
    underheads_scatter_stone = world.get_region(EnumRegions.UNDERHEADS_SCATTER_STONE.value)
    underheads_alveoli = world.get_region(EnumRegions.UNDERHEADS_ALVEOLI.value)
    underheads_tree_roots = world.get_region(EnumRegions.UNDERHEADS_TREE_ROOTS.value)
    underheads_surrogate_smidge = world.get_region(EnumRegions.UNDERHEADS_SURROGATE_SMIDGE.value)
    underheads_mountainborn_marah = world.get_region(EnumRegions.UNDERHEADS_MOUNTAINBORN_MARAH.value)
    underheads_overgrown_blob = world.get_region(EnumRegions.UNDERHEADS_MOUNTAINBORN_OVERGROWN_BLOB.value)
    
    kankan = world.get_region("Kankan Upper Main")
    
    jagged_forest = world.get_region("Jagged Forest")
    # blade_garden_upper = world.get_region("Blade Garden Upper")
    # blade_garden_middle = world.get_region("Blade Garden Middle")
    # blade_garden_lower = world.get_region("Blade Garden Lower")
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
    name: EnumLoc
    ap_id: int
    rule: Optional[Callable[[CollectionState], bool]] = None
    needGrasp: bool = False
    
location_data: list[Grime2LocationData] = [
    # Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, EnumLoc.SURROGATE_BIRTHPLACE, location_base_id + 1),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, EnumLoc.BIRTHPLACE_LOWER_MAUL_AXE, location_base_id + 2),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, EnumLoc.BIRTHPLACE_LOWER_ATRIUM_1, location_base_id + 3),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, EnumLoc.BIRTHPLACE_LOWER_ATRIUM_2, location_base_id + 4),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, EnumLoc.BIRTHPLACE_LOWER_LEFT, location_base_id + 5),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, EnumLoc.BIRTHPLACE_LOWER_OVERGROWN_BARRIER, location_base_id + 6),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_UPPER.value, EnumLoc.BIRTHPLACE_UPPER_FORMLESS_SKIN, location_base_id + 7),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_UPPER.value, EnumLoc.BIRTHPLACE_UPPER_EMBEDDING_NAIL, location_base_id + 8),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_UPPER.value, EnumLoc.BIRTHPLACE_UPPER_FORCE_CAPACITY, location_base_id + 9),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.SURROGATE_DRIED_PAINT, location_base_id + 10),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.SEAL_DRIED_PAINT, location_base_id + 11),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_HANDCLOTH_CHEST, location_base_id + 12),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_HANDCLOTH_HANDS, location_base_id + 13),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_KNIFEHAND, location_base_id + 14),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_ATRIUM_SPIKE_PIT, location_base_id + 15),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_HANDCLOTH_LEGS, location_base_id + 16),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_FRAGMENTS_BEFORE_SEAL, location_base_id + 17),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_ATRIUM_ABOVE_SEAL, location_base_id + 18),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_FRAGMENTS_CHAINS_ROOM_1, location_base_id + 19),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_FRAGMENTS_CHAINS_ROOM_2, location_base_id + 20),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_CLASPED_MACE, location_base_id + 21),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_ATRIUM_AFTER_CLASPED_MACE, location_base_id + 22),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_ITEM_SPIKE_PIT, location_base_id + 23),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_SPIKE_GAP_FRAGMENTS, location_base_id + 24),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, EnumLoc.DRIED_PAINT_SPIKE_GAP_ATRIUM, location_base_id + 25),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_SEALED_CHAMBER.value, EnumLoc.SURROGATE_SEALED_CHAMBER, location_base_id + 26),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_SEALED_CHAMBER.value, EnumLoc.SEALED_CHAMBER_FRAGMENTS, location_base_id + 27),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_BOUND_SHELL.value, EnumLoc.SEALED_CHAMBER_BOUND_SHELL, location_base_id + 28, rule=lambda state: state.has(EnumItem.AC_GRASP, Grime2World.player)),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.SEALED_CHAMBER_PRISMATIC_PEARL, location_base_id + 29), # placing this in "Hall" because its acquired after BoundShell
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.SURROGATE_HALL, location_base_id + 30),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.SEAL_HALL, location_base_id + 31),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_LEFT_OF_SURROGATE, location_base_id + 32),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_RIGHT_OF_SURROGATE, location_base_id + 33),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_EMBEDDING_NAIL_SURROGATE, location_base_id + 34),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_THROWING_THUMBS, location_base_id + 35),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_ATRIUM_UNDER_YEARNING, location_base_id + 36),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_ATRIUM_ABOVE_SURROGATE, location_base_id + 37),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_ATRIUM_TOPLEFT_SURROGATEL, location_base_id + 38),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_TOPLEFT_OVERGROWN_BLOB, location_base_id + 39),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_TOPLEFT_ATRIUM, location_base_id + 40),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_FRAGMENTS_ABOVE_SURROGATE, location_base_id + 41),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_PEARL, location_base_id + 42),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_TOP_ATRIUM_BREAKABLE, location_base_id + 43),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_FRAGMENTS_AFTER_HUNT_ABOVE, location_base_id + 44),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_FRAGMENTS_AFTER_HUNT_LEDGE, location_base_id + 45),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_HOMING_DROPLET_TOP, location_base_id + 46),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_ATRIUM_RIGHT_OF_KNIFEHAND, location_base_id + 47),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_RUST_FISTS, location_base_id + 48),
    Grime2LocationData(EnumRegions.TEMPLE_OF_HANDS_HALL.value, EnumLoc.HALL_BLOODROOT_SPLINTER_TOP, location_base_id + 49),
    
    # # # # # # #
    # Mudfalls
    # # # # # # #
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_SURROGATE_ALCOVE, location_base_id + 1001),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_ATRIUM, location_base_id + 1002),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_FRAGMENTS, location_base_id + 1003),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_OVERGROWN_BLOB, location_base_id + 1004),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_BLOODROOT, location_base_id + 1005),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_ATRIUM_ALCOVE, location_base_id + 1006),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_MISC, location_base_id + 1007),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_BLOODROOT_ELEVATOR, location_base_id + 1008),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_FRAGMENTS_ELEVATOR, location_base_id + 1009),
    Grime2LocationData(EnumRegions.MUDFALLS_ELEVATOR.value, EnumLoc.MUDFALLS_LUMP_OF_HANDS, location_base_id + 1010), #  // Needs jump boost and Grasp Hook and Grasp Slide
    Grime2LocationData(EnumRegions.MUDFALLS_ELEVATOR.value, EnumLoc.MUDFALLS_PEARL, location_base_id + 1011), #   // Needs jump boost and Grasp Hook and Grasp Slide
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_SEAL_LEFT, location_base_id + 1012),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_SURROGATE_MANZIL, location_base_id + 1013),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_MISC_FORCE, location_base_id + 1014),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_PEARL_MANZIL, location_base_id + 1015),
    Grime2LocationData(EnumRegions.MUDFALLS_ABOVE_MANZIL_RIGHT.value, EnumLoc.MUDFALLS_PEARL_MANZIL_ABOVE, location_base_id + 1016), #  // Burst Jump or Handjump OR Grasp Hook
    Grime2LocationData(EnumRegions.MUDFALLS_ABOVE_MANZIL_RIGHT_TOP.value, EnumLoc.MUDFALLS_SIGIL_BARRIER, location_base_id + 1017), #  // Burst Jump or Handjump
    Grime2LocationData(EnumRegions.MUDFALLS_ABOVE_MANZIL_CENTER.value, EnumLoc.MUDFALLS_ATRIUM_MANZIL, location_base_id + 1018), #  // Wall Jump
    Grime2LocationData(EnumRegions.MUDFALLS_ABOVE_MANZIL_SIDE.value, EnumLoc.MUDFALLS_HOMING_DROPLET, location_base_id + 1019), #  // HandJump AND Air Dash OR Wall Jump
    Grime2LocationData(EnumRegions.MUDFALLS_ABOVE_MANZIL_TOP.value, EnumLoc.MUDFALLS_REINFORCING_WEAVE, location_base_id + 1020), #  // ((HandJump AND Air Dash) OR Wall Jump) AND Item Grasp
    Grime2LocationData(EnumRegions.MUDFALLS_ABOVE_MANZIL_LEFT.value, EnumLoc.MUDFALLS_LUMP_OF_HANDS_MANZIL, location_base_id + 1021), #  // Grasp Hook AND Grasp Slide AND (BurstJumpORHandJump) AND Air Dash
    Grime2LocationData(EnumRegions.MUDFALLS_ABOVE_MANZIL_LEFT_TOP.value, EnumLoc.MUDFALLS_BLOODROOT_MANZIL, location_base_id + 1022), #  // Grasp Hook AND Grasp Slide AND (BurstJumpORHandJump) AND Air Dash AND WallJump
    Grime2LocationData(EnumRegions.MUDFALLS_STRAND.value, EnumLoc.MUDFALLS_MARAH_STRAND, location_base_id + 1023), #  // Wall Jump AND Grasp Hook
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_HOMING_DROPLET_MANZIL, location_base_id + 1024),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_BLOODROOT_UNDERGROUND, location_base_id + 1025),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_ATRIUM_UNDERGROUND, location_base_id + 1026),
    Grime2LocationData(EnumRegions.MUDFALLS_SPIKE_PIT.value, EnumLoc.MUDFALLS_HEART_OF_A_DANCER, location_base_id + 1027), #  // Item Grasp
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_ARMOR_FORGED_LITTLE, location_base_id + 1028),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_FRAGMENTS_CAVE, location_base_id + 1029),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_OVERGROWN_BLOB_CAVE, location_base_id + 1030),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_SEAL_RIGHT, location_base_id + 1031),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_PEARL_FACELESS, location_base_id + 1032),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_OVERGROWN_BLOB_MANZIL, location_base_id + 1033),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_ATRIUM_FACELESS, location_base_id + 1034),
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_WEAPON_FORGED_STAKE, location_base_id + 1035), #  // BARRIER/Underheads . Wall Jump (Burst/Hand Jump)
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_WEAPON_THROWING_STARS, location_base_id + 1036), #  // Chisel Key // Needs jump boost and Grasp Hook and Grasp Slide
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_MANZIL_SPHERE, location_base_id + 1037), #  // Chisel Key // Needs jump boost and Grasp Hook and Grasp Slide
    Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_SIBLING_WEAVE, location_base_id + 1038), #  // Chisel Key // Needs jump boost and Grasp Hook and Grasp Slide
    # Grime2LocationData(EnumRegions.MUDFALLS.value, EnumLoc.MUDFALLS_MANZIL_BREATHCROWN, location_base_id + 1039), #  // Chisel Key // Needs jump boost and Grasp Hook and Grasp Slide

    # # # # # # #
    # Faceless Mountains
    # # # # # # #
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_SURROGATE_HALFMADE, location_base_id + 2001),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_PEARL, location_base_id + 2002),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_SPIKE_BALL_SURROGATE, location_base_id + 2003), # (Wall Climb AND Dash Slide) OR Item Grasp AND (Wall Clumb OR Hand Jump OR Burst Jump)
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS_DROPOT.value, EnumLoc.FACELESS_BLOODROOT_DROPOT, location_base_id + 2004),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_SEAL_UPPER, location_base_id + 2005),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_SPIKE_BALL_PIT, location_base_id + 2006),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_FRAGMENTS, location_base_id + 2007),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_WEAPON_ATTUNING_BOW, location_base_id + 2008),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_SURROGATE_INTERTWINING, location_base_id + 2009),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_ATRIUM_LONG_1, location_base_id + 2010),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_ATRIUM_LONG_2, location_base_id + 2011),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_SPIKE_BALL_LONG_ROOM, location_base_id + 2012),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_HOMING_DROPLET_LONG, location_base_id + 2013),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_GRUNT_GARBS_HANDS, location_base_id + 2014),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_BLOODROOT_LONG, location_base_id + 2015),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_GRUNT_GARBS_LEGS, location_base_id + 2016), # Grasp
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_GRUNT_GARBS_CHEST, location_base_id + 2017),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_FRAGMENTS_MELDED_L, location_base_id + 2018),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_FRAGMENTS_MELDED_R, location_base_id + 2019),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS_MELDED.value, EnumLoc.FACELESS_BOSS_MELDED_REWARD, location_base_id + 2020),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_FRAGMENTS_MUDFALLS, location_base_id + 2021), # Grasp OR Hand Jump OR Burst Jump
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_BRUTE_GARBS_HANDS, location_base_id + 2022), # Grasp
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_WEAPON_SPEAR, location_base_id + 2023),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_SEAL_LOWER, 2024),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_BRUTE_GARBS_CHEST, location_base_id + 2025),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_BRUTE_GARBS_LEGS, location_base_id + 2026),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_BLOODROOT_DARSH, location_base_id + 2027),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS.value, EnumLoc.FACELESS_OVERGROWN_BLOB, location_base_id + 2028),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS_DARSH.value, EnumLoc.FACELESS_BOSS_DARSH_REWARD, location_base_id + 2029),
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS_WANTING_ATRIUM.value, EnumLoc.FACELESS_ATRIUM_WANTING_TREE_1, location_base_id + 2030), # WallJump AND Grasphook
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS_WANTING_BLOODROOTS.value, EnumLoc.FACELESS_ATRIUM_WANTING_TREE_2, location_base_id + 2031), # WallJump AND Grasphook AND BurstJump/Handjump
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS_WANTING_BLOODROOTS.value, EnumLoc.FACELESS_BLOODROOT_WANTING_TREE_1, location_base_id + 2032), # WallJump AND Grasphook AND BurstJump/Handjump
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS_WANTING_BLOODROOTS.value, EnumLoc.FACELESS_BLOODROOT_WANTING_TREE_2, location_base_id + 2033), # WallJump AND Grasphook AND BurstJump/Handjump
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS_WANTING_BLOODROOTS.value, EnumLoc.FACELESS_BLOODROOT_SURROGATE, location_base_id + 2034), # (Handjump OR BurstJump) AND Wall BClimb
    Grime2LocationData(EnumRegions.FACELESS_MOUNTAINS_DARSH.value, EnumLoc.FACELESS_HOMING_DROPLET_MARAHS, location_base_id + 2035),
    # Galloping Dropot only needs Wall CLimb

    # # # # # # #
    # Underheads
    # # # # # # #
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_SURROGATE_SUNKEN, location_base_id + 3001),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_SEAL_SUNKEN, location_base_id + 3002),
    Grime2LocationData(EnumRegions.UNDERHEADS_LEFT_MIDDLE.value, EnumLoc.UNDERHEADS_BLOODROOT_MUDFALLS, location_base_id + 3003),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_SPIKE_BALL_SUNKEN, location_base_id + 3004),
    Grime2LocationData(EnumRegions.UNDERHEADS_FORGED_PICK.value, EnumLoc.UNDERHEADS_WEAPON_FORGED_PICK, location_base_id + 3005), #GraspANDGraspHook
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_SCATTER_STONE_PICK, location_base_id + 3006),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_FRAGMENTS, location_base_id + 3007),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_FORGED_BOULDER_CHEST, location_base_id + 3008),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_SPIKE_BALL_SEAL, location_base_id + 3009),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_BLOODROOT_SEAL_LEFT, location_base_id + 3010),
    Grime2LocationData(EnumRegions.UNDERHEADS_SCATTER_STONE.value, EnumLoc.UNDERHEADS_SCATTER_STONE_SAND, location_base_id + 3011),
    Grime2LocationData(EnumRegions.UNDERHEADS_LOWER_HUNT.value, EnumLoc.UNDERHEADS_MARAH_STRAND_DROPOT, location_base_id + 3012),
    Grime2LocationData(EnumRegions.UNDERHEADS_LOWER_HUNT.value, EnumLoc.UNDERHEADS_ATRIUM_SAND, location_base_id + 3013),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_SCATTER_STONE_LEGS, location_base_id + 3014),
    Grime2LocationData(EnumRegions.UNDERHEADS_BOULDER_HANDS.value, EnumLoc.UNDERHEADS_FORGED_BOULDER_HANDS, location_base_id + 3015), #(GraspANDGraspHook) AND (WallClimb Or AirDash)
    Grime2LocationData(EnumRegions.UNDERHEADS_BEFORE_MOUNTAINBORN.value, EnumLoc.UNDERHEADS_BLOODROOT_FORGED_HANDS, location_base_id + 3016),
    Grime2LocationData(EnumRegions.UNDERHEADS_BEFORE_MOUNTAINBORN.value, EnumLoc.UNDERHEADS_SEAL_RIGHT, location_base_id + 3017),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_ATRIUM_SEAL_1, location_base_id + 3018),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_ATRIUM_SEAL_2, location_base_id + 3019),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_ATRIUM_GAP, location_base_id + 3020),
    Grime2LocationData(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, EnumLoc.UNDERHEADS_FORGED_BOULDER_LEGS, location_base_id + 3021),
    Grime2LocationData(EnumRegions.UNDERHEADS_ALVEOLI.value, EnumLoc.UNDERHEADS_SPIKE_BALL_ABOVE_SUNKEN, location_base_id + 3022), #GraspANDGraspHook
    Grime2LocationData(EnumRegions.UNDERHEADS_ALVEOLI.value, EnumLoc.UNDERHEADS_ALVEOLI, location_base_id + 3023), #GraspAndGraspHook
    Grime2LocationData(EnumRegions.UNDERHEADS_BEFORE_MOUNTAINBORN.value, EnumLoc.UNDERHEADS_ATRIUM_SERGEANT, location_base_id + 3024),
    Grime2LocationData(EnumRegions.UNDERHEADS_BEFORE_MOUNTAINBORN.value, EnumLoc.UNDERHEADS_SURROGATE_CURLING, location_base_id + 3025),
    Grime2LocationData(EnumRegions.UNDERHEADS_RIGHT.value, EnumLoc.UNDERHEADS_SMIDGE_OF_PAINT, location_base_id + 3026), #Grasphook AND WallJump
    Grime2LocationData(EnumRegions.UNDERHEADS_MOUNTAINBORN.value, EnumLoc.UNDERHEADS_MOUNTAINBORN, location_base_id + 3027),
    Grime2LocationData(EnumRegions.UNDERHEADS_RIGHT.value, EnumLoc.UNDERHEADS_BLOODROOT_MOUNTAINBORN, location_base_id + 3028),
    Grime2LocationData(EnumRegions.UNDERHEADS_MOUNTAINBORN.value, EnumLoc.UNDERHEADS_MARAH_STRAND_ABOVE_MOUNTAINBORN, location_base_id + 3029),
    Grime2LocationData(EnumRegions.UNDERHEADS_RIGHT.value, EnumLoc.UNDERHEADS_OVERGROWN_BLOB, location_base_id + 3030), #BurstJumpOrHandJumpANDWallJump
    Grime2LocationData(EnumRegions.UNDERHEADS_TREE_ROOTS.value, EnumLoc.UNDERHEADS_WEAPON_BARBED_SWORD, location_base_id + 3031), #GraspANDGraspHookANDWallJump
    Grime2LocationData(EnumRegions.UNDERHEADS_RIGHT.value, EnumLoc.UNDERHEADS_HOMING_DROPLETS, location_base_id + 3032),
    Grime2LocationData(EnumRegions.UNDERHEADS_RIGHT.value, EnumLoc.UNDERHEADS_MARAH_STRAND_MOUNTAINBORN, location_base_id + 3033), #BurstJumpANDAirDashANDWallJump
    Grime2LocationData(EnumRegions.UNDERHEADS_LAHAV_KNIGHT.value, EnumLoc.UNDERHEADS_THIRD_LAHAV, location_base_id + 3034),
    Grime2LocationData(EnumRegions.UNDERHEADS_RIGHT.value, EnumLoc.UNDERHEADS_BLOODROOT_JAGGED, location_base_id + 3035),
    Grime2LocationData(EnumRegions.UNDERHEADS_LEFT_UPPER.value, EnumLoc.UNDERHEADS_ATRIUM_MUDFALLS_1, location_base_id + 3036), #AirDashANDWallJump(GraspHookANDGrasp)
    Grime2LocationData(EnumRegions.UNDERHEADS_LEFT_UPPER.value, EnumLoc.UNDERHEADS_ATRIUM_MUDFALLS_2, location_base_id + 3037),
    Grime2LocationData(EnumRegions.UNDERHEADS_LEFT_UPPER.value, EnumLoc.UNDERHEADS_FORCE, location_base_id + 3038),
    Grime2LocationData(EnumRegions.UNDERHEADS_LEFT_LOWER.value, EnumLoc.UNDERHEADS_BLOODROOT_DREGBOURG, location_base_id + 3039),

    # # # # # # #
    # Tree Roots
    # # # # # # #
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_SEAL_RIGHT, location_base_id + 4001),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_SURROGATE, location_base_id + 4002),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_MARAH_STRAND_BOTTOM, location_base_id + 4003),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_SCATTER_STONE_SURROGATE, location_base_id + 4004),
    Grime2LocationData(EnumRegions.TREE_ROOTS_VISAGE.value, EnumLoc.TREEROOTS_FORCE, location_base_id + 4005), #HandJumpORBurstJump
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_MARAH_STRAND_VISAGE_1, location_base_id + 4006),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_MARAH_STRAND_VISAGE_2, location_base_id + 4007),
    Grime2LocationData(EnumRegions.TREE_ROOTS_VISAGE.value, EnumLoc.TREEROOTS_HAND_VISAGE_REAWRD, location_base_id + 4008), #HandJumpORBurstJump
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_ATRIUM_SURROGATE, location_base_id + 4009),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_MARAH_STRAND_SURROGATE, location_base_id + 4010),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_SCATTER_STONE_PIT, location_base_id + 4011),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_ATRIUM_HUNT, location_base_id + 4012),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_SMIDGE_OF_PAINT_WALL, location_base_id + 4013),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_MARAH_STRAND_HUNT, location_base_id + 4014),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_SEAL_LEFT, location_base_id + 4015),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_SCATTER_STONE_SEAL, location_base_id + 4016),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_SMIDGE_OF_PAINT_SEAL, location_base_id + 4017),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_BLOODROOT, location_base_id + 4018),
    Grime2LocationData(EnumRegions.TREE_ROOTS.value, EnumLoc.TREEROOTS_ATRIUM_TOP, location_base_id + 4019),

    # # # # # # #
    # Marah's Orchard
    # # # # # # #
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_SURROGATE_BRIDGE, location_base_id + 5001),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_MARAH_STRAND_LEFT_SURROGATE, location_base_id + 5002),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_DISCARDED_FLESH, location_base_id + 5003),
    # Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_MARAH_STRAND_SURROGATE, location_base_id + 5004),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_ATRIUM_TOPLEFT, location_base_id + 5005),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_BLOODROOT_DROPOT, location_base_id + 5006),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_MARAH_STRAND_DROPOT, location_base_id + 5007),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_POACHER_CHEST, location_base_id + 5008),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_SEAL_DROPOT, location_base_id + 5009),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_POACHER_HANDS, location_base_id + 5010),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_FRAGMENTS_HANDS, location_base_id + 5011),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_ATRIUM_LEGS, location_base_id + 5012),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_POACHER_LEGS, location_base_id + 5013),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_FRAGMENTS_LEGS, location_base_id + 5014),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_FORCE, location_base_id + 5015),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_ATRIUM_SURROGATE, location_base_id + 5016),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_SURROGATE_ENTRANCE, location_base_id + 5017),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_SPIKE_BALL_PITCHER, location_base_id + 5018), #(HandJumpORBurstJump)ANDGraspHookANDGraspSlideAndWallJump
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_SKITTERING_DROPOT_CONT, location_base_id + 5019), #(HandJumpORBurstJump)ANDGraspHookANDGraspSlideAndWallJumpANDAirDash
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_HOMING_DROPLET, location_base_id + 5020),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_ALVEOLI, location_base_id + 5021),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_BLOODROOT_ALVEOLI, location_base_id + 5022),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_ATRIUM_SHORTBLADE, location_base_id + 5023),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_SMIDGE_OF_PAINT_FACEBLOB, location_base_id + 5024), #HandJump/BurstJump/WallJump
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_FACEBLOB_REWARD, location_base_id + 5025),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_ALVEOLI_FACEBLOB, location_base_id + 5026),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_OVERGROWN_BLOB_SEAL, location_base_id + 5027),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_SMIDGE_OF_PAINT_ALVEOLI, location_base_id + 5028),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_ATRIUM_SEAL, location_base_id + 5029),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_SEAL_LEFT, location_base_id + 5030),
    Grime2LocationData(EnumRegions.MARAHS_ORCHARD_MAIN.value, EnumLoc.MARAHS_SPIKE_BALL_SEAL, location_base_id + 5031),

    # # # # # # #
    # Kankan
    # # # # # # #
    Grime2LocationData(EnumRegions.KANKAN_UPPER_HEART.value, EnumLoc.KANKAN_HEART_OF_A_TRAVELER, location_base_id + 6001),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_HEART.value, EnumLoc.KANKAN_VOLATILE_VASE_HEART, location_base_id + 6002),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_DROPOT.value, EnumLoc.KANKAN_SKITTERING_DROPOT_CONT, location_base_id + 6003),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_MAIN.value, EnumLoc.KANKAN_SEAL_UPPER, location_base_id + 6004),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_MAIN.value, EnumLoc.KANKAN_BLOODROOT_BY_ET, location_base_id + 6005),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_MAIN.value, EnumLoc.KANKAN_SURROGATE_NAILGLADER, location_base_id + 6006),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_DROPOT.value, EnumLoc.KANKAN_VOLATILE_VASE_TOP, location_base_id + 6007),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_DROPOT.value, EnumLoc.KANKAN_FORCE_UPPER, location_base_id + 6008),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_JAVELIN.value, EnumLoc.KANKAN_CHARGING_JAVELIN_, location_base_id + 6009), #(BurstJump OR HandJump) AND Grasp
    Grime2LocationData(EnumRegions.KANKAN_UPPER_PALACE.value, EnumLoc.KANKAN_WARDEN_REWARD, location_base_id + 6010),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_MAIN.value, EnumLoc.KANKAN_BLOODROOT_SURROGATE, location_base_id + 6011),
    Grime2LocationData(EnumRegions.KANKAN_UPPER_MAIN.value, EnumLoc.KANKAN_RAKIK_REWARD, location_base_id + 6012),
    
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_ATRIUM_ELEVATOR, location_base_id + 6101),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_MARAH_STRAND_ELEVATOR, location_base_id + 6102),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_FRAGMENTS_SURROGATE, location_base_id + 6103),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_VOLATILE_VASE_SAVIOUR, location_base_id + 6104),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_ATRIUM.value, EnumLoc.KANKAN_ATRIUM_SURROGATE, location_base_id + 6105), #WallJump
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_SURROGATE_SAVIOUR, location_base_id + 6106),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_BLOODROOT_BUILDING, location_base_id + 6107),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_ATRIUM_ALVEOLI, location_base_id + 6108),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_ALVEOLI, location_base_id + 6109),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_ALV_HOUSE.value, EnumLoc.KANKAN_VOLATILE_VASE_ALVEOLI, location_base_id + 6110), #WallJump
    Grime2LocationData(EnumRegions.KANKAN_LOWER_ALV_HOUSE_TOP.value, EnumLoc.KANKAN_PITCHER_GUARD_LEGS, location_base_id + 6111),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_ALV_HOUSE_TOP.value, EnumLoc.KANKAN_MARAH_STRAND_HANDS, location_base_id + 6112),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_PITCHER_GUARD_HANDS, location_base_id + 6113),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_PITCHER_GUARD_CHEST, location_base_id + 6114),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_FORCE_LOWER, location_base_id + 6115),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_HOLSTER.value, EnumLoc.KANKAN_FRAGMENTS_HOLSTER, location_base_id + 6116), #AirDash OR (BurstJump OR HandJump)
    Grime2LocationData(EnumRegions.KANKAN_LOWER_HOLSTER.value, EnumLoc.KANKAN_VOLATILE_VASE_HOLSTER, location_base_id + 6117), #WallJump
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_CHARGING_JAVELIN_QISSA, location_base_id + 6118),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_BLOODROOT_JAGGED, location_base_id + 6119),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_MARAH_STRAND_SEAL, location_base_id + 6120),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_PREACHER.value, EnumLoc.KANKAN_PREACHER_REWARD, location_base_id + 6121),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_PREACHER.value, EnumLoc.KANKAN_DISCARDED_FLESH, location_base_id + 6122),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_VOLATILE_VASE_PREACHER, location_base_id + 6123),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_ATRIUM_JAIL, location_base_id + 6124),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_MARAH_STRAND_JAIL, location_base_id + 6125),
    Grime2LocationData(EnumRegions.KANKAN_LOWER_MAIN.value, EnumLoc.KANKAN_SEAL_LOWER, location_base_id + 6126),

    # # # # # # #
    # Nailglade
    # # # # # # #
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_LAHAVIST_NOMAD_LEGS, location_base_id + 7001),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_LAHAVIST_NOMAD_HANDS, location_base_id + 7002),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_LAHAVIST_NOMAD_CHEST, location_base_id + 7003),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_MARAH_STRAND_LAHAV_KNIGHT, location_base_id + 7004),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_SEAL_RIGHT, location_base_id + 7005),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_SCOUT_CHEST, location_base_id + 7006),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_SCOUT_LEGS, location_base_id + 7007),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_HANDBEAST_REWARD, location_base_id + 7008),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_SCOUT_HANDS, location_base_id + 7009), # grasphook/walljump
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_BLOODROOT_SCOUT, location_base_id + 7010), # grasphook/walljump
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_THIRD_OF_FLESH_HANDBEAST, location_base_id + 7011), # Ghook+Airdash+Walljump
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_MARAH_STRAND_BREATHCROWN, location_base_id + 7012), # walljump
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_MARAH_STRAND_TOWN_LOWER, location_base_id + 7013),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_EMBEDDING_NAIL_TOWN_EDGE, location_base_id + 7014),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_MARAH_STRAND_DROPOT, location_base_id + 7015),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_ALVEOLI_TREE, location_base_id + 7016), # airdash
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_HEART_OF_A_BREATHWEAVER, location_base_id + 7117), # walljump+(handjump or bjump+adash)
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_BLOODROOT_TOWN, location_base_id + 7018), #  walljump+(handjump or bjump+adash)
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_BLOODROOT_WORKSHOP, location_base_id + 7019), #  Workshop Key
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_ATRIUM_WORKSHOP_1, location_base_id + 7020), # Workshop Key
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_VOLATILE_VASE_WORKSHOP, location_base_id + 7021), # Workshop Key
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_ATRIUM_WORKSHOP_2, location_base_id + 7022), # Workshop Key
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_VOLATILE_VASE_BURDEN, location_base_id + 7023), # Workshop Key
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_ATRIUM_TOWN, location_base_id + 7024),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_TWINPALM_REWARD, location_base_id + 7025),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_BLOODROOT_KNIGHT, location_base_id + 7026), # AirDash
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_LAHAV_KNIGHT, location_base_id + 7027), # AirDash
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_DISCARDED_FLESH, location_base_id + 7028), # 07_NailGlade_Background_AlwaysOn_BAKED_BASE_HARD_HIGH_LAYER 1
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_FINGERCLUMP_MACE, location_base_id + 7029),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_SURROGATE_OUTSKIRTS, location_base_id + 7030),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_FORCE, location_base_id + 7031), # ADash+WJump
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_HOMING_DROPLET, location_base_id + 7032), # ADash+WJump +Grasp
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_MARAH_STRAND_SURROGATE, location_base_id + 7033), # ADash+WJump +Grasp
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_ATRIUM_SURROGATE, location_base_id + 7034), # ADash+WJump +Grasp
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_FIGHTER_CHEST, location_base_id + 7035), # ADash+WJump +Grasp
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_FIGHTER_LEGS, location_base_id + 7036), # ADash+WJump +Grasp
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_FIGHTER_HANDS, location_base_id + 7037), # ADash+WJump +Grasp
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_BLOODROOT_SURROGATE, location_base_id + 7038), # ADash+WJump +Grasp
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_FRAGMENTS, location_base_id + 7039),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_SEAL_LEFT, location_base_id + 7040),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_SMIDGE_OF_PAINT, location_base_id + 7041),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_OVERGROWN_BLOB, location_base_id + 7042),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_THIRD_OF_FLESH_TOWN, location_base_id + 7043),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_MARAH_STRAND_FLESH, location_base_id + 7044),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_MARAH_STRAND_TOWN_UPPER, location_base_id + 7045),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_THIRD_OF_FLESH_UNDERHEADS, location_base_id + 7046),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_BLOODROOT_JAGGED, location_base_id + 7047),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_ATRIUM_FOREST, location_base_id + 7048),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_EMBEDDING_NAIL_TOWN, location_base_id + 7049),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_CHAIN_JAVELIN, location_base_id + 7050),
    Grime2LocationData(EnumRegions.NAILGLADE.value, EnumLoc.NAILGLADE_RAKING_SWORD, location_base_id + 7051),
    

    # # # # # # #
    # DregBourg
    # # # # # # #
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SURROGATE_ENTRANCE, location_base_id + 8001),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_PEARL, location_base_id + 8002), #HandJumpORBurstJump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_THROWING_NAILS, location_base_id + 8003),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_MARAH_STRAND_GUARDS, location_base_id + 8004), #//ForgedLittleORAirDash// WallJump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FRAGMENTS_GUARDS, location_base_id + 8005), #//ForgedLittleORAirDash// WallJump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SMASHING_BLOCK_GUARDS, location_base_id + 8006), #//ForgedLittleORAirDash// (HandJumpORBurstJump)ANDAirDash
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_BLOODROOT_SEAL_UPPER, location_base_id + 8007), 
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SEAL_UPPER, location_base_id + 8008),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FORGED_PEBBLE_CHEST, location_base_id + 8009),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM, location_base_id + 8010),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SCATTER_STONE_BREATHCROWN, location_base_id + 8011), #GraspHook AND WallJump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM_PEBBLE_HANDS, location_base_id + 8012),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FORGED_PEBBLE_HANDS, location_base_id + 8013), #HandJumpOrBurstJump AND WallJump And GraspHook
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_MARAH_STRAND_PEBBLE, location_base_id + 8014),
    #//Forged Breathcrown not synced yet
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FORGED_PEBBLE_LEGS, location_base_id + 8015), #WallJump/AirDash/BurstJump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SPIKE_PIT, location_base_id + 8016), #AirDashANDGraspHook OR HandJump\
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM_SERGEANT, location_base_id + 8017), #walljump + high jump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM_SURROGATE, location_base_id + 8018), #high jump + Air Dash + grasp
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_MARAH_STRAND_FISTS, location_base_id + 8019),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FORGED_FISTS, location_base_id + 8020),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SMASHING_BLOCK_TOP, location_base_id + 8021),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM_TOP, location_base_id + 8022),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SURROGATE_HAVEN, location_base_id + 8023),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_BLOODROOT_HAVEN, location_base_id + 8024),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FRAGMENTS_REEF, location_base_id + 8025),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_DISCARDED_FLESH, location_base_id + 8026), #12_PaintReef_Background_Purple_BAKED_BASE_HARD_HIGH_LAYER 1
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_HOMING_DROPLETS, location_base_id + 8027),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM_FLESH, location_base_id + 8028), #highjump+walljump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_BLOODROOT_FLESH, location_base_id + 8029), #//highjump+walljump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FRAGMENTS_DROPOT, location_base_id + 8030),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SMASHING_BLOCK_PIT, location_base_id + 8031), #ItemGrasp highjump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SCATTER_STONE_SEAL, location_base_id + 8032), #highjump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SEAL_LOWER, location_base_id + 8033), #highjump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_MARAH_STRAND_SEAL, location_base_id + 8034), #highjump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_BLOODROOT_SEAL_LOWER, location_base_id + 8035), #highjump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SMASHING_BLOCK_SEAL, location_base_id + 8036), #highjump+Walljump
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ANVILHEAD_REWARD, location_base_id + 8037),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_SMASHING_BLOCK_ANVILHEAD, location_base_id + 8038),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_BLOODROOT_ANVILHEAD, location_base_id + 8039),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_BLOODROOT_SURROGATE, location_base_id + 8040),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FRAGMENTS_ENTRANCE, location_base_id + 8041),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM_NAILGLADE_RIGHT, location_base_id + 8042),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM_NAILGLADE_LEFT, location_base_id + 8043),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_BLOODROOT_NAILGLADE_LEFT, location_base_id + 8044),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_BLOODROOT_NAILGLADE_RIGHT, location_base_id + 8045),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_MARAH_STRAND_NAILGLADE, location_base_id + 8046),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM_NAILGLADE, location_base_id + 8047),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_EMBEDDING_NAIL, location_base_id + 8048),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FORCE, location_base_id + 8049),
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_ATRIUM_MINIBOSS, location_base_id + 8050), #Airdash
    Grime2LocationData(EnumRegions.DREGBOURG.value, EnumLoc.DREGBOURG_FORGED_ANVIL, 8051),

    # # # # # # #
    # Jagged Forest
    # # # # # # #
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_SURROGATE_LEARNING, location_base_id + 9001),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_FORCE, location_base_id + 9002),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_CHAIN_JAVELIN_PIT, location_base_id + 9003),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_LEARNING, location_base_id + 9004),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLADE_MAMMOTH_REWARD, location_base_id + 9005),
    #// Kankan-side
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_SURROGATE_LAHAV, location_base_id + 9006),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_ATRIUM_SEAL, location_base_id + 9007),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_SEAL_ABOVE, location_base_id + 9008),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_FIRSTSMITH_DELIVERY, location_base_id + 9009),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_FRAGMENTS_SEAL_ABOVE, location_base_id + 9010),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_SEAL_UPPER, location_base_id + 9011),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_FRAGMENTS_SEAL_UNDER, location_base_id + 9012),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_SEAL_LEFT, location_base_id + 9013),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_GOZ_SICKLE, location_base_id + 9014),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_CHAIN_JAVELIN, location_base_id + 9015),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_VANGUARD_RIGHT, location_base_id + 9016),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_VANGUARD_LEFT, location_base_id + 9017),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_ATRIUM_VANGUARD, location_base_id + 9018),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_PITCHER_LEGS, location_base_id + 9019),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_DROPOT_CONTAINER, location_base_id + 9020),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_MARAH_STRAND_DROPOT, location_base_id + 9021),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_SEAL_LOWER, location_base_id + 9022),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_BOTTOM, location_base_id + 9023),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_CHAIN_JAVELIN_BOTTOM, location_base_id + 9024),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_DROPOT_1, location_base_id + 9025),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_DROPOT_2, location_base_id + 9026),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_ATRIUM_DROPOT, location_base_id + 9027),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_FRAGMENTS_DROPOT_RIGHT, location_base_id + 9028),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_FRAGMENTS_DROPOT_LEFT, location_base_id + 9029),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_CHARGING_JAVELIN, location_base_id + 9030),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_MARAH_STRAND_SURROGATE, location_base_id + 9031),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BEASTPLATE_CHEST, location_base_id + 9032),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BEASTPLATE_LEGS, location_base_id + 9033),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BEASTPLATE_HANDS, location_base_id + 9034),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_BEASTPLATE, location_base_id + 9035),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_SURROGATE_CAVE, location_base_id + 9036), 
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_LAHAV_KNIGHT_REWARD, location_base_id + 9037),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_LAHAVIST_WANDERER_LEGS, location_base_id + 9038),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_LAHAVIST_WANDERER_HANDS, location_base_id + 9039),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_LAHAVIST_WANDERER_CHEST, location_base_id + 9040),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_MARAH_STRAND_LAHAV, location_base_id + 9041),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_ALVEOLI_NEAR, location_base_id + 9042),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_BLOODROOT_ALVEOLI_BEHIND, location_base_id + 9043),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_ALVEOLI_TREE, location_base_id + 9044),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_HEART_OF_A_WARRIOR, location_base_id + 9045),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_LAHAVIST_BREATHCROWN, location_base_id + 9046),
    Grime2LocationData(EnumRegions.JAGGED_FOREST.value, EnumLoc.JAGGED_CLAWING_SCYTHE, location_base_id + 9047),
        
        #// [14:08:58.309] [Grime2_AP_Client] 07_NailGlade_Background_AlwaysOn_BAKED_BASE_HARD_HIGH_LAYER 1
        #// [14:08:58.311] [Grime2_AP_Client] Pitcher Spear received.
        
    # # # # # # #
    # Blade Garden
    # # # # # # #
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_SEAL_RIGHT, location_base_id + 10001),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_ATRIUM_DROPOT, location_base_id + 10002), #Grasp
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_BLOODROOT_DUNAL_RIGHT, location_base_id + 10003),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_BLOODROOT_DUNAL_LEFT, location_base_id + 10004),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_SURROGATE_GARDEN, location_base_id + 10005),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_BLOODROOT_WORKSHOP, location_base_id + 10006),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_MARAH_STRAND_WORKSHOP, location_base_id + 10007),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_FORCE, location_base_id + 10008),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_CHAR_JAV_WORKSHOP, location_base_id + 10009),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_CHAR_JAV_SEAL, location_base_id + 10010),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_SEAL_LEFT, location_base_id + 10011),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_CHAR_JAV_SEAL_RIGHT, location_base_id + 10012),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_CHAR_JAV_SEAL_LEFT_L, location_base_id + 10013),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_MARAH_STRAND_AXE, location_base_id + 10014),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_SURROGATE_AXE, location_base_id + 10015),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_BLOODROOT_LAHAVISTS, location_base_id + 10016),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_FRAGMENTS_VER, location_base_id + 10017),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_BLOODROOT_VER, location_base_id + 10018),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_FALLEN_GREATBLADE_HANDS, location_base_id + 10019),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_BLOODROOT_GREATBLADE_HANDS, location_base_id + 10020),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_FALLEN_GREATBLADE_CHEST, location_base_id + 10021),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_FALLEN_GREATBLADE_LEGS, location_base_id + 10022),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_ATRIUM_GREATBLADE_LEGS, location_base_id + 10023),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_BLOODROOT_TOP_LEFT, location_base_id + 10024),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_BLOODROOT_TOP_RIGHT, location_base_id + 10025),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_ATRIUM_ALVEOLI_TREE, location_base_id + 10026),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_ALVEOLI_TREE, location_base_id + 10027),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_CHAR_JAV_SEAL_LEFT_R, location_base_id + 10028),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_MARAH_STRAND_SEAL, location_base_id + 10029),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_ATRIUM_SEAL_RIGHT, location_base_id + 10030),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_BLOODROOT_SEAL_LEFT, location_base_id + 10031),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_MAMMOTH_AXE, location_base_id + 10032),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_UPPER.value, EnumLoc.GARDEN_MARAH_STRAND_SEAL_BELOW, location_base_id + 10033),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_BLOODROOT_AXE_LEFT, location_base_id + 10034),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_BLOODROOT_AXE_RIGHT, location_base_id + 10035),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_AXE_SURROGATE, location_base_id + 10036),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_BLOODROOT_AXE_BOTTOM, location_base_id + 10037),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_MARAH_STRAND_AXE_BELOW, location_base_id + 10038),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_BLOODROOT_QUADBLADE_LEFT, location_base_id + 10039),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_BLOODROOT_QUADBLADE_BELOW, location_base_id + 10040),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_SURROGATE_QUADBLADE, location_base_id + 10041),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_PENSPEAR_1, location_base_id + 10042),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_PENSPEAR_2, location_base_id + 10043),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_QUADBLADE_REWARD, location_base_id + 10044),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_CHAR_JAV_QUAD_1, location_base_id + 10045),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_MIDDLE.value, EnumLoc.GARDEN_CHAR_JAV_QUAD_2, location_base_id + 10046),
    # //["08_BladeGarden_04:-3065176"] = new LocationEnum(0, "BladeGarden:Marah Strand top of Quadblade arena"), // (3082.73, 1242.58, 3.76) Inaccessible
    Grime2LocationData(EnumRegions.BLADE_GARDEN_LOWER.value, EnumLoc.GARDEN_LOWER_FRAGMENTS, location_base_id + 10047),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_LOWER.value, EnumLoc.GARDEN_LOWER_BLOODROOT, location_base_id + 10048),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_LOWER.value, EnumLoc.GARDEN_LOWER_PEN_PIERCED_LEGS, location_base_id + 10049),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_LOWER.value, EnumLoc.GARDEN_LOWER_PEN_PIERCED_CHEST, location_base_id + 10050),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_LOWER.value, EnumLoc.GARDEN_LOWER_PEN_PIERCED_HANDS, location_base_id + 10051),
    Grime2LocationData(EnumRegions.BLADE_GARDEN_LOWER.value, EnumLoc.GARDEN_QUADRANT_BLADE, location_base_id + 10052),
        
    # # # # # # #
    # Paint Reef
    # # # # # # #
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_REEF_DIVER_HANDS, location_base_id + 11001),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_ATRIUM_SHELL, location_base_id + 11002),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_ATRIUM_ENTRANCE, location_base_id + 11003),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_SMASHING_BLOCK_ENTRANCE, location_base_id + 11004), #bjump + ghook + adash + wjump
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_REEF_DIVER_CHEST, location_base_id + 11005),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_REEF_DIVER_LEGS, location_base_id + 11006), #wjump
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_SMASHING_BLOCK_DIVER, location_base_id + 11007), #wjump
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_ATRIUM_SEAL_1, location_base_id + 11008),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_MARAH_STRAND_SEAL, location_base_id + 11009),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_ATRIUM_SEAL_2, location_base_id + 11010),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_FRAGMENTS_SEAL, location_base_id + 11011), #HighJump AND (WallJump OR IGrasp)
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_LUMP_OF_HANDS_SEAL, location_base_id + 11012),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_SMASHING_BLOCK_SEAL_1, location_base_id + 11013),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BLOODROOT_SEAL, location_base_id + 11014),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_SMASHING_BLOCK_SEAL_2, location_base_id + 11015),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_SMIDGE_OF_PAINT, location_base_id + 11016),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_SURROGATE_STAR_TINT, location_base_id + 11017),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_SEAL_UPPER, location_base_id + 11018),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BLOODROOT_START_TINT, location_base_id + 11019),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_FORCE, location_base_id + 11020),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_FLEETING_CARESS_REWARD, location_base_id + 11021),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_REEF_BLOOM_HANDS, location_base_id + 11022),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_REEF_BLOOM_LEGS, location_base_id + 11023),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_SURROGATE_BLADE_TINT, location_base_id + 11024),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_MARAH_STRAND_STAR_TINT, location_base_id + 11025),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BLOODROOT_BLADE_TINT_LEFT, location_base_id + 11026),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_REEF_BLOOM_CHEST, location_base_id + 11027),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BLOODROOT_BLADE_TINT_ABOVE, location_base_id + 11028),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_SEAL_LOWER, location_base_id + 11029),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_DISCARDED_FLESH, location_base_id + 11030), #12_PaintReef_05_BAKED_BASE_SOFT_HIGH_LAYER 0
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_MARAH_STRAND_SHELL_BEFORE, location_base_id + 11031),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_MARAH_STRAND_SHELL_1, location_base_id + 11032),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_MARAH_STRAND_SHELL_2, location_base_id + 11033),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_MARAHS_SHELL_REWARD, location_base_id + 11034),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BIRTHPLACE_FRAGMENTS_FIRST, location_base_id + 11035),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BIRTHPLACE_FRAGMENTS_RIGHT, location_base_id + 11036),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BIRTHPLACE_FRAGMENTS_MIDDLE, location_base_id + 11037),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BIRTHPLACE_FRAGMENTS_LEFT, location_base_id + 11038),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BIRTHPLACE_LUMP_OF_HANDS, location_base_id + 11039),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BIRTHPLACE_BLOODROOT_TOP, location_base_id + 11040),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BIRTHPLACE_ATRIUM_TOP, location_base_id + 11041),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BIRTHPLACE_ATRIUM_BOTTOM, location_base_id + 11042),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_BIRTHPLACE_BLOODROOT_LOWER, location_base_id + 11043),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_LUMP_OF_HANDS_BARRIER, location_base_id + 11044),
    Grime2LocationData(EnumRegions.PAINT_REEF.value, EnumLoc.REEF_FRAIL_HORN, location_base_id + 11045),
]

LOCATION_NAME_TO_ID = {location.name.value: location.ap_id for location in location_data}


def create_events(world: Grime2World) -> None:
    """
    Placeholder
    """
    # mountainborn_region = world.get_region(EnumRegions.UNDERHEADS_MOUNTAINBORN.value)
    # mountainborn_region.add_event(
    #     EnumLoc.UNDERHEADS_MOUNTAINBORN.value,
    #     "Mountainborn Cleared",
    #     location_type=Grime2Location,
    #     item_type=items.Grime2Item
    # )
    
    victory_zone = world.get_region(EnumRegions.MUDFALLS)
    victory_zone.add_event(
        EnumLoc.MUDFALLS_MANZIL_BREATHCROWN, "Victory", location_type=Grime2Location, item_type=items.Grime2Item
    )
