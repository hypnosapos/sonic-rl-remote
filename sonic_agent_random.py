import retro


def main():
    env = retro.make(game='SonicTheHedgehog-Genesis', state='GreenHillZone.Act1')
    obs = env.reset()
    while True:
        env.render()
        #action = env.action_space.sample()
        #print(action)
        # B, A, MODE, START, UP, DOWN, LEFT, RIGHT, C, Y, X, Z
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        obs, rew, done, info = env.step(action)
        action = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        obs, rew, done, info = env.step(action)
        print(info)
        if done:
            obs = env.reset()


if __name__ == '__main__':
    main()
