import random
import time

class ObjectFinderAgent:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        self.agent_position = [0, 0]  # Posición inicial
        self.target_position = [random.randint(0, grid_size-1), random.randint(0, grid_size-1)]
    
    def display_grid(self):
        """Muestra la cuadrícula con la posición del agente y el objeto."""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if [i, j] == self.agent_position:
                    print(" A ", end="")  # Agente
                elif [i, j] == self.target_position:
                    print(" O ", end="")  # Objeto
                else:
                    print(" . ", end="")
            print()
        print("\n")

    def move_agent(self):
        """Mueve el agente paso a paso hacia el objetivo."""
        while self.agent_position != self.target_position:
            self.display_grid()
            time.sleep(1)
            
            # Movimiento en dirección al objetivo
            if self.agent_position[0] < self.target_position[0]:
                self.agent_position[0] += 1
            elif self.agent_position[0] > self.target_position[0]:
                self.agent_position[0] -= 1
            elif self.agent_position[1] < self.target_position[1]:
                self.agent_position[1] += 1
            elif self.agent_position[1] > self.target_position[1]:
                self.agent_position[1] -= 1
        
        # Muestra el estado final
        self.display_grid()
        print("¡Objeto encontrado!")

if __name__ == "__main__":
    agent = ObjectFinderAgent()
    agent.move_agent()
