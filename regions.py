from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from .enums import EnumRegions

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
    temple_of_hands = Region("Temple of Hands", world.player, world.multiworld)
    mudfalls = Region("Mudfalls", world.player, world.multiworld)
    faceless_mountains = Region("Faceless Mountains", world.player, world.multiworld)
    marahs_orchard = Region("Marah's Orchard", world.player, world.multiworld)
    underheads = Region("Underheads", world.player, world.multiworld)
    kankan = Region("Kankan", world.player, world.multiworld)
    jagged_forest = Region("Jagged Forest", world.player, world.multiworld)
    blade_garden = Region("Blade Garden", world.player, world.multiworld)
    nailglade = Region("Nailglade", world.player, world.multiworld)
    tree_roots = Region("Tree Roots", world.player, world.multiworld)
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
        temple_of_hands,
        mudfalls,
        faceless_mountains,
        marahs_orchard,
        underheads,
        kankan,
        jagged_forest,
        blade_garden,
        nailglade,
        tree_roots,
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
    temple_of_hands = world.get_region(EnumRegions.TEMPLE_OF_HANDS)
    mudfalls = world.get_region(EnumRegions.MUDFALLS)
    faceless_mountains = world.get_region(EnumRegions.FACELESS_MOUNTAINS)
    marahs_orchard = world.get_region(EnumRegions.MARAHS_ORCHARD)
    underheads = world.get_region(EnumRegions.UNDERHEADS)
    kankan = world.get_region(EnumRegions.KANKAN)
    jagged_forest = world.get_region(EnumRegions.JAGGED_FOREST)
    blade_garden = world.get_region(EnumRegions.BLADE_GARDEN)
    nailglade = world.get_region(EnumRegions.NAILGLADE)
    tree_roots = world.get_region(EnumRegions.TREE_ROOTS)
    dregbourg = world.get_region(EnumRegions.DREGBOURG)
    paint_reef = world.get_region(EnumRegions.PAINT_REEF)
    palladium = world.get_region(EnumRegions.PALLADIUM)
    fallen_path = world.get_region(EnumRegions.FALLEN_PATH)
    mudpits = world.get_region(EnumRegions.MUDPITS)
    skyrise = world.get_region(EnumRegions.SKYRISE)
    starmire = world.get_region(EnumRegions.STARMIRE)
    wanting_tree = world.get_region(EnumRegions.WANTING_TREE)

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.

    # An even easier way is to use the region.connect helper.
    menu.connect(temple_of_hands, "Menu to Temple of Hands")
    
    temple_of_hands.connect(mudfalls, "Temple of Hands to Mudfalls")
    temple_of_hands.connect(paint_reef, "Temple of Hands to Paint Reef")
    mudfalls.connect(temple_of_hands, "Mudfalls to Temple of Hands")
    mudfalls.connect(faceless_mountains, "Mudfalls to Faceless Mountains")
    mudfalls.connect(underheads, "Mudfalls to Underheads")
    mudfalls.connect(dregbourg, "Mudfalls to Dregbourg")
    mudfalls.connect(mudpits, "Mudfalls to Mudpits")
    mudfalls.connect(palladium, "Mudfalls to Palladium")
    faceless_mountains.connect(mudfalls, "Faceless Mountains to Mudfalls")
    faceless_mountains.connect(marahs_orchard, "Faceless Mountains to Marah's Orchard")
    faceless_mountains.connect(tree_roots, "Faceless Mountains to Tree Roots")
    faceless_mountains.connect(wanting_tree, "Faceless Mountains to Wanting Tree")
    marahs_orchard.connect(kankan, "Marah's Orchard to Kankan")
    marahs_orchard.connect(underheads, "Marah's Orchard to Underheads")
    marahs_orchard.connect(faceless_mountains, "Marah's Orchard to Faceless Mountains")
    underheads.connect(mudfalls, "Underheads to Mudfalls")
    underheads.connect(marahs_orchard, "Underheads to Marah's Orchard")
    underheads.connect(dregbourg, "Underheads to Dregbourg")
    underheads.connect(nailglade, "Underheads to Nailglade")
    underheads.connect(tree_roots, "Underheads to Tree Roots")
    kankan.connect(marahs_orchard, "Kankan to Marah's Orchard")
    kankan.connect(jagged_forest, "Kankan to Jagged Forest")
    jagged_forest.connect(kankan, "Jagged Forest to Kankan")
    jagged_forest.connect(nailglade, "Jagged Forest to Nailglade")
    jagged_forest.connect(blade_garden, "Jagged Forest to Blade Garden")
    blade_garden.connect(jagged_forest, "Blade Garden to Jagged Forest")
    blade_garden.connect(nailglade, "Blade Garden to Nailglade")
    nailglade.connect(paint_reef, "Nailglade to Paint Reef")
    nailglade.connect(blade_garden, "Nailglade to Blade Garden")
    nailglade.connect(jagged_forest, "Nailglade to Jagged Forest")
    nailglade.connect(underheads, "Nailglade to Underheads")
    nailglade.connect(dregbourg, "Nailglade to Dregbourg")
    tree_roots.connect(underheads, "Tree Roots to Underheads")
    tree_roots.connect(marahs_orchard, "Tree Roots to Marah's Orchard")
    tree_roots.connect(faceless_mountains, "Tree Roots to Faceless Mountains")
    dregbourg.connect(paint_reef, "Dregbourg to Paint Reef")
    dregbourg.connect(mudfalls, "Dregbourg to Mudfalls")
    # dregbourg.connect(underheads, "Dregbourg to Underheads") # This is generally only a one-way in game.
    dregbourg.connect(nailglade, "Dregbourg to Nailglade")
    paint_reef.connect(temple_of_hands, "Paint Reef to Temple of Hands")
    paint_reef.connect(dregbourg, "Paint Reef to Dregbourg")
    paint_reef.connect(nailglade, "Paint Reef to Nailglade")
    palladium.connect(mudfalls, "Palladium to Mudfalls")
    palladium.connect(fallen_path, "Palladium to Fallen Path")
    fallen_path.connect(palladium, "Fallen Path to Palladium")
    fallen_path.connect(mudpits, "Fallen Path to Mudpits")
    fallen_path.connect(skyrise, "Fallen Path to ")
    mudpits.connect(mudfalls, "Mudpits to Mudfalls")
    mudpits.connect(fallen_path, "Mudpits to Fallen Path")
    skyrise.connect(fallen_path, "Skyrise to Fallen Path")
    skyrise.connect(starmire, "Skyrise to Starmire")
    starmire.connect(skyrise, "Starmire to Skyrise")
    wanting_tree.connect(faceless_mountains, "Wanting Tree to Faceless Mountains")


    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    # overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     overworld.connect(top_middle_room, "Overworld to Top Middle Room")