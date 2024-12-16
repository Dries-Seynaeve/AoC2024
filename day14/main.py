width = 11
tall = 7

with open("input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


def get_robot(line):
    line = line.split()
    position = line[0].split("=")[1].split(",")
    velocity = line[1].split("=")[1].split(",")

    r=  Robot(int(position[0]), int(position[1]), \
              int(velocity[0]), int(velocity[1]))
    return r

def parse_input(lines):
    robots = [get_robot(line) for line in lines]
    positions = [r.get_position_after_100s() for r in robots]

    w_half = width // 2
    t_half = tall // 2

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for r in positions:
        if r[0] < w_half:
            if r[1] < t_half:
                q1 += 1
            if r[1] > t_half:
                q2 += 1
        if r[0] > w_half:
            if r[1] < t_half:
                q3 += 1
            if r[1] > t_half:
                q4 += 1
    print(q1, q2, q3, q4)
    return q1*q2*q3*q4
    

class Robot():
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def take_steps(self, n):
        for i in range(n):
            self.take_step()

    def take_step(self):
        self.x += self.vx
        self.y += self.vy

        while self.x < 0:
            self.x += 11
        while self.x >= 11:
            self.x -= 11
        while self.y < 0:
            self.y += 7
        while self.y >= 7:
            self.y -= 7

    def get_position_after_100s(self):
        self.take_steps(100)
        return self.x, self.y

if __name__ == "__main__":
    print(parse_input(lines))