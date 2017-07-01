"""ga envirenment, showes the state, reward, alive info to a deep reinforcement agent.
Functions:
    step(act) -> state, reward, alive
    reset() -> state, reward, alive

Attr:
    alive: if it's failed, if not fail, alive == True.
    action_space
    observation_space
"""
from drlff.env import ga, io
import numpy as np

ffp = io.main()
observation_space = ffp.range
scale_space = ffp.scale
action_space = tuple(range(-len(scale_space), len(scale_space)+1))


def act_parser(act):
    # [-len, len]
    act = int(act)
    if abs(act) > len(scale_space):
        raise ValueError('act out of range of %d' % len(scale_space))
    action = np.zeros(len(scale_space))
    if act != 0:
        action[abs(act) - 1] = sign(act)
    return action * scale_space


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
