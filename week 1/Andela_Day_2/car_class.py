class Car(object):
    def __init__(self, name = "General", model = "GM", type = None):
        self.name = name
        self.num_of_wheels = 4
        self.model = model
        self.type = type
        self.speed = 0
        self.num_of_doors = 4
        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2

        if self.type == "trailer":
            self.num_of_wheels = 8

    def is_saloon(self):

        if self.type != "trailer":
            self.type = "saloon"
        return True



    def drive(self, x):
        if self.type == "trailer":
            self.speed = x * 11
        else:
            self.speed = x * (1000/3.0)

        return self





