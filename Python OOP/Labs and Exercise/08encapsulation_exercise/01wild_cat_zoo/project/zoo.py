class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{self.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{self.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w == worker_name][0]
        except IndexError:
            return f"There is no {worker_name} in the zoo"
        return f"{worker_name} fired successfully"



    def pay_workers(self):
        money_to_pay = sum([w.salary for w in self.workers])

        if money_to_pay <= self.__budget:
            self.__budget -= money_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_to_feed = sum([a.money_for_car for a in self.animals])

        if money_to_feed <= self.__budget:
            self.__budget -= money_to_feed
            return f"You tended all the animals. They are happy. Budget left: {money_to_feed}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        amount_of_lion = len(lions)
        result += f"----- {amount_of_lion} Lions:\n"
        for lion in lions:
            result += f"{lion}/n"

        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        amount_of_tiger = len(tigers)
        result += f"----- {amount_of_tiger} Tigers:\n"
        for tiger in tigers:
            result += f"{tigers}/n"

        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetahs"]
        amount_of_cheetahs = len(cheetahs)
        result += f"----- {amount_of_cheetahs} Lions:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}/n"

        return result

    def worker_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [w for w in self.workers if w.__class__.__name__ == "Keepers"]
        caretaker = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            result += f"{k}\n"

        result += f"----- {len(caretaker)} Caretaker:\n"
        for c in caretaker:
            result += f"{c}\n"

        result += f"----- {len(vets)} Keepers:\n"
        for v in vets:
            result += f"{v}\n"

        return result

