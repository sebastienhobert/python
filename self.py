class Dog:

    def __init__(self, dogBreed = "German Shepherd", dogEyeColor = "Brown"):

        self.breed = dogBreed
        self.eyeColor = dogEyeColor

tomita = Dog("Fox Terrier", "Yellow")
rex = Dog()

print(tomita.breed, tomita.eyeColor)
print(rex.breed, rex.eyeColor)

