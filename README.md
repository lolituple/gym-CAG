# gym-CAG

# attention 

不要把该文件放在非英文路径下!

需要tkinter, opencv, numpy, gym库的支持

# Installation

在gym-CAG-master文件目录的命令行中运行

```bash
pip install -e .
```

# Quick example

```python
import gym
import gym_CAG

env = gym.make('CAG-v0')
env.reset()

for _ in range(50):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
env.close()


```
