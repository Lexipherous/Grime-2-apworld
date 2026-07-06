from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification as IC
from dataclasses import dataclass

from .enums import EnumLoc, EnumItem, GRIME_GAME_NAME
if TYPE_CHECKING:
    from .world import Grime2World

item_base_id = 6942013372314159

def get_random_filler_item_name(world: Grime2World) -> str:
    #if world.random.randint(0, 99) < world.options.trap_chance:
    if world.random.randint(0, 99) < 0:
        return "Math Trap"
    else:
        filler_items = [EnumItem.MI_BLOODROOT_SPLINTER,
                        EnumItem.MI_BLOODROOT_SHARD,
                        EnumItem.MI_BLOODROOT_CHUNK,
                        EnumItem.MI_THIN_MARAH_STRAND,
                        EnumItem.MI_LONG_MARAH_STRAND,
                        EnumItem.MI_LUSCIOUS_MARAH_STRAND,
                        EnumItem.MI_BREATH_MARK]
    
    filler_item = world.random.choice(filler_items)
    
    return filler_item

class Grime2Item(Item):
    game = GRIME_GAME_NAME


@dataclass
class Grime2ItemData:
    name: str
    classification: IC
    ap_id: int
    count: int = 1
    isStarterWeapon: bool = False
    isWeapon: bool = False

def populate_items():
    item_list_weapons = populate_items_weapons()
    item_list_armor_sets = populate_items_armor_sets()
    item_list_armor_pieces = populate_items_armor_pieces()
    item_list_quest_items = populate_items_quest_items()
    item_list_item_molds = populate_items_item_molds()
    item_list_prey_molds = populate_items_prey_molds()
    item_list_misc = populate_items_misc()
    item_list_breathcrowns = populate_items_breathcrowns()
    item_list_ability_movement = populate_items_ability_movement()
    item_list_ability_combat = populate_items_ability_combat()
    item_list_traits = populate_items_traits()
    
    item_list = (item_list_weapons + 
                 item_list_armor_sets +
                 item_list_armor_pieces +
                 item_list_quest_items + 
                 item_list_item_molds +
                 item_list_prey_molds + 
                 item_list_misc + 
                 item_list_breathcrowns + 
                 item_list_ability_movement + 
                 item_list_ability_combat + 
                 item_list_traits)
    
    return item_list

def populate_items_weapons():
    item_list: list[Grime2ItemData] = [
        # Weapons
        Grime2ItemData(EnumItem.W_ATTUNING_BOW.value, IC.useful, item_base_id + 10001, isWeapon=True),
        Grime2ItemData(EnumItem.W_BARBED_SWORD.value, IC.useful, item_base_id + 10002, isWeapon=True),
        Grime2ItemData(EnumItem.W_BEAK_FISTS.value, IC.useful, item_base_id + 10003, isWeapon=True),
        Grime2ItemData(EnumItem.W_BEAST_BOW.value, IC.useful, item_base_id + 10004, isWeapon=True),
        Grime2ItemData(EnumItem.W_BLADEROOT_GREATSWORD.value, IC.useful, item_base_id + 10005, isWeapon=True),
        Grime2ItemData(EnumItem.W_BLADEROOT_SWORD.value, IC.useful, item_base_id + 10006, isWeapon=True),
        Grime2ItemData(EnumItem.W_BLOODMETAL_SCYTHE.value, IC.useful, item_base_id + 10007, isWeapon=True),
        Grime2ItemData(EnumItem.W_BOWBLADES.value, IC.useful, item_base_id + 10008, isWeapon=True),
        Grime2ItemData(EnumItem.W_CLASPED_MACE.value, IC.useful, item_base_id + 10009, isWeapon=True, isStarterWeapon=True),
        Grime2ItemData(EnumItem.W_CLAWING_SCYTHE.value, IC.useful, item_base_id + 10010, isWeapon=True),
        Grime2ItemData(EnumItem.W_FACELESS_SPEAR.value, IC.useful, item_base_id + 10011, isWeapon=True),
        Grime2ItemData(EnumItem.W_FINGER_FISTS.value, IC.useful, item_base_id + 10012, isWeapon=True),
        Grime2ItemData(EnumItem.W_FINGERCLUMP_MACE.value, IC.useful, item_base_id + 10013, isWeapon=True),
        Grime2ItemData(EnumItem.W_FORGED_FISTS.value, IC.useful, item_base_id + 10014, isWeapon=True),
        Grime2ItemData(EnumItem.W_FORGED_PICK.value, IC.useful, item_base_id + 10015, isWeapon=True),
        Grime2ItemData(EnumItem.W_FORGED_STAKE.value, IC.useful, item_base_id + 10016, isWeapon=True),
        Grime2ItemData(EnumItem.W_GOEL_GREATSWORD.value, IC.useful, item_base_id + 10017, isWeapon=True),
        Grime2ItemData(EnumItem.W_GOZ_SICKLE.value, IC.useful, item_base_id + 10018, isWeapon=True),
        Grime2ItemData(EnumItem.W_GRIPPING_GREATAXE.value, IC.useful, item_base_id + 10019, isWeapon=True),
        Grime2ItemData(EnumItem.W_JAW_AXE.value, IC.useful, item_base_id + 10020, isWeapon=True),
        Grime2ItemData(EnumItem.W_KNIFEHAND.value, IC.useful, item_base_id + 10021, isWeapon=True, isStarterWeapon=True),
        Grime2ItemData(EnumItem.W_MAMMOTH_AXE.value, IC.useful, item_base_id + 10022, isWeapon=True),
        Grime2ItemData(EnumItem.W_MAUL_AXE.value, IC.useful, item_base_id + 10023, isWeapon=True, isStarterWeapon=True),
        Grime2ItemData(EnumItem.W_NAIL_BOW.value, IC.useful, item_base_id + 10024, isWeapon=True),
        Grime2ItemData(EnumItem.W_PITCHER_SPEAR.value, IC.useful, item_base_id + 10025, isWeapon=True, ),
        Grime2ItemData(EnumItem.W_RAKING_SWORD.value, IC.useful, item_base_id + 10026, isWeapon=True, ),
        Grime2ItemData(EnumItem.W_RUST_FISTS.value, IC.useful, item_base_id + 10027, isWeapon=True, ),
        Grime2ItemData(EnumItem.W_SPEARHAND.value, IC.useful, item_base_id + 10028, isWeapon=True, ),
        Grime2ItemData(EnumItem.W_THROWING_NAILS.value, IC.useful, item_base_id + 10029, isWeapon=True, ),
        Grime2ItemData(EnumItem.W_THROWING_STARS.value, IC.useful, item_base_id + 10030, isWeapon=True, ),
        Grime2ItemData(EnumItem.W_THROWING_THUMBS.value, IC.useful, item_base_id + 10031, isWeapon=True, isStarterWeapon=True),
        Grime2ItemData(EnumItem.W_TOOTH_HAMMER.value, IC.useful, item_base_id + 10032, isWeapon=True, ),
        Grime2ItemData(EnumItem.W_ZEV_BLADES.value, IC.useful, item_base_id + 10033, isWeapon=True, ),
        
        # Weapons - Cut
        # Grime2ItemData(EnumItem.W_ALLOYBARK_CLEAVERS, IC.useful, item_base_id + 10034, ),
        # Grime2ItemData(EnumItem.W_BLADEROOT_JAVELIN, IC.useful, item_base_id + 10035, ),
        # Grime2ItemData(EnumItem.W_CODA_SCYTHESWORD, IC.useful, item_base_id + 10036, ),
    ]
    return item_list
