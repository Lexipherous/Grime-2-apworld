from test.bases import WorldTestBase
from ..items import create_all_items
from ..world import Grime2World
from ..enums import GRIME_GAME_NAME


class Grime2TestBase(WorldTestBase):
    game = GRIME_GAME_NAME
    world: Grime2World