import gym
from gym import spaces
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


env = gym.make('CarRacing-v0')

frames = []
rewards = []
tiles_visited = []
track_length = []


for i_episode in range(1):
    observation = env.reset()
    turn_angle = 0.

    for frame in range(5000):
        env.render()

        if frame % 3 == 0:
            action = [turn_angle, 0, 0.1] #spaces.Box(0, 1, 0) # env.action_space.sample() # steer, gas, brake
        else:
            action = [turn_angle, 0.1, 0] #spaces.Box(0, 1, 0) # env.action_space.sample() # steer, gas, brake

        observation, reward, done, info = env.step(action)

        # if frame%25 == 0:
        #     obs = plt.imshow(observation)
        #     figure = obs.get_figure()
        #     figure.savefig(('baseline_imgs//{}_original.jpg').format(frame))
        #     figure.clf()

        # grayscale the state map
        observation_gray = 0.33 * observation[:,:,0] + 0.33 * observation[:,:,1] + 0.33 * observation[:,:,2]

        # if frame%25 == 0:
        #     obs = plt.imshow(observation_gray)
        #     figure = obs.get_figure()
        #     figure.savefig(('baseline_imgs//{}_grayscale.jpg').format(frame))
        #     figure.clf()

        # reduce the dimensions to focus only on important areas
        observation_binary = observation_gray < 125

        # if frame%25 == 0:
        #     obs = plt.imshow(observation_binary)
        #     figure = obs.get_figure()
        #     figure.savefig(('baseline_imgs/{}_binary.jpg').format(frame))
        #     figure.clf()

        observation_cropped = observation_binary[60:80, 20:70]

        # if frame%25 == 0:
        #     obs = plt.imshow(observation_cropped)
        #     figure = obs.get_figure()
        #     figure.savefig(('baseline_imgs//{}_cropped.jpg').format(frame))
        #     figure.clf()

        # start turning once intro view is complete
        if frame > 25:
            if np.sum(observation_cropped[:, :20]) > 100:
                turn_angle = -0.3
            elif np.sum(observation_cropped[:, 30:]) > 100:
                turn_angle = .3
            else:
                turn_angle = 0.

        if done:
            print('-----------------')
            print(frame + 1, env.reward, env.tile_visited_count, len(env.track) + 1)
            frames.append(frame + 1)
            rewards.append(env.reward)
            tiles_visited.append(env.tile_visited_count)
            track_length.append(len(env.track) + 1)
            break

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(np.average(np.array(frames)))
print(np.min(np.array(frames)))
print(np.max(np.array(frames)))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print(np.average(np.array(rewards)))
print(np.min(np.array(rewards)))
print(np.max(np.array(rewards)))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print(np.average(np.array(tiles_visited)))
print(np.min(np.array(tiles_visited)))
print(np.max(np.array(tiles_visited)))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print(np.average(np.array(track_length)))
print(np.min(np.array(track_length)))
print(np.max(np.array(track_length)))

env.close()