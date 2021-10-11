#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Fri Apr 23 15:15:39 2021
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
    originPath='/Users/Jadyn/Desktop/mpr/mprax_lastrun.py',
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
    size=[1440, 990], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
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

# Initialize components for Routine "intro"
introClock = core.Clock()
introduction = visual.TextStim(win=win, name='introduction',
    text='This is a test of your ability to control the mouse.\n\nYou will see some green boxes, one at a time. Move your mouse cursor over each box and click on it ONCE. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cont = event.Mouse(win=win)
x, y = [None, None]
cont.mouseClock = core.Clock()
clickhere = visual.TextBox2(
     win, text='   Click here to continue', font='Arial',
     pos=(0, -0.25),     letterHeight=0.02,
     size=(0.25, 0.03), borderWidth=None,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='green', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='clickhere',
     autoLog=False,
)

# Initialize components for Routine "begin"
beginClock = core.Clock()
practice = visual.TextStim(win=win, name='practice',
    text='BEGIN PRACTICE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pracblock"
pracblockClock = core.Clock()
prtarget = visual.ImageStim(
    win=win,
    name='prtarget', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
prresp = event.Mouse(win=win)
x, y = [None, None]
prresp.mouseClock = core.Clock()
prinst = visual.TextStim(win=win, name='prinst',
    text='Click on the green box to continue',
    font='Arial',
    pos=(0, -0.25), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "newblock"
newblockClock = core.Clock()
fivesec = visual.TextStim(win=win, name='fivesec',
    text='This time you will have 5 seconds to click on each box.\n\nTry to click on the box before it disappears. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testblock"
testblockClock = core.Clock()
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
instr = visual.TextStim(win=win, name='instr',
    text='Click on the green box to continue',
    font='Arial',
    pos=(0, -0.25), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
end_at_5s=False


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the cont
gotValidClick = False  # until a click is received
# keep track of which components have finished
introComponents = [introduction, cont, clickhere]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction* updates
    if introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction.frameNStart = frameN  # exact frame index
        introduction.tStart = t  # local t and not account for scr refresh
        introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction, 'tStartRefresh')  # time at next scr refresh
        introduction.setAutoDraw(True)
    # *cont* updates
    if cont.status == NOT_STARTED and t >= 3-frameTolerance:
        # keep track of start time/frame for later
        cont.frameNStart = frameN  # exact frame index
        cont.tStart = t  # local t and not account for scr refresh
        cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont, 'tStartRefresh')  # time at next scr refresh
        cont.status = STARTED
        cont.mouseClock.reset()
        prevButtonState = cont.getPressed()  # if button is down already this ISN'T a new click
    if cont.status == STARTED:  # only update if started and not finished!
        buttons = cont.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # *clickhere* updates
    if clickhere.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        clickhere.frameNStart = frameN  # exact frame index
        clickhere.tStart = t  # local t and not account for scr refresh
        clickhere.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(clickhere, 'tStartRefresh')  # time at next scr refresh
        clickhere.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction.started', introduction.tStartRefresh)
thisExp.addData('introduction.stopped', introduction.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = cont.getPos()
buttons = cont.getPressed()
thisExp.addData('cont.x', x)
thisExp.addData('cont.y', y)
thisExp.addData('cont.leftButton', buttons[0])
thisExp.addData('cont.midButton', buttons[1])
thisExp.addData('cont.rightButton', buttons[2])
thisExp.addData('cont.started', cont.tStart)
thisExp.addData('cont.stopped', cont.tStop)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "begin"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
beginComponents = [practice]
for thisComponent in beginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "begin"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = beginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice* updates
    if practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice.frameNStart = frameN  # exact frame index
        practice.tStart = t  # local t and not account for scr refresh
        practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice, 'tStartRefresh')  # time at next scr refresh
        practice.setAutoDraw(True)
    if practice.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            practice.tStop = t  # not accounting for scr refresh
            practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice, 'tStopRefresh')  # time at next scr refresh
            practice.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin"-------
for thisComponent in beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice.started', practice.tStartRefresh)
thisExp.addData('practice.stopped', practice.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx', selection='0:10'),
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
    
    # ------Prepare to start Routine "pracblock"-------
    continueRoutine = True
    # update component parameters for each repeat
    prtarget.setPos((target_x, target_y))
    prtarget.setSize((target_w, target_h))
    prtarget.setImage(target_file)
    # setup some python lists for storing info about the prresp
    prresp.x = []
    prresp.y = []
    prresp.leftButton = []
    prresp.midButton = []
    prresp.rightButton = []
    prresp.time = []
    prresp.clicked_name = []
    prresp.clicked_image = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    pracblockComponents = [prtarget, prresp, prinst]
    for thisComponent in pracblockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pracblockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pracblock"-------
    while continueRoutine:
        # get current time
        t = pracblockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pracblockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prtarget* updates
        if prtarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prtarget.frameNStart = frameN  # exact frame index
            prtarget.tStart = t  # local t and not account for scr refresh
            prtarget.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prtarget, 'tStartRefresh')  # time at next scr refresh
            prtarget.setAutoDraw(True)
        # *prresp* updates
        if prresp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prresp.frameNStart = frameN  # exact frame index
            prresp.tStart = t  # local t and not account for scr refresh
            prresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prresp, 'tStartRefresh')  # time at next scr refresh
            prresp.status = STARTED
            prresp.mouseClock.reset()
            prevButtonState = prresp.getPressed()  # if button is down already this ISN'T a new click
        if prresp.status == STARTED:  # only update if started and not finished!
            buttons = prresp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [prtarget]:
                        if obj.contains(prresp):
                            gotValidClick = True
                            prresp.clicked_name.append(obj.name)
                            prresp.clicked_image.append(obj.image)
                    x, y = prresp.getPos()
                    prresp.x.append(x)
                    prresp.y.append(y)
                    buttons = prresp.getPressed()
                    prresp.leftButton.append(buttons[0])
                    prresp.midButton.append(buttons[1])
                    prresp.rightButton.append(buttons[2])
                    prresp.time.append(prresp.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *prinst* updates
        if prinst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prinst.frameNStart = frameN  # exact frame index
            prinst.tStart = t  # local t and not account for scr refresh
            prinst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prinst, 'tStartRefresh')  # time at next scr refresh
            prinst.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracblockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pracblock"-------
    for thisComponent in pracblockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('prtarget.started', prtarget.tStartRefresh)
    trials.addData('prtarget.stopped', prtarget.tStopRefresh)
    # store data for trials (TrialHandler)
    if len(prresp.x): trials.addData('prresp.x', prresp.x[0])
    if len(prresp.y): trials.addData('prresp.y', prresp.y[0])
    if len(prresp.leftButton): trials.addData('prresp.leftButton', prresp.leftButton[0])
    if len(prresp.midButton): trials.addData('prresp.midButton', prresp.midButton[0])
    if len(prresp.rightButton): trials.addData('prresp.rightButton', prresp.rightButton[0])
    if len(prresp.time): trials.addData('prresp.time', prresp.time[0])
    if len(prresp.clicked_name): trials.addData('prresp.clicked_name', prresp.clicked_name[0])
    if len(prresp.clicked_image): trials.addData('prresp.clicked_image', prresp.clicked_image[0])
    trials.addData('prresp.started', prresp.tStart)
    trials.addData('prresp.stopped', prresp.tStop)
    trials.addData('prinst.started', prinst.tStartRefresh)
    trials.addData('prinst.stopped', prinst.tStopRefresh)
    # the Routine "pracblock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "newblock"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
newblockComponents = [fivesec]
for thisComponent in newblockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
newblockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "newblock"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = newblockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=newblockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fivesec* updates
    if fivesec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fivesec.frameNStart = frameN  # exact frame index
        fivesec.tStart = t  # local t and not account for scr refresh
        fivesec.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fivesec, 'tStartRefresh')  # time at next scr refresh
        fivesec.setAutoDraw(True)
    if fivesec.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fivesec.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            fivesec.tStop = t  # not accounting for scr refresh
            fivesec.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fivesec, 'tStopRefresh')  # time at next scr refresh
            fivesec.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in newblockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "newblock"-------
