# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:11:40 2021

@author: Atharv Kulkarni
"""
import os
import sys
import numpy as np 
import pandas as pd
from envirtual import env
import itertools
import plotting


class QL():
    def __init__(self, env, action_list, states_list ):
        
        self.alpha = 0.7
        self.epsilon = 0.2
        self.discount_factor = 0.5
        self.num_episodes = 100
        self.num_actions = len(action_list)
        self.states_list = [['F','R','L','S'],['No class detected','Right class', 'Left class', 'Stop class']]
        self.actions_list = ['F', 'R', 'L', 'S']
 
        
    
    def greedy_policy(self, Q, epsilon, num_actions):
        def policy(state):
       
            action_probabilities = np.ones(self.num_actions,
                    dtype = float) * self.epsilon / self.num_actions
                      
            print('THIS IS THE STATE:',state)
            S = self.matrix(state)
            best_action = np.argmax(Q.loc[S])
            # We want index value as input not the column name
            action_probabilities[best_action] += (1.0 - epsilon)
            return action_probabilities
       
        return policy
        # Returns action probabilities




    def qLearning(self,env):

        Q = pd.read_csv (r'C:\Users\Atharv Kulkarni\Downloads\qtable.csv')
        Q = Q.set_index('States')
        

        stats = plotting.EpisodeStats(
            episode_lengths = np.zeros(self.num_episodes),
            episode_rewards = np.zeros(self.num_episodes))    

        A = ['Forward', 'Right', 'Left', 'Stop']
        S = [['F','R','L','S'],['No class detected','Right class', 'Left class', 'Stop class']]  # Note that this is a state list and not representative of a state itself
        I = ['No class detected','F']
        
        
        A = env.env_space
        print(A)
        policy = self.greedy_policy(Q, self.epsilon, A())
           
        
        for i in range(self.num_episodes):
               
            state = env.reset()  
            for t in itertools.count():
                   
                S = self.matrix(state)
                action_probabilities = policy(state)
       
                action = self.actions_list[np.random.choice(np.arange(
                          len(action_probabilities)),
                           p = action_probabilities)]
       
                next_state, reward, done = env.state_transition(action)
                print('NEXT STATE: ',next_state)
                Sf = self.matrix(next_state)
                stats.episode_rewards[i] += reward
                stats.episode_lengths[i] = t
                   
                # Temporal_Difference Update
                best_next_action = Q.columns[np.argmax(Q.loc[Sf])]    
                td_target = reward + self.discount_factor * Q.loc[Sf,best_next_action]
                td_delta = td_target - Q.loc[S,action]
                Q.loc[S,action] += self.alpha * td_delta
       
                # done is True if episode terminated   
                if done is True:
                    break
                       
                state = next_state
                print(Q)
           
        return Q, stats   
    
    
    def matrix(self,state):
        if state == ['F','No class detected']:
            return 'S1'
        
        if state == ['F','Right class']:
            return 'S2'
        
        if state == ['F','Left class']:
            return 'S3'
        
        if state == ['F','Stop class']:
            return 'S4'
        
        if state == ['R','No class detected']:
            return 'S5'
        
        if state == ['R','Right class']:
            return 'S6'
        
        if state == ['R','Left class']:
            return 'S7'
        
        if state == ['R','Stop class']:
            return 'S8'
        
        if state == ['L','No class detected']:
            return 'S9'
        
        if state == ['L','Right class']:
            return 'S10'
        
        if state == ['L','Left class']:
            return 'S11'
        
        if state == ['L','Stop class']:
            return 'S12'
        
        if state == ['S','No class detected']:
            return 'S13'
        
        if state == ['S','Right class']:
            return 'S14'
        
        if state == ['S','Left class']:
            return 'S15'
        
        if state == ['S','Stop class']:
            return 'S16'

