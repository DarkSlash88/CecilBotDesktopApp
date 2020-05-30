import re
from DataBuilder import Data

data = Data()

def command_parse(author, message):
    #Data lookup patterns
    rcommandpattern = r"\A!r-?\w*"
    wcommandpattern = r"\A![w|?|3x]-?\w*"
    skillpattern = r"\A!skill\s.*"
    bosspattern = r"\A!boss\s.*"
    codepattern = r"\A!code[s]?\s\w*"
    itempattern = r"\A!item\s.*"
    specialequipmentpattern = r"\A!specialequipment\s.*"
    specialweaponpattern = r"\A!specialweapon\s.*"
    statuseffectpattern = r"\A!statuseffect\s\.*"
    rootpattern = r"\A!base\s.*"

    #General command patterns
    hellopattern = r"\A!hello"
    commandspattern = r"\A!command[s]?"
    beyondchaospattern = "\A!beyondchaos"
    discordpattern = r"\A!discord"
    getbcpattern = r"\A!getbc"
    permadeath = r"\A!permadeath"
    aboutpattern = r"\A!about"

    if re.search(rcommandpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!", "", message).lower()
            return (data.random_skillsets[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(wcommandpattern, message, re.IGNORECASE):
        return "W-/?-/3x-[spellset] is just like r-[spellset] but gets casted more than once. " \
               "NOTE: W-/?-/3x/etc. spellsets with Spiraler, Quadra Slam, " \
               "and/or Quadra Slice will not cast those spells!"

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


    elif re.search(hellopattern, message, re.IGNORECASE):
        return f"Hello {author}!"
    elif re.search(commandspattern, message, re.IGNORECASE):
        return "Basic commands: !hello, !about, !getBC, !discord, !beyondchaos, !permadeath " \
               "<!R[spell] commands: ex.'!RTime'> " \
               "<!Skill [SkillName] commands: ex.'!skill fire 3'> " \
               "<!Boss [BossName] commands: ex. '!boss Kefka3'> " \
               "<!Code [CodeName] commands: ex. '!code capslockoff'> " \
               "<!Item [ItemName] commands: ex. '!item potion'> " \
               "<!StatusEffect [EffectName] commands: ex: '!statuseffect poison'> " \
               "<!Base [SkillBase] commands: ex. '!base Fir'> " \
               "<!SpecialEquipment [EquipName] commands: ex. '!specialequipment red duster'> " \
               "<!SpecialWeapons [WeaponName] commands: ex. '!specialweapon portal gun'>"
    elif re.search(beyondchaospattern, message, re.IGNORECASE):
        return "Originally developed by Abyssonym, but now maintained by SubtractionSoup, " \
               "Beyond Chaos is a randomizer, a program that remixes game content randomly, " \
               "for FF6. Every time you run Beyond Chaos, it will generate a completely unique, " \
               "brand-new mod of FF6 for you to challenge and explore. There are over 10 billion " \
               "different possible randomizations! Nearly everything is randomized, " \
               "including treasure, enemies, colors, graphics, character abilities, and more."
    elif re.search(getbcpattern, message, re.IGNORECASE):
        return "Current EX version by SubtractionSoup: https://github.com/subtractionsoup/beyondchaos/releases/latest"
    elif re.search(discordpattern, message, re.IGNORECASE):
        return "Check out the Beyond Chaos Barracks - https://discord.gg/S3G3UXy"
    elif re.search(permadeath, message, re.IGNORECASE):
        return "Permadeath means starting a new randomized game upon game over"
    elif re.search(aboutpattern, message, re.IGNORECASE):
        return "CecilBot is a program to help players by providing a list of skills and " \
               "spells within each skill-set. CecilBot was made by GreenKnight5 and inspired by " \
               "FF6Rando community member Cecil188, and uses databases authored by Cecil188. " \
               "Please PM any questions, comments, concerns to @GreenKnight5 or @Cecil188."



"""Commands to add
!commands
!beyondchaos - 
!getbc - Current EX version by SubtractionSoup: https://github.com/subtractionsoup/beyondchaos/releases/latest
!discord - Check out the Beyond Chaos Barracks - https://discord.gg/S3G3UXy
!permadeath - Permadeath means starting a new randomized game upon game over
!about - CecilBot is a program to help players by providing a list of skills and spells within each skill-set. CecilBot was made by GreenKnight5 and inspired by FF6Rando community member Cecil188, and uses databases authored by Cecil188. Please PM any questions, comments, concerns to @GreenKnight5 or @Cecil188.
"""

if __name__ == "__main__":
    print(command_parse("greenKnight5", "!?-fire"))

