
# There are 60 trials in total, with visual stimulus flashing from 1 to 4 times, and audio stimulus ranging from 0 to 4 times, with 3 trials* each condition.
# Illusion trials: 1 flash ~ x beeps (2<=x<=4);
# Control trials: x flashes ~ x beeps (2<=x<=4), and x flashes~0 beep (2<=x<=4);


import expyriment;
import numpy as np;
from expyriment.misc import constants as constants;

#time in millisecond
audio_duration=7;
visual_duration=17;
#gap between beeps
gap_audio=57;
#number of beeps for illusion trials
beeps_illusion_trials=[2,3,4];
#gap between flashes
gap_visual=50;

#intial gap between the 1st beep and the 1st flash
gap_onset_visual_audio=23-audio_duration

num_total_trials=60
#categoraized into 4 types*3 conditions/type*5 trials/condition  for coding convenience:
#one_flash_x_beeps,x_flash_1_beeps, x_flash_0_beeps,x_flashes_x_beeps
type_of_trials=4;

exp = expyriment.design.Experiment(name="First Experiment");
expyriment.control.initialize(exp);

#specify stimuli parameters
stim_visual=expyriment.stimuli.Circle(50, colour=(255,255,255));
stim_visual_absence=expyriment.stimuli.Circle(50, colour=(0,0,0));
stim_audio=expyriment.stimuli.Tone(audio_duration);

#preload stimuli 
stim_visual.preload();
stim_audio.preload();

expyriment.control.start();
# for j in range (1):

#     stim_visual.present()
#     exp.clock.wait(audio_number*(audio_duration+audio_gap))
    
#     for i in range(audio_number):
#         stim_audio.present()
#         exp.clock.wait(audio_gap)    

#each condition is 5 trials, from (60 trials/4 categories)/3 choices for illusion trials
num_trial_per_type=(num_total_trials/type_of_trials);
num_of_trials_per_condition=num_trial_per_type/len(beeps_illusion_trials);



def one_flash_x_beeps(x=0):
    #exp.clock.reset_stopwatch();

    stim_audio.present();
    exp.clock.wait(gap_onset_visual_audio);
    stim_visual.present();
    for i in range(beeps_illusion_trials[x]-1):
        stim_audio.present();
        exp.clock.wait(gap_audio);
def x_flashes_1_beep(x=0):
     stim_audio.present();
     exp.clock.wait(gap_onset_visual_audio);
     for i in range(beeps_illusion_trials[x]):
         stim_visual.present();
         exp.clock.wait(visual_duration);
         #stim_visual_absence.present();
         exp.stimuli.BlankScreen.present();
         exp.clock.wait(gap_visual);
def x_flashes_0_beep(x=0):
     for i in range(beeps_illusion_trials[x]):
         stim_visual.present();
         exp.clock.wait(visual_duration);
         #stim_visual_absence.present();
         exp.stimuli.BlankScreen.present();

         exp.clock.wait(gap_visual);
 
def x_flashes_x_beeps(x=0):
    visual_onset=[];    
    audio_onset=[];
    for i in range(beeps_illusion_trials[x]):
        visual_onset.append(gap_onset_visual_audio+i*(gap_visual +visual_duration));
        audio_onset.append(i*(audio_duration+gap_audio));
    
    exp.clock.reset_stopwatch();

    for i in range(beeps_illusion_trials[x]): 
       # exp.clock.reset_stopwatch()
       while time_count<(visual_onset[-1] or audio_onset[-1]):
            if exp.clock.stopwatch_time()==audio_onset[i]:
                stim_audio.present();
                exp.clock.wait(gap_onset_visual_audio);
            if exp.clock.stopwatch_time()==visual_onset[i]:       
                stim_visual.present();
                exp.clock.wait(visual_duration);
           #expyriment.stimuli.BlankScreen.present()
            #exp.clock.wait(visual_gap)   
            
#list for recording responses         
response_list=[];

#random order of trials          
trial_num=np.arange(num_total_trials);
np.random.shuffle(trial_num);
#
for k in range(num_total_trials):
    #press SPACE to start each trial
    expyriment.stimuli.TextScreen("Press SPACE to start Trial ",str(k)).present();

    #expyriment.stimuli.TextScreen("Trial ", str(k)).present()
    exp.keyboard.wait(constants.K_SPACE);
    trial_condition= trial_num[k];
    
    #illusion trials: one flash multiple beeps
    if trial_condition<(1+num_trial_per_type):
#    for s in range(len(illusion_audio)):
        if trial_condition<(1+1*num_of_trials_per_condition):
            one_flash_x_beeps(0)
        elif trial_condition<(1+2*num_of_trials_per_condition):
            one_flash_x_beeps(1)
        elif trial_condition<(1+3*num_of_trials_per_condition):
            one_flash_x_beeps(2)
    
    # controls
    # multiple flashes, 1 beep or no beep
    elif trial_condition<(1+2*num_trial_per_type):
    #   for s in range(len(illusion_audio)):
        if trial_condition<(1+1*num_of_trials_per_condition):
            x_flashes_1_beep(0);
        elif trial_condition<(1+2*num_of_trials_per_condition):
            x_flashes_1_beep(1);    
        elif trial_condition<(1+3*num_of_trials_per_condition):
            x_flashes_1_beep(2);
            
    elif trial_condition<(1+3*num_trial_per_type):
        if trial_condition<(1+1*num_of_trials_per_condition):
              x_flashes_0_beep(0);
        elif trial_condition<(1+2*num_of_trials_per_condition):
            x_flashes_0_beep(1);
        elif trial_condition<(1+3*num_of_trials_per_condition):
            x_flashes_0_beep(2);
    
         
    #multiple flashes&beeps
    else:
        if trial_condition<(1+1*num_of_trials_per_condition):
            x_flashes_x_beeps(0);
        elif trial_condition<(1+2*num_of_trials_per_condition):
            x_flashes_x_beeps(1);
        elif trial_condition<(1+3*num_of_trials_per_condition):
            x_flashes_x_beeps(2);
    
    # response options
    expyriment.stimuli.TextScreen("How many flashes did you see?", "Please respond by pressing any key from 1~4 on the keyboard").present();

    response, time=exp.keyboard.wait([constants.K_0,constants.K_1,constants.K_2,constants.K_3,constants.K_4]);
    response_list.append(response);
  

expyriment.control.end()
