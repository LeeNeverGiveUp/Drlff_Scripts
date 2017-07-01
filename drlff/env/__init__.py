from drlff.env import ga, io
import numpy as np

ffp = io.main()
observation_space = ffp.range
action_space = ffp.scale


def act_parser(act):
    # [-len, len]
    act = int(act)
    if abs(act) > len(action_space):
        raise ValueError('act out of range of %d' % len(action_space))
    action = np.zeros(len(action_space))
    if act != 0:
        action[abs(act) -1] = sign(act)
    return action * action_space


def step(act):
    alive = ffp + act_parser(act)
    state = ffp.value
    reward = ga.run()

    return state, reward, alive


def reset():
    ffp.reset()
    alive = True
    reward = ga.run()

    return state, reward, alive
