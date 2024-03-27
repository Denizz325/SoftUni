class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude: str):
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
<<<<<<< HEAD
town.set_latitude("42° 41\' 51.fourth_exercise\" N")
=======
town.set_latitude("42° 41\' 51.fourth_ex\" N")
>>>>>>> de306f38a8c64fa7f70c194e8cab08628700344e
town.set_longitude("23° 19\' 26.94\" E")
print(town)
