#!/usr/bin/env python3
"""Base environment, packed the original state, act, err.
BaseEnv contains:

    _do_act_get_alive(act)
    _reset()
    _state
    _error
    log(info)
"""
import os
from drlff.environment import ga, io
from drlff.conf import files_output


class BaseEnv(object):
    """Env Base, control parameters basically
    Attrs:
        _log_path

        _ffp
            force field parameters object

        observation_space

        scale_space

    Methods:
        __init__
            set the basic _log_path, _ffp, observation_space, and scale_space

        _do_act_get_alive
            Adds a list of delta parameters to force field parameters, and return the alive

            Inputs:
                act:
                    list, same shape as scale_space

            Returns:
                _alive:
                    bool, returns False if there is one or more param out of the range described in observation_space

        _reset
            reset ffield, and ffield is placed in the '.bak' folder.

        _get_state
            Returns:
                _state:
                    A list of the parameters.

        _get_error
            Returns:
                _error:
                    error calculated by GARFField

        log
            Inputs:
                info:
                    anything wanna log to the _log_path"""

    def __init__(self):
        super(BaseEnv, self).__init__()

        self._log_path = os.path.join(files_output['log'], 'drlff.log')

        self._ffp = io.main()
        self.observation_space = self._ffp.range
        self.scale_space = tuple(map(lambda x: x[1] * (x[0][1] - x[0][0]), zip(self.observation_space, self._ffp.scale)))

    def _do_act_get_alive(self, act):
        self._alive_ = self._ffp + act
        return self._alive_

    def _apply_params_get_error(self, params):
        self._ffp.value = params
        return ga.run()

    def _reset(self):
        self._ffp.reset()

    @property
    def _state(self):
        self._state_ = self._ffp.value
        return self._state_

    @property
    def _error(self):
        self._error_ = ga.run()
        return self._error_

    def log(self, info=None):
        with open(self._log_path, 'a') as f:
            f.write(str(info) + '\n')