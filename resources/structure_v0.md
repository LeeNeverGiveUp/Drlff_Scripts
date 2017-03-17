# Module Definatioin #
## 1. ENV wrapper for OpenAi gym ##
This wrapper is for OpenAi gym for testing DQN in a easy way.  
The aim of this wrapper is to make it compatible with LAMMPS Force Field Environment.

### Used APIs: ###
- env.reset()
- env.observation_space.shape[0]
- env.action_space.n
- env.action_space.sample()
- env.step(act) => state, reward, done, message
- env.render()

## 2. LAMMPS Force Field Environment ##
This is a wrapped API for training DQN, similar to OpenAI gym.

### Planned to Implement: ###
- env.reset()
- env.observation_space.shape[0]
- env.action_space.n
- env.action_space.sample()
- **env.step(act) => state, reward, done, message**
- env.render()
- env.play() (a wrapper for step, easier to use in training)
- env.io (json, yaml, LAMMPS compatible force field file)

## 3. DQN Optimizer ##
- 省略

# Process #
```
Init parameters  
for i in epoches:  
	Compute state  
	Judge weather it is done, reset if done else evaluate reward  
	Return state, reward, done, message to DQN  
	Train DQN  
```
