import minedojo

env = minedojo.make(task_id="harvest_milk", image_size=(160, 256))
print(env.task_prompt)
print(env.task_guidance)


obs = env.reset()
print("after reset")
obs_space = env.observation_space
print(not obs_space["rgb"])
