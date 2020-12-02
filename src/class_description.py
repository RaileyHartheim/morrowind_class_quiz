class ClassDescription:
    def __init__(self):
        self.description = {
                "acrobat":  {
                    "Description": "Acrobat is a polite euphemism for agile burglars and second-story men. These thieves avoid detection by stealth, and rely on mobility and cunning to avoid capture.",
                    "Specialization": "Stealth",
                    "Attributes": "Agility, Endurance",
                    "Major skills": ["Acrobatics", "Athletics", "Marksman", "Sneak", "Unarmored"],
                    "Minor skills": ["Speechcraft", "Alteration", "Spear", "Hand-to-hand", "Light Armor"],
                    "Spells": ["none"]
                },
                "agent":  {
                    "Description": "Agents are operatives skilled in deception and avoidance, but trained in self-defense and the use of deadly force. Self-reliant and independent, agents devote themselves to personal goals, or to various patrons or causes.",
                    "Specialization": "Stealth",
                    "Attributes": "Personality, Agility",
                    "Major skills": ["Speechcraft", "Sneak", "Acrobatics", "Light Armor", "Short Blade"],
                    "Minor skills": ["Mercantile", "Conjuration", "Block", "Unarmored", "Illusion"],
                    "Spells": ["none"]
                },
               "archer":  {
                    "Description": "Archers are fighters specializing in long-range combat and rapid movement. Opponents are kept at distance by ranged weapons and swift maneuver, and engaged in melee with sword and shield after the enemy is wounded and weary.",
                    "Specialization": "Combat",
                    "Attributes": "Agility, Strength",
                    "Major skills": ["Marksman", "Long Blade", "Block", "Athletics", "Light Armor"],
                    "Minor skills": ["Unarmored", "Spear", "Restoration", "Sneak", "Medium Armor"],
                    "Spells": ["none"]
                },
                "assassin":  {
                    "Description": "Assassins are killers who rely on stealth and mobility to approach victims undetected. Execution is with ranged weapons or with short blades for close work. Assassins include ruthless murderers and principled agents of noble causes.",
                    "Specialization": "Stealth",
                    "Attributes": "Speed, Intelligence",
                    "Major skills": ["Sneak", "Marksman", "Light Armor", "Short Blade", "Acrobatics"],
                    "Minor skills": ["Security", "Long Blade", "Alchemy", "Block", "Athletics"],
                    "Spells": ["none"]
                },
                "barbarian":  {
                    "Description": "Barbarians are the proud, savage warrior elite of the plains nomads, mountain tribes, and sea reavers. They tend to be brutal and direct, lacking civilized graces, but they glory in heroic feats, and excel in fierce, frenzied single combat.",
                    "Specialization": "Combat",
                    "Attributes": "Strength, Speed",
                    "Major skills": ["Axe", "Medium Armor", "Blunt Weapon", "Athletics", "Block"],
                    "Minor skills": ["Acrobatics", "Light Armor", "Armorer", "Marksman", "Unarmored"],
                    "Spells": ["none"]
                },
                "bard":  {
                    "Description": "Bards are loremasters and storytellers. They crave adventure for the wisdom and insight to be gained, and must depend on sword, shield, spell and enchantment to preserve them from the perils of their educational experiences.",
                    "Specialization": "Stealth",
                    "Attributes": "Personality, Intelligence",
                    "Major skills": ["Speechcraft", "Alchemy", "Acrobatics", "Long Blade", "Block"],
                    "Minor skills": ["Mercantile", "Illusion", "Medium Armor", "Enchant", "Security"],
                    "Spells": ["none"]
                },
                "battlemage":  {
                    "Description": "Battlemages are wizard-warriors, trained in both lethal spellcasting and heavily armored combat. They sacrifice mobility and versatility for the ability to supplement melee and ranged attacks with elemental damage and summoned creatures.",
                    "Specialization": "Magic",
                    "Attributes": "Intelligence, Strength",
                    "Major skills": ["Alteration", "Destruction", "Conjuration", "Axe", "Heavy Armor"],
                    "Minor skills": ["Mysticism", "Long Blade", "Marksman", "Enchant", "Alchemy"],
                    "Spells": ["Shield (5pts for 30sec on self)", "Water Walking (for 60sec on self)", "Bound Dagger (for 60 sec on self)", "Summon Ancestral Ghost (for 60 sec on self)", "Fire Bite (fire damage 15-30 pts on touch)"]
                },
                "crusader":  {
                    "Description": "Any heavily armored warrior with spellcasting powers and a good cause may call himself a Crusader. Crusaders do well by doing good. They hunt monsters and villains, making themselves rich by plunder as they rid the world of evil.",
                    "Specialization": "Combat",
                    "Attributes": "Agility, Strength",
                    "Major skills": ["Blunt Weapon", "Long Blade", "Destruction", "heavy Armor", "Block"],
                    "Minor skills": ["Restoration", "Armorer", "Hand-to-hand", "Medium Armor", "Alchemy"],
                    "Spells": ["Fire Bite (fire damage 15-30 pts on touch"]
                },
                "healer":  {
                    "Description": "Healers are spellcasters who swear solemn oaths to heal the afflicted and cure the diseased. When threatened, they defend themselves with reason and disabling attacks and magic, relying on deadly force only in extremity.",
                    "Specialization": "Magic",
                    "Attributes": "Willpower, Personality",
                    "Major skills": ["Restoration", "Mysticism", "Alteration", "Hand-to-hand", "Speechcraft"],
                    "Minor skills": ["Illusion", "Alchemy", "Unarmored", "Light Armor", "Blunt Weapon"],
                    "Spells": ["Hearth Heal (restore health 20-80 pts on self)", "Shield (5 pts for 30 sec on self)", "Water Walking (for 60 sec on self)", "Detect Creature (detect animal 50-150 ft on self)"]
                },
                "knight":  {
                    "Description": "Of noble birth, or distinguished in battle or tourney, knights are civilized warriors, schooled in letters and courtesy, governed by the codes of chivalry. In addition to the arts of war, knights study the lore of healing and enchantment.",
                    "Specialization": "Combat",
                    "Attributes": "Strength, Personality",
                    "Major skills": ["Long Blade", "Axe", "Speechcraft", "Heavy Armor", "Block"],
                    "Minor skills": ["Restoration", "Mercantile", "Medium Armor", "Enchant", "Armorer"],
                    "Spells": ["none"]
                },
                "mage":  {
                    "Description": "Most mages claim to study magic for its intellectual rewards, but they also often profit from its practical applications. Varying widely in temperament and motivation, mages share but one thing in common - an avid love of spellcasting.",
                    "Specialization": "Magic",
                    "Attributes": "Intelligence, Willpower",
                    "Major skills": ["Mysticism", "Destruction", "Alteration", "Illusion", "Restoration"],
                    "Minor skills": ["Enchant", "Alchemy", "Unarmored", "Short Blade", "Conjuration"],
                    "Spells": ["Hearth Heal (restore health 20-80 pts on self)", "Shield (5 pts for 30 sec on self", "Water Walking (for 60 sec on self)", "Fire Bite (fire damage 15-30 pts on touch)", "Chameleon (10 per cent for 30 sec on self)", "Sanctuary (10 pts for 30 sec on self)", "Detect Creature (detect animal 50-150 ft for 5 sec on self)"]
                },
                "monk":  {
                    "Description": "Monks are students of the ancient martial arts of hand-to-hand combat and unarmored self defense. Monks avoid detection by stealth, mobility, and agility, and are skilled with a variety of ranged and close-combat weapons.",
                    "Specialization": "Stealth",
                    "Attributes": "Agility, Willpower",
                    "Major skills": ["Hand-to-hand", "Unarmored", "Athletics", "Acrobatics", "Sneak"],
                    "Minor skills": ["Block", "Marksman", "Light Armor", "Restoration", "Blunt Weapon"],
                    "Spells": ["none"]
                },
                "nightblade":  {
                    "Description": "Nightblades are spellcasters who use their magics to enhance mobility, concealment, and stealthy close combat. They have a sinister reputation, since many nightblades are thieves, enforcers, assassins, or covert agents.",
                    "Specialization": "Magic",
                    "Attributes": "Willpower, Speed",
                    "Major skills": ["Mysticism", "Illusion", "Alteration", "Sneak", "Short Blade"],
                    "Minor skills": ["Light Armor", "Unarmored", "Destruction", "Marksman", "Security"],
                    "Spells": ["Shield (5 pts for 30 sec on self", "Water Walking (for 60 sec on self)", "Fire Bite (fire damage 15-30 pts on touch)", "Chameleon (10 per cent for 30 sec on self)", "Sanctuary (10 pts for 30 sec on self)", "Detect Creature (detect animal 50-150 ft for 5 sec on self)"]
                },
                "pilgrim":  {
                    "Description": "Pilgrims are travellers, seekers of truth and enlightenment. They fortify themselves for road and wilderness with arms, armor, and magic, and through wide experience of the world, they become shrewd in commerce and persuasion.",
                    "Specialization": "Stealth",
                    "Attributes": "Personality, Endurance",
                    "Major skills": ["Speechcraft", "Mercantile", "Marksman", "Restoration", "Medium Armor"],
                    "Minor skills": ["Illusion", "Hand-to-hand", "Short Blade", "Block", "Alchemy"],
                    "Spells": ["Hearth Heal (restore health 20-80 pts on self)"]
                },
                "rogue":  {
                    "Description": "Rogues are adventurers and opportunists with a gift for getting in and out of trouble. Relying variously on charm and dash, blades and business sense, they thrive on conflict and misfortune, trusting to their luck and cunning to survive.",
                    "Specialization": "Combat",
                    "Attributes": "Speed, Personality",
                    "Major skills": ["Short Blade", "Mercantile", "Axe", "Light Armor", "Hand-to-hand"],
                    "Minor skills": ["Block", "Medium Armor", "Speechcraft", "Athletics", "Long Blade"],
                    "Spells": ["none"]
                },
                "scout":  {
                    "Description": "Scouts rely on stealth to survey routes and opponents, using ranged weapons and skirmish tactics when forced to fight. By contrast with barbarians, in combat scouts tend to be cautious and methodical, rather than impulsive.",
                    "Specialization": "Combat",
                    "Attributes": "Speed, Endurance",
                    "Major skills": ["Sneak", "Long Blade", "Medium Armor", "Athletics", "Block"],
                    "Minor skills": ["Marksman", "Alchemy", "Alteration", "Light Armor", "Unarmored"],
                    "Spells": ["none"]
                },
                "sorcerer":  {
                    "Description": "Though spellcasters by vocation, sorcerers rely most on summonings and enchantments. They are greedy for magic scrolls, rings, armor and weapons, and commanding undead and Daedric servants gratifies their egos.",
                    "Specialization": "Magic",
                    "Attributes": "Intelligence, Endurance",
                    "Major skills": ["Enchant", "Conjuration", "Mysticism", "Destruction", "Alteration"],
                    "Minor skills": ["Illusion", "Medium Armor", "Heavy Armor", "Marksman", "Short Blade"],
                    "Spells": ["Shield (5 pts for 30 sec on self)", "Water Walking (for 60 sec on self)", "Bound Dagger (for 60 sec on self)", "Summon Ancestral Ghost (for 60 sec on self)", "Fire Bite (fire damage 15-30 pts on touch)", "Detect Creature (detect animal 50-150 ft for 5 sec on self)"]
                },
                "spellsword":  {
                    "Description": "Spellswords are spellcasting specialists trained to support Imperial troops in skirmish and in battle. Veteran spellswords are prized as mercenaries, and well-suited for careers as adventurers and soldiers-of-fortune.",
                    "Specialization": "Magic",
                    "Attributes": "Willpower, Endurance",
                    "Major skills": ["Block", "Restoration", "Long Blade", "Destruction", "Alteration"],
                    "Minor skills": ["Blunt Weapon", "Enchant", "Alchemy", "Medium Armor", "Axe"],
                    "Spells": ["Hearth Heal (restore health 20-80 pts on self", "Shield (5 pts for 30 sec on self)", "Water Walking (for 60 sec on self)", "Fire Bite (fire damage 15-30 pts on touch)"]
                },
                "thief":  {
                    "Description": "Thieves are pickpockets and pilferers. Unlike robbers, who kill and loot, thieves typically choose stealth and subterfuge over violence, and often entertain romantic notions of their charm and cleverness in their acquisitive activities.",
                    "Specialization": "Stealth",
                    "Attributes": "Speed, Agility",
                    "Major skills": ["Security", "Sneak", "Acrobatics", "Light Armor", "Short Blade"],
                    "Minor skills": ["Marksman", "Speechcraft", "Hand-to-hand", "Mercantile", "Athletics"],
                    "Spells": ["none"]
                },
                "warrior":  {
                    "Description": "Warriors are the professional men-at-arms, soldiers, mercenaries, and adventurers of the Empire, trained with various weapons and armor styles, conditioned by long marches, and hardened by ambush, skirmish, and battle.",
                    "Specialization": "Combat",
                    "Attributes": "Strength, Endurance",
                    "Major skills": ["Long Blade", "Medium Armor", "Heavy Armor", "Athletics", "Block"],
                    "Minor skills": ["Armorer", "Spear", "Marksman", "Axe", "Blunt Weapon"],
                    "Spells": ["none"]
                },
                "witchhunter":  {
                    "Description": "Witchhunters are dedicated to rooting out and destroying the perverted practices of dark cults and profane sorcery. They train for martial, magical, and stealthy war against vampires, witches, warlocks, and necromancers.",
                    "Specialization": "Magic",
                    "Attributes": "Intelligence, Agility",
                    "Major skills": ["Conjuration", "Enchant", "Alchemy", "Light Armor", "Marksman"],
                    "Minor skills": ["Unarmored", "Block", "Blunt Weapon", "Sneak", "Mysticism"],
                    "Spells": ["Bound Dagger (for 60 sec on self)", "Summon Ancestral Ghost (for 60 sec on self)"]
                }
            }