def populate_items_armor_sets():
    
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.A_BEASTPLATE_SET.value, IC.useful, item_base_id + 10101, ),
        Grime2ItemData(EnumItem.A_BRUTE_GARBS_SET.value, IC.useful, item_base_id + 10102, ),
        Grime2ItemData(EnumItem.A_FALLEN_GREATBLADE_SET.value, IC.useful, item_base_id + 10103, ),
        Grime2ItemData(EnumItem.A_FORGED_BOULDER_SET.value, IC.useful, item_base_id + 10104, ),
        Grime2ItemData(EnumItem.A_FORGED_LITTLES_SET.value, IC.useful, item_base_id + 10105, ),
        Grime2ItemData(EnumItem.A_FORGED_PEBBLE_SET.value, IC.useful, item_base_id + 10106, ),
        Grime2ItemData(EnumItem.A_FORMLESS_SET.value, IC.useful, item_base_id + 10107, ),
        Grime2ItemData(EnumItem.A_GRUNT_GARBS_SET.value, IC.useful, item_base_id + 10108, ),
        Grime2ItemData(EnumItem.A_HANDCLOTH_SET.value, IC.useful, item_base_id + 10109, ),
        Grime2ItemData(EnumItem.A_IMPALED_SMITHED_SET.value, IC.useful, item_base_id + 10110, ),
        Grime2ItemData(EnumItem.A_LAHAVIST_NOMAD_SET.value, IC.useful, item_base_id + 10111, ),
        Grime2ItemData(EnumItem.A_LAHAVIST_WANDERER_SET.value, IC.useful, item_base_id + 10112, ),
        Grime2ItemData(EnumItem.A_MASK_COLLECTOR_SET.value, IC.useful, item_base_id + 10113, ),
        Grime2ItemData(EnumItem.A_NAILGLADE_FIGHTER_SET.value, IC.useful, item_base_id + 10114, ),
        Grime2ItemData(EnumItem.A_NAILGLADE_SCOUT_SET.value, IC.useful, item_base_id + 10115, ),
        Grime2ItemData(EnumItem.A_ORCHARD_HOMAGE_SET.value, IC.useful, item_base_id + 10116, ),
        Grime2ItemData(EnumItem.A_PENPIERCED_SET.value, IC.useful, item_base_id + 10117, ),
        Grime2ItemData(EnumItem.A_PITCHER_GUARD_SET.value, IC.useful, item_base_id + 10118, ),
        Grime2ItemData(EnumItem.A_POACHER_SET.value, IC.useful, item_base_id + 10119, ),
        Grime2ItemData(EnumItem.A_REEF_BLOOM_SET.value, IC.useful, item_base_id + 10120, ),
        Grime2ItemData(EnumItem.A_REEF_DIVER_SET.value, IC.useful, item_base_id + 10121, ),
        Grime2ItemData(EnumItem.A_TAINTED_HECKLES_SET.value, IC.useful, item_base_id + 10122, ),
        Grime2ItemData(EnumItem.A_WITCHCAP_SET.value, IC.useful, item_base_id + 10123, ),
    ]
    return item_list
