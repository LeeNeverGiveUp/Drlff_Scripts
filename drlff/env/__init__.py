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
    # [0, 2*len]
    act = int(act) - len(scale_space)
    if abs(act) > len(scale_space):
        raise ValueError('act out of range of %d' % len(scale_space))
    action = np.zeros(len(scale_space))
    if act != 0:
        action[abs(act) - 1] = np.sign(act)
    return action * scale_space


def step(act):
    alive = ffp + act_parser(act)
    state = ffp.value
    reward = ga.run()
    print(state, reward, alive)
    with open('/tmp/drlff.log', 'a') as f:
        f.write(str((state, reward, alive)) + '\n')

    return state, reward, 1-alive


def reset():
    ffp.reset()
    state = ffp.value
    alive = True
    reward = ga.run()
    with open('/tmp/drlff.log', 'a') as f:
        f.write('reseted\n')

    return state, reward, 1-alive


def render():
    return
    with open('/tmp/drlff.log', 'a') as f:
        f.write(str(step(0)) + '\n')
