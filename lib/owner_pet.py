class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type,owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("The provided owner is not of type Owner.")
            self.owner = owner
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets
    
    def add_pet(self, pet):
        if not isinstance(pet,Pet):
            raise Exception("Invalid pet. Must be an instance of Pet")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
    
