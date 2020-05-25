from os import path
from DataHelper import *
import xlrd

try:
    from sys import _MEIPASS
    MEI = True
    tblpath = path.join(_MEIPASS, "DataFiles")
except ImportError:
    # this prepends the absolute file path of the calling script
    #   to the virtual path passed as a param - GreenKnight5
    bundle_dir = path.dirname(path.abspath(__file__))
    tblpath = path.join(bundle_dir, "DataFiles")

    MEI = False

# Probably not needed
def open_mei_fallback(filename, mode='r'):
    # this prepends the absolute file path of the calling script
    #   to the file passed as a param - GreenKnight5
    filename = path.join(path.dirname(path.abspath(__file__)), filename)

    if not MEI:
        return open(filename, mode)

    try:
        f = open(filename, mode)
    except IOError:
        f = open(path.join(_MEIPASS, filename), mode)
    return f


# Make RE read/do this in the future for any version
BOSS_MOVES_TABLE = path.join(tblpath, "Boss Moves v7.xls")
CODES_TABLE = path.join(tblpath, "Codes v5.xls")
ITEM_TABLE = path.join(tblpath, "Item Table v2.xls")
RANDOM_SKILLSETS_TABLE = path.join(tblpath, "Random Skillsets v2.xls")
ROOT_TABLE = path.join(tblpath, "Root Table v4.xls")
SKILL_PARAMETERS_TABLE = path.join(tblpath, "Skill Parameters v3.xls")
SPECIAL_EQUIPMENT_TABLE = path.join(tblpath, "Special Equipment v3.xls")
SPECIAL_WEAPONS_TABLE = path.join(tblpath, "Special Weapons v4.xls")
STATUS_EFFECTS_TABLE = path.join(tblpath, "Status Effects v3.xls")



class Data:
    def __init__(self):
        # self.boss_moves = dict_builder("DataFiles/Boss Moves v7.xls")
        self.boss_moves = dict_builder(BOSS_MOVES_TABLE)
        self.codes = dict_builder(CODES_TABLE)
        self.item_table = dict_builder(ITEM_TABLE)
        self.random_skillsets = dict_builder(RANDOM_SKILLSETS_TABLE)
        self.root_table = dict_builder(ROOT_TABLE)
        self.skill_parameters = dict_builder(SKILL_PARAMETERS_TABLE)
        self.special_equipment = dict_builder(SPECIAL_EQUIPMENT_TABLE)
        self.special_weapons = dict_builder(SPECIAL_WEAPONS_TABLE)
        self.status_effects = dict_builder(STATUS_EFFECTS_TABLE)

# For testing
if __name__ == "__main__":
    d = Data()
    print(d.boss_moves)
    print(d.random_skillsets)
    print(d.codes)