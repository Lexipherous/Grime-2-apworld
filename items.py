from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification as IC
from dataclasses import dataclass
if TYPE_CHECKING:
    from .world import Grime2World
    
def get_random_filler_item_name(world: Grime2World) -> str:
    # APQuest has an option called "trap_chance".
    # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # For this purpose, we need to use a random generator.

    # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # This ensures that generating with the same generator seed twice yields the same output.
    # DO NOT use a bare random object from Python's built-in random module.
    # if world.random.randint(0, 99) < world.options.trap_chance:
    #     return "Math Trap"
    return "Bloodroot Splinter"

class Grime2Item(Item):
    game = "Grime 2"


@dataclass
class Grime2ItemData:
    name: str
    classification: IC
    ap_id: int
    count: int = 1
    game: str = "Grime 2"
    isStarterWeapon: bool = False

def populate_items():
    item_list: list[Grime2ItemData] = [
        # Weapons
        Grime2ItemData("Attuning Bow", IC.useful, 10001),
        # Grime2ItemData("Attuning Bow", IC.useful, "66737bdd-e371-4b5c-abe1-2b54365ce837", 10002),
        # Grime2ItemData("Barbed Sword", IC.useful, "b9487eac-9a9c-4b5d-9cbf-b005fee33576", 10002),
        # Grime2ItemData("Beak Fists", IC.useful, "5c109ef3-40cf-4b23-98b7-eb75429259fa", 10003),
        # Grime2ItemData("Beast Bow", IC.useful, "4763f53f-1ae9-4ee8-91e7-a939d859cf3c", 10004),
        # Grime2ItemData("Bladeroot Greatsword", IC.useful, "b31dad4f-1bc3-4488-b60c-c3efab095664", 10005),
        # Grime2ItemData("Bladeroot Sword", IC.useful, "10b865ed-b6bf-41a2-b8c1-8973d9c011c8", 10006),
        # Grime2ItemData("Bloodmetal Scythe", IC.useful, "ff17e22a-c733-4b4f-9bb9-0b0c1f065cde", 10007),
        # Grime2ItemData("Bowblades", IC.useful, "87391639-26d9-4354-a9a3-bc6eaa98368d", 10008),
        Grime2ItemData("Clasped Mace", IC.useful, 10009, isStarterWeapon=True),
        # Grime2ItemData("Clawing Scythe", IC.useful, "af1d39e2-a98a-477a-8db8-ba8cc2444b8f", 10010),
        # Grime2ItemData("Faceless Spear", IC.useful, "c67a2c34-2e7a-472d-bef8-268eebfecc8d", 10011),
        # Grime2ItemData("Finger Fists", IC.useful, "cc6c9d0b-fa48-41cf-ba63-8f78d3590d8d", 10012),
        # Grime2ItemData("Fingerclump Mace", IC.useful, "ac20f040-1b8b-4433-be12-3d9b09889e48", 10013),
        # Grime2ItemData("Forged Fists", IC.useful, "9bec668b-e98a-4837-acad-42d15c09ab99", 10014),
        # Grime2ItemData("Forged Pick", IC.useful, "71bd683f-41e8-4829-8a22-665277113c2f", 10015),
        # Grime2ItemData("Forged Stake", IC.useful, "3a0adcbe-ed7b-47c4-95c3-fd3f400f8f28", 10016),
        # Grime2ItemData("Goel Greatsword", IC.useful, "f4d79025-f995-409d-b60d-51ee7efa885a", 10017),
        # Grime2ItemData("Goz Sickle", IC.useful, "d6617c66-b217-4f3a-a954-dcf2b788be7e", 10018),
        # Grime2ItemData("Gripping Greataxe", IC.useful, "7aa15bf2-d502-4372-a951-d09449c52efd", 10019),
        # Grime2ItemData("Jaw Axe", IC.useful, "0e6f2e0c-8006-4496-b665-72905eaad418", 10020),
        Grime2ItemData("Knifehand", IC.useful, 10021, isStarterWeapon=True),
        # Grime2ItemData("Mammoth Axe", IC.useful, "07f07e35-9df6-4eb6-9f68-857a46345a2e", 10022),
        Grime2ItemData("Maul Axe", IC.useful, 10023, isStarterWeapon=True),
        # Grime2ItemData("Nail Bow", IC.useful, "cfc541a1-945a-4906-8b83-d41c7e92ae99", 10024),
        # Grime2ItemData("Pitcher Spear", IC.useful, "f92e6e09-c70c-4e15-b26d-e3c4106be29b", 10025, ),
        # Grime2ItemData("Raking Sword", IC.useful, "d43099d9-3c6b-456a-88f9-094a91d3728a", 10026, ),
        # Grime2ItemData("Rust Fists", IC.useful, "7240ae79-0ad4-4449-9540-f8f512457a93", 10027, ),
        # Grime2ItemData("Spearhand", IC.useful, "825d901c-6a41-466a-895c-b6bdbb0d0b2d", 10028, ),
        # Grime2ItemData("Throwing Nails", IC.useful, "3665b49e-5528-46d5-b3d4-19d90950e71b", 10029, ),
        # Grime2ItemData("Throwing Stars", IC.useful, "848f020e-fe1a-469d-8d94-41fa4db7a65b", 10030, ),
        Grime2ItemData("Throwing Thumbs", IC.useful, 10031, isStarterWeapon=True),
        # Grime2ItemData("Tooth Hammer", IC.useful, "ab2f39c4-635f-44d5-b18c-244d0558a8fb", 10032, ),
        # Grime2ItemData("Zev Blades", IC.useful, "e5f49c7f-29cf-4f12-8fdc-3d675051e435", 10033, ),
        
        # Quest Items
        Grime2ItemData("Locked Sphere", IC.progression, "96f4e840-0412-4231-824f-bba5ecbb0503", 11001),
        
        # Misc Items
        # Grime2ItemData("Bloodroot Chunk", IC.filler, "924cc1b9-8b66-4302-9cf1-ae2b949a0ee6", 12001),
        # Grime2ItemData("Bloodroot Shard", IC.filler, "3317fe57-2dd2-4d46-a124-050ad9e2754a", 12002),
        Grime2ItemData("Bloodroot Splinter", IC.filler, "cc3fc898-f110-418f-89be-72fa681469f9", 12003),
        # Grime2ItemData("Thin Marah Strand", IC.filler, "2bdaab02-ba9f-4455-a907-f091e93c493b", 12004),
        # Grime2ItemData("Long Marah Strand", IC.filler, "1d18e1f8-1cae-4498-8465-fb4c7ae13817", 12005),
        # Grime2ItemData("Luscious Marah Strand", IC.filler, "dfcc44ec-44b9-4694-8f75-af64ec09fba5", 12006),
    ]
    return item_list

ITEM_TABLE = {item.name: item for item in populate_items()}
ITEM_NAME_TO_ID = {item.name: item.ap_id for item in ITEM_TABLE.values()}


def create_item_with_correct_classification(world: Grime2World, name: str) -> Grime2Item:
    data = ITEM_TABLE[name]
    return Grime2Item(name, data.classification, data.ap_id, world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: Grime2World) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.
    item_pool: list[Item] = []
    for item_data in ITEM_TABLE.values():
        item_pool += [world.create_item(item_data.name) for _ in range(item_data.count)]
    
    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(item_pool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += item_pool

    # # Sometimes, you might want the player to start with certain items already in their inventory.
    # # These items are called "precollected items".
    # # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # # Players can add precollected items themselves via the generic "start_inventory" option.
    # # If you want to add your own precollected items, you can do so via world.push_precollected().
    # if world.options.start_with_one_confetti_cannon:
    #     # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
    #     starting_confetti_cannon = world.create_item("Confetti Cannon")
    #     world.push_precollected(starting_confetti_cannon)

filler_list: list[str] = []