def populate_items_armor_pieces():
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.A_BEASTPLATE_CHEST.value, IC.useful, item_base_id + 10131, ),
        Grime2ItemData(EnumItem.A_BEASTPLATE_HANDS.value, IC.useful, item_base_id + 10132, ),
        Grime2ItemData(EnumItem.A_BEASTPLATE_LEGS.value, IC.useful, item_base_id + 10133, ),
        Grime2ItemData(EnumItem.A_BRUTE_GARBS_CHEST.value, IC.useful, item_base_id + 10134, ),
        Grime2ItemData(EnumItem.A_BRUTE_GARBS_HANDS.value, IC.useful, item_base_id + 10135, ),
        Grime2ItemData(EnumItem.A_BRUTE_GARBS_LEGS.value, IC.useful, item_base_id + 10136, ),
        Grime2ItemData(EnumItem.A_FALLEN_GREATBLADE_CHEST.value, IC.useful, item_base_id + 10137, ),
        Grime2ItemData(EnumItem.A_FALLEN_GREATBLADE_HANDS.value, IC.useful, item_base_id + 10138, ),
        Grime2ItemData(EnumItem.A_FALLEN_GREATBLADE_LEGS.value, IC.useful, item_base_id + 10139, ),
        Grime2ItemData(EnumItem.A_FORGED_BOULDER_CHEST.value, IC.useful, item_base_id + 10140, ),
        Grime2ItemData(EnumItem.A_FORGED_BOULDER_HANDS.value, IC.useful, item_base_id + 10141, ),
        Grime2ItemData(EnumItem.A_FORGED_BOULDER_LEGS.value, IC.useful, item_base_id + 10142, ),
        Grime2ItemData(EnumItem.A_FORGED_LITTLES_CHEST.value, IC.useful, item_base_id + 10143, ),
        Grime2ItemData(EnumItem.A_FORGED_LITTLES_HANDS.value, IC.useful, item_base_id + 10144, ),
        Grime2ItemData(EnumItem.A_FORGED_LITTLES_LEGS.value, IC.useful, item_base_id + 10145, ),
        Grime2ItemData(EnumItem.A_FORGED_PEBBLE_CHEST.value, IC.useful, item_base_id + 10146, ),
        Grime2ItemData(EnumItem.A_FORGED_PEBBLE_HANDS.value, IC.useful, item_base_id + 10147, ),
        Grime2ItemData(EnumItem.A_FORGED_PEBBLE_LEGS.value, IC.useful, item_base_id + 10148, ),
        Grime2ItemData(EnumItem.A_FORMLESS_CHEST.value, IC.useful, item_base_id + 10149, ),
        Grime2ItemData(EnumItem.A_FORMLESS_HANDS.value, IC.useful, item_base_id + 10150, ),
        Grime2ItemData(EnumItem.A_FORMLESS_LEGS.value, IC.useful, item_base_id + 10151, ),
        Grime2ItemData(EnumItem.A_GRUNT_GARBS_CHEST.value, IC.useful, item_base_id + 10152, ),
        Grime2ItemData(EnumItem.A_GRUNT_GARBS_HANDS.value, IC.useful, item_base_id + 10153, ),
        Grime2ItemData(EnumItem.A_GRUNT_GARBS_LEGS.value, IC.useful, item_base_id + 10154, ),
        Grime2ItemData(EnumItem.A_HANDCLOTH_CHEST.value, IC.useful, item_base_id + 10155, ),
        Grime2ItemData(EnumItem.A_HANDCLOTH_HANDS.value, IC.useful, item_base_id + 10156, ),
        Grime2ItemData(EnumItem.A_HANDCLOTH_LEGS.value, IC.useful, item_base_id + 10157, ),
        Grime2ItemData(EnumItem.A_IMPALED_SMITHED_CHEST.value, IC.useful, item_base_id + 10158, ),
        Grime2ItemData(EnumItem.A_IMPALED_SMITHED_HANDS.value, IC.useful, item_base_id + 10159, ),
        Grime2ItemData(EnumItem.A_IMPALED_SMITHED_LEGS.value, IC.useful, item_base_id + 10160, ),
        Grime2ItemData(EnumItem.A_LAHAVIST_NOMAD_CHEST.value, IC.useful, item_base_id + 10161, ),
        Grime2ItemData(EnumItem.A_LAHAVIST_NOMAD_HANDS.value, IC.useful, item_base_id + 10162, ),
        Grime2ItemData(EnumItem.A_LAHAVIST_NOMAD_LEGS.value, IC.useful, item_base_id + 10163, ),
        Grime2ItemData(EnumItem.A_LAHAVIST_WANDERER_CHEST.value, IC.useful, item_base_id + 10164, ),
        Grime2ItemData(EnumItem.A_LAHAVIST_WANDERER_HANDS.value, IC.useful, item_base_id + 10165, ),
        Grime2ItemData(EnumItem.A_LAHAVIST_WANDERER_LEGS.value, IC.useful, item_base_id + 10166, ),
        Grime2ItemData(EnumItem.A_MASK_COLLECTOR_CHEST.value, IC.useful, item_base_id + 10167, ),
        Grime2ItemData(EnumItem.A_MASK_COLLECTOR_HANDS.value, IC.useful, item_base_id + 10168, ),
        Grime2ItemData(EnumItem.A_MASK_COLLECTOR_LEGS.value, IC.useful, item_base_id + 10169, ),
        Grime2ItemData(EnumItem.A_NAILGLADE_FIGHTER_CHEST.value, IC.useful, item_base_id + 10170, ),
        Grime2ItemData(EnumItem.A_NAILGLADE_FIGHTER_HANDS.value, IC.useful, item_base_id + 10171, ),
        Grime2ItemData(EnumItem.A_NAILGLADE_FIGHTER_LEGS.value, IC.useful, item_base_id + 10172, ),
        Grime2ItemData(EnumItem.A_NAILGLADE_SCOUT_CHEST.value, IC.useful, item_base_id + 10173, ),
        Grime2ItemData(EnumItem.A_NAILGLADE_SCOUT_HANDS.value, IC.useful, item_base_id + 10174, ),
        Grime2ItemData(EnumItem.A_NAILGLADE_SCOUT_LEGS.value, IC.useful, item_base_id + 10175, ),
        Grime2ItemData(EnumItem.A_ORCHARD_HOMAGE_CHEST.value, IC.useful, item_base_id + 10176, ),
        Grime2ItemData(EnumItem.A_ORCHARD_HOMAGE_HANDS.value, IC.useful, item_base_id + 10177, ),
        Grime2ItemData(EnumItem.A_ORCHARD_HOMAGE_LEGS.value, IC.useful, item_base_id + 10178, ),
        Grime2ItemData(EnumItem.A_PENPIERCED_CHEST.value, IC.useful, item_base_id + 10179, ),
        Grime2ItemData(EnumItem.A_PENPIERCED_HANDS.value, IC.useful, item_base_id + 10180, ),
        Grime2ItemData(EnumItem.A_PENPIERCED_LEGS.value, IC.useful, item_base_id + 10181, ),
        Grime2ItemData(EnumItem.A_PITCHER_GUARD_CHEST.value, IC.useful, item_base_id + 10182, ),
        Grime2ItemData(EnumItem.A_PITCHER_GUARD_HANDS.value, IC.useful, item_base_id + 10183, ),
        Grime2ItemData(EnumItem.A_PITCHER_GUARD_LEGS.value, IC.useful, item_base_id + 10184, ),
        Grime2ItemData(EnumItem.A_POACHER_CHEST.value, IC.useful, item_base_id + 10185, ),
        Grime2ItemData(EnumItem.A_POACHER_HANDS.value, IC.useful, item_base_id + 10186, ),
        Grime2ItemData(EnumItem.A_POACHER_LEGS.value, IC.useful, item_base_id + 10187, ),
        Grime2ItemData(EnumItem.A_REEF_BLOOM_CHEST.value, IC.useful, item_base_id + 10188, ),
        Grime2ItemData(EnumItem.A_REEF_BLOOM_HANDS.value, IC.useful, item_base_id + 10189, ),
        Grime2ItemData(EnumItem.A_REEF_BLOOM_LEGS.value, IC.useful, item_base_id + 10190, ),
        Grime2ItemData(EnumItem.A_REEF_DIVER_CHEST.value, IC.useful, item_base_id + 10191, ),
        Grime2ItemData(EnumItem.A_REEF_DIVER_HANDS.value, IC.useful, item_base_id + 10192, ),
        Grime2ItemData(EnumItem.A_REEF_DIVER_LEGS.value, IC.useful, item_base_id + 10193, ),
        Grime2ItemData(EnumItem.A_TAINTED_HECKLES_CHEST.value, IC.useful, item_base_id + 10194, ),
        Grime2ItemData(EnumItem.A_TAINTED_HECKLES_HANDS.value, IC.useful, item_base_id + 10195, ),
        Grime2ItemData(EnumItem.A_TAINTED_HECKLES_LEGS.value, IC.useful, item_base_id + 10196, ),
        Grime2ItemData(EnumItem.A_WITCHCAP_CHEST.value, IC.useful, item_base_id + 10197, ),
        Grime2ItemData(EnumItem.A_WITCHCAP_HANDS.value, IC.useful, item_base_id + 10198, ),
        Grime2ItemData(EnumItem.A_WITCHCAP_LEGS.value, IC.useful, item_base_id + 10199, ),
    ]
    return item_list
