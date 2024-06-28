class Tier:
    def __init__(self, name, alter, geschlecht, art):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht
        self.art = art

    def __str__(self):
        return "Tier(name " + self.name + ",alter " + str(self.alter) + ",geschlecht"  + self.geschlecht + ",art" + self.art + ")"


class Zoo:
    def __init__(self):
        self.tiere = []

    def add_tier(self,tier):
        self.tiere.append(tier)

    def get_tier_by_geschlecht(self, geschlecht):
        found_tiere = []
        for index in range(len(self.tiere)):
            tier = self.tiere[index]
            if tier.geschlecht == geschlecht:
                found_tiere.append(tier)

        print("found following tiere:")
        for found_tier in found_tiere:
            print(str(found_tier))

    def get_tier_by_art(self, art):
        found_tiere = []

        for tier in self.tiere:
            if tier.art == art:
                found_tiere.append(tier)

        print("found following tiere:")
        for found_tier in found_tiere:
            print(str(found_tier))


if __name__ == "__main__":
    zoo = Zoo()
    zoo.add_tier(Tier("Leo", 5, "männlich", "Löwe"))
    zoo.add_tier(Tier("Manfred", 20, "männlich", "Elefant"))
    zoo.add_tier(Tier("Hilde", 30, "weiblich", "Elefant"))
    for tier in zoo.tiere:
        print(str(tier))

    #zoo.get_tier_by_geschlecht("weiblich")
    zoo.get_tier_by_art("Löwe")