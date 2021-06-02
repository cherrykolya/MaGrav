class Polygon:
    # Class describe figures in model
    # points - coordinates (x,y) in which every 
    # connected with next and previous.

    def __init__(self):
        1

    def read_from_json(self, data, p):
        self.Name = 'Polygon ' + str(p)
        self.Points = data['Coordinates']
        self.Density = data['Density']