import numpy as np

class Ring:
    def __init__(self, num_beads, lenth_bond):
        self.num_beads = num_beads
        self.lenth_bond = lenth_bond
        self.radius = lenth_bond / (2*np.sin(np.pi/num_beads))
    def get_bonds(self):
        bonds = []
        for i in range (1, self.num_beads):
            bonds.append([i, i+1])
        bonds.append([1, self.num_beads])
        return bonds
    def get_coordinates(self):
        x = []
        y = []
        z = []
        for i in range(self.num_beads):
            alfa = 2*i*np.pi/self.num_beads
            x.append(self.radius*np.cos(alfa))
            y.append(self.radius*np.sin(alfa))
            z.append(0.0)
        return x,y,z
            
        
if __name__ == '__main__':
    R1 = Ring(5,0.5)
    R2 = Ring(200, 1.0)
    print(R1.get_bonds())
    print(R1.get_coordinates())