def populate_items_quest_items():
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.QI_LOCKED_SPHERE.value, IC.progression, item_base_id + 10250),
        # Grime2ItemData(EnumItem.QI_AXE_GREATBLADE_TORSO.value, IC.progression, item_base_id + 10251),
        Grime2ItemData(EnumItem.QI_BREATHSMITH_LOCATION_INFO.value, IC.progression, item_base_id + 10252),
        Grime2ItemData(EnumItem.QI_HOLSTERS_REMAINS.value, IC.progression, item_base_id + 10253),
        # Grime2ItemData(EnumItem.QI_FRAIL_HORN.value, IC.progression, item_base_id + 10254),
        # Grime2ItemData(EnumItem.QI_FORGED_ANVIL.value, IC.filler, item_base_id + 10255),
        # Grime2ItemData(EnumItem.QI_PENSPEAR_1.value, IC.progression, item_base_id + 10256),
        # Grime2ItemData(EnumItem.QI_PENSPEAR_2.value, IC.progression, item_base_id + 10257),
        Grime2ItemData(EnumItem.QI_PITCHER_LEGS.value, IC.progression, item_base_id + 10258),
        # Grime2ItemData(EnumItem.QI_QUADRANT_BLADE.value, IC.progression, item_base_id + 10259),
        # Grime2ItemData(EnumItem.QI_SWORD_GREATBLADE_TORSO.value, IC.progression, item_base_id + 10260),
        Grime2ItemData(EnumItem.QI_NAILGLADE_WORKSHOP_KEY.value, IC.progression, item_base_id + 10261),
    ]
    return item_list
