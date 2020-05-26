import re
from DataBuilder import Data

data = Data()

def command_parse(message):
    rcommandpattern = r"\A!(r|R)-*\w*"
    wcommandpattern = r"\A!(w|W)-*\w*"
    skillpattern = r"\A!skill\s.*"
    bosspattern = r"\A!boss\s.*"
    codepattern = r"\A!code\s\w*"
    itempattern = r"\A!item\s.*"
    specialequipmentpattern = r"\A!specialequipment\s.*"
    specialweaponpattern = r"\A!specialweapon\s.*"
    statuseffectpattern = r"\A!statuseffect\s\.*"
    rootpattern = r"\A!base\s.*"

    if re.search(rcommandpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!", "", message).lower()
            return (data.random_skillsets[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(wcommandpattern, message, re.IGNORECASE):
        print("wcommand")
    elif re.search(skillpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!skill ", "", message)
            return (data.skill_parameters[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(bosspattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!boss ", "", message)
            return (data.boss_moves[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(codepattern, message, re.IGNORECASE):
        # make command to see all
        try:
            temp = re.sub("!code ", "", message)
            return (data.codes[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(itempattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!item ", "", message)
            return (data.item_table[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(specialequipmentpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!specialequipment ", "", message)
            return (data.special_equipment[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(specialweaponpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!specialweapon ", "", message)
            return (data.special_weapons[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(statuseffectpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!statuseffect ", "", message)
            return (data.status_effects[temp])
        except:
            pass
    elif re.search(rootpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!base ", "", message)
            return (data.root_table[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again. REMEBER: capitalization matters!")




"""Commands to add
!commands
!beyondchaos - 
!getbc - Current EX version by SubtractionSoup: https://github.com/subtractionsoup/beyondchaos/releases/latest
!discord - Check out the Beyond Chaos Barracks - https://discord.gg/S3G3UXy
!permadeath - Permadeath means starting a new randomized game upon game over
!about - CecilBot is a program to help players by providing a list of skills and spells within each skill-set. CecilBot was made by GreenKnight5 and inspired by FF6Rando community member Cecil188, and uses databases authored by Cecil188. Please PM any questions, comments, concerns to @GreenKnight5 or @Cecil188.
"""

if __name__ == "__main__":
    print(command_parse("!base Fi"))

