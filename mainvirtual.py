# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:14:11 2021

@author: Atharv Kulkarni
"""
from envirtual import env
from Qvirtual import QL
import plotting


# # Detection
# net = jetson.inference.detectNet("ssd-mobilenet-v1", threshold=0.6)
# num_class = net.GetNumClasses()
# camera = jetson.utils.videoSource("/dev/video0")
# display = jetson.utils.videoOutput()


# Environemnt variables
A = ['F', 'R', 'L', 'S']
S = [['F','R','L','S'],['No class detected','Right class', 'Left class', 'Stop class']]  # Note that this is a state list and not representative of a state itself
I = ['No class detected','F']


environment = env(A,S,I)
rl = QL(environment,A,S)

q_table, statistics = rl.qLearning(environment)
plotting.plot_episode_stats(statistics)
