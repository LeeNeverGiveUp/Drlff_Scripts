#!/usr/bin/env python3
"""All envs, use make method to get wanted environment

Available envs:
    BaseEnv
    SimpleEnv
    DDPGEnv

Attrs:
    action_space
    observation_space
    scale_space

Methods:
    step(act) -> state, reward, done
    reset() -> state, reward, done
    render()
    log(info)
"""
import numpy as np
from functools import reduce
from drlff.environment.envs.base import BaseEnv
from collections import deque


class SimpleEnv(BaseEnv):
    """Sinple Env, uses params as state, discrate act and error as reward"""

    def __init__(self):
        super(SimpleEnv, self).__init__()
        self.action_space = tuple(range(-len(self.scale_space), len(self.scale_space) + 1))

    def get_act(self, act):
        # [-len, len]
        act = int(act) - len(self.scale_space)
        if abs(act) > len(self.scale_space):
            raise ValueError('act out of range of %d' % len(self.scale_space))
        action = np.zeros(len(self.scale_space))
        if act != 0:
            action[abs(act) - 1] = np.sign(act)
        return action * self.scale_space

    def step(self, act):
        alive = self._do_act_get_alive(self.get_act(act))
        state = self._state
        reward = self._error
        print(state, reward, alive)
        self.log(str((state, reward, alive)) + '\n')

        return state, -reward, not alive

    def reset(self, ):
        self._reset()
        state = self._state
        alive = True
        reward = self._error
        self.log('reseted\n')

        return state, -reward, not alive

    def render(self):
        return


class DDPGEnv(BaseEnv):
    """DDPGEnv
    State: gradients
    Act: apply gradient to params
    Reward: -diff(error)"""

    def __init__(self, limits=0.5, step_size=0.1):
        """
        limits: float, (0, 1], percentage of limit of the max step size of an act.
        step_size: float, (0, 1], step size parameger of computing gradient."""
        super(DDPGEnv, self).__init__()
        try:
            limits = abs(float(limits))
        except Exception:
            raise ValueError('limits is not a number: ' + str(limits))

        try:
            step_size = abs(float(step_size))
            if step_size == 0:
                raise Exception
        except Exception:
            raise ValueError('step_size is not a number: ' + str(step_size))

        self.action_space = tuple(map(lambda x: (-x, x), map(lambda x: limits * abs(x[1] - x[0]), self.observation_space)))
        self.step_size = step_size
        self._buffer = dict()
        self._buffer['error'] = deque([self._error] * 2, maxlen=2)

    def _gradient(self):
        base_value = self._ffp.value
        grad = list()
        for i, scale in enumerate(self.scale_space):
            act0, act1 = list(base_value), list(base_value)
            act0[i] += scale * self.step_size
            act1[i] -= scale * self.step_size
            grad.append((self._apply_params_get_error(act0) - self._apply_params_get_error(act1)) / scale)
        self._ffp.value = base_value
        return grad

    def _limit(self, act):
        """limit act to the range of action_space"""
        for i, a in enumerate(act):
            if a > self.action_space[i][1]:
                act[i] = self.action_space[i][1]
            elif a < self.action_space[i][0]:
                act[i] = self.action_space[i][0]
        return act

    def _ddpg_get_reward(self):
        self._buffer['error'].appendleft(self._error)
        return -reduce(lambda x, y: x - y, self._buffer['error'])

    def _ddpg_get_state(self):
        return self._gradient()

    def step(self, act):
        alive = self._do_act_get_alive(self._limit(act))
        state = self._ddpg_get_state()
        reward = self._ddpg_get_reward()
        print(state, reward, alive)
        self.log(str((state, reward, alive)) + '\n')

        return state, reward, not alive

    def reset(self, ):
        self._reset()
        self._buffer['error'] = deque([self._error] * 2, maxlen=2)
        state = self._ddpg_get_state()
        alive = True
        reward = 0
        self.log('reseted\n')

        return state, reward, not alive