def populate_items_item_molds():
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.IM_CELEBRATION_BELL.value, IC.useful, item_base_id + 10280, ),
        Grime2ItemData(EnumItem.IM_CHAIN_JAVELIN.value, IC.useful, item_base_id + 10281, ),
        Grime2ItemData(EnumItem.IM_CHARGING_JAVELIN.value, IC.useful, item_base_id + 10282, ),
        Grime2ItemData(EnumItem.IM_DEFENSE_SIGILS.value, IC.useful, item_base_id + 10283, ),
        Grime2ItemData(EnumItem.IM_DRIED_ALVEOLI.value, IC.useful, item_base_id + 10284, ),
        Grime2ItemData(EnumItem.IM_EMBEDDING_NAIL.value, IC.useful, item_base_id + 10285, ),
        Grime2ItemData(EnumItem.IM_HOMING_DROPLET.value, IC.useful, item_base_id + 10286, ),
        Grime2ItemData(EnumItem.IM_KNOCKBACK_WEAVE.value, IC.useful, item_base_id + 10287, ),
        Grime2ItemData(EnumItem.IM_LUMP_OF_HANDS.value, IC.useful, item_base_id + 10288, ),
        Grime2ItemData(EnumItem.IM_OVERGROWN_BLOB.value, IC.useful, item_base_id + 10289, ),
        Grime2ItemData(EnumItem.IM_PRIMING_SPEAR.value, IC.useful, item_base_id + 10290, ),
        Grime2ItemData(EnumItem.IM_REINFORCING_WEAVE.value, IC.useful, item_base_id + 10291, ),
        Grime2ItemData(EnumItem.IM_SCATTER_STONE.value, IC.useful, item_base_id + 10292, ),
        Grime2ItemData(EnumItem.IM_SHARPENING_WEAVE.value, IC.useful, item_base_id + 10293, ),
        Grime2ItemData(EnumItem.IM_SIGIL_BARRIER.value, IC.useful, item_base_id + 10294, ),
        Grime2ItemData(EnumItem.IM_SMASHING_BLOCK.value, IC.useful, item_base_id + 10295, ),
        Grime2ItemData(EnumItem.IM_SMIDGE_OF_PAINT.value, IC.useful, item_base_id + 10296, ),
        Grime2ItemData(EnumItem.IM_SPIKE_BALL.value, IC.useful, item_base_id + 10297, ),
        Grime2ItemData(EnumItem.IM_TRIGGER_BOMB.value, IC.useful, item_base_id + 10298, ),
        Grime2ItemData(EnumItem.IM_VOLATILE_VASE.value, IC.useful, item_base_id + 10299, ),
    ]
    return item_list
def populate_items_prey_molds():
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.PM_CURLED_FINGER.value, IC.useful, item_base_id + 10330, ),
        Grime2ItemData(EnumItem.PM_BROKEN_FORGED.value, IC.useful, item_base_id + 10331, ),
        Grime2ItemData(EnumItem.PM_FACELESS_CHARGER.value, IC.useful, item_base_id + 10332, ),
        Grime2ItemData(EnumItem.PM_FACELESS_CLUBBER.value, IC.useful, item_base_id + 10333, ),
        Grime2ItemData(EnumItem.PM_FACELESS_SCRAPPER.value, IC.useful, item_base_id + 10334, ),
        Grime2ItemData(EnumItem.PM_FORGED_LITTLE.value, IC.useful, item_base_id + 10335, ),
        Grime2ItemData(EnumItem.PM_FORGED_LONG.value, IC.useful, item_base_id + 10336, ),
        Grime2ItemData(EnumItem.PM_FORGED_PEBBLE.value, IC.useful, item_base_id + 10337, ),
        Grime2ItemData(EnumItem.PM_FORGED_SOLDIER.value, IC.useful, item_base_id + 10338, ),
        Grime2ItemData(EnumItem.PM_HARDENED_HALFMADE.value, IC.useful, item_base_id + 10339, ),
        Grime2ItemData(EnumItem.PM_HEAVY_RUSTEDSMITHED.value, IC.useful, item_base_id + 10340, ),
        Grime2ItemData(EnumItem.PM_RUSTED_HALFMADE.value, IC.useful, item_base_id + 10341, ),
        Grime2ItemData(EnumItem.PM_LAUF_MOLD.value, IC.useful, item_base_id + 10342, ),
        Grime2ItemData(EnumItem.PM_LAZEV_SHARP.value, IC.useful, item_base_id + 10343, ),
        Grime2ItemData(EnumItem.PM_MAULING_FINGER.value, IC.useful, item_base_id + 10344, ),
        Grime2ItemData(EnumItem.PM_MEEKPALM.value, IC.useful, item_base_id + 10345, ),
        Grime2ItemData(EnumItem.PM_NAILGLADE_FIGHTER.value, IC.useful, item_base_id + 10346, ),
        Grime2ItemData(EnumItem.PM_PLUNGING_FINGER.value, IC.useful, item_base_id + 10347, ),
        Grime2ItemData(EnumItem.PM_POACHING_NEEDLER.value, IC.useful, item_base_id + 10348, ),
        Grime2ItemData(EnumItem.PM_SHORTBLADE_AXE.value, IC.useful, item_base_id + 10349, ),
        Grime2ItemData(EnumItem.PM_SPIKED_FINGER.value, IC.useful, item_base_id + 10350, ),
        Grime2ItemData(EnumItem.PM_STAR_RUSTEDSMITHED.value, IC.useful, item_base_id + 10351, ),
        Grime2ItemData(EnumItem.PM_SWORD_LAHAVIST.value, IC.useful, item_base_id + 10352, ),
        Grime2ItemData(EnumItem.PM_SWORD_SCABBARD.value, IC.useful, item_base_id + 10353, ),
    ]
    return item_list
