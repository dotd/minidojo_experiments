import minedojo

"""
Action:
MultiDiscrete([  3   3   4  25  25   8 244  36])
https://docs.minedojo.org/sections/core_api/action_space.html


State space
obs["rgb"] - image
https://docs.minedojo.org/sections/core_api/obs_space.html

"""

if __name__ == "__main__":
    env = minedojo.make(
        task_id="combat_spider_plains_leather_armors_diamond_sword_shield",
        image_size=(288, 512),
        world_seed=123,
        seed=42,
    )

    print(f"[INFO] Create a task with prompt: {env.task_prompt}")

    obs = env.reset()
    for _ in range(20):
        print(env.action_space)
        obs, reward, done, info = env.step(env.action_space.no_op())
    env.close()

    print("[INFO] Installation Success")
