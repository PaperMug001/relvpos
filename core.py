import math

class RelvPos:
    def __init__(self):
        self.origin = (0, 0)   # starting origin
        self.objects = {}      # store all created objects

    def get_coords(self, name: str):
        if name not in self.objects:
            print(f"Object '{name}' is not defined")
            return None
        return self.objects[name]["coords"]

    def change_origin(self, name: str):
        if name not in self.objects:
            print(f"Object '{name}' is not defined")
            return "Origin not changed"
        self.origin = self.objects[name]["coords"]
        return "Origin set"

    def create_point(self, distance: float, angle: float, name: str, origin_point: str):
        coords = self.get_coords(origin_point)
        origin_point = coords if coords is not None else self.origin


        x0, y0 = self.origin
        angle_rad = math.radians(angle)  # convert to radians
        x = round(x0 + distance * math.cos(angle_rad))
        y = round(y0 + distance * math.sin(angle_rad))

        self.objects[name] = {
            "coords": (x, y),
            "type": "point"
        }
        return f"Point '{name}' created at {(x, y)}"

    def delete_point(self, name: str):
        if name not in self.objects:
            return f"Object '{name}' is not defined"
        self.objects.pop(name)
        return f"Point '{name}' removed"

    def is_overlap(self, p1: str, p2: str) -> bool:
        coords1 = self.get_coords(p1)
        coords2 = self.get_coords(p2)
        if coords1 is None or coords2 is None:
            return False
        return coords1 == coords2
