## Original Study Reference ##
Here is the PCBS project replicating Experiment 1 in Sham et al.(2000) "What you see is what you hear". 
Full study please see Shams, L., Kamitani, Y., & Shimojo, S. (2002). Visual illusion induced by sound. Cognitive Brain Research, 14(1), 147–152. https://doi.org/10.1016/s0926-6410(02)00069-1 
<br />
**All figures were from the original study.**
<br />
<br />
_Platform: Python 3_
<br />
_Library: expyriment, numpy_
<br />
<br />
## Findings in the Original Study ## 
This expeirmient was famous for demonstrating a cross-modal perception interaction, namely visual and audio processing. In the results, the number of flashes perceived by participants were biased by the number of beeps, in single flash trials: when there was 1 flash displayed with x beeps, when asking how many flashes they saw, they reported not 1, but x) (fig 3).<br />

 <img src="https://user-images.githubusercontent.com/47482896/117947255-501f2880-b310-11eb-824b-c15228224e47.png" width="650" height="550">

<br />

That was contrasting with the control trials: trials with only visual stimulus (0 beep) and trials with only 1 beep (fig 4).<br />
<img src="https://user-images.githubusercontent.com/47482896/117947764-ccb20700-b310-11eb-82bc-4f88ce3c28e7.png" width="650" height="550">
<br />
<br />
<br />

## Design of Experiment 1 ##
**_Overview:_**<br />
There are 60 trials in total, with visual stimulus flashing from 1 to 4 times, and audio stimulus ranging from 0 to 4 times, with 5 trials* each condition. <br />
**_Breakdown of types and conditions:_**<br />
Illusion trials: 1_flash_x beeps (2<=x<=4);  <br />
Control trials: x_flashes_x beeps (2<=x<=4), x_flashes_1_beep (2<=x<=4), and x_flashes_0_beep (2<=x<=4); <br />
<br />


The onsets and durations of stimuli are summarized in the figure 2:<br />
 <img src="https://user-images.githubusercontent.com/47482896/118040889-6d84de80-b372-11eb-9686-605de78611bf.png" width="650" height="550">
<br />

## Instruction ##
There are 60 trials in total. The task is to identify how many flashes are there for each trial.<br />
The participant needs to press ENTER to start the game with subject number, then when seeing "ready", press SPACE;<br />
To start each trial, the participant needs to press SPACE, and then respond by pressing one key from 1, 2, 3, and 4 on the keyboard;<br />
The results will be displayed on Python after the experiment, with correct answer (number of flashes, number of beeps) and the participant's response for each trial.
 <br /><br />
 
## Attention: Undesirable Effect of the Stimulus##
There is a clear difference between 1-flash trials and multiple-flash ones, as the flash is very obvious. It might be due to the limitation of the program or parameters. Therefore, the participant could easily tell 1_flash_x_beeps apart when referencing with other control trials. The illusion could not be replicated successfully.

 <br /><br />

**Any feedback would be very much appreciated.**
