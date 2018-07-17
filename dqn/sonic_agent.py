from keras.layers import *
from keras.models import Sequential
from keras.optimizers import Adam
from runner import GymRunner

from dqn.qlearning_agent import QLearningAgent


class Agent(QLearningAgent):
    def __init__(self):
        super().__init__(4)

    def build_model(self):

        n_actions = self.action_size
        n_frames = 4
        width_size = 224
        height_size = 320

        model = Sequential()
        model.add(
            Conv2D(32, (5, 5), strides=(4, 4), activation='relu', padding='same', input_shape=(n_frames, width_size, height_size), data_format='channels_first'))

        model.add(Dropout(0.2))

        model.add(Conv2D(32, (3, 3), strides=(2, 2), activation='relu', padding='same', data_format='channels_first'))

        model.add(Dropout(0.2))

        model.add(Conv2D(32, (3, 3), strides=(2, 2), activation='relu', padding='same', data_format='channels_first'))

        model.add(Dropout(0.3))

        model.add(Conv2D(64, (3, 3), strides=(2, 2), activation='relu', padding='same', data_format='channels_first'))

        model.add(Flatten())

        model.add(BatchNormalization())

        model.add(Dense(256, activation='relu'))

        model.add(Reshape((256, 1)))

        model.add(LSTM(256))

        model.add(Dense(n_actions, activation='softmax'))

        print(model.summary())

        model.compile(Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

        # load the weights of the model if reusing previous training session
        # model.load_weights("models/mario-v0.h5")

        return model


if __name__ == '__main__':
    gym = GymRunner()
    agent = Agent()

    gym.train(agent, 100000)
    gym.run(agent, 5000)
