#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:25:41 2021

@author: xuhuijuan
"""

import expyriment;
import numpy;

audio_duration=100;
audio_gap=57;
stim_variable=[1,2,3,4,5];
visual_gap=50
visual_duration=audio_duration

exp = expyriment.design.Experiment(name="First Experiment")
expyriment.control.initialize(exp)

audio_number=stim_variable[numpy.random.choice(stim_variable)]
visual_number=stim_variable[numpy.random.choice(stim_variable)]
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

#one flash, multiple beeps
if visual_number==1:
    stim_visual.present()
#    exp.clock.wait(visual_duration)
    for i in range(audio_number):
        stim_audio.present()
        exp.clock.wait(audio_gap)
else:
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
