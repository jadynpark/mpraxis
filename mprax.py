#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Mon Mar  8 15:59:36 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'mprax'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/Jadyn/Desktop/mpr/mprax.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "block1"
block1Clock = core.Clock()
target = visual.ImageStim(
    win=win,
    name='target', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
resp = event.Mouse(win=win)
x, y = [None, None]
resp.mouseClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Please click on the green box',
    font='Arial',
    pos=(0, -0.25), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "great"
greatClock = core.Clock()
inst2 = visual.TextStim(win=win, name='inst2',
    text='Great! Now the box will disappear after 5 seconds. Please try to click on the box before it disappears. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "block2"
block2Clock = core.Clock()
target2 = visual.ImageStim(
    win=win,
    name='target2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
resp2 = event.Mouse(win=win)
x, y = [None, None]
resp2.mouseClock = core.Clock()
instructions2 = visual.TextStim(win=win, name='instructions2',
    text='Please click on the green box',
    font='Arial',
    pos=(0, -0.25), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx', selection='0:9'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block1"-------
    continueRoutine = True
    # update component parameters for each repeat
    target.setPos((target_x, target_y))
    target.setSize((target_w, target_h))
    target.setImage(target_file)
    # setup some python lists for storing info about the resp
    resp.x = []
    resp.y = []
    resp.leftButton = []
    resp.midButton = []
    resp.rightButton = []
    resp.time = []
    resp.clicked_name = []
    resp.clicked_image = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    block1Components = [target, resp, instructions]
    for thisComponent in block1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block1"-------
    while continueRoutine:
        # get current time
        t = block1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        # *resp* updates
        if resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            resp.mouseClock.reset()
            prevButtonState = resp.getPressed()  # if button is down already this ISN'T a new click
        if resp.status == STARTED:  # only update if started and not finished!
            buttons = resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target]:
                        if obj.contains(resp):
                            gotValidClick = True
                            resp.clicked_name.append(obj.name)
                            resp.clicked_image.append(obj.image)
                    x, y = resp.getPos()
                    resp.x.append(x)
                    resp.y.append(y)
                    buttons = resp.getPressed()
                    resp.leftButton.append(buttons[0])
                    resp.midButton.append(buttons[1])
                    resp.rightButton.append(buttons[2])
                    resp.time.append(resp.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *instructions* updates
        if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions.frameNStart = frameN  # exact frame index
            instructions.tStart = t  # local t and not account for scr refresh
            instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
            instructions.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block1"-------
    for thisComponent in block1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('target.started', target.tStartRefresh)
    trials.addData('target.stopped', target.tStopRefresh)
    # store data for trials (TrialHandler)
    if len(resp.x): trials.addData('resp.x', resp.x[0])
    if len(resp.y): trials.addData('resp.y', resp.y[0])
    if len(resp.leftButton): trials.addData('resp.leftButton', resp.leftButton[0])
    if len(resp.midButton): trials.addData('resp.midButton', resp.midButton[0])
    if len(resp.rightButton): trials.addData('resp.rightButton', resp.rightButton[0])
    if len(resp.time): trials.addData('resp.time', resp.time[0])
    if len(resp.clicked_name): trials.addData('resp.clicked_name', resp.clicked_name[0])
    if len(resp.clicked_image): trials.addData('resp.clicked_image', resp.clicked_image[0])
    trials.addData('resp.started', resp.tStart)
    trials.addData('resp.stopped', resp.tStop)
    trials.addData('instructions.started', instructions.tStartRefresh)
    trials.addData('instructions.stopped', instructions.tStopRefresh)
    # the Routine "block1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "great"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
greatComponents = [inst2]
for thisComponent in greatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
greatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "great"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = greatClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=greatClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst2* updates
    if inst2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst2.frameNStart = frameN  # exact frame index
        inst2.tStart = t  # local t and not account for scr refresh
        inst2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst2, 'tStartRefresh')  # time at next scr refresh
        inst2.setAutoDraw(True)
    if inst2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inst2.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            inst2.tStop = t  # not accounting for scr refresh
            inst2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inst2, 'tStopRefresh')  # time at next scr refresh
            inst2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in greatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "great"-------
for thisComponent in greatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('inst2.started', inst2.tStartRefresh)
thisExp.addData('inst2.stopped', inst2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx', selection='0:9'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block2"-------
    continueRoutine = True
    # update component parameters for each repeat
    target2.setPos((target_x, target_y))
    target2.setSize((target_w, target_h))
    target2.setImage(target_file)
    # setup some python lists for storing info about the resp2
    resp2.x = []
    resp2.y = []
    resp2.leftButton = []
    resp2.midButton = []
    resp2.rightButton = []
    resp2.time = []
    resp2.clicked_name = []
    resp2.clicked_image = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    block2Components = [target2, resp2, instructions2]
    for thisComponent in block2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block2"-------
    while continueRoutine:
        # get current time
        t = block2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target2* updates
        if target2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target2.frameNStart = frameN  # exact frame index
            target2.tStart = t  # local t and not account for scr refresh
            target2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2, 'tStartRefresh')  # time at next scr refresh
            target2.setAutoDraw(True)
        if target2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                target2.tStop = t  # not accounting for scr refresh
                target2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target2, 'tStopRefresh')  # time at next scr refresh
                target2.setAutoDraw(False)
        # *resp2* updates
        if resp2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp2.frameNStart = frameN  # exact frame index
            resp2.tStart = t  # local t and not account for scr refresh
            resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp2, 'tStartRefresh')  # time at next scr refresh
            resp2.status = STARTED
            resp2.mouseClock.reset()
            prevButtonState = resp2.getPressed()  # if button is down already this ISN'T a new click
        if resp2.status == STARTED:  # only update if started and not finished!
            buttons = resp2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target2]:
                        if obj.contains(resp2):
                            gotValidClick = True
                            resp2.clicked_name.append(obj.name)
                            resp2.clicked_image.append(obj.image)
                    x, y = resp2.getPos()
                    resp2.x.append(x)
                    resp2.y.append(y)
                    buttons = resp2.getPressed()
                    resp2.leftButton.append(buttons[0])
                    resp2.midButton.append(buttons[1])
                    resp2.rightButton.append(buttons[2])
                    resp2.time.append(resp2.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *instructions2* updates
        if instructions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions2.frameNStart = frameN  # exact frame index
            instructions2.tStart = t  # local t and not account for scr refresh
            instructions2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions2, 'tStartRefresh')  # time at next scr refresh
            instructions2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block2"-------
    for thisComponent in block2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('target2.started', target2.tStartRefresh)
    trials_2.addData('target2.stopped', target2.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    if len(resp2.x): trials_2.addData('resp2.x', resp2.x[0])
    if len(resp2.y): trials_2.addData('resp2.y', resp2.y[0])
    if len(resp2.leftButton): trials_2.addData('resp2.leftButton', resp2.leftButton[0])
    if len(resp2.midButton): trials_2.addData('resp2.midButton', resp2.midButton[0])
    if len(resp2.rightButton): trials_2.addData('resp2.rightButton', resp2.rightButton[0])
    if len(resp2.time): trials_2.addData('resp2.time', resp2.time[0])
    if len(resp2.clicked_name): trials_2.addData('resp2.clicked_name', resp2.clicked_name[0])
    if len(resp2.clicked_image): trials_2.addData('resp2.clicked_image', resp2.clicked_image[0])
    trials_2.addData('resp2.started', resp2.tStart)
    trials_2.addData('resp2.stopped', resp2.tStop)
    trials_2.addData('instructions2.started', instructions2.tStartRefresh)
    trials_2.addData('instructions2.stopped', instructions2.tStopRefresh)
    # the Routine "block2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
