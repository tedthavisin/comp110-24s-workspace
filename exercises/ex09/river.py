"""File to define River class."""
from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear
__author__ = "730676554"


class River:
    """Makes a river."""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks ages."""
        alive_bears: list[Bear] = []
        alive_fish: list[Fish] = []
        for b in self.bears:
            if b.age <= 3:
                alive_bears.append(b)
        for f in self.fish:
            if f.age <= 5:
                alive_fish.append(f)

        self.fish = alive_fish
        self.bears = alive_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes fish."""
        i: int = 0
        while i < amount:
            self.fish.pop(0)  # removes first index
        return None

    def bears_eating(self) -> None:
        """The bears are eating."""
        for b in self.bears:
            if len(self.fish) > 4:
                i: int = 0
                while i < 3:
                    self.remove_fish
                    b.eat(1)
        return None
    
    def check_hunger(self) -> None:
        """Check the hunger of the bears."""
        full: list[Bear] = []
        for b in self.bears:
            if b.hunger_score > -1:
                full.append(b)
        self.bears = full
        return None
        
    def repopulate_fish(self) -> None:
        """Repopulates the fishies."""
        i: int = 0
        while i < len(self.fish):
            if i % 2 == 0:
                self.fish.append(Fish())
                self.fish.append(Fish())
                self.fish.append(Fish())
                self.fish.append(Fish())
            i += 1
        return None
    
    def repopulate_bears(self) -> None:
        """Repopulates the bears."""
        i: int = 0
        while i < len(self.bears):
            if i % 2 == 0:
                self.bears.append(Bear())
            i += 1
        return None
    
    def view_river(self) -> None:
        """Prints of the river ecosystem."""
        print(f'~~~ Day {self.day}: ~~~')
        print(f'Fish population: {len(self.fish)}')
        print(f'Bear population: {len(self.bears)}')
        return None
            
    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self) -> None:
        """Runs one_river_day 7 times."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i = i + 1
        return None