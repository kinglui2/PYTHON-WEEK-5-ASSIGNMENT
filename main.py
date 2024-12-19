# Parent class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours

    def power_on(self):
        return f"{self.model} is powering on..."

    def power_off(self):
        return f"{self.model} is powering off..."

    def show_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours"


# Child class: GamingSmartphone (inherits from Smartphone)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu, refresh_rate):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu  # Graphics Processing Unit for gaming
        self.refresh_rate = refresh_rate  # in Hz

    def power_on(self):
        return f"{self.model} is powering on with gaming mode activated!"

    def show_specs(self):
        basic_specs = super().show_specs()
        return f"{basic_specs}, GPU: {self.gpu}, Refresh Rate: {self.refresh_rate}Hz"

    def play_game(self, game):
        return f"Playing {game} on {self.model} with smooth graphics and high FPS!"


# Child class: FoldableSmartphone (inherits from Smartphone)
class FoldableSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, fold_type):
        super().__init__(brand, model, storage, battery_life)
        self.fold_type = fold_type  # e.g., horizontal, vertical

    def power_on(self):
        return f"{self.model} is powering on, and it's in {self.fold_type} mode."

    def show_specs(self):
        basic_specs = super().show_specs()
        return f"{basic_specs}, Fold Type: {self.fold_type}"

    def fold_phone(self):
        return f"Folding {self.model} into {self.fold_type} mode."


# Creating objects of each class
basic_phone = Smartphone("Samsung", "Galaxy A13", 64, 20)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 128, 18, "Adreno 660", 144)
foldable_phone = FoldableSmartphone("Samsung", "Galaxy Z Flip 5", 256, 22, "horizontal")

# Calling methods on each object
print(basic_phone.show_specs())
print(basic_phone.power_on())
print("")

print(gaming_phone.show_specs())
print(gaming_phone.play_game("PUBG"))
print(gaming_phone.power_on())
print("")

print(foldable_phone.show_specs())
print(foldable_phone.fold_phone())
print(foldable_phone.power_on())
