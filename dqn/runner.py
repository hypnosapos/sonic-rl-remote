import numpy as np
import retro

from PIL import Image

N_FRAMES = 4
WIDTH_SIZE = 224
HEIGHT_SIZE = 320


class GymRunner:
    def __init__(self, max_timesteps=100000):
        self.env = retro.make(game='SonicTheHedgehog-Genesis', state='GreenHillZone.Act1', scenario="/Users/david.suarez/Work/i+d/sonic-rl/dqn/scenario.json")
        self.max_timesteps = max_timesteps

    def train(self, agent, num_episodes):
        return self.run(agent, num_episodes, do_train=True)

    def run(self, agent, num_episodes, do_train=False):
        for episode in range(num_episodes):

            self.env.reset()

            # Reset does not return image until first action is set.
            frame = np.zeros((WIDTH_SIZE, HEIGHT_SIZE, N_FRAMES), dtype=np.uint8)

            img = Image.fromarray(frame).convert('L').resize((WIDTH_SIZE, HEIGHT_SIZE))

            frame = np.array(img.getdata(), dtype=np.uint8).reshape(WIDTH_SIZE, HEIGHT_SIZE)

            frames = [frame] * N_FRAMES

            state = frames

            total_reward = 0

            for t in range(self.max_timesteps):

                self.env.render()

                action = agent.select_action(state, do_train)

                action_translated = self.translate_action(action)

                # execute the selected action
                next_state, reward, done, _ = self.env.step(action_translated)

                img = Image.fromarray(next_state).convert('L').resize((WIDTH_SIZE, HEIGHT_SIZE))
                img = np.array(img.getdata(), dtype=np.uint8).reshape(WIDTH_SIZE, HEIGHT_SIZE)

                next_state = state
                next_state.append(img)
                next_state.pop(0)

                # record the results of the step
                if do_train:
                    agent.record(state, action, reward, next_state, done)

                total_reward += reward

                state.append(img)
                state.pop(0)

                if done:
                    break

            # train the agent based on a sample of past experiences
            if do_train:
                agent.replay()

            print("episode: {}/{} | score: {} | e: {:.3f}".format(
                episode + 1, num_episodes, total_reward, agent.epsilon))

    def translate_action(self, network_output):
        environment_input = np.ones(12)
        action_key = np.argmax(network_output)

        # [Right + B]
        if action_key == 0:
            environment_input = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        # [Left + B]
        elif action_key == 1:
            environment_input = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        # [Right]
        elif action_key == 2:
            environment_input = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        # [Left]
        elif action_key == 3:
            environment_input = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

        return environment_input



