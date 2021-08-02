import re
from DataBuilder import Data

data = Data()

def command_parse(author, message):
    #Data lookup patterns
    rchaospattern = r"\A!r-?chaos"
    rcommandpattern = r"\A!r-?\w*"
    wcommandpattern = r"\A![w|?|3x]-\w*"
    skillpattern = r"\A!skill\s.*"
    bosspattern = r"\A!boss\s.*"
    codepattern = r"\A!code[s]?\s\w*"
    itempattern = r"\A!item\s.*"
    toolpattern = r"\A!tool\s.*"
    specialequipmentpattern = r"\A!specialequipment\s.*"
    specialweaponpattern = r"\A!specialweapon\s.*"
    statuseffectpattern = r"\A!statuseffect\s\.*"
    rootpattern = r"\A!base\s.*"
    communitycommandpattern = r"\A!.*"

    #General command patterns
    hellopattern = r"\A!hello"
    commandspattern = r"\A!bccommand[s]?"
    beyondchaospattern = "\A!beyondchaos"
    discordpattern = r"\A!bcdiscord"
    getbcpattern = r"\A!getbc"
    permadeath = r"\A!permadeath"
    aboutpattern = r"\A!about"


    if re.search(rchaospattern, message, re.IGNORECASE):
        return "It's literal chaos. It can roll any spell or skill in the game. Use at your own risk! Danger Odds:(8/256=3.13%)"

    elif re.search(rcommandpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!", "", message).lower()
            return (data.random_skillsets[temp])
        except:
            #in case someone enteres a community command that starts with "r"
            try:
                temp = re.sub("!", "", message).lower()
                return (data.commands[temp])
            except:
                return "Null"

    elif re.search(wcommandpattern, message, re.IGNORECASE):
        return "W-/?-/3x-[spellset] is just like r-[spellset] but " \
               "gets cast more than once. NOTE: These spellsets that " \
               "include Spiraler, Quadra Slam, and/or Quadra Slice will " \
               "not cast those spells!"

    elif re.search(skillpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!skill ", "", message).lower()
            return (data.skill_parameters[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(bosspattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!boss ", "", message).lower()
            return (data.boss_disambiguations[temp])
        except:
            try:
                temp = re.sub("!boss ", "", message).lower()
                return (data.boss_moves[temp])
            except:
                return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
            return
    elif re.search(codepattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!code ", "", message).lower()
            return (data.codes[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(itempattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!item ", "", message).lower()
            return (data.item_table[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(toolpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!tool ", "", message).lower()
            return (data.tool_table[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                    f"and try again.")
    elif re.search(specialequipmentpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!specialequipment ", "", message).lower()
            return (data.special_equipment[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(specialweaponpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!specialweapon ", "", message).lower()
            return (data.special_weapons[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again.")
    elif re.search(statuseffectpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!statuseffect ", "", message).lower()
            return (data.status_effects[temp])
        except:
            pass
    elif re.search(rootpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!base ", "", message)
            return (data.root_table[temp])
        except:
            return (f"Sorry, could not find {temp}. Please check your spelling "
                  f"and try again. REMEMBER: capitalization matters!")


    elif re.search(hellopattern, message, re.IGNORECASE):
        return f"Hello {author}!"
    elif re.search(commandspattern, message, re.IGNORECASE):
        return "Basic commands: !hello, !about, !getBC, !bcdiscord, !beyondchaos, !permadeath " \
               "<!R[spell] commands: ex.'!RTime'> " \
               "<!Skill [SkillName] commands: ex.'!skill fire 3'> " \
               "<!Boss [BossName] commands: ex. '!boss Kefka3'> " \
               "<!Code [CodeName] commands: ex. '!code capslockoff'> " \
               "<!Item [ItemName] commands: ex. '!item potion'> " \
               "<!StatusEffect [EffectName] commands: ex: '!statuseffect poison'> " \
               "<!Base [SkillBase] commands: ex. '!base Fir'> " \
               "<!SpecialEquipment [EquipName] commands: ex. '!specialequipment red duster'> " \
               "<!SpecialWeapons [WeaponName] commands: ex. '!specialweapon portal gun'>" \
               "<!Tool [ToolName] commands: ex. '!tool bio blaster'>"
    elif re.search(beyondchaospattern, message, re.IGNORECASE):
        return "Originally developed by Abyssonym, then maintained by SubtractionSoup, " \
               "now maintained by DarkSlash88, Beyond Chaos is a randomizer, " \
               "a program that remixes game content randomly, for FF6. Every time you run Beyond Chaos," \
               "it will generate a completely unique, brand-new mod of FF6 for you to challenge and explore." \
               "Nearly everything is randomized, including treasure, enemies, colors," \
               "graphics, character abilities, music, sprites, and more."
    elif re.search(getbcpattern, message, re.IGNORECASE):
        return "Current CE version by DarkSlash88: https://github.com/FF6BeyondChaos/BeyondChaosRandomizer/releases"
    elif re.search(discordpattern, message, re.IGNORECASE):
        return "Check out the Beyond Chaos Barracks - https://discord.gg/S3G3UXy"
    elif re.search(permadeath, message, re.IGNORECASE):
        return "Permadeath means starting a new randomized game upon game over"
    elif re.search(aboutpattern, message, re.IGNORECASE):
        return "CecilBot is a program to help players by providing a list of skills and " \
               "spells within each skill-set. CecilBot was made by GreenKnight5 and inspired by " \
               "FF6Rando community member Cecil188, and uses databases authored by Cecil188. " \
               "Please PM any questions, comments, concerns to @GreenKnight5 or @Cecil188."
    elif re.search(communitycommandpattern, message, re.IGNORECASE):
        try:
            temp = re.sub("!", "", message).lower()
            return (data.commands[temp])
        except:
            return "Null"
    else:
        return "Null"


# for testing
if __name__ == "__main__":
    print(command_parse("greenKnight5", "!r-chaos"))

