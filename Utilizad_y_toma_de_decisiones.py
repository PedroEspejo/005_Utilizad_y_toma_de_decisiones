import random

# Paso 1: Definición del entorno (simulado como una cuadrícula)
class Environment:
    def __init__(self):
        self.states = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.actions = ["Up", "Down", "Left", "Right"]

    def get_reward(self, state, action):
        # Define las recompensas asociadas a las acciones en el entorno
        rewards = {
            (0, 0): {"Up": -1, "Down": 0, "Left": -1, "Right": 0},
            (0, 1): {"Up": -1, "Down": 0, "Left": 0, "Right": -1},
            (1, 0): {"Up": 0, "Down": -1, "Left": -1, "Right": 0},
            (1, 1): {"Up": 0, "Down": -1, "Left": 0, "Right": -1},
        }
        return rewards[state][action]

# Paso 2: Modelo de Utilidad (valores de utilidad para cada estado)
def create_utility_model():
    return {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}

# Paso 3: Implementación del Agente
class Agent:
    def __init__(self, environment, utility_model):
        self.environment = environment
        self.utility_model = utility_model

    def choose_action(self, state):
        # Implementa la toma de decisiones basada en utilidad (utilizando valores de utilidad)
        actions = self.environment.actions
        random.shuffle(actions)  # Para simular la elección aleatoria
        return max(actions, key=lambda action: self.utility_model[state] + self.environment.get_reward(state, action))

# Paso 4: Entrenamiento y Prueba (simulación)
def train_and_test_agent(agent, environment, utility_model, num_iterations=100):
    for _ in range(num_iterations):
        state = random.choice(environment.states)
        action = agent.choose_action(state)
        reward = environment.get_reward(state, action)
        next_state = random.choice(environment.states)
        # Actualizar el modelo de utilidad (puedes ajustar el valor de aprendizaje)
        learning_rate = 0.1
        utility_model[state] += learning_rate * (reward + utility_model[next_state] - utility_model[state])

# Paso 5: Interfaz de Usuario (Opcional): Puedes implementar una interfaz gráfica si lo deseas.

# Paso 6: Informe: Documenta tus hallazgos y resultados.

# Ejemplo de uso:
if __name__ == "__main__":
    env = Environment()
    utility_model = create_utility_model()
    agent = Agent(env, utility_model)
    
    print("Modelo de utilidad inicial:", utility_model)
    train_and_test_agent(agent, env, utility_model, num_iterations=1000)
    print("Modelo de utilidad después del entrenamiento:", utility_model)
