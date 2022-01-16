#!/usr/bin/env python3
import glob
import os
for filepath in glob.iglob('./**/*box.txt', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace("002_master_chef_can" , "can")
    s = s.replace("003_cracker_box" , "box")
    s = s.replace("004_sugar_box" , "box")
    s = s.replace("005_tomato_soup_can" , "can")
    s = s.replace("006_mustard_bottle" , "vessel")
    s = s.replace("007_tuna_fish_can" , "can")
    s = s.replace("008_pudding_box" , "box")
    s = s.replace("009_gelatin_box" , "box")
    s = s.replace("010_potted_meat_can" , "can")
    s = s.replace("011_banana" , "banana")
    s = s.replace("019_pitcher_base" , "vessel")
    s = s.replace("021_bleach_cleanser" , "vessel")
    s = s.replace("024_bowl" , "vessel")
    s = s.replace("025_mug" , "vessel")
    s = s.replace("035_power_drill" , "tool")
    s = s.replace("036_wood_block" , "box")
    s = s.replace("037_scissors" , "tool")
    s = s.replace("040_large_marker" , "tool")
    s = s.replace("051_large_clamp" , "tool")
    s = s.replace("052_extra_large_clamp" , "tool")
    s = s.replace("061_foam_brick" , "box")
    with open(filepath, "w") as file:
        file.write(s)
