from gym.envs.registration import register

register(
    id='CAG-v0',
    entry_point='gym_CAG.envs:CrazyArcadeEnv',
    timestep_limit=1000,
)
