# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 09:47:58 2017

@author: seantab
"""
import numpy as np
import matplotlib.pyplot as plt
import gym



env =gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())