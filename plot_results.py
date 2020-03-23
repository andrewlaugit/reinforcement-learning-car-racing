import numpy as np
import matplotlib.pyplot as plt

def plot():
    plt.figure()
    durations = np.loadtxt('./racing_RGB_training_results.csv', delimiter=',')
    plt.title('Car Racing training results')
    plt.xlabel('Episode')
    plt.ylabel('Duration')
    plt.plot(durations[:], label='Episode result')

    # Take 100 episode averages and plot them too
    mean = np.zeros(durations.shape[0])
    for i in range(0, len(durations)-100):
        mean[i+100] = np.mean(durations[i : i +100])
    plt.plot(mean, label='Mean for past 100 episodes')

    # plt.annotate(' Solved\nProblem', xy=(138, 195.5), xytext=(129, 450), arrowprops=dict(facecolor='black', headwidth=10, width=2))
    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot()