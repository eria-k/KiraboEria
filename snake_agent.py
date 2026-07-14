import random
import pickle
from snake_game import SnakeGame

# =====================================================
# Q-LEARNING PARAMETERS
# =====================================================

LEARNING_RATE = 0.1      # Alpha
DISCOUNT = 0.9           # Gamma

EPSILON = 1.0            # Exploration

EPSILON_DECAY = 0.995

MIN_EPSILON = 0.01

# =====================================================
# Q-TABLE AGENT
# =====================================================

class QLearningAgent:

    def __init__(self):

        self.q_table = {}

        self.epsilon = EPSILON

    # --------------------------------------------------

    def get_q_values(self, state):

        if state not in self.q_table:

            self.q_table[state] = [

                0.0,

                0.0,

                0.0

            ]

        return self.q_table[state]

    # --------------------------------------------------

    def choose_action(self, state):

        if random.random() < self.epsilon:

            return random.randint(0,2)

        q_values = self.get_q_values(state)

        return q_values.index(max(q_values))

    # --------------------------------------------------

    def learn(

        self,

        state,

        action,

        reward,

        next_state,

        done

    ):

        current_q = self.get_q_values(state)

        next_q = self.get_q_values(next_state)

        if done:

            target = reward

        else:

            target = reward + DISCOUNT * max(next_q)

        current_q[action] = current_q[action] + LEARNING_RATE * (

            target - current_q[action]

        )

        self.q_table[state] = current_q

    # --------------------------------------------------

    def decay_epsilon(self):

        if self.epsilon > MIN_EPSILON:

            self.epsilon *= EPSILON_DECAY

    # --------------------------------------------------

    def save(self, filename="best_qtable.pkl"):

        with open(filename,"wb") as f:

            pickle.dump(self.q_table,f)

    # --------------------------------------------------

    def load(self, filename="best_qtable.pkl"):

        with open(filename,"rb") as f:

            self.q_table = pickle.load(f)
# =====================================================
# TRAINING
# =====================================================

def train(render=False, episodes=5000):

    game = SnakeGame(render=render)

    agent = QLearningAgent()

    best_score = 0

    scores = []

    for episode in range(episodes):

        state = game.reset()

        done = False

        score = 0

        while not done:

            action = agent.choose_action(state)

            next_state, reward, done, score = game.step(action)

            agent.learn(

                state,

                action,

                reward,

                next_state,

                done

            )

            state = next_state

        # Decay epsilon ONCE per episode
        agent.decay_epsilon()

        scores.append(score)

        avg_score = sum(scores[-100:]) / len(scores[-100:])

        if score > best_score:

            best_score = score

            agent.save("best_qtable.pkl")

        if (episode + 1) % 100 == 0:

            print(

                f"Episode {episode+1}/{episodes}"

                f" | Score {score}"

                f" | Best {best_score}"

                f" | Avg {avg_score:.2f}"

                f" | Epsilon {agent.epsilon:.3f}"

            )

    agent.save("last_qtable.pkl")

    print("\nTraining Complete!")

    print(f"Best Score : {best_score}")

    print(f"Q-table Size : {len(agent.q_table)}")

    game.close()

    return agent


# =====================================================
# TESTING
# =====================================================

def test(model="best_qtable.pkl", games=5):

    game = SnakeGame(render=True)

    agent = QLearningAgent()

    try:

        agent.load(model)

    except FileNotFoundError:

        print("Model not found.")

        return

    agent.epsilon = 0

    total = 0

    for game_number in range(games):

        state = game.reset()

        done = False

        score = 0

        while not done:

            action = agent.choose_action(state)

            state, reward, done, score = game.step(action)

        total += score

        print(

            f"Game {game_number+1} Score : {score}"

        )

    print()

    print(

        f"Average Score : {total/games:.2f}"

    )

    game.close()


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    print("1 Train")

    print("2 Test")

    choice = input("Choice : ")

    if choice == "1":

        train(

            render=True,

            episodes=5000

        )

    else:

        test()
        