
# There are 60 trials in total, with visual stimulus flashing from 1 to 4 times, and audio stimulus ranging from 0 to 4 times, with 5 trials* each condition.
# Illusion trials: 1 flash x beeps (2<=x<=4);
# Control trials: x flashes x beeps (2<=x<=4),x flashes 1 beep (2<=x<=4), and x flashes 0 beep (2<=x<=4);


import expyriment;
import numpy as np;
from expyriment.misc import constants as constants;

#time is in millisecond
audio_duration=7;
visual_duration=17;
#gap between beeps
gap_audio=57;

#list for number of beeps for illusion trials, same goes with flashes for control trials
num_beeps_options_for_illusion_trials=[2,3,4];
num_flashes_for_control_trials=num_beeps_options_for_illusion_trials;
#gap between flashes
gap_visual=50;

#intial gap between the 1st beep and the 1st flash
gap_onset_visual_audio=23-audio_duration

num_total_trials=60;
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
stim_visual_absence.preload();
stim_audio.preload();

expyriment.control.start();

#each condition is 5 trials, from (60 trials/4 categories)/3 choices for illusion trials
num_trial_per_type=(num_total_trials/type_of_trials);
num_of_trials_per_condition=num_trial_per_type/len(num_beeps_options_for_illusion_trials);



def one_flash_x_beeps(x=0):
    stim_audio.present();
    exp.clock.wait(gap_onset_visual_audio);
    stim_visual.present();
    for i in range(num_beeps_options_for_illusion_trials[x]-1):
        stim_audio.present();
        exp.clock.wait(gap_audio);
    return 1, num_beeps_options_for_illusion_trials[x];

def x_flashes_1_beep(x=0):
     stim_audio.present();
     exp.clock.wait(gap_onset_visual_audio);
     for i in range(num_flashes_for_control_trials[x]):
         stim_visual.present();
         exp.clock.wait(visual_duration);
         stim_visual_absence.present();
         exp.clock.wait(gap_visual);
     return num_flashes_for_control_trials[x],1;

def x_flashes_0_beep(x=0):
     for i in range(num_flashes_for_control_trials[x]):
         stim_visual.present();
         exp.clock.wait(visual_duration);
         stim_visual_absence.present();
         exp.clock.wait(gap_visual);
     return num_flashes_for_control_trials[x], 0;

def x_flashes_x_beeps(x=0):
    visual_onset=[];    
    audio_onset=[];
    #append event onset time seperately for visual and audio stimuli
    for i in range(num_beeps_options_for_illusion_trials[x]):
        visual_onset.append(gap_onset_visual_audio+i*(gap_visual +visual_duration));
        audio_onset.append(i*(audio_duration+gap_audio));
    #reset timer 
    exp.clock.reset_stopwatch();
    #start events in corresponding order, audio first, then wait for the difference between onset time and comes visual, proceed in loop
    for i in range(num_beeps_options_for_illusion_trials[x]):
        stim_audio.present();
        exp.clock.wait(visual_onset[i]-audio_onset[i]);
        stim_visual.present();
        exp.clock.wait(visual_duration);
        stim_visual_absence.present();
        if i<num_beeps_options_for_illusion_trials[x]-1:
            exp.clock.wait(audio_onset[i+1]-visual_onset[i+1]);
 
    return num_flashes_for_control_trials[x], num_beeps_options_for_illusion_trials[x] ;     

#list for recording responses  & correct answers       
response_list=[];
correct_answer=[];
#random order of trials          
trial_num=np.arange(num_total_trials);
np.random.shuffle(trial_num);

for k in range(num_total_trials):
    #press SPACE to start each trial
    expyriment.stimuli.TextScreen("Press SPACE to start Trial ",str(k)).present();

    #expyriment.stimuli.TextScreen("Trial ", str(k)).present()
    exp.keyboard.wait(constants.K_SPACE);
    trial_condition= trial_num[k];
    num_flash,num_beep=0,0;
    #illusion trials: one flash multiple beeps
    if trial_condition<(1+num_trial_per_type):
        if trial_condition<(1+1*num_of_trials_per_condition):
            num_flash,num_beep=one_flash_x_beeps(0);
        elif trial_condition<(1+2*num_of_trials_per_condition):
            num_flash,num_beep=one_flash_x_beeps(1)
        elif trial_condition<(1+3*num_of_trials_per_condition):
            num_flash,num_beep=one_flash_x_beeps(2)

    # controls
    # multiple flashes, 1 beep or no beep
    elif trial_condition<(1+2*num_trial_per_type):
        if trial_condition<(1+1*num_trial_per_type+1*num_of_trials_per_condition):
            num_flash,num_beep=x_flashes_1_beep(0);

        elif trial_condition<(1+1*num_trial_per_type+2*num_of_trials_per_condition):
            num_flash,num_beep=x_flashes_1_beep(1);    
        elif trial_condition<(1+1*num_trial_per_type+3*num_of_trials_per_condition):
            num_flash,num_beep=x_flashes_1_beep(2);

    elif trial_condition<(1+3*num_trial_per_type):
        if trial_condition<(1+2*num_trial_per_type+2*num_of_trials_per_condition):
            num_flash,num_beep=x_flashes_0_beep(0);
        elif trial_condition<(1+2*num_trial_per_type+2*num_of_trials_per_condition):
            num_flash,num_beep=x_flashes_0_beep(1);
        elif trial_condition<(1+2*num_trial_per_type+3*num_of_trials_per_condition):
            num_flash,num_beep=x_flashes_0_beep(2);
    
         
    #multiple flashes&beeps
    else:
    #if trial_condition<(1+4*num_trial_per_type):
        if trial_condition<(1+3*num_trial_per_type+1*num_of_trials_per_condition):
            num_flash,num_beep=x_flashes_x_beeps(0);
        elif trial_condition<(1+3*num_trial_per_type+2*num_of_trials_per_condition):
            num_flash,num_beep=x_flashes_x_beeps(1);
        elif trial_condition<(1+3*num_trial_per_type+3*num_of_trials_per_condition):
            num_flash,num_beep=x_flashes_x_beeps(2);
    
    correct_answer.append([num_flash,num_beep]);
    
    # response options
    expyriment.stimuli.TextScreen("How many flashes did you see?", "Please respond by pressing any key from 1~4 on the keyboard").present();
    #keys' corresponding numbers 
    response, time=exp.keyboard.wait([constants.K_0,constants.K_1,constants.K_2,constants.K_3,constants.K_4]);
    if response==49:
        response=1;
    elif response==50:
        response=2;
    elif response==51:
        response=3;
    elif response==52:
        response=4;
    response_list.append(response);
#print result at the end
for i in range(num_total_trials):  
    trial_number=i+1;
    print("Answer for trial "+str(trial_number)+" (flash, beep): "+str(correct_answer[i])+" ; Your response: "+ str(response_list[i])+" ");
    if correct_answer[i][0]!=response_list[i]:
        print("False \n");
    else:
        print("Correct \n");
expyriment.control.end()