for thisComponent in newblockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fivesec.started', fivesec.tStartRefresh)
thisExp.addData('fivesec.stopped', fivesec.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx', selection='0:10'),
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
    
    # ------Prepare to start Routine "testblock"-------
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
    testblockComponents = [target, resp, instr]
    for thisComponent in testblockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testblockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testblock"-------
    while continueRoutine:
        # get current time
        t = testblockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testblockClock)
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
        if target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
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
        
        # *instr* updates
        if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr.frameNStart = frameN  # exact frame index
            instr.tStart = t  # local t and not account for scr refresh
            instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
            instr.setAutoDraw(True)
        # first check whether to end in response to an earlier keypress
        if t >= 5.0 and end_at_5s: 
            continueRoutine = False
        elif t >= 5.0: # all trials end at this stage
            continueRoutine = False
        
        # otherwise, check for a new keypress:
        keys = event.getKeys()
        
        if keys: # if at least one key exists in the list,
            if 'escape' in keys: # now need to check for the quit key ourselves
                core.quit() 
        
            elif t < 5.0: # just remember this for later
                end_at_5s = True 
                thisExp.addData('RT', t) # but store the current time as the RT
        
            else: # we have a keypress between 2 and 4 s
                thisExp.addData('RT', t)
                continueRoutine = False
        else: #add this 
              thisExp.addData('RT', None) #and this
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testblockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testblock"-------
    for thisComponent in testblockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('target.started', target.tStartRefresh)
    trials_2.addData('target.stopped', target.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    if len(resp.x): trials_2.addData('resp.x', resp.x[0])
    if len(resp.y): trials_2.addData('resp.y', resp.y[0])
    if len(resp.leftButton): trials_2.addData('resp.leftButton', resp.leftButton[0])
    if len(resp.midButton): trials_2.addData('resp.midButton', resp.midButton[0])
    if len(resp.rightButton): trials_2.addData('resp.rightButton', resp.rightButton[0])
    if len(resp.time): trials_2.addData('resp.time', resp.time[0])
    if len(resp.clicked_name): trials_2.addData('resp.clicked_name', resp.clicked_name[0])
    if len(resp.clicked_image): trials_2.addData('resp.clicked_image', resp.clicked_image[0])
    trials_2.addData('resp.started', resp.tStart)
    trials_2.addData('resp.stopped', resp.tStop)
    trials_2.addData('instr.started', instr.tStartRefresh)
    trials_2.addData('instr.stopped', instr.tStopRefresh)
    # the Routine "testblock" was not non-slip safe, so reset the non-slip timer
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
