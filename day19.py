from collections import deque
from math import prod
import re

DEFAULT_INPUT = 'day19.txt'

def day_19(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        blueprints = [list(map(int, re.findall(r'\d+', line))) for line in f.readlines()]
    return sum(blueprint[0] * max_geodes(24, *blueprint[1:]) for blueprint in blueprints), \
           prod(max_geodes(32, *blueprint[1:]) for blueprint in blueprints[:3])

def max_geodes(starting_time: int, ore_cost: int, clay_cost: int,
               obs_cost_ore: int, obs_cost_clay: int,
               geode_cost_ore: int, geode_cost_obs: int) -> int:
    d = deque([(starting_time, 0, 1, 0, 0, 0, 0, 0, 0)])
    seen = set([(0, 1, 0, 0, 0, 0, 0, 0)])
    while d:
        time, ore, ore_bots, clay, clay_bots, obs, obs_bots, geode, geode_bots = d.popleft()
        if time == 0:
            continue
        if ore >= geode_cost_ore and obs >= geode_cost_obs:
            new_state = (ore - geode_cost_ore + ore_bots, ore_bots,
                         clay + clay_bots, clay_bots,
                         obs - geode_cost_obs + obs_bots, obs_bots,
                         geode + geode_bots, geode_bots + 1)
            if new_state not in seen:
                seen.add(new_state)
                d.append((time - 1,) + new_state)
        else:
            if ore >= ore_cost and ore_bots <= max(ore_cost, clay_cost, obs_cost_ore, geode_cost_ore):
                new_state = (ore - ore_cost + ore_bots, ore_bots + 1,
                             clay + clay_bots, clay_bots,
                             obs + obs_bots, obs_bots,
                             geode + geode_bots, geode_bots)
                if new_state not in seen:
                    seen.add(new_state)
                    d.append((time - 1,) + new_state)
            if ore >= clay_cost and clay_bots <= obs_cost_clay:
                new_state = (ore - clay_cost + ore_bots, ore_bots,
                             clay + clay_bots, clay_bots + 1,
                             obs + obs_bots, obs_bots,
                             geode + geode_bots, geode_bots)
                if new_state not in seen:
                    seen.add(new_state)
                    d.append((time - 1,) + new_state)
            if ore >= obs_cost_ore and clay >= obs_cost_clay and obs_bots <= geode_cost_obs:
                new_state = (ore - obs_cost_ore + ore_bots, ore_bots,
                             clay - obs_cost_clay + clay_bots, clay_bots,
                             obs + obs_bots, obs_bots + 1,
                             geode + geode_bots, geode_bots)
                if new_state not in seen:
                    seen.add(new_state)
                    d.append((time - 1,) + new_state)
            new_state = (ore + ore_bots, ore_bots,
                         clay + clay_bots, clay_bots,
                         obs + obs_bots, obs_bots,
                         geode + geode_bots, geode_bots)
            if new_state not in seen:
                seen.add(new_state)
                d.append((time - 1,) + new_state)
    return max(seen, key=lambda blueprint:blueprint[6])[6]

    
if __name__ == '__main__':
    part_1, part_2 = day_19()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
