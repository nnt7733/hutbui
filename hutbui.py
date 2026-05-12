import random, time

def vacuum_agent(sensor, rows, cols):
    position, status = sensor
    if status == 'DIRTY': return 'SUCK'
    r, c = position
    if c % 2 == 0:
        return 'MOVE_DOWN' if r < rows - 1 else ('MOVE_RIGHT' if c < cols - 1 else 'DONE')
    return 'MOVE_UP' if r > 0 else ('MOVE_RIGHT' if c < cols - 1 else 'DONE')

class Environment:
    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols
        self.grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
        self.pos = [0, 0]

    def get_sensor(self):
        r, c = self.pos
        return (list(self.pos), 'DIRTY' if self.grid[r][c] == 1 else 'CLEAN')

    def do_action(self, action):
        r, c = self.pos
        if action == 'SUCK': self.grid[r][c] = 0
        elif action == 'MOVE_DOWN': self.pos[0] += 1
        elif action == 'MOVE_UP': self.pos[0] -= 1
        elif action == 'MOVE_RIGHT': self.pos[1] += 1
        else: return False
        print(f"Action: {action} at {self.pos}")
        return True

    def display(self):
        for r in range(self.rows):
            print("  " + "    ".join(f"R({self.grid[r][c]})" if [r, c] == self.pos else str(self.grid[r][c]) for c in range(self.cols)))

if __name__ == "__main__":
    rs, cs = int(input("Rows: ")), int(input("Cols: "))
    env = Environment(rs, cs)
    print("\nInitial Grid:")
    env.display()
    step = 1
    while True:
        time.sleep(1)
        print(f"\nStep {step}")
        action = vacuum_agent(env.get_sensor(), rs, cs)
        if action == 'DONE' or not env.do_action(action): break
        env.display()
        step += 1