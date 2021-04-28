"""
#change names into "onset""interval/duration"
import expyriment;
import numpy;
import pygame;
audio_duration=7;
audio_gap=57;
illusion_audio=[2,3,4]
#stim_variable=range(1,20);
visual_gap=50
visual_duration=17
visual_audio_gap=23
num_of_trial=60
type_of_trials=4

exp = expyriment.design.Experiment(name="First Experiment")
expyriment.control.initialize(exp)

trial_type_num= numpy.random.randint(1,60);

#illusion_audio_number=stim_variable[numpy.random.choice(stim_variable)];
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

trial_category=num_of_trial/type_of_trials
audi_repitition=trial_category/len(illusion_audio)




def one_flash_x_beeps(x=0):
    stim_audio.present();
    exp.clock.wait(visual_audio_gap);
    stim_visual.present();
    for i in range(illusion_audio[x]-1):
        stim_audio.present()
        exp.clock.wait(audio_gap);
def x_flashes_1_beep(x=0):
     stim_audio.present()
     exp.clock.wait(visual_audio_gap)
     for i in range(illusion_audio[x]):
         stim_visual.present()
         exp.clock.wait(visual_duration)
         stim_visual_absence.present()
         exp.clock.wait(visual_gap)
def x_flashes_0_beep(x=0):
     for i in range(illusion_audio[x]):
         stim_visual.present()
         exp.clock.wait(visual_duration)
         stim_visual_absence.present()
         exp.clock.wait(visual_gap)
 
def x_flashes_x_beeps(x=0):
    visual_onset=[]    
    audio_onset=[]
    for i in range(illusion_audio[x]):
        visual_onset.append(visual_audio_gap+i*(visual_gap+visual_duration));
        audio_onset.append(i*(audio_duration+audio_gap));
    pygame.init()
    for i in range(illusion_audio[x]): 
        if pygame.time.get_ticks()==audio_onset[i]:
            stim_audio.present()
            exp.clock.wait(visual_audio_gap)
        if pygame.time.get_ticks()==visual_onset[i]:       
            stim_visual.present()
            exp.clock.wait(visual_duration)
            stim_visual_absence.present()
            exp.clock.wait(visual_gap)   
            
            
response_list=[]            
# 5 trials per condition, 15 illusionary, 45 non-illusionary
for k in range(type_of_trials):
    # illusion trials: one flash, multiple beeps
    
    if trial_type_num<(1+trial_category):
#    for s in range(len(illusion_audio)):
        if trial_type_num<(1+1*audi_repitition):
            one_flash_x_beeps(x=0)
        elif trial_type_num<(1+2*audi_repitition):
            one_flash_x_beeps(x=1)
        elif trial_type_num<(1+3*audi_repitition):
            one_flash_x_beeps(x=2)
  
    #multiple flashes, 1 beep or no beep
    elif trial_type_num<(1+2*trial_category):
    #   for s in range(len(illusion_audio)):
        if trial_type_num<(1+1*audi_repitition):
            x_flashes_1_beep(0);
        elif trial_type_num<(1+2*audi_repitition):
            x_flashes_1_beep(1);    
        elif trial_type_num<(1+3*audi_repitition):
            x_flashes_1_beep(2);
            
    elif trial_type_num<(1+3*trial_category):
        if trial_type_num<(1+1*audi_repitition):
             x_flashes_0_beep(x=0);
        elif trial_type_num<(1+2*audi_repitition):
            x_flashes_0_beep(x=1);
        elif trial_type_num<(1+3*audi_repitition):
            x_flashes_0_beep(x=2);
    
         
    #multiple flashes&beeps
    else:
        if trial_type_num<(1+1*audi_repitition):
            x_flashes_x_beeps(x=0);
        elif trial_type_num<(1+2*audi_repitition):
            x_flashes_x_beeps(x=1);
        elif trial_type_num<(1+3*audi_repitition):
            x_flashes_x_beeps(x=2);
    
    response, time=expyriment.io.Keyboard.wait(keys=['0','1','2','3','4']);
    response_list.append(response);

       
#one beep, multiple flashes
# if number==1:
#     stim_audio.present()
#    exp.clock.wait(visual_duration)


expyriment.control.end()
