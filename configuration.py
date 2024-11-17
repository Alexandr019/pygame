# -*- coding: utf-8 -*-


WIN_WIDTH = 800
WIN_HEIGHT = 600
TILESIZE = 32
FPS =60


HEALTH_LAYER =6
PLAYER_LAYER =5
WEAPON_LAYER = 7
ENEMY_LAYER=3
BLOCKS_LAYER= 2
GROUND_LAYER=1

PLAYER_STEPS = 3
ENEMY_STEPS =1
BULLET_STEPS= 6

ENEMY_HEALTH = 6
PLAYER_HEALTH= 10

BLACK=(0,0,0)
GREEN= (0,255,0)
RED =(255,0,0)

tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B........BBB.............................................B',
    'B.........B................I.............................B',
    'B.E.......B...I..............................E...........B',
    'B.....................................................B..B',
    'B...............................O............BBB.........B',
    'B........B.RR...............L.........................BB.B',
    'B........B.................LLL...................LL....O.B',
    'B..BB.......W.............LLLLL..........................B',
    'BE............O..........LLLLLLL.........................B',
    'B.........................LLLLL.............BBBBB......RRB',
    'B..E.......................LLL.........................RRB',
    'BE..........................L...........................RB',
    'B.........................................B..............B',
    'B.........................................B..............B',
    'B.........................................B..............B',
    'B............................B...B........B..............B',
    'B...........................BB...BB..H...................B',
    'B..........................BLB...BLB......P..............B',
    'B.........................BLLB...BLLB....................B',
    'BBB...BBBLLLLLLLLLLLLLLLLBLLLB...BLLLBLLLLLLLLLLLLBBB...BB',
    'B.H....EBLLLLLLLLLLLLLLLBLLLLB...BLLLLBLLLLLLLLLLLBI....WB',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB...BBBBBBBBBBBBBBBBBBBBBBBBB',
    'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNB...BNNNNNNNNNNNNNNNNNNNNNNNN',
    'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNB...BNNNNNNNNNNNNNNNNNNNNNNNN',
    'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNB...BNNNNNNNNNNNNNNNNNNNNNNNN',
    'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNB...BNNNNNNNNNNNNNNNNNNNNNNNN',
    'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNB...BNNNNNNNNNNNNNNNNNNNNNNNN',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB...BBBBBBBBBBBBBBBBBBBBBBBBB',
    'B.........B.....H.......BLLLLB...BLLLLB............W.....B',
    'B.E.......B...I..........BLLLB...BLLLB...................B',
    'B.........................BLLB...BLLB.................B..B',
    'B..........................BLB...BLB.........BBB.........B',
    'B........B.LL...............BB...BB...................BB.B',
    'B........B...................B...B...............LL....O.B',
    'B..BB.......W......................E.....................B',
    'BE............O..........B...............................B',
    'B........................B..................BBBBB......RRB',
    'B..E............BBBBBBBBBB............I................RRB',
    'BE.......................B..............................RB',
    'B..........E.............B.I.................E...........B',
    'B........................B...............................B',
    'B..........................H.............................B',
    'B..........I.................................I...........B',
    'B..........................L.............................B',
    'B.......................LLLLLLL..........................B',
    'B.......BBB.BBB...BBBLLLLLLLLLLLLLBBB...BBB.BBBB.........B',
    'B.....E.BLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLB.E.......B',
    'B..O....BLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLB......O..B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    ]