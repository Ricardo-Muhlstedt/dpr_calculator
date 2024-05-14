import math as math

class rogue:
    n_actions = 1
    n_bonus_actions = 1
    n_reactions = 1
    weapon_damage_die = 8
    sneak_attack_die = 6

    def __init__(self):
        lvl = int(input("Enter lvl (1-20): "))
        if lvl <= 0 or lvl > 20:
            raise ValueError("Level must be between 1 and 20")
        dex =  int(input("Enter dexterity (1-20): "))
        if dex <= 0 or dex > 20:
            raise ValueError("Dexterity must be between 1 and 20")
        self.lvl = lvl
        self.dex = dex
        self.check_ability_improvement()
        self.n_sneak_attack_die = self.calculate_n_sneak_attack_die()
        self.dex_modifier = self.calculate_dex_modifier()
        self.proficiency_bonus = self.calculate_proficiency_bonus()
        self.damage_weapon = self.calculate_damage_weapon()
        self.damage_sneak = self.calculate_damage_sneak()
        self.base_damage = self.calculate_base_damage()
        self.enemy_ac = self.calculate_enemy_ac()
        self.attack_bonus = self.calculate_attack_bonus()
        self.hit_chance =  self.calculate_hit_chance()
    

    def calculate_proficiency_bonus(self):
        return (self.lvl - 1) // 4 + 2

    def calculate_dex_modifier(self):
        return self.dex - 10 // 2
    
    def calculate_enemy_ac(self):
        if self.lvl <= 3:
            return 13
        elif self.lvl == 4:
            return 14
        elif 5 <= self.lvl <= 7:
            return 15
        elif 8 <= self.lvl <= 9:
            return 16
        elif 10 <= self.lvl <= 12:
            return 17
        elif 13 <= self.lvl <= 16:
            return 18
        else:
            return 19
        
    def check_ability_improvement(self):

        def choice_af(choice):
            while choice not in ['a', 'f']:
                choice = input("Invalid choice. Choose A for ability score improvement or F for feat: ").strip().lower()
            return choice
        
        def dex_check(self, choice):
            choice = choice_af(choice)

            if choice == 'a' and self.dex < 20:
                self.increase_dexterity(self)
                print("You chose ability score improvement.")
            elif choice == 'a' and self.dex >= 20:
                while choice == 'a':
                    print("Your ability score is already maxed")
                    choice = input("Choose A for ability score improvement or F for feat: ").strip().lower()
                print("You chose feat.")

        improvement_levels = [4, 8, 10, 12, 16, 19]
        for level in improvement_levels:
            if self.lvl >= level:
                choice = input(f"At level {level}, choose ability score improvement (A) or feat (F): ").strip().lower()
                dex_check(self, choice)
            else:
                break
    
    def increase_dexterity(self):
        self.dex += 1

    def calculate_attack_bonus(self):
        return self.dex_modifier + self.proficiency_bonus
    
    def calculate_hit_chance(self):
        return 1 - ((self.enemy_ac - self.attack_bonus) / 20)
    
    def calculate_n_sneak_attack_die(self):
        if self.lvl == 1:
            return 1
        else:
            return math.ceil(self.lvl / 2)
        
    def calculate_damage_weapon(self):
        return (sum(range(1, self.weapon_damage_die + 1)) / self.weapon_damage_die)
    
    def calculate_damage_sneak(self):
        return (sum(range(1, self.sneak_attack_die+ 1))) / (self.sneak_attack_die) * self.n_sneak_attack_die 

    def calculate_base_damage(self):
        return (self.damage_weapon + self.damage_sneak)
    
    def sneak_attack(self):
        if (self.n_actions > 0):
            self.n_actions = self.n_actions - 1
            dpr = round(0.05 * (self.base_damage) + self.hit_chance * (self.base_damage + self.dex_modifier + self.proficiency_bonus), 2)
            return print("average damage per round: " + str(dpr)) 
        else:
            return print("failed")

               
p1 = rogue()

p1.sneak_attack()

print("actions remaining: " + str(p1.n_actions) + 
      "\nbonus actions remaining: " + str(p1.n_bonus_actions) +
      "\nability score: " + str(p1.dex))