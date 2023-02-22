import numpy as np

def periodic(coord, box):
    if abs(coord) > 0.5 * box:
        return coord - np.sign(coord) * box
    return coord


class Box():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def periodic_correct(self, xb, yb, zb):
        xb = periodic(xb, self.x)
        yb = periodic(yb, self.y)
        zb = periodic(zb, self.z)
        return xb, yb, zb
    
class Ring:
    def __init__(self, num_beads, length_bond):
        self.num_beads = num_beads
        self.lenth_bond = length_bond
        self.radius = length_bond / (2*np.sin(np.pi/num_beads))
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
    length_chain = 100
    length_bond = 0.69336
    ring = Ring(num_beads=length_chain, length_bond=length_bond)
    box_size = 2*ring.radius + 2
    box = Box(box_size, box_size, box_size)
    num_atoms = int(box.x * box.y * box.z * 3)
    num_solvent = num_atoms - length_chain
    x,y,z = ring.get_coordinates()
    bonds = ring.get_bonds()
    num_bonds = len(bonds)
    
    fcoord = open('COORD', 'w')
    fbonds = open('BONDS', 'w')
    fcoord.write(f'num_atoms {num_atoms} box_size {box.x} {box.y} {box.z}\n')
    fbonds.write(
        f'num_bonds {num_bonds} num_atoms {num_atoms} box_size {box.x} {box.y} {box.z}\n')
    temp = 0
    for x_b,y_b,z_b in zip(x, y, z):
        temp += 1
        fcoord.write(f'{temp: <10} {x_b: <25} {y_b: <25} {z_b: <25} 1\n'.format(temp, x_b, y_b, z_b))
    for i in range(num_bonds):
            fbonds.write(f'{bonds[i][0]} {bonds[i][1]}\n')
    fbonds.close()
    x_s = np.random.uniform(-box.x/2, box.x/2, num_solvent)
    y_s = np.random.uniform(-box.y/2, box.y/2, num_solvent)
    z_s = np.random.uniform(-box.z/2, box.z/2, num_solvent)
    for x, y, z in zip(x_s, y_s, z_s):
        temp += 1
        fcoord.write(
            f'{temp: <10} {x: <25} {y: <25} {z: <25} 3\n'.format(x, y, z, temp))
    fcoord.close()