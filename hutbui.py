import random
import time

def interpret_input(percept):
    location, status = percept
    return {'pos': location, 'status': status}

def simple_reflex_agent(percept, rows, cols):
    state = interpret_input(percept)
    if state['status'] == 'DIRTY':
        return 'SUCK'
    
    r, c = state['pos']
    if c % 2 == 0:
        if r < rows - 1:
            return 'MOVE_DOWN'
        elif c < cols - 1:
            return 'MOVE_RIGHT'
    else:
        if r > 0:
            return 'MOVE_UP'
        elif c < cols - 1:
            return 'MOVE_RIGHT'
            
    return 'DONE'

class VacuumEnvironment:
    def __init__(self, rows, cols, grid):
        self.rows = rows
        self.cols = cols
        self.grid = grid
        self.robot_pos = [0, 0]

    def get_percept(self):
        r, c = self.robot_pos
        status = 'DIRTY' if self.grid[r][c] == 1 else 'CLEAN'
        return (list(self.robot_pos), status)

    def execute_action(self, action):
        r, c = self.robot_pos
        if action == 'SUCK':
            self.grid[r][c] = 0
            print(f"Action: SUCK at [{r}, {c}]")
        elif action == 'MOVE_DOWN':
            self.robot_pos[0] += 1
            print(f"Action: MOVE_DOWN to {self.robot_pos}")
        elif action == 'MOVE_UP':
            self.robot_pos[0] -= 1
            print(f"Action: MOVE_UP to {self.robot_pos}")
        elif action == 'MOVE_RIGHT':
            self.robot_pos[1] += 1
            print(f"Action: MOVE_RIGHT to {self.robot_pos}")
        elif action == 'DONE':
            print("Action: DONE")
            return False
        return True

    def display(self):
        for r in range(self.rows):
            row_str = "  "
            for c in range(self.cols):
                val = self.grid[r][c]
                if [r, c] == self.robot_pos:
                    row_str += f"R({val}) "
                else:
                    row_str += f"{val}    "
            print(row_str)

if __name__ == "__main__":
    rows = int(input("Rows: "))
    cols = int(input("Cols: "))
    
    grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
        
    env = VacuumEnvironment(rows, cols, grid)
    print("\nInitial Grid:")
    env.display()
    
    step = 1
    while True:
        time.sleep(1)
        print(f"\nStep {step}")
        percept = env.get_percept()
        action = simple_reflex_agent(percept, rows, cols)
        
        success = env.execute_action(action)
        env.display()
        
        if action == 'DONE' or not success:
            break
        step += 1