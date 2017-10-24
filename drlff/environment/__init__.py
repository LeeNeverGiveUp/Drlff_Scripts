#!/usr/bin/env python3
"""Usage:
from drlff import environment
env = environment.make('SimpleEnv')

or:
env = environment.make('DDPGEnv', limits=0.2, step_size=0.05)

To get available ENVs, run:
environment.env_list()"""
from drlff.environment.envs import make, env_list