def populate_items_misc():
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.MI_BLOODROOT_CHUNK.value, IC.filler, item_base_id + 10380),
        Grime2ItemData(EnumItem.MI_BLOODROOT_SHARD.value, IC.filler, item_base_id + 10381),
        Grime2ItemData(EnumItem.MI_BLOODROOT_SPLINTER.value, IC.filler, item_base_id + 10382),
        Grime2ItemData(EnumItem.MI_THIN_MARAH_STRAND.value, IC.filler, item_base_id + 10383),
        Grime2ItemData(EnumItem.MI_LONG_MARAH_STRAND.value, IC.filler, item_base_id + 10384),
        Grime2ItemData(EnumItem.MI_LUSCIOUS_MARAH_STRAND.value, IC.filler, item_base_id + 10385),
        Grime2ItemData(EnumItem.MI_BREATH_MARK.value, IC.filler, item_base_id + 10386),
        Grime2ItemData(EnumItem.MI_CHISEL_KEY.value, IC.filler, item_base_id + 10387),
        # Grime2ItemData(EnumItem.MI_CHROMA_BLUE.value, IC.filler, item_base_id + 10388),
        # Grime2ItemData(EnumItem.MI_CHROMA_CYAN.value, IC.filler, item_base_id + 10389),
        # Grime2ItemData(EnumItem.MI_CHROMA_GREEN.value, IC.filler, item_base_id + 10390),
        # Grime2ItemData(EnumItem.MI_CHROMA_ORANGE.value, IC.filler, item_base_id + 10391),
        # Grime2ItemData(EnumItem.MI_CHROMA_PINK.value, IC.filler, item_base_id + 10392),
        # Grime2ItemData(EnumItem.MI_CHROMA_PURPLE.value, IC.filler, item_base_id + 10393),
        # Grime2ItemData(EnumItem.MI_CHROMA_RED.value, IC.filler, item_base_id + 10394),
        # Grime2ItemData(EnumItem.MI_CHROMA_YELLOW.value, IC.filler, item_base_id + 10395),
        Grime2ItemData(EnumItem.MI_DROPOT_RUNNER_CONTAINER.value, IC.filler, item_base_id + 10396, 5),
        Grime2ItemData(EnumItem.MI_GALLOPING_DROPOT_CONTAINER.value, IC.filler, item_base_id + 10397, 5),
        Grime2ItemData(EnumItem.MI_SKITTERING_DROPOT_CONTAINER.value, IC.filler, item_base_id + 10398, 5),
        Grime2ItemData(EnumItem.MI_MUDFALLS_DELIVERY.value, IC.filler, item_base_id + 10399),
        Grime2ItemData(EnumItem.MI_FIRSTSMITH_DELIVERY.value, IC.filler, item_base_id + 10400),
        Grime2ItemData(EnumItem.MI_GLAIR.value, IC.filler, item_base_id + 10401, 24),
        # Grime2ItemData(EnumItem.MI_HEART_OF_A_BREATHWEAVER.value, IC.filler, item_base_id + 10402),
        # Grime2ItemData(EnumItem.MI_HEART_OF_A_TRAVELER.value, IC.filler, item_base_id + 10403),
        # Grime2ItemData(EnumItem.MI_HEART_OF_A_DANCER.value, IC.filler, item_base_id + 10404),
        # Grime2ItemData(EnumItem.MI_HEART_OF_A_WARRIOR.value, IC.filler, item_base_id + 10405),
        Grime2ItemData(EnumItem.MI_THIRD_OF_FLESH.value, IC.filler, item_base_id + 10406, 3),
    ]
    return item_list
def populate_items_breathcrowns():
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.BC_HANDPAINT_BREATHCROWN.value, IC.filler, item_base_id + 10431),
        Grime2ItemData(EnumItem.BC_KANKAN_BREATHCROWN.value, IC.filler, item_base_id + 10432),
        Grime2ItemData(EnumItem.BC_THIRSTING_BREATHCROWN.value, IC.filler, item_base_id + 10433),
        Grime2ItemData(EnumItem.BC_KNIGHT_BREATHCROWN.value, IC.filler, item_base_id + 10434),
        Grime2ItemData(EnumItem.BC_LAHAVIST_BREATHCROWN.value, IC.filler, item_base_id + 10435),
        Grime2ItemData(EnumItem.BC_MANZILS_BREATHCROWN.value, IC.filler, item_base_id + 10436),
        Grime2ItemData(EnumItem.BC_NAILGLADER_BREATHCROWN.value, IC.filler, item_base_id + 10437),
        Grime2ItemData(EnumItem.BC_FORGED_BREATHCROWN.value, IC.filler, item_base_id + 10438),
        Grime2ItemData(EnumItem.BC_BLADEBEAST_BREATHCROWN.value, IC.filler, item_base_id + 10439),
    ]
    return item_list
def populate_items_ability_movement():
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.AM_BURSTJUMP.value, IC.progression, item_base_id + 10480), # "Trait_Special_Super Jump"
        Grime2ItemData(EnumItem.AM_HANDJUMP.value, IC.progression, item_base_id + 10481), # "Trait_Special_Double Jump"
        Grime2ItemData(EnumItem.AM_GRASPHOOK.value, IC.progression, item_base_id + 10482), # "Trait_Special_Grasphook"
        Grime2ItemData(EnumItem.AM_GRASPSLIDE.value, IC.progression, item_base_id + 10483), # "Trait_Special_Grasphook Sliding"
        Grime2ItemData(EnumItem.AM_AIRDASH.value, IC.progression, item_base_id + 10484), # "Trait_Special_Air Dash"
        Grime2ItemData(EnumItem.AM_WALLJUMP.value, IC.progression, item_base_id + 10485), # "Trait_Special_Wall Snap"
        Grime2ItemData(EnumItem.AM_DASHSLIDE.value, IC.progression, item_base_id + 10486), # "Trait_Special_Dash Plunge"
        Grime2ItemData(EnumItem.AM_CHAINDASH.value, IC.progression, item_base_id + 10487), # "Trait_Growth_Chain dash"
    ]
    return item_list
def populate_items_ability_combat():
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.AC_MOLD_WARDS.value, IC.progression, item_base_id + 10500), # "Trait_Growth_Mold I Frame"
        Grime2ItemData(EnumItem.AC_GRASP.value, IC.progression, item_base_id + 10501), # "Trait_Special_Grasp"
        Grime2ItemData(EnumItem.AC_FORCE.value, IC.progression, item_base_id + 10502), # "Trait_Special_Force"
        Grime2ItemData(EnumItem.AC_GRASP_COUNTER.value, IC.progression, item_base_id + 10503), # "Trait_Special_Grasp Counter"
        Grime2ItemData(EnumItem.AC_DEATHMARK.value, IC.progression, item_base_id + 10504), # "Trait_Special_Deathmark"
        Grime2ItemData(EnumItem.AC_DASH_COUNTER.value, IC.progression, item_base_id + 10505), # "Trait_Special_Dash Counter"
        Grime2ItemData(EnumItem.AC_RAGE_VULNERABILITY.value, IC.progression, item_base_id + 10506), # "Trait_Special_Bonus Damage On Red Attacks"
        Grime2ItemData(EnumItem.AC_ADDITIONAL_MOLD.value, IC.progression, item_base_id + 10507), # "Trait_Special_Additional Mold Set"
        Grime2ItemData(EnumItem.AC_ITEM_GRASP.value, IC.filler, item_base_id + 10508), # "Trait_Special_Item Grasp"   -   Unlocked via Third of Flesh
        Grime2ItemData(EnumItem.AC_EXTENDED_GRASP_RANGE.value, IC.progression, item_base_id + 10509), # "Trait_Special_Grasp Range"
        Grime2ItemData(EnumItem.AC_FLAWLESS_REFORM.value, IC.progression, item_base_id + 10510), # "Trait_Special_Crushing Damage Removal"
        Grime2ItemData(EnumItem.AC_PAINT_RESTORATION.value, IC.progression, item_base_id + 10511), # "Trait_Special_Checkpoint Paint Restoration"
        Grime2ItemData(EnumItem.AC_PROJECTILE_PARRY.value, IC.progression, item_base_id + 10512), # "Trait_Special_Projectile Parry"
    ]
    return item_list
def populate_items_traits():
    item_list: list[Grime2ItemData] = [
        Grime2ItemData(EnumItem.T_FORCE_PARRY.value, IC.filler, item_base_id + 10550, 3), # "Trait_Growth_Force On Parry" 
        Grime2ItemData(EnumItem.T_FORCE_MOLD.value, IC.filler, item_base_id + 10551, 3), # "Trait_Growth_Force On Mold" 
        Grime2ItemData(EnumItem.T_FORCE_DASH.value, IC.filler, item_base_id + 10552, 3), # "Trait_Growth_Dash Echo_Force" 
        Grime2ItemData(EnumItem.T_FINE_EDGED_PARRY.value, IC.filler, item_base_id + 10553, 1), # "Trait_Growth_Parry Fine Edged" 
        Grime2ItemData(EnumItem.T_PARRY_INFUSION.value, IC.filler, item_base_id + 10554, 1), # "Trait_Growth_Parry Infusion" 
        Grime2ItemData(EnumItem.T_FORCEFUL_MOLD.value, IC.filler, item_base_id + 10555, 3), # "Trait_Growth_Mold Exhausted Boost" 
        Grime2ItemData(EnumItem.T_CAST_EVASION.value, IC.filler, item_base_id + 10556, 3), # "Trait_Growth_Mold I Frame" 
        Grime2ItemData(EnumItem.T_DASH_RECOVERY.value, IC.filler, item_base_id + 10557, 2), # "Trait_Growth_Dash Cooldown Reduction" 
        Grime2ItemData(EnumItem.T_FIRST_STIKE.value, IC.filler, item_base_id + 10558, 3), # "Trait_Growth_Parry_First Hit Buff" 
        Grime2ItemData(EnumItem.T_MOLD_PROTECTION.value, IC.filler, item_base_id + 10559, 3), # "Trait_Growth_Mold Transformed Protection" 
        Grime2ItemData(EnumItem.T_ENERGIZING_DASH.value, IC.filler, item_base_id + 10560, 3), # "Trait_Growth_Dash Counter Force" 
        Grime2ItemData(EnumItem.T_BURST_DASH.value, IC.filler, item_base_id + 10561, 3), # "Trait_Growth_Dash Echo_Damage" 
        Grime2ItemData(EnumItem.T_RAGE_PARRY.value, IC.filler, item_base_id + 10562, 3), # "Trait_Growth_Parry Super" 
        Grime2ItemData(EnumItem.T_EMPOWERING_PARRY.value, IC.filler, item_base_id + 10563, 2), # "Trait_Growth_Parry Stacking Damage Buff" 
        Grime2ItemData(EnumItem.T_RAGE_MOLDS.value, IC.filler, item_base_id + 10564, 3), # "Trait_Growth_Mold Bonus Damage On Super Attacks" 
        Grime2ItemData(EnumItem.T_FORCE_REGENERATION.value, IC.filler, item_base_id + 10565, 3), # "Trait_Growth_Force Regen" 
        Grime2ItemData(EnumItem.T_RAGE_DASH.value, IC.filler, item_base_id + 10566, 3), # "Trait_Growth_Dash Echo_Damage Super" 
        Grime2ItemData(EnumItem.T_MARKING_PARRY.value, IC.filler, item_base_id + 10567, 1), # "Trait_Growth_Parry Death Mark" 
        Grime2ItemData(EnumItem.T_PAINT_PARRY.value, IC.filler, item_base_id + 10568, 3), # "Trait_Growth_Parry Paint" 
        Grime2ItemData(EnumItem.T_PROJECTILE_PARRY.value, IC.filler, item_base_id + 10569, 3), # "Trait_Growth_Projectile Reflect Damage Increase" 
        Grime2ItemData(EnumItem.T_PAINT_DASH.value, IC.filler, item_base_id + 10570, 3), # "Trait_Growth_Dash Echo_Paint" 
        Grime2ItemData(EnumItem.T_ATTACK_DASH.value, IC.filler, item_base_id + 10571, 3), # "Trait_Growth_Dash Echo_Buff" 
        Grime2ItemData(EnumItem.T_AREA_PARRY.value, IC.filler, item_base_id + 10572, 1), # "Trait_Growth_AoE Parry" 
        Grime2ItemData(EnumItem.T_PROJECTILE_GRASP.value, IC.filler, item_base_id + 10573, 1), # "Trait_Growth_Projectile Grasp" 
        Grime2ItemData(EnumItem.T_GRASP_WISPS.value, IC.filler, item_base_id + 10574, 2), # "Trait_Growth_Grasp Counter Wisps" 
    ]
    return item_list
    

ITEM_TABLE = {item.name: item for item in populate_items()}
ITEM_NAME_TO_ID = {item.name: item.ap_id for item in ITEM_TABLE.values()}


def create_item_with_correct_classification(world: Grime2World, name: str) -> Grime2Item:
    data = ITEM_TABLE[name]
    return Grime2Item(name, data.classification, data.ap_id, world.player)


def create_all_items_helper(item_pool, world, tmp_items):
    for item_data in tmp_items.values():
        item_pool += [world.create_item(item_data.name) for _ in range(item_data.count)]
    return item_pool


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: Grime2World) -> None:
    # Populate an item pool list
    item_pool: list[Item] = []
    
    item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_weapons()}) # Populate Weapons
    if True:
        item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_armor_sets()})  # Populate Armor Sets
    else:
        item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_armor_pieces()})  # Populate Armor Pieces
        
    item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_quest_items()}) # Populate Quest Items
    item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_item_molds()}) # Populate Item Molds
    item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_prey_molds()}) # Populate Prey Molds
    item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_misc()}) # Populate Misc Items
    item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_breathcrowns()}) # Populate Breathcrowns
    item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_ability_movement()}) # Populate Ability Movement
    item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_ability_combat()}) # Populate Ability Combat
    item_pool = create_all_items_helper(item_pool, world, {item.name: item for item in populate_items_traits()}) # Populate Traits
        
    # Consider if we're starting with a weapon
    match world.options.starting_weapon.value:
        case 0:
            # Maul Axe as Starter
            starter_weapon = world.random.choice([
                item for item in ITEM_TABLE.values() if item.name == EnumItem.W_MAUL_AXE
            ])
        case 1:
            # Any usable starter
            starter_weapon = world.random.choice([
                item for item in ITEM_TABLE.values() if item.isStarterWeapon
            ])
        case 2:
            # Any usable starter except Maul Axe
            # Any usable starter
            starter_weapon = world.random.choice([
                item for item in ITEM_TABLE.values() if item.isStarterWeapon and item.name != EnumItem.W_MAUL_AXE
            ])
        case 3:
            # Any weapon
            starter_weapon = world.random.choice([
                item for item in ITEM_TABLE.values() if item.isWeapon
            ])
    # Push the starter weapon to the maul axe location
    maul_axe_location = world.get_location(EnumLoc.BIRTHPLACE_LOWER_MAUL_AXE.value)
    maul_axe_location.place_locked_item(world.create_item(starter_weapon.name))
    # Remove start weapon from item_pool
    for i, item in enumerate(item_pool):
        if item.name == starter_weapon.name:
            item_pool.pop(i)
            break
    
    # We have our item pool, now check if we need filler items
    number_of_items = len(item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    # Action on any needed filler items
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # Submit the pool to the multiworld itempool.
    world.multiworld.itempool += item_pool

filler_list: list[str] = []
