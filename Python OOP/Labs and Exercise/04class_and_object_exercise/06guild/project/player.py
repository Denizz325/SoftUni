class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_coast: int) -> str:
        if skill_name in self.skills.keys():
            return "Skill already added"

        self.skills[skill_name] = mana_coast
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        skill_print = "\n".join(f"==={skill} - {mana}" for skill, mana in self.skills.items())
        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{skill_print}"
