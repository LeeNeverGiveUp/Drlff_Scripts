#!/usr/bin/env python3
"""Use make to get environment instance, just like OpenAI gym
Usage:
    act = 0     # Just for test, do the "0" act
    from drlff import environment
    env = environment.make('SimpleEnv')
    env.reset()
    state, reward, done = env.step(act)

To lookup env list, use:
    environment.envs_list()
"""
from drlff.environment.envs import envs

ENVS_LIST = ['BaseEnv', 'SimpleEnv', 'DDPGEnv']


def env_list():
    return ENVS_LIST


def make(name='', *args, **kwargs):
    '''Return an object of selected ENV and send args and kwargs to the ENV.
    '''
    if name not in ENVS_LIST:
        raise IndexError('Did not found in ENVS_LIST: ' + name + '\nENVS_LIST: [' + ', '.join(ENVS_LIST) + ']')

    return getattr(envs, name)(*args, **kwargs)