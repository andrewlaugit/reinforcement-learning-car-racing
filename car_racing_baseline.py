import gym
from gym import spaces
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


env = gym.make('CarRacing-v0')

for i_episode in range(15):
    observation = env.reset()
    turn_angle = 0.

    for frame in range(5000):
        env.render()

        if frame % 3 == 0:
            action = [turn_angle, 0, 0.1] #spaces.Box(0, 1, 0) # env.action_space.sample() # steer, gas, brake
        else:
            action = [turn_angle, 0.1, 0] #spaces.Box(0, 1, 0) # env.action_space.sample() # steer, gas, brake

        observation, reward, done, info = env.step(action)

        if frame%25 == 0:
            obs = plt.imshow(observation)
            figure = obs.get_figure()
            figure.savefig(('blah_1_{}.jpg').format(frame))
            figure.clf()

        # grayscale the state map
        observation_gray = 0.33 * observation[:,:,0] + 0.33 * observation[:,:,1] + 0.33 * observation[:,:,2]

        # reduce the dimensions to focus only on important areas
        observation_gray = observation_gray[:80, :]
        observation_gray = observation_gray < 125

        # start turning once intro view is complete
        if frame > 25:
            if np.sum(observation_gray[60:, 20:40]) > 100:
                turn_angle = -0.3
            elif np.sum(observation_gray[60:, 50:70]) > 100:
                turn_angle = .3
            else:
                turn_angle = 0.

        # if t%25 == 0:
        #     # plt.plot(observation_gray)
        #     obs = sn.heatmap(observation_gray)
        #     figure = obs.get_figure()
        #     figure.savefig(('blah_1_{}.jpg').format(t))
        #     figure.clf()

        if done:
            print('-----------------')
            print(frame, env.reward)
            print('tiles visited', env.tile_visited_count)
            print('track length', len(env.track))
            break

env.close()