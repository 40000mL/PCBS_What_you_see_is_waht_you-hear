#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:25:41 2021

@author: xuhuijuan
"""

import expyriment;
import numpy;

audio_duration=7;
audio_gap=57;
stim_variable=[1,2,3,4];
visual_gap=50
visual_duration=17
visual_audio_gap=23
num_of_trials=60
type_of_trials=4

exp = expyriment.design.Experiment(name="First Experiment")
expyriment.control.initialize(exp)

trial_type_num= nympy.random.randint(1,60);

illusion_audio_number=stim_variable[numpy.random.choice(stim_variable[1:]]
stim_visual=expyriment.stimuli.Circle(50, colour=(255,255,255));
stim_visual_absence=expyriment.stimuli.Circle(50, colour=(0,0,0));
stim_audio=expyriment.stimuli.Tone(audio_duration)

#trial.add_stimulus(stimu_visual)¶
#trial.add_stimulus(stimu_audio)¶
stim_visual.preload()
stim_audio.preload()
expyriment.control.start()
# for j in range (1):

#     stim_visual.present()
#     exp.clock.wait(audio_number*(audio_duration+audio_gap))
    
#     for i in range(audio_number):
#         stim_audio.present()
#         exp.clock.wait(audio_gap)    


# 5 trials per condition, 15 illusionary, 45 non-illusionary
for k in range(type_of_trials):
    # illusion trials: one flash, multiple beeps
    if trial_type_num<(1+k*num_of_trial/type_of_trials):
      
        stim_audio.present();
        exp.clock.wait(visual_audio_gap);
        stim_visual.present();
#    ??exp.clock.wait(visual_duration)
        for i in range(illusion_audio_number-1):
            stim_audio.present()
            exp.clock.wait(audio_gap)
    
    #multiple flashes, 1 beep or no beep
    elif trial_type_num<(1+k*num_of_trial/type_of_trials):
        visual_number=stim_variable[numpy.random.choice(stim_variable)]

        stim_audio.present()
        exp.clock.wait(visual_audio_gap)

        for i in range(visual_number):
            stim_visual.present()
            exp.clock.wait(visual_duration)
            stim_visual_absence.present()
            exp.clock.wait(visual_gap)
        
    elif trial_type_num<(1+k*num_of_trial/type_of_trials):
        visual_number=stim_variable[numpy.random.choice(stim_variable)]

        for i in range(visual_number):
            stim_visual.present()
            exp.clock.wait(visual_duration)
            stim_visual_absence.present()
            exp.clock.wait(visual_gap)
        
    #multiple flashes&beeps
    else:
        visual_number=stim_variable[numpy.random.choice(stim_variable)]

        stim_audio.present()
        exp.clock.wait(visual_audio_gap)

        for i in range(visual_number):
            stim_visual.present()
            exp.clock.wait(visual_duration)
            stim_visual_absence.present()
            exp.clock.wait(visual_gap)


       
#one beep, multiple flashes
# if number==1:
#     stim_audio.present()
#    exp.clock.wait(visual_duration)


expyriment.control.end()
