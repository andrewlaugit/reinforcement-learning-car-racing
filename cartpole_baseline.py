import gym
import numpy as np

env = gym.make('CartPole-v0')

length = []
for i_episode in range(100):
    observation = env.reset()

    for t in range(1000):
        env.render()

        # move right if pole is tilted right
        if observation[2] > 0:
            action = 1
        # move left if pole is tilted left
        else:
            action = 0

        observation, reward, done, info = env.step(action)

        # done is defined as when the cart get out of the frame or passes 14 degrees in either direction
        if done:
            print("episode:", i_episode, " ended after", t)
            length.append(t)
            break

# get the results
print(np.average(np.array(length)))
print(np.min(np.array(length)))
print(np.max(np.array(length)))

env.close()