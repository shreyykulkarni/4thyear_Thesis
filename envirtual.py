# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:09:33 2021

@author: Atharv Kulkarni
"""
import numpy as np
import time


# State transition has been done in the class constructor
    
class env():
    def __init__(self, actions_list, states_list, input_state):
        
        # Initializing all state variables
        self.reward = 0
        self.states_list = [['F','R','L','S'],['No class detected','Right class', 'Left class', 'Stop class']]
        self.actions_list = ['F', 'R', 'L', 'S']
        
        self.input_state = ['No class detected','F']
        self.initial_class = self.input_state[0]
        self.initial_v = self.input_state[1]
        
        self.current_v = self.input_state[1] 
        self.previous_v = self.current_v
        self.no_class = 'No class detected'
        self.right_class = 'Right class'
        self.left_class = 'Left class'
        self.stop_class = 'Stop class'
        
        self.current_class = self.input_state[0]
        self.previous_class = self.current_class
    
        self.previous_action = None
        

        # Rewards directory
        self.reward_dir = {'Correct action':10, 'Incorrect action':-1}
    
    
    '''MOTOR FUNCTIONS'''
    
    def foward(self, action):
        
        return 'F'
    
    
    def stop(self, action):

        return 'S'
    
    
    def right(self, action):

        return 'R'
    
    
    def left(self, action):

        return 'L'
        
    
    
    
    def action_description(self, action, velocity=None):

        if velocity is None:
            velocity = self.current_v
        
            
        # Descriptions
        if action == self.actions_list[0]:
            velocity = self.foward(action)

        elif action == self.actions_list[3]:
            velocity = self.stop(action)
        
        elif action == self.actions_list[1]:
            velocity = self.right(action)
        
        elif action == self.actions_list[2]:
            velocity = self.left(action)
        
        return velocity
    
    
    
    
    def reward_function(self, action,img_class, reward=None):
        
        img_class = self.current_class
        
        if reward == None:
            reward = self.reward
            
        if self.current_class == self.no_class:
            if action == self.actions_list[0]:
                reward = self.reward_dir['Correct action']
            else:
                reward =self.reward_dir['Incorrect action']
                
        if self.current_class == self.right_class:
            if action == self.actions_list[1]:
                reward = self.reward_dir['Correct action']
            else:
                reward =self.reward_dir['Incorrect action']
        
        if self.current_class == self.left_class:
            if action == self.actions_list[2]:
                reward = self.reward_dir['Correct action']
            else:
                reward =self.reward_dir['Incorrect action']
                
        if self.current_class == self.stop_class:
            if action == self.actions_list[3]:
                reward = self.reward_dir['Correct action']
            else:
                reward =self.reward_dir['Incorrect action']
            
        return reward

    

    
    def class_selection(self):
        A = [0,1,2,3]
        B = np.random.choice(A)
        
        if B == 0:
            self.current_class = self.right_class
            
        if B == 1:
            self.current_class = self.left_class
            
        if B == 2:
            self.current_class = self.stop_class
            
        if B == 3:
            self.current_class = self.no_class
        
        return self.current_class
    
    
    def state_transition(self, action,current_class=None, reward=None):
        # You essentially use this function to input an action and end up in a different state
        # Previous state becomes current at the end, and next state becomes current
        
        if reward == None:
            reward = self.reward
           
        self.previous_action = action
        self.previous_v = self.current_v
        self.previous_class = self.current_class
        self.previous_reward = reward
        print('Previous reward:',self.previous_reward)
        # Transition to new state
        self.current_v = self.action_description(self.previous_action)
        self.current_class = self.class_selection() 
        self.reward = self.reward_function(action,self.current_class)
        print('Next reward:',self.reward)
        diff = self.reward 
        
        if  diff < 0:
            done = True
        else:
            done = False
            
        return [self.current_v, self.current_class], reward, done
    # Issue with current class. What to represent
    
    
    
# WHEN DO YOU RESET A FUNCTION        
    def reset(self):
        # if reward_function(action) == self.reward_dir['Incorrect action']:
        current_class, current_v = self.current_class, self.current_v
        return [current_v, current_class]
    
    
    
    def env_space(self):
        action_space = self.actions_list
        state_space = [self.current_v, self.current_class]
        return [action_space, state_space]





# Observe that self.reward has self.previous_reward as an input.
# This way self.reward inout for the reward function is not zero. 
# And in case the agent makes more than correct decision at once, the rewards are summed.


    
    
    
        
        