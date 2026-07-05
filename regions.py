from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .rules import *
from .enums import EnumRegions, EnumLoc, EnumItem

if TYPE_CHECKING:
    from .world import Grime2World

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).

def create_and_connect_regions(world: Grime2World) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: Grime2World) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    menu = Region("Menu", world.player, world.multiworld)
    temple_of_hands_birthplace_lower = Region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value, world.player, world.multiworld)
    temple_of_hands_overgrown_barrier = Region(EnumRegions.TEMPLE_OF_HANDS_OVERGROWN_BARRIER.value, world.player, world.multiworld)
    temple_of_hands_birthplace_upper = Region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_UPPER.value, world.player, world.multiworld)
    temple_of_hands_dried_paint = Region(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value, world.player, world.multiworld)
    temple_of_hands_sealed_chamber = Region(EnumRegions.TEMPLE_OF_HANDS_SEALED_CHAMBER.value, world.player, world.multiworld)
    temple_of_hands_bound_shell = Region(EnumRegions.TEMPLE_OF_HANDS_BOUND_SHELL.value, world.player, world.multiworld)
    temple_of_hands_hall = Region(EnumRegions.TEMPLE_OF_HANDS_HALL.value, world.player, world.multiworld)
    temple_of_hands_birthplace_high_upper = Region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_HIGH_UPPER, world.player, world.multiworld)
    temple_of_hands_dried_paint_birthplace_upper = Region(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT_BIRTHPLACE_UPPER, world.player, world.multiworld)
    temple_of_hands_birthplace_reef_upper = Region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_REEF_UPPER, world.player, world.multiworld)
    temple_of_hands_dried_paint_reef_upper = Region(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT_REEF, world.player, world.multiworld)
    
    mudfalls = Region(EnumRegions.MUDFALLS.value, world.player, world.multiworld)
    mudfalls_elevator = Region(EnumRegions.MUDFALLS_ELEVATOR.value, world.player, world.multiworld)
    mudfalls_above_manzil_right = Region(EnumRegions.MUDFALLS_ABOVE_MANZIL_RIGHT.value, world.player, world.multiworld)
    mudfalls_above_manzil_right_top = Region(EnumRegions.MUDFALLS_ABOVE_MANZIL_RIGHT_TOP.value, world.player, world.multiworld)
    mudfalls_above_manzil_center = Region(EnumRegions.MUDFALLS_ABOVE_MANZIL_CENTER.value, world.player, world.multiworld)
    mudfalls_above_manzil_top = Region(EnumRegions.MUDFALLS_ABOVE_MANZIL_TOP.value, world.player, world.multiworld)
    mudfalls_above_manzil_side = Region(EnumRegions.MUDFALLS_ABOVE_MANZIL_SIDE.value, world.player, world.multiworld)
    mudfalls_above_manzil_left = Region(EnumRegions.MUDFALLS_ABOVE_MANZIL_LEFT.value, world.player, world.multiworld)
    mudfalls_above_manzil_left_top = Region(EnumRegions.MUDFALLS_ABOVE_MANZIL_LEFT_TOP.value, world.player, world.multiworld)
    mudfalls_strand = Region(EnumRegions.MUDFALLS_STRAND.value, world.player, world.multiworld)
    mudfalls_spike_pit = Region(EnumRegions.MUDFALLS_SPIKE_PIT.value, world.player, world.multiworld)
    
    faceless_mountains_mudfalls = Region(EnumRegions.FACELESS_MOUNTAINS_MUDFALLS.value, world.player, world.multiworld)
    faceless_mountains_dropot = Region(EnumRegions.FACELESS_MOUNTAINS_DROPOT.value, world.player, world.multiworld)
    faceless_mountains_melded = Region(EnumRegions.FACELESS_MOUNTAINS_MELDED.value, world.player, world.multiworld)
    faceless_mountains_main = Region(EnumRegions.FACELESS_MOUNTAINS.value, world.player, world.multiworld)
    faceless_mountains_wanting_atrium = Region(EnumRegions.FACELESS_MOUNTAINS_WANTING_ATRIUM.value, world.player, world.multiworld)
    faceless_mountains_wanting_bloodroots = Region(EnumRegions.FACELESS_MOUNTAINS_WANTING_BLOODROOTS.value, world.player, world.multiworld)
    faceless_mountains_darsh = Region(EnumRegions.FACELESS_MOUNTAINS_DARSH.value, world.player, world.multiworld)
    
    marahs_orchard_entrance = Region("Marah's Orchard Entrance", world.player, world.multiworld)
    marahs_orchard_faceblob = Region("Marah's Orchard Faceblob", world.player, world.multiworld)
    marahs_orchard_main = Region("Marah's Orchard Main", world.player, world.multiworld)
    marahs_orchard_prime_above = Region("Marah's Orchard Above Prime Pitcher", world.player, world.multiworld)
    marahs_orchard_prime_dropot = Region("Marah's Orchard Above Prime Pitcher Dropot", world.player, world.multiworld)
    marahs_orchard_prime = Region("Marah's Orchard Prime Pitcher", world.player, world.multiworld)
    
    underheads_left_upper = Region(EnumRegions.UNDERHEADS_LEFT_UPPER.value, world.player, world.multiworld)
    underheads_left_middle = Region(EnumRegions.UNDERHEADS_LEFT_MIDDLE.value, world.player, world.multiworld)
    underheads_left_lower = Region(EnumRegions.UNDERHEADS_LEFT_LOWER.value, world.player, world.multiworld)
    underheads_surrogate_left = Region(EnumRegions.UNDERHEADS_SURROGATE_LEFT.value, world.player, world.multiworld)
    underheads_lower_hunt = Region(EnumRegions.UNDERHEADS_LOWER_HUNT.value, world.player, world.multiworld)
    underheads_before_mountainborn = Region(EnumRegions.UNDERHEADS_BEFORE_MOUNTAINBORN.value, world.player, world.multiworld)
    underheads_mountainborn = Region(EnumRegions.UNDERHEADS_MOUNTAINBORN.value, world.player, world.multiworld)
    underheads_lahav_knight = Region(EnumRegions.UNDERHEADS_LAHAV_KNIGHT.value, world.player, world.multiworld)
    underheads_nailglade_transition = Region(EnumRegions.UNDERHEADS_NAILGLADE_TRANSITION.value, world.player, world.multiworld)
    underheads_right = Region(EnumRegions.UNDERHEADS_RIGHT.value, world.player, world.multiworld)
    underheads_forged_little = Region(EnumRegions.UNDERHEADS_FORGED_LITTLE.value, world.player, world.multiworld)
    underheads_boulder_hands = Region(EnumRegions.UNDERHEADS_BOULDER_HANDS.value, world.player, world.multiworld)
    underheads_forged_pick = Region(EnumRegions.UNDERHEADS_FORGED_PICK.value, world.player, world.multiworld)
    underheads_scatter_stone = Region(EnumRegions.UNDERHEADS_SCATTER_STONE.value, world.player, world.multiworld)
    underheads_aleoli = Region(EnumRegions.UNDERHEADS_ALVEOLI.value, world.player, world.multiworld)
    underheads_surrogate_smidge = Region(EnumRegions.UNDERHEADS_SURROGATE_SMIDGE.value, world.player, world.multiworld)
    underheads_mountainborn_marah = Region(EnumRegions.UNDERHEADS_MOUNTAINBORN_MARAH.value, world.player, world.multiworld)
    underheads_tree_roots = Region(EnumRegions.UNDERHEADS_TREE_ROOTS.value, world.player, world.multiworld)
    underheads_overgrown_blob = Region(EnumRegions.UNDERHEADS_MOUNTAINBORN_OVERGROWN_BLOB.value, world.player, world.multiworld)
    
    kankan_upper_main = Region("Kankan Upper Main", world.player, world.multiworld)
    kankan_upper_heart = Region("Kankan Upper Heart", world.player, world.multiworld)
    kankan_upper_dropot = Region("Kankan Upper Dropot", world.player, world.multiworld)
    kankan_upper_heod = Region("Kankan Upper Heod", world.player, world.multiworld)
    kankan_upper_palace = Region("Kankan Palace Top", world.player, world.multiworld)
    kankan_upper_before_palace = Region("Kankan Before Palace", world.player, world.multiworld)
    kankan_upper_jail = Region("Kankan Palace Jail", world.player, world.multiworld)
    kankan_upper_javelin = Region("Kankan Upper Javelin", world.player, world.multiworld)
    kankan_lower_main = Region("Kankan Lower", world.player, world.multiworld)
    kankan_lower_alv_house = Region("Kankan Lower Alveoli House", world.player, world.multiworld)
    kankan_lower_alv_house_top = Region("Kankan Lower Alveoli House Tops", world.player, world.multiworld)
    kankan_lower_holster = Region("Kankan Lower Holster", world.player, world.multiworld)
    kankan_lower_atrium = Region("Kankan Lower Hidden Atrium", world.player, world.multiworld)
    kankan_lower_preacher = Region("Kankan Lower Preacher", world.player, world.multiworld)
    
    jagged_forest = Region("Jagged Forest", world.player, world.multiworld)
    
    blade_garden_upper = Region("Blade Garden Upper", world.player, world.multiworld)
    blade_garden_middle = Region("Blade Garden Middle", world.player, world.multiworld)
    blade_garden_lower = Region("Blade Garden Lower", world.player, world.multiworld)
    
    nailglade = Region("Nailglade", world.player, world.multiworld)
    
    tree_roots = Region("Tree Roots", world.player, world.multiworld)
    tree_roots_visage = Region("Tree Roots Visage", world.player, world.multiworld)
    
    dregbourg = Region("Dregbourg", world.player, world.multiworld)
    
    paint_reef = Region("Paint Reef", world.player, world.multiworld)
    
    palladium = Region("Palladium", world.player, world.multiworld)
    
    fallen_path = Region("Fallen Path", world.player, world.multiworld)
    
    mudpits = Region("Mudpits", world.player, world.multiworld)
    
    skyrise = Region("Skyrise", world.player, world.multiworld)
    
    starmire = Region("Starmire", world.player, world.multiworld)
    
    wanting_tree = Region("Wanting Tree", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [
        menu,
        temple_of_hands_birthplace_lower,
        temple_of_hands_overgrown_barrier,
        temple_of_hands_birthplace_upper,
        temple_of_hands_dried_paint,
        temple_of_hands_sealed_chamber,
        temple_of_hands_bound_shell,
        temple_of_hands_hall,
        temple_of_hands_birthplace_high_upper,
        temple_of_hands_dried_paint_birthplace_upper,
        temple_of_hands_birthplace_reef_upper,
        temple_of_hands_dried_paint_reef_upper,
        
        mudfalls,
        mudfalls_elevator,
        mudfalls_above_manzil_right,
        mudfalls_above_manzil_right_top,
        mudfalls_above_manzil_center,
        mudfalls_above_manzil_top,
        mudfalls_above_manzil_side,
        mudfalls_above_manzil_left,
        mudfalls_above_manzil_left_top,
        mudfalls_strand,
        mudfalls_spike_pit,

        faceless_mountains_mudfalls,
        faceless_mountains_dropot,
        faceless_mountains_melded,
        faceless_mountains_main,
        faceless_mountains_wanting_atrium,
        faceless_mountains_wanting_bloodroots,
        faceless_mountains_darsh,
        
        marahs_orchard_entrance,
        marahs_orchard_faceblob,
        marahs_orchard_main,
        marahs_orchard_prime_above,
        marahs_orchard_prime_dropot,
        marahs_orchard_prime,

        underheads_left_upper,
        underheads_left_middle,
        underheads_left_lower,
        underheads_surrogate_left,
        underheads_lower_hunt,
        underheads_before_mountainborn,
        underheads_mountainborn,
        underheads_lahav_knight,
        underheads_nailglade_transition,
        underheads_right,
        underheads_forged_little,
        underheads_boulder_hands,
        underheads_forged_pick,
        underheads_scatter_stone,
        underheads_aleoli,
        underheads_tree_roots,
        underheads_surrogate_smidge,
        underheads_mountainborn_marah,
        underheads_overgrown_blob,

        kankan_upper_main,
        kankan_upper_heart,
        kankan_upper_dropot,
        kankan_upper_heod,
        kankan_upper_before_palace,
        kankan_upper_palace,
        kankan_upper_jail,
        kankan_upper_javelin,
        kankan_lower_main,
        kankan_lower_alv_house,
        kankan_lower_alv_house_top,
        kankan_lower_holster,
        kankan_lower_atrium,
        kankan_lower_preacher,
        
        jagged_forest,
        blade_garden_upper,
        blade_garden_middle,
        blade_garden_lower,
        nailglade,
        
        tree_roots,
        tree_roots_visage,
        
        dregbourg,
        paint_reef,
        palladium,
        fallen_path,
        mudpits,
        skyrise,
        starmire,
        wanting_tree,
    ]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # if world.options.hammer:
    #     top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
    #     regions.append(top_middle_room)
        
    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: Grime2World) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    menu = world.get_region("Menu")
    temple_of_hands_birthplace_lower = world.get_region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_LOWER.value)
    temple_of_hands_overgrown_barrier = world.get_region(EnumRegions.TEMPLE_OF_HANDS_OVERGROWN_BARRIER.value)
    temple_of_hands_birthplace_upper = world.get_region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_UPPER.value)
    temple_of_hands_birthplace_high_upper = world.get_region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_HIGH_UPPER.value)
    temple_of_hands_dried_paint_birthplace_upper = world.get_region(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT_BIRTHPLACE_UPPER.value)
    temple_of_hands_dried_paint = world.get_region(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT.value)
    temple_of_hands_bound_shell = world.get_region(EnumRegions.TEMPLE_OF_HANDS_BOUND_SHELL.value)
    temple_of_hands_sealed_chamber = world.get_region(EnumRegions.TEMPLE_OF_HANDS_SEALED_CHAMBER.value)
    temple_of_hands_hall = world.get_region(EnumRegions.TEMPLE_OF_HANDS_HALL.value)
    temple_of_hands_birthplace_reef_upper = world.get_region(EnumRegions.TEMPLE_OF_HANDS_BIRTHPLACE_REEF_UPPER.value)
    temple_of_hands_dried_paint_reef_upper = world.get_region(EnumRegions.TEMPLE_OF_HANDS_DRIED_PAINT_REEF.value)
    
    mudfalls = world.get_region(EnumRegions.MUDFALLS.value)
    mudfalls_elevator = world.get_region(EnumRegions.MUDFALLS_ELEVATOR.value)
    mudfalls_above_manzil_right = world.get_region(EnumRegions.MUDFALLS_ABOVE_MANZIL_RIGHT.value)
    mudfalls_above_manzil_right_top = world.get_region(EnumRegions.MUDFALLS_ABOVE_MANZIL_RIGHT_TOP.value)
    mudfalls_above_manzil_center = world.get_region(EnumRegions.MUDFALLS_ABOVE_MANZIL_CENTER.value)
    mudfalls_above_manzil_top = world.get_region(EnumRegions.MUDFALLS_ABOVE_MANZIL_TOP.value)
    mudfalls_above_manzil_side = world.get_region(EnumRegions.MUDFALLS_ABOVE_MANZIL_SIDE.value)
    mudfalls_above_manzil_left = world.get_region(EnumRegions.MUDFALLS_ABOVE_MANZIL_LEFT.value)
    mudfalls_above_manzil_left_top = world.get_region(EnumRegions.MUDFALLS_ABOVE_MANZIL_LEFT_TOP.value)
    mudfalls_strand = world.get_region(EnumRegions.MUDFALLS_STRAND.value)
    mudfalls_spike_pit = world.get_region(EnumRegions.MUDFALLS_SPIKE_PIT.value)
    
    faceless_mountains_mudfalls = world.get_region(EnumRegions.FACELESS_MOUNTAINS_MUDFALLS.value)
    faceless_mountains_dropot = world.get_region(EnumRegions.FACELESS_MOUNTAINS_DROPOT.value)
    faceless_mountains_melded = world.get_region(EnumRegions.FACELESS_MOUNTAINS_MELDED.value)
    faceless_mountains_main = world.get_region(EnumRegions.FACELESS_MOUNTAINS.value)
    faceless_mountains_wanting_atrium = world.get_region(EnumRegions.FACELESS_MOUNTAINS_WANTING_ATRIUM.value)
    faceless_mountains_wanting_bloodroots = world.get_region(EnumRegions.FACELESS_MOUNTAINS_WANTING_BLOODROOTS.value)
    faceless_mountains_darsh = world.get_region(EnumRegions.FACELESS_MOUNTAINS_DARSH.value)
    
    marahs_orchard_entrance = world.get_region(EnumRegions.MARAHS_ORCHARD_ENTRANCE.value)
    marahs_orchard_faceblob = world.get_region(EnumRegions.MARAHS_ORCHARD_FACEBLOB.value)
    marahs_orchard_main = world.get_region(EnumRegions.MARAHS_ORCHARD_MAIN.value)
    marahs_orchard_prime_above = world.get_region(EnumRegions.MARAHS_ORCHARD_PRIME_ABOVE.value)
    marahs_orchard_prime_dropot = world.get_region(EnumRegions.MARAHS_ORCHARD_PRIME_ABOVE_DROPOT.value)
    marahs_orchard_prime = world.get_region(EnumRegions.MARAHS_ORCHARD_PRIME.value)
    
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
    
    kankan_upper_main = world.get_region(EnumRegions.KANKAN_UPPER_MAIN.value)
    kankan_upper_heart = world.get_region(EnumRegions.KANKAN_UPPER_HEART.value)
    kankan_upper_dropot = world.get_region(EnumRegions.KANKAN_UPPER_DROPOT.value)
    kankan_upper_heod = world.get_region(EnumRegions.KANKAN_UPPER_HEOD.value)
    kankan_upper_before_palace = world.get_region(EnumRegions.KANKAN_UPPER_BEFORE_PALACE.value)
    kankan_upper_palace = world.get_region(EnumRegions.KANKAN_UPPER_PALACE.value)
    kankan_upper_jail = world.get_region(EnumRegions.KANKAN_UPPER_JAIL.value)
    kankan_upper_javelin = world.get_region(EnumRegions.KANKAN_UPPER_JAVELIN.value)
    kankan_lower_main = world.get_region(EnumRegions.KANKAN_LOWER_MAIN.value)
    kankan_lower_alv_house = world.get_region(EnumRegions.KANKAN_LOWER_ALV_HOUSE.value)
    kankan_lower_alv_house_top = world.get_region(EnumRegions.KANKAN_LOWER_ALV_HOUSE_TOP.value)
    kankan_lower_holster = world.get_region(EnumRegions.KANKAN_LOWER_HOLSTER.value)
    kankan_lower_atrium = world.get_region(EnumRegions.KANKAN_LOWER_ATRIUM.value)
    kankan_lower_preacher = world.get_region(EnumRegions.KANKAN_LOWER_PREACHER.value)
    
    jagged_forest_kankan = world.get_region(EnumRegions.JAGGED_FOREST.value)
    jagged_forest_main = world.get_region(EnumRegions.JAGGED_FOREST.value)
    jagged_forest_legs = world.get_region(EnumRegions.JAGGED_FOREST.value)
    jagged_forest_learning = world.get_region(EnumRegions.JAGGED_FOREST.value)
    jagged_forest_cave = world.get_region(EnumRegions.JAGGED_FOREST.value)
    jagged_forest_lahav_knight = world.get_region(EnumRegions.JAGGED_FOREST.value)
    jagged_forest_mammoth = world.get_region(EnumRegions.JAGGED_FOREST.value)
    jagged_forest_garden_trans = world.get_region(EnumRegions.JAGGED_FOREST.value)
    
    blade_garden_upper = world.get_region(EnumRegions.BLADE_GARDEN_UPPER.value)
    blade_garden_middle = world.get_region(EnumRegions.BLADE_GARDEN_MIDDLE.value)
    blade_garden_lower = world.get_region(EnumRegions.BLADE_GARDEN_LOWER.value)
    
    nailglade = world.get_region(EnumRegions.NAILGLADE.value)
    
    tree_roots = world.get_region(EnumRegions.TREE_ROOTS.value)
    tree_roots_visage = world.get_region(EnumRegions.TREE_ROOTS_VISAGE.value)
    
    dregbourg = world.get_region(EnumRegions.DREGBOURG.value)
    paint_reef = world.get_region(EnumRegions.PAINT_REEF.value)
    palladium = world.get_region(EnumRegions.PALLADIUM.value)
    fallen_path = world.get_region(EnumRegions.FALLEN_PATH.value)
    mudpits = world.get_region(EnumRegions.MUDPITS.value)
    skyrise = world.get_region(EnumRegions.SKYRISE.value)
    starmire = world.get_region(EnumRegions.STARMIRE.value)
    wanting_tree = world.get_region(EnumRegions.WANTING_TREE.value)


    menu.connect(temple_of_hands_birthplace_lower, "Menu to Temple of Hands")
    # # # # # # #
    # Mudfalls
    # # # # # # #
    # Entrance/Exits
    temple_of_hands_birthplace_lower.connect(temple_of_hands_overgrown_barrier, "ToH Birthplace Lower to Overgrown Barrier")
    temple_of_hands_overgrown_barrier.connect(temple_of_hands_birthplace_lower, "Overgrown Barrier to ToH Birthplace Lower")
    temple_of_hands_overgrown_barrier.connect(temple_of_hands_dried_paint, "Overgrown Barrier to ToH Dried Paint", lambda state: state.has(EnumItem.AC_GRASP, world.player))
    temple_of_hands_dried_paint.connect(temple_of_hands_overgrown_barrier, "ToH Dried Paint to Overgrown Barrier") # Needs overgrown barrier defeated and grasp
    temple_of_hands_dried_paint.connect(temple_of_hands_dried_paint_birthplace_upper, "ToH Dried Paint to ToH Dried Paint before Birthplace Upper") # needs embedding nail and grasp, or handjump
    temple_of_hands_dried_paint_birthplace_upper.connect(temple_of_hands_dried_paint, "ToH Dried Paint before Birthplace Upper to ToH Dried Paint")
    temple_of_hands_dried_paint_birthplace_upper.connect(temple_of_hands_birthplace_upper, "ToH Dried Paint before Birthplace Upper to ToH Birthplace Upper") # needs embedding nail and grasp, or handjump
    temple_of_hands_birthplace_upper.connect(temple_of_hands_dried_paint_birthplace_upper, "ToH Birthplace Upper to ToH Dried Paint before Birthplace Upper")
    temple_of_hands_birthplace_upper.connect(temple_of_hands_birthplace_high_upper, "ToH Birthplace Upper to ToH Birthplace High Upper") # needs highjump and walljump
    temple_of_hands_birthplace_high_upper.connect(temple_of_hands_birthplace_upper, "ToH Birthplace High Upper to ToH Birthplace Upper") # needs highjump and walljump
    temple_of_hands_birthplace_high_upper.connect(temple_of_hands_birthplace_reef_upper, "ToH Birthplace High Upper to ToH Birthplace Reef Upper")
    temple_of_hands_birthplace_reef_upper.connect(temple_of_hands_birthplace_lower, "ToH Birthplace High Upper to ToH Birthplace Lower")
    temple_of_hands_birthplace_lower.connect(temple_of_hands_birthplace_reef_upper, "ToH Birthplace Lower to ToH Birthplace High Upper") # needs high jump and wall jump
    temple_of_hands_dried_paint.connect(temple_of_hands_sealed_chamber, "ToH Dried Paint to ToH Sealed Chamber")
    temple_of_hands_sealed_chamber.connect(temple_of_hands_dried_paint, "ToH Sealed Chamber to ToH Dried Paint")
    temple_of_hands_sealed_chamber.connect(temple_of_hands_bound_shell, "ToH Sealed Chamber to Bound Shell")
    temple_of_hands_bound_shell.connect(temple_of_hands_sealed_chamber, "Bound Shell to ToH Sealed Chamber")
    temple_of_hands_bound_shell.connect(temple_of_hands_hall, "Bound Shell to ToH Hall", lambda state: state.has(EnumItem.AC_GRASP, world.player))
    temple_of_hands_hall.connect(temple_of_hands_bound_shell, "ToH Hall to Bound Shell")
    temple_of_hands_bound_shell.connect(temple_of_hands_dried_paint_reef_upper, "Bound Shell to Reef", lambda state: state.has(EnumItem.AC_GRASP, world.player))
    temple_of_hands_dried_paint.connect(temple_of_hands_hall, "ToH Dried Paint to ToH Hall")
    temple_of_hands_hall.connect(temple_of_hands_dried_paint, "ToH Hall to ToH Dried Paint")
    temple_of_hands_hall.connect(temple_of_hands_sealed_chamber, "ToH Hall to ToH Ceiling Items") # needs burst jump or plunging finger
    temple_of_hands_hall.connect(mudfalls, "ToH Hall to Mudfalls")
    
    # # # # # # #
    # Mudfalls
    # # # # # # #
    # Entrance/Exits
    mudfalls.connect(temple_of_hands_dried_paint, "Mudfalls to Temple of Hands")
    mudfalls.connect(faceless_mountains_mudfalls, "Mudfalls to Faceless Mountains")
    mudfalls.connect(underheads_left_middle, "Mudfalls to Underheads Middle")
    mudfalls.connect(underheads_left_upper, "Mudfalls to Underheads Upper", lambda state: canClimbWalls(world.player, state) and canGraspHook(world.player, state) and canAirDash(world.player, state))
    mudfalls.connect(dregbourg, "Mudfalls to Dregbourg")
    mudfalls.connect(mudpits, "Mudfalls to Mudpits")
    mudfalls.connect(palladium, "Mudfalls to Palladium")
    # Interzone
    mudfalls.connect(mudfalls_elevator, "Mudfalls to Mudfalls-Elevator", lambda state: canGraspHookSlide(world.player, state))
    mudfalls.connect(mudfalls_above_manzil_right, "Mudfalls to Mudfalls-AboveManzil-Right", lambda state: canGraspHookSlide(world.player, state))
    mudfalls_above_manzil_right.connect(mudfalls_above_manzil_right_top, "Mudfalls-AboveManzil-Right to Mudfalls-AboveManzil-Right-Top", lambda state: canGraspHookSlide(world.player, state))
    mudfalls_above_manzil_right_top.connect(mudfalls_above_manzil_right, "Mudfalls-AboveManzil-Right-Top to Mudfalls-AboveManzil-Right")
    mudfalls_above_manzil_right.connect(mudfalls, "Mudfalls-AboveManzil-Right to Mudfalls")
    mudfalls.connect(mudfalls_above_manzil_center, "Mudfalls to Mudfalls-AboveManzil-Center", lambda state: canClimbWalls(world.player, state))
    mudfalls.connect(mudfalls_above_manzil_side, "Mudfalls to Mudfalls-AboveManzil-Side", lambda state: (canAirDash(world.player, state) and canHandJump(world.player, state)) or canClimbWalls(world.player, state))
    mudfalls_above_manzil_center.connect(mudfalls_above_manzil_top, "Mudfalls-AboveManzil-Center to Mudfalls-AboveManzil-Top", lambda state: ((canAirDash(world.player, state) and canHandJump(world.player, state)) or canClimbWalls(world.player, state)) and canItemGrasp(world.player, state))
    mudfalls_above_manzil_center.connect(mudfalls_above_manzil_left, "Mudfalls-AboveManzil-Center to Mudfalls-AboveManzil-Left", lambda state: canGraspHookSlide(world.player, state) and canAirDash(world.player, state) and canHighJump(world.player, state))
    mudfalls_above_manzil_left.connect(mudfalls_above_manzil_left_top, "Mudfalls-AboveManzil-Left to Mudfalls-AboveManzil-Left-Top", lambda state: canClimbWalls(world.player, state))
    mudfalls.connect(mudfalls_strand, "Mudfalls to Mudfalls Strand", lambda state: canClimbWalls(world.player, state))
    mudfalls.connect(mudfalls_spike_pit, "Mudfalls to Mudfalls Spike Pit", lambda state: canItemGrasp(world.player, state))
    
    # # # # # # #
    # Faceless Mountains
    # # # # # # #
    # Entrance/Exits
    faceless_mountains_mudfalls.connect(mudfalls, "Faceless Mountains to Mudfalls")
    faceless_mountains_darsh.connect(marahs_orchard_entrance, "Faceless Mountains to Marah's Orchard")
    faceless_mountains_main.connect(tree_roots, "Faceless Mountains to Tree Roots")
    faceless_mountains_wanting_bloodroots.connect(wanting_tree, "FM Wanting Bloodroots to Wanting Tree")
    # Interzone
    faceless_mountains_mudfalls.connect(faceless_mountains_main, "Faceless Mountains Entrance to Faceless Mountains")
    faceless_mountains_main.connect(faceless_mountains_dropot, "Faceless Mountains to Dropot Area")
    faceless_mountains_main.connect(faceless_mountains_melded, "Faceless Mountains to FM Melded Giant")
    faceless_mountains_main.connect(faceless_mountains_darsh, "Faceless Mountains to FM Darsh")
    faceless_mountains_main.connect(faceless_mountains_wanting_atrium, "Faceless Mountains to FM Wanting Atrium", lambda state: canClimbWalls(world.player, state) and canGraspHook(world.player, state) and canHighJump(world.player, state))
    faceless_mountains_wanting_atrium.connect(faceless_mountains_wanting_bloodroots, "FM Wanting Atrium to FM Wanting Bloodroots", lambda state: canClimbWalls(world.player, state) and canGraspHook(world.player, state) and canHighJump(world.player, state))
    
    # # # # # # #
    # Marah's Orchard
    # # # # # # #
    # Entrance/Exits
    marahs_orchard_prime.connect(kankan_upper_main, "Marah's Orchard to Kankan", lambda state: state.has("Mountainborn Cleared", world.player) and state.has("Locked Sphere", world.player))
    marahs_orchard_faceblob.connect(underheads_right, "Marah's Orchard to Underheads")
    marahs_orchard_entrance.connect(faceless_mountains_darsh, "Marah's Orchard Entrance to Faceless Mountains Darsh")
    # Interzone
    marahs_orchard_entrance.connect(marahs_orchard_main, "Marah's Orchard Entrance to Marah's Orchard Main")
    marahs_orchard_main.connect(marahs_orchard_faceblob, "Marah's Orchard Main to Marah's Orchard Faceblob")
    marahs_orchard_main.connect(marahs_orchard_prime, "Marah's Orchard Main to Prime Pitcher")
    marahs_orchard_main.connect(marahs_orchard_prime_above, "Marah's Orchard Main to Above Prime Pitcher")
    marahs_orchard_prime_above.connect(marahs_orchard_prime_dropot, "Marah's Orchard Main to Dropot above Prime Pitcher")
    
    # # # # # # #
    # Underheads
    # # # # # # #
    # Entrance/Exits
    underheads_left_middle.connect(mudfalls, "Underheads to Mudfalls")
    underheads_alveoli.connect(faceless_mountains_main, "Underheads to Faceless Mountains")
    underheads_right.connect(marahs_orchard_faceblob, "Underheads to Marah's Orchard")
    underheads_right.connect(underheads_tree_roots, "Underheads to Tree Roots", lambda state: canClimbWalls(world.player, state) and canHighJump(world.player, state))
    underheads_nailglade_transition.connect(nailglade, "Underheads Lahav Knight to Nailglade Transition")
    underheads_left_lower.connect(dregbourg, "Underheads Left Lower to Dregbourg")
    # Interzone
    underheads_lahav_knight.connect(underheads_nailglade_transition, "Underheads to Lahav Knight")
    underheads_left_upper.connect(underheads_alveoli, "Underheads to Underhead Alveoli", lambda state: canGraspHook(world.player, state))
    underheads_left_middle.connect(underheads_surrogate_left, "Underheads Left Middle to Underheads Surrogate")
    underheads_surrogate_left.connect(underheads_left_middle, "Underheads Surrogate to Underheads Left Middle")
    underheads_surrogate_left.connect(underheads_forged_pick, "Underheads Surrogate to Underheads Forged Pick", lambda state: canHighJump(world.player, state) or canClimbWalls(world.player, state) or canGraspHook(world.player, state))
    underheads_lower_hunt.connect(underheads_left_middle, "Underheads Lower Hunt to Underheads Left Middle")
    underheads_left_middle.connect(underheads_lower_hunt, "Underheads Left Middle to Underheads Lower Hunt")
    underheads_lower_hunt.connect(underheads_left_lower, "Underheads Lower Hunt to Underheads Left Lower")
    underheads_lower_hunt.connect(underheads_scatter_stone, "Underheads Lower Hunt to Underheads Scatter Stone")
    underheads_lower_hunt.connect(underheads_surrogate_left, "Underheads Lower Hunt to Underheads Surrogate")
    underheads_surrogate_left.connect(underheads_forged_little, "Underheads Surrogate to Underheads Forged Little")
    underheads_surrogate_left.connect(underheads_boulder_hands, "Underheads Surrogate to Underheads Boulder Hands", lambda state: canGraspHook(world.player, state) and (canAirDash(world.player, state) or canClimbWalls(world.player, state)))
    underheads_boulder_hands.connect(underheads_before_mountainborn, "Underheads Boulder Hands to Underheads Before Mountainborn")
    underheads_before_mountainborn.connect(underheads_surrogate_left, "Underheads Before Mountainborn to Underheads Surrogate")
    underheads_before_mountainborn.connect(underheads_mountainborn, "Underheads Before Mountainborn to Underheads Mountainborn")
    underheads_before_mountainborn.connect(underheads_tree_roots, "Underheads Before Mountainborn to Underheads Tree Roots")
    underheads_mountainborn.connect(underheads_right, "Underheads Mountainborn to Underheads Right")
    underheads_right.connect(underheads_lahav_knight, "Underheads Right to Underheads Lahav Knight")
    underheads_before_mountainborn.connect(underheads_surrogate_smidge, "Underheads Before Mountainborn to Underheads Smidge", lambda state: canClimbWalls(world.player, state) or canGraspHook(world.player, state))
    underheads_mountainborn.connect(underheads_mountainborn_marah, "Underheads Mountainborn to Underheads Mountainborn Marah", lambda state: canClimbWalls(world.player, state) and canBurstJump(world.player, state) and canAirDash(world.player, state))
    underheads_right.connect(underheads_overgrown_blob, "Underheads Right to Underheads Overgrown Blob", lambda state: canClimbWalls(world.player, state) and canHighJump(world.player, state))
    
    # # # # # # #
    # Kankan
    # # # # # # #
    # Entrance/Exits
    kankan_upper_main.connect(marahs_orchard_prime, "Kankan Upper to Marah's Orchard")
    kankan_lower_main.connect(jagged_forest_kankan, "Kankan Lower to Jagged Forest")
    # Interzone
    kankan_upper_main.connect(kankan_upper_heart, "Kankan Upper to Kankan Upper Heart", lambda state: canGraspHookSlide(world.player, state))
    kankan_upper_heart.connect(kankan_upper_dropot, "Kankan Upper to Kankan Upper Dropot", lambda state: canHighJump(world.player, state))
    kankan_upper_dropot.connect(kankan_upper_heod, "Kankan Upper Dropot to Kankan Upper Heod", lambda state: canItemExplode(world.player, state))
    kankan_upper_main.connect(kankan_upper_before_palace, "Kankan Upper to Kankan Upper Before Palace")
    kankan_upper_before_palace.connect(kankan_upper_palace, "Kankan Upper Before Palace to Kankan Upper Palace", lambda state: state.has(EnumItem.QI_BREATHSMITH_LOCATION_INFO.value, world.player))
    kankan_upper_palace.connect(kankan_upper_jail, "Kankan Upper Palace to Kankan Upper Jail", lambda state: state.has(EnumItem.QI_LOCKED_SPHERE.value, world.player))
    kankan_upper_main.connect(kankan_lower_main, "Kankan Upper to Kankan Lower")
    kankan_upper_main.connect(kankan_upper_javelin, "Kankan Upper to Kankan Upper Javelin", lambda state: canHighJump(world.player, state))
    kankan_lower_main.connect(kankan_upper_main, "Kankan Lower to Kankan Upper")
    kankan_lower_main.connect(kankan_lower_alv_house, "Kankan Lower to Kankan Lower Alveoli House", lambda state: canClimbWalls(world.player, state))
    kankan_lower_main.connect(kankan_lower_alv_house_top, "Kankan Lower to Kankan Lower Alveoli House Top", lambda state: canClimbWalls(world.player, state))
    kankan_lower_main.connect(kankan_lower_holster, "Kankan Lower to Kankan Lower Holster", lambda state: canAirDash(world.player, state) or canHighJump(world.player, state) or canItemGrasp(world.player, state))
    kankan_lower_main.connect(kankan_lower_atrium, "Kankan Lower to Atrium", lambda state: canClimbWalls(world.player, state))
    kankan_lower_main.connect(kankan_lower_preacher, "Kankan Lower to Preacher")
    
    # # # # # # #
    # Jagged Forest
    # # # # # # #
    # Entrance/Exits
    jagged_forest_kankan.connect(kankan_lower_main, "JF Main to Kankan")
    jagged_forest_main.connect(nailglade, "JF Main to Nailglade")
    jagged_forest_garden_trans.connect(blade_garden_upper, "JF Main to Blade Garden")
    # Interzone
    jagged_forest_kankan.connect(jagged_forest_main, "JF Kankan to JF Main", lambda state: canGraspHook(world.player, state) or canClimbWalls(world.player, state))
    jagged_forest_main.connect(jagged_forest_legs, "JF Main to JF Legs", lambda state: canAirDash(world.player, state))
    jagged_forest_main.connect(jagged_forest_cave, "JF Main to JF Cave", lambda state: canDashSlide(world.player, state) or canAirDash(world.player, state))# ghook&wjump&(airdashORDashslide)
    jagged_forest_cave.connect(jagged_forest_main, "JF Cave to JF Main")
    jagged_forest_cave.connect(jagged_forest_lahav_knight, "JF Cave to JF Lahav Knight")
    jagged_forest_main.connect(jagged_forest_learning, "JF Main to JF Learning")
    jagged_forest_learning.connect(jagged_forest_mammoth, "JF Learning to JF Mammoth")
    jagged_forest_mammoth.connect(jagged_forest_garden_trans, "JF Mammoth to BG Transition")

    
    # # # # # # #
    # Blade Garden
    # # # # # # #
    # Entrance/Exits
    blade_garden_upper.connect(jagged_forest_garden_trans, "BG_Upper to Jagged Forest")
    blade_garden_upper.connect(nailglade, "BG_Upper to Nailglade")
    #blade_garden_upper.connect(nailglade, "Blade Garden to Nailglade") #workshop
    # Interzone
    blade_garden_upper.connect(blade_garden_middle, "BG_Upper to BG_Middle")
    blade_garden_middle.connect(blade_garden_upper, "BG_Middle to BG_Upper")
    blade_garden_middle.connect(blade_garden_lower, "BG_Middle to BG_Lower")
    
    
    
    
    # # # # # # #
    # Nailglade
    # # # # # # #
    # Entrance/Exits
    nailglade.connect(paint_reef, "Nailglade to Paint Reef")
    nailglade.connect(blade_garden, "Nailglade to Blade Garden")
    nailglade.connect(jagged_forest, "Nailglade to Jagged Forest")
    nailglade.connect(underheads_nailglade_transition, "Nailglade to Underheads", lambda state: isBreathcrowned(world.player, state))
    nailglade.connect(dregbourg, "Nailglade to Dregbourg")
    # Interzone
    
    # # # # # # #
    # Tree Roots
    # # # # # # #
    # Entrance/Exits
    tree_roots.connect(underheads_alveoli, "Tree Roots to Underheads Alveoli")
    tree_roots.connect(underheads_before_mountainborn, "Tree Roots to Underheads Before Mountainborn")
    tree_roots.connect(faceless_mountains_main, "Tree Roots to Faceless Mountains")
    # Interzone
    tree_roots.connect(tree_roots_visage, "Tree Roots to Tree Roots Visage", lambda state: canHighJump(world.player, state))
    
    # # # # # # #
    # Dregbourg
    # # # # # # #
    # Entrance/Exits
    dregbourg.connect(paint_reef, "Dregbourg to Paint Reef")
    dregbourg.connect(mudfalls, "Dregbourg to Mudfalls")
    # dregbourg.connect(underheads, "Dregbourg to Underheads") # This is generally only a one-way in game.
    dregbourg.connect(nailglade, "Dregbourg to Nailglade")
    # Interzone
    
    # # # # # # #
    # Paint Reef
    # # # # # # #
    # Entrance/Exits
    paint_reef.connect(temple_of_hands_birthplace_lower, "Paint Reef to Temple of Hands Birthplace Lower")
    paint_reef.connect(dregbourg, "Paint Reef to Dregbourg")
    paint_reef.connect(nailglade, "Paint Reef to Nailglade")
    # Interzone
    
    # # # # # # #
    # Palladium
    # # # # # # #
    # Entrance/Exits
    palladium.connect(mudfalls, "Palladium to Mudfalls")
    palladium.connect(fallen_path, "Palladium to Fallen Path")
    # Interzone
    
    # # # # # # #
    # Fallen Path
    # # # # # # #
    # Entrance/Exits
    fallen_path.connect(palladium, "Fallen Path to Palladium")
    fallen_path.connect(mudpits, "Fallen Path to Mudpits")
    fallen_path.connect(skyrise, "Fallen Path to ")
    # Interzone
    
    # # # # # # #
    # Mudpits
    # # # # # # #
    # Entrance/Exits
    mudpits.connect(mudfalls, "Mudpits to Mudfalls")
    mudpits.connect(fallen_path, "Mudpits to Fallen Path")
    # Interzone
    
    # # # # # # #
    # Skyrise
    # # # # # # #
    # Entrance/Exits
    skyrise.connect(fallen_path, "Skyrise to Fallen Path")
    skyrise.connect(starmire, "Skyrise to Starmire")
    # Interzone
    
    # # # # # # #
    # Starmire
    # # # # # # #
    # Entrance/Exits
    starmire.connect(skyrise, "Starmire to Skyrise")
    # Interzone
    
    # # # # # # #
    # Wanting Tree
    # # # # # # #
    # Entrance/Exits
    wanting_tree.connect(faceless_mountains_wanting_bloodroots, "Wanting Tree to Faceless Mountains")
    # Interzone


    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in py.
    # overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     overworld.connect(top_middle_room, "Overworld to Top Middle Room")