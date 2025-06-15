#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Thu Apr 17 14:25:17 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'Audiometer_v2'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/manastanavde/Downloads/Audiometer_v2 copy/Audiometer_v2.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_respStart') is None:
        # initialise key_respStart
        key_respStart = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_respStart',
        )
    # create speaker 'sound_left'
    deviceManager.addDevice(
        deviceName='sound_left',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'sound_right'
    deviceManager.addDevice(
        deviceName='sound_right',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('key_respEnd') is None:
        # initialise key_respEnd
        key_respEnd = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_respEnd',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "WelcomeScreen" ---
    textWelc = visual.TextStim(win=win, name='textWelc',
        text='Welcome to the experiment!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    textExplain = visual.TextStim(win=win, name='textExplain',
        text="This is an audiometry test to measure your absolute threshold of hearing. \n\nYou will be presented with sounds of different frequencies, following which you have to indicate if you hear them (by pressing the 'Yes' button) or not (by pressing the 'No' button).\n\nYou will first hear sounds from your left ear, followed by sounds from your right ear.\n\nPress SPACEBAR to start.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_respStart = keyboard.Keyboard(deviceName='key_respStart')
    
    # --- Initialize components for Routine "blank500" ---
    textBlank = visual.TextStim(win=win, name='textBlank',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "trial_left" ---
    # Run 'Begin Experiment' code from codetrials_left
    # Global variables
    step = 5
    sound_file_path = "Audio_Regen_4/"
    dummy_file_path = f"{sound_file_path}dummy.wav"
    
    # Frequencies used in the audiometer
    frequencies = [125, 250, 500, 1000, 2000, 4000, 6000, 8000]  # List of frequencies
    
    # Fixed lower limit for both ears
    lower_lim_left = -20.0  
    
    # Updated dictionary mapping frequencies to their corresponding upper limits
    upper_limits = {
        125: 40.0,
        250: 50.0,
        500: 60.0,
        1000: 70.0,
        2000: 70.0,
        4000: 60.0,
        6000: 50.0,
        8000: 50.0
    }
    
    # Initialize variables for the left ear
    current_dB_left = 30.0
    frequency_index_left = 0
    frequency_left = frequencies[frequency_index_left]
    upper_lim_left = upper_limits[frequency_left]
    reversals_left = 0
    reading_num_left = 0
    trial_num_left = 0
    user_resp_left = []
    readings_left = []
    dummy_play_count_left = 0
    limit_played_left = False
    waiting_for_y_left = False
    dummy_trial_repeats = 0
    frequency_updated = False
    
    next_freq_text_left = visual.TextStim(win=win, name='next_freq_text_left',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    yes_button_left = visual.ImageStim(
        win=win,
        name='yes_button_left', units='cm', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-8, 0), draggable=False, size=(5, 5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    no_button_left = visual.ImageStim(
        win=win,
        name='no_button_left', units='cm', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(8,0), draggable=False, size=(5, 5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    sound_left = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=False, 
        speaker='sound_left',    name='sound_left'
    )
    sound_left.setVolume(1.0)
    mouse_left = event.Mouse(win=win)
    x, y = [None, None]
    mouse_left.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "blank500" ---
    textBlank = visual.TextStim(win=win, name='textBlank',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "blank500" ---
    textBlank = visual.TextStim(win=win, name='textBlank',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Int_Message" ---
    textInterval = visual.TextStim(win=win, name='textInterval',
        text='All trials for the left ear have finished. We will now proceed to the trials for the right ear.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "blank500" ---
    textBlank = visual.TextStim(win=win, name='textBlank',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "trial_right" ---
    # Run 'Begin Experiment' code from codetrials_right
    # Global variables
    step = 5
    sound_file_path = "Audio_Regen_4/"
    dummy_file_path = f"{sound_file_path}dummy.wav"
    
    # Frequencies used in the audiometer
    frequencies = [125, 250, 500, 1000, 2000, 4000, 6000, 8000]  # List of frequencies
    
    # Fixed lower limit for both ears
    lower_lim_right = -20  
    
    # Updated dictionary mapping frequencies to their corresponding upper limits
    upper_limits = {
        125: 40,
        250: 50,
        500: 60,
        1000: 70,
        2000: 70,
        4000: 60,
        6000: 50,
        8000: 50
    }
    
    ### === RIGHT EAR VARIABLES === ###
    trial_num_right = 0  # Counter to keep track of trials
    reading_num_right = 0  # Counter to keep track of reading number
    user_resp_right = []  # List to keep track of key responses
    reversals_right = 0  # Counter variable to keep track of reversals
    readings_right = []  # List to keep track of all readings
    frequency_index_right = 0  # Index to keep track of the current frequency
    frequency_right = frequencies[frequency_index_right]  # Current frequency
    upper_lim_right = upper_limits[frequency_right]  # Set dynamic upper limit
    
    current_dB_right = 30.0  # Initial dB level for the first trial
    current_filename_right = f"{sound_file_path}{frequency_right}_{current_dB_right:.1f}_right.wav"  # Initial filename
    
    next_freq_message_right = ""  # Message for next frequency
    latest_reading_right = None  # Store latest dB reading
    waiting_for_y_right = False  # Flag for response tracking
    dummy_play_count_right = 0  # Counter for dummy.wav plays
    limit_played_right = False  # Flag to check if limit sound was played
    dummy_responses_right = []  # List to keep track of dummy.wav responses
    dummy_trial_repeats = 0 #Counter for the amount of times a set of 3 dummy trials has been run
    next_freq_text_right = visual.TextStim(win=win, name='next_freq_text_right',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    yes_button_right = visual.ImageStim(
        win=win,
        name='yes_button_right', units='cm', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-8, 0), draggable=False, size=(5, 5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    no_button_right = visual.ImageStim(
        win=win,
        name='no_button_right', units='cm', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(8,0), draggable=False, size=(5,5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    sound_right = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=False, 
        speaker='sound_right',    name='sound_right'
    )
    sound_right.setVolume(1.0)
    mouse_right = event.Mouse(win=win)
    x, y = [None, None]
    mouse_right.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "blank500" ---
    textBlank = visual.TextStim(win=win, name='textBlank',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "blank500" ---
    textBlank = visual.TextStim(win=win, name='textBlank',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "EndScreen" ---
    textEnd = visual.TextStim(win=win, name='textEnd',
        text='Thanks for participating in this experiment! Please notify the experimenter about the completion.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_respEnd = keyboard.Keyboard(deviceName='key_respEnd')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "WelcomeScreen" ---
    # create an object to store info about Routine WelcomeScreen
    WelcomeScreen = data.Routine(
        name='WelcomeScreen',
        components=[textWelc, textExplain, key_respStart],
    )
    WelcomeScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_respStart
    key_respStart.keys = []
    key_respStart.rt = []
    _key_respStart_allKeys = []
    # store start times for WelcomeScreen
    WelcomeScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    WelcomeScreen.tStart = globalClock.getTime(format='float')
    WelcomeScreen.status = STARTED
    thisExp.addData('WelcomeScreen.started', WelcomeScreen.tStart)
    WelcomeScreen.maxDuration = None
    # keep track of which components have finished
    WelcomeScreenComponents = WelcomeScreen.components
    for thisComponent in WelcomeScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WelcomeScreen" ---
    WelcomeScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelc* updates
        
        # if textWelc is starting this frame...
        if textWelc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelc.frameNStart = frameN  # exact frame index
            textWelc.tStart = t  # local t and not account for scr refresh
            textWelc.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelc, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelc.started')
            # update status
            textWelc.status = STARTED
            textWelc.setAutoDraw(True)
        
        # if textWelc is active this frame...
        if textWelc.status == STARTED:
            # update params
            pass
        
        # if textWelc is stopping this frame...
        if textWelc.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textWelc.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                textWelc.tStop = t  # not accounting for scr refresh
                textWelc.tStopRefresh = tThisFlipGlobal  # on global time
                textWelc.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textWelc.stopped')
                # update status
                textWelc.status = FINISHED
                textWelc.setAutoDraw(False)
        
        # *textExplain* updates
        
        # if textExplain is starting this frame...
        if textExplain.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            textExplain.frameNStart = frameN  # exact frame index
            textExplain.tStart = t  # local t and not account for scr refresh
            textExplain.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textExplain, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textExplain.started')
            # update status
            textExplain.status = STARTED
            textExplain.setAutoDraw(True)
        
        # if textExplain is active this frame...
        if textExplain.status == STARTED:
            # update params
            pass
        
        # *key_respStart* updates
        waitOnFlip = False
        
        # if key_respStart is starting this frame...
        if key_respStart.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_respStart.frameNStart = frameN  # exact frame index
            key_respStart.tStart = t  # local t and not account for scr refresh
            key_respStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_respStart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_respStart.started')
            # update status
            key_respStart.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_respStart.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_respStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_respStart.status == STARTED and not waitOnFlip:
            theseKeys = key_respStart.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_respStart_allKeys.extend(theseKeys)
            if len(_key_respStart_allKeys):
                key_respStart.keys = _key_respStart_allKeys[-1].name  # just the last key pressed
                key_respStart.rt = _key_respStart_allKeys[-1].rt
                key_respStart.duration = _key_respStart_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            WelcomeScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WelcomeScreen" ---
    for thisComponent in WelcomeScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for WelcomeScreen
    WelcomeScreen.tStop = globalClock.getTime(format='float')
    WelcomeScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('WelcomeScreen.stopped', WelcomeScreen.tStop)
    # check responses
    if key_respStart.keys in ['', [], None]:  # No response was made
        key_respStart.keys = None
    thisExp.addData('key_respStart.keys',key_respStart.keys)
    if key_respStart.keys != None:  # we had a response
        thisExp.addData('key_respStart.rt', key_respStart.rt)
        thisExp.addData('key_respStart.duration', key_respStart.duration)
    thisExp.nextEntry()
    # the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    # create an object to store info about Routine blank500
    blank500 = data.Routine(
        name='blank500',
        components=[textBlank],
    )
    blank500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for blank500
    blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blank500.tStart = globalClock.getTime(format='float')
    blank500.status = STARTED
    thisExp.addData('blank500.started', blank500.tStart)
    blank500.maxDuration = None
    # keep track of which components have finished
    blank500Components = blank500.components
    for thisComponent in blank500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    blank500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank* updates
        
        # if textBlank is starting this frame...
        if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.tStart = t  # local t and not account for scr refresh
            textBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textBlank.started')
            # update status
            textBlank.status = STARTED
            textBlank.setAutoDraw(True)
        
        # if textBlank is active this frame...
        if textBlank.status == STARTED:
            # update params
            pass
        
        # if textBlank is stopping this frame...
        if textBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank.tStop = t  # not accounting for scr refresh
                textBlank.tStopRefresh = tThisFlipGlobal  # on global time
                textBlank.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlank.stopped')
                # update status
                textBlank.status = FINISHED
                textBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            blank500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blank500
    blank500.tStop = globalClock.getTime(format='float')
    blank500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('blank500.stopped', blank500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if blank500.maxDurationReached:
        routineTimer.addTime(-blank500.maxDuration)
    elif blank500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_left = data.TrialHandler2(
        name='trials_left',
        nReps=500.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(trials_left)  # add the loop to the experiment
    thisTrials_left = trials_left.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_left.rgb)
    if thisTrials_left != None:
        for paramName in thisTrials_left:
            globals()[paramName] = thisTrials_left[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_left in trials_left:
        currentLoop = trials_left
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_left.rgb)
        if thisTrials_left != None:
            for paramName in thisTrials_left:
                globals()[paramName] = thisTrials_left[paramName]
        
        # --- Prepare to start Routine "trial_left" ---
        # create an object to store info about Routine trial_left
        trial_left = data.Routine(
            name='trial_left',
            components=[next_freq_text_left, yes_button_left, no_button_left, sound_left, mouse_left],
        )
        trial_left.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codetrials_left
        # Set the initial sound file for the left ear
        current_filename_left = f"{sound_file_path}{frequency_left}_{current_dB_left:.1f}_left.wav"
        sound_left.setSound(current_filename_left, secs=30.0, hamming=False)
        
        # Print the current filename and dB level for debugging
        print(f"Filename: {current_filename_left}")
        print(f"Current dB (left): {current_dB_left}")
        
        
        yes_button_left.setImage('Mouse/Yes.png')
        no_button_left.setImage('Mouse/No.png')
        sound_left.setSound(current_filename_left, secs=30.0, hamming=False)
        sound_left.setVolume(1.0, log=False)
        sound_left.seek(0)
        # setup some python lists for storing info about the mouse_left
        mouse_left.x = []
        mouse_left.y = []
        mouse_left.leftButton = []
        mouse_left.midButton = []
        mouse_left.rightButton = []
        mouse_left.time = []
        mouse_left.clicked_name = []
        gotValidClick = False  # until a click is received
        mouse_left.mouseClock.reset()
        # store start times for trial_left
        trial_left.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial_left.tStart = globalClock.getTime(format='float')
        trial_left.status = STARTED
        thisExp.addData('trial_left.started', trial_left.tStart)
        trial_left.maxDuration = None
        # keep track of which components have finished
        trial_leftComponents = trial_left.components
        for thisComponent in trial_left.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_left" ---
        # if trial has changed, end Routine now
        if isinstance(trials_left, data.TrialHandler2) and thisTrials_left.thisN != trials_left.thisTrial.thisN:
            continueRoutine = False
        trial_left.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *next_freq_text_left* updates
            
            # if next_freq_text_left is active this frame...
            if next_freq_text_left.status == STARTED:
                # update params
                pass
            
            # *yes_button_left* updates
            
            # if yes_button_left is starting this frame...
            if yes_button_left.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                yes_button_left.frameNStart = frameN  # exact frame index
                yes_button_left.tStart = t  # local t and not account for scr refresh
                yes_button_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yes_button_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'yes_button_left.started')
                # update status
                yes_button_left.status = STARTED
                yes_button_left.setAutoDraw(True)
            
            # if yes_button_left is active this frame...
            if yes_button_left.status == STARTED:
                # update params
                pass
            
            # *no_button_left* updates
            
            # if no_button_left is starting this frame...
            if no_button_left.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                no_button_left.frameNStart = frameN  # exact frame index
                no_button_left.tStart = t  # local t and not account for scr refresh
                no_button_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no_button_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'no_button_left.started')
                # update status
                no_button_left.status = STARTED
                no_button_left.setAutoDraw(True)
            
            # if no_button_left is active this frame...
            if no_button_left.status == STARTED:
                # update params
                pass
            
            # *sound_left* updates
            
            # if sound_left is starting this frame...
            if sound_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_left.frameNStart = frameN  # exact frame index
                sound_left.tStart = t  # local t and not account for scr refresh
                sound_left.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_left.started', tThisFlipGlobal)
                # update status
                sound_left.status = STARTED
                sound_left.play(when=win)  # sync with win flip
            
            # if sound_left is stopping this frame...
            if sound_left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_left.tStartRefresh + 30.0-frameTolerance or sound_left.isFinished:
                    # keep track of stop time/frame for later
                    sound_left.tStop = t  # not accounting for scr refresh
                    sound_left.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_left.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sound_left.stopped')
                    # update status
                    sound_left.status = FINISHED
                    sound_left.stop()
            # *mouse_left* updates
            
            # if mouse_left is starting this frame...
            if mouse_left.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                mouse_left.frameNStart = frameN  # exact frame index
                mouse_left.tStart = t  # local t and not account for scr refresh
                mouse_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mouse_left.started')
                # update status
                mouse_left.status = STARTED
                prevButtonState = mouse_left.getPressed()  # if button is down already this ISN'T a new click
            if mouse_left.status == STARTED:  # only update if started and not finished!
                x, y = mouse_left.getPos()
                mouse_left.x.append(x)
                mouse_left.y.append(y)
                buttons = mouse_left.getPressed()
                mouse_left.leftButton.append(buttons[0])
                mouse_left.midButton.append(buttons[1])
                mouse_left.rightButton.append(buttons[2])
                mouse_left.time.append(mouse_left.mouseClock.getTime())
                buttons = mouse_left.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames((yes_button_left,no_button_left), namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_left):
                                gotValidClick = True
                                mouse_left.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse_left.clicked_name.append(None)
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[sound_left]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial_left.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_left.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_left" ---
        for thisComponent in trial_left.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial_left
        trial_left.tStop = globalClock.getTime(format='float')
        trial_left.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial_left.stopped', trial_left.tStop)
        # Run 'End Routine' code from codetrials_left
        # Store the current_dB value before updating it
        previous_dB_left = current_dB_left
        
        # Check for mouse clicks on "Yes" or "No" buttons
        clicked_button = None
        while clicked_button is None:
            if mouse_left.isPressedIn(yes_button_left):
                clicked_button = 'y'
            elif mouse_left.isPressedIn(no_button_left):
                clicked_button = 'n'
            core.wait(0.01)
        
        # Update current_dB based on the clicked button
        if clicked_button == 'y':
            print("Yes button clicked")  # Debugging statement
            user_resp_left.append('y')
            current_dB_left -= step * 2
        elif clicked_button == 'n':
            print("No button clicked")  # Debugging statement
            user_resp_left.append('n')
            current_dB_left += step
        
        # Ensure current_dB stays within the defined limits
        if lower_lim_left <= current_dB_left <= upper_lim_left:
            current_filename_left = f"{sound_file_path}{frequency_left}_{current_dB_left:.1f}_left.wav"
            dummy_play_count_left = 0  # Reset dummy play count if within limits
            limit_played_left = False  # Reset limit played flag
        elif current_dB_left > upper_lim_left:
            print("Current dB exceeds upper limit")
            current_dB_left = upper_lim_left  # Ensure current_dB does not exceed upper limit
            if not limit_played_left:
                current_filename_left = f"{sound_file_path}{frequency_left}_{upper_lim_left:.1f}_left.wav"
                limit_played_left = True  # Mark that the limit sound has been played
                print("Playing upper limit sound")
            else:
                if 'n' in user_resp_left[-1]:
                    # Skip to the next frequency
                    frequency_index_left += 1
                    if frequency_index_left < len(frequencies):
                        frequency_left = frequencies[frequency_index_left]
                        current_dB_left = 30.0  # Reset dB for new frequency
                        upper_lim_left = upper_limits[frequency_left]
                        reversals_left = 0
                        reading_num_left = 0
                        trial_num_left = 0
                        user_resp_left = []  # Reset user responses for the new frequency
                        readings_left = []  # Reset readings for the new frequency
                        frequency_updated = False  # ✅ Reset the flag for the new frequency
                        next_freq_message_left = f"Next frequency: {frequency_left} Hz"
                        print(f"Moving to next frequency: {frequency_left} Hz")
                    else:
                        trials_left.finished = True  # End experiment if all frequencies are done
                        print("All frequencies tested, ending Left Ear")
        elif current_dB_left < lower_lim_left:
            print("Current dB below lower limit")
            current_dB_left = lower_lim_left  # Ensure current_dB does not go below lower limit
            if not limit_played_left:
                current_filename_left = f"{sound_file_path}{frequency_left}_{lower_lim_left:.1f}_left.wav"
                limit_played_left = True  # Mark that the limit sound has been played
                print("Playing lower limit sound")
                sound_left.setSound(current_filename_left, secs=30.0, hamming=False)
                sound_left.play()
            else:
                event.clearEvents(eventType='mouse')  # Clear mouse events before detecting clicks
                while not any(mouse_left.getPressed()):
                    pass
                if mouse_left.isPressedIn(yes_button_left):
                    print("Yes button clicked during dummy trial")
                    dummy_play_count_left = 0
                    y_count = 0
                    n_count = 0
                    while dummy_play_count_left < 3:
                        event.clearEvents(eventType='mouse')  # Clear previous events
                        print(f"Playing dummy.wav {dummy_play_count_left + 1} time(s)")
                        
                        # Show a blank screen briefly between trials
                        win.color = (0, 0, 0)  # Set screen to black (or another neutral color)
                        win.flip()
                        core.wait(0.5)  # Keep the screen blank for 500ms
                        
                        # Restore original screen and redraw buttons
                        win.color = (0, 0, 0)  # Assuming white background, adjust as needed
                        yes_button_left.draw()
                        no_button_left.draw()
                        win.flip()
                        
                        sound_left.setSound(dummy_file_path, secs=30.0, hamming=False)
                        sound_left.play()
                        
                        click_detected = False
                        while not click_detected:
                            if any(mouse_left.getPressed()):
                                if mouse_left.isPressedIn(yes_button_left):
                                    print("Yes button clicked during dummy trial playback")
                                    y_count += 1
                                    thisExp.addData(f'dummy_response_{dummy_play_count_left + 1}_left', 'y')
                                    click_detected = True
                                elif mouse_left.isPressedIn(no_button_left):
                                    print("No button clicked during dummy trial playback")
                                    n_count += 1
                                    thisExp.addData(f'dummy_response_{dummy_play_count_left + 1}_left', 'n')
                                    click_detected = True
                            core.wait(0.01)  # Prevent high CPU usage
                        dummy_play_count_left += 1
                    if y_count >= 2:
                        frequency_index_left += 1
                        if frequency_index_left < len(frequencies):
                            frequency_left = frequencies[frequency_index_left]
                            current_dB_left = 30.0
                            upper_lim_left = upper_limits[frequency_left]
                            reversals_left = 0
                            reading_num_left = 0
                            trial_num_left = 0
                            user_resp_left = []
                            readings_left = []  # Reset readings for the new frequency
                            frequency_updated = False  # ✅ Reset the flag for the new frequency
                            print(f"Moving to next frequency: {frequency_left} Hz")
                        else:
                            trials_left.finished = True
                            print("All frequencies tested, ending experiment")
                    elif n_count >= 2:
                        dummy_trial_repeats += 1
                        thisExp.addData('Level_left', -20)
                        readings_left.append(-20)
                        if dummy_trial_repeats < 3:
                            # Go back to the lower limit and start again
                            current_dB_left = lower_lim_left
                            print(f"Restarting from lower limit: {current_dB_left}")
                        else:
                            # Dummy trial concordant check
                            if readings_left.count(-20) >= 3 and dummy_trial_repeats >= 3:
                                if not frequency_updated:  # Ensure frequency update happens only once
                                    if frequency_index_left < len(frequencies) - 1:
                                        frequency_index_left += 1  # Move to next frequency
                                        frequency_left = frequencies[frequency_index_left]  # Update frequency
                                        frequency_updated = True  # Mark that the frequency has been updated
                                        current_dB_left = 30.0  # Reset dB for new frequency
                                        upper_lim_left = upper_limits[frequency_left]
                                        reversals_left = 0
                                        reading_num_left = 0
                                        trial_num_left = 0
                                        user_resp_left = []  # Reset user responses for the new frequency
                                        readings_left = []  # Reset readings for the new frequency
                                        frequency_updated = False  # ✅ Reset the flag for the new frequency
                                        next_freq_message_left = f"Next frequency: {frequency_left} Hz"
                                        print(f"Dummy trial triggered frequency change: {frequency_left} Hz (Index: {frequency_index_left})")
                                    else:
                                        trials_left.finished = True  # End experiment
                                        print("All frequencies tested, ending Left Ear")
                elif mouse_left.isPressedIn(no_button_left):
                    print("No button clicked during dummy trial")  # Debugging statement
                    user_resp_left.append('n')
                    print(f"User response left: {user_resp_left}")  # Debugging statement
                    # Continue with the normal procedure
                    current_dB_left += step
        
        # Track user responses and reversals
        print(f"User response left: {user_resp_left}")  # Debugging statement
        if len(user_resp_left) > 1:
            if user_resp_left[-1] != user_resp_left[-2]:
                reversals_left += 1
                print(f"Reversals left: {reversals_left}")  # Debugging statement
                # Track the value of previous_dB at every 2nd reversal
                if reversals_left % 2 == 0:
                    if user_resp_left[-1] == 'n':
                        # Wait for the next 'y' to record the reading
                        waiting_for_y_left = True
                        print("Waiting for next 'y' to record the reading")  # Debugging statement
                    elif user_resp_left[-1] == 'y':
                        latest_reading_left = previous_dB_left
                        readings_left.append(latest_reading_left)
                        reading_num_left += 1
                        print(f"Recording reading (2nd reversal): {latest_reading_left}")  # Debugging statement
                        thisExp.addData('Readings_left', latest_reading_left)  # Add the latest reading to the experiment data
                        waiting_for_y_left = False  # Reset the flag
                elif waiting_for_y_left and user_resp_left[-1] == 'y':
                    latest_reading_left = previous_dB_left
                    readings_left.append(latest_reading_left)
                    reading_num_left += 1
                    print(f"Recording reading (waiting for y): {latest_reading_left}")  # Debugging statement
                    thisExp.addData('Readings_left', latest_reading_left)  # Add the latest reading to the experiment data
                    waiting_for_y_left = False  # Reset the flag
        
        # Check for concordant readings
        if not frequency_updated and len(readings_left) >= 3:
            most_common_reading = max(set(readings_left), key=readings_left.count)
            if readings_left.count(most_common_reading) >= 3 or len(readings_left) > 10:
                if frequency_index_left < len(frequencies) - 1:
                    frequency_index_left += 1  # Move to next frequency
                    frequency_left = frequencies[frequency_index_left]  # Update frequency
                    current_dB_left = 30.0  # Reset dB level for the new frequency
                    upper_lim_left = upper_limits[frequency_left]  # Reset upper limit for the new frequency
                    reversals_left = 0  # Reset reversals for the new frequency
                    reading_num_left = 0  # Reset reading number for the new frequency
                    trial_num_left = 0  # Reset trial number for the new frequency
                    user_resp_left = []  # Reset user responses for the new frequency
                    readings_left = []  # Reset readings for the new frequency
                    next_freq_message_left = f"Next frequency: {frequency_left} Hz"  # Update the message variable
                    print(f"Normal trials triggered frequency change: {frequency_left} Hz (Index: {frequency_index_left})")
                else:
                    trials_left.finished = True  # End the experiment if all frequencies are done
                    print("All frequencies tested, ending Left Ear")
        # Add data to the experiment
        thisExp.addData('Level_left', current_dB_left)
        trial_num_left += 1
        
        # Print the final filename for debugging
        print(f"Final filename: {current_filename_left}")
        sound_left.pause()  # ensure sound has stopped at end of Routine
        # store data for trials_left (TrialHandler)
        trials_left.addData('mouse_left.x', mouse_left.x)
        trials_left.addData('mouse_left.y', mouse_left.y)
        trials_left.addData('mouse_left.leftButton', mouse_left.leftButton)
        trials_left.addData('mouse_left.midButton', mouse_left.midButton)
        trials_left.addData('mouse_left.rightButton', mouse_left.rightButton)
        trials_left.addData('mouse_left.time', mouse_left.time)
        trials_left.addData('mouse_left.clicked_name', mouse_left.clicked_name)
        # the Routine "trial_left" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[textBlank],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        thisExp.addData('blank500.started', blank500.tStart)
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        # if trial has changed, end Routine now
        if isinstance(trials_left, data.TrialHandler2) and thisTrials_left.thisN != trials_left.thisTrial.thisN:
            continueRoutine = False
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textBlank* updates
            
            # if textBlank is starting this frame...
            if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBlank.frameNStart = frameN  # exact frame index
                textBlank.tStart = t  # local t and not account for scr refresh
                textBlank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlank.started')
                # update status
                textBlank.status = STARTED
                textBlank.setAutoDraw(True)
            
            # if textBlank is active this frame...
            if textBlank.status == STARTED:
                # update params
                pass
            
            # if textBlank is stopping this frame...
            if textBlank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    textBlank.tStop = t  # not accounting for scr refresh
                    textBlank.tStopRefresh = tThisFlipGlobal  # on global time
                    textBlank.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textBlank.stopped')
                    # update status
                    textBlank.status = FINISHED
                    textBlank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank500.stopped', blank500.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 500.0 repeats of 'trials_left'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "blank500" ---
    # create an object to store info about Routine blank500
    blank500 = data.Routine(
        name='blank500',
        components=[textBlank],
    )
    blank500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for blank500
    blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blank500.tStart = globalClock.getTime(format='float')
    blank500.status = STARTED
    thisExp.addData('blank500.started', blank500.tStart)
    blank500.maxDuration = None
    # keep track of which components have finished
    blank500Components = blank500.components
    for thisComponent in blank500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    blank500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank* updates
        
        # if textBlank is starting this frame...
        if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.tStart = t  # local t and not account for scr refresh
            textBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textBlank.started')
            # update status
            textBlank.status = STARTED
            textBlank.setAutoDraw(True)
        
        # if textBlank is active this frame...
        if textBlank.status == STARTED:
            # update params
            pass
        
        # if textBlank is stopping this frame...
        if textBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank.tStop = t  # not accounting for scr refresh
                textBlank.tStopRefresh = tThisFlipGlobal  # on global time
                textBlank.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlank.stopped')
                # update status
                textBlank.status = FINISHED
                textBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            blank500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blank500
    blank500.tStop = globalClock.getTime(format='float')
    blank500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('blank500.stopped', blank500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if blank500.maxDurationReached:
        routineTimer.addTime(-blank500.maxDuration)
    elif blank500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Int_Message" ---
    # create an object to store info about Routine Int_Message
    Int_Message = data.Routine(
        name='Int_Message',
        components=[textInterval],
    )
    Int_Message.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Int_Message
    Int_Message.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Int_Message.tStart = globalClock.getTime(format='float')
    Int_Message.status = STARTED
    thisExp.addData('Int_Message.started', Int_Message.tStart)
    Int_Message.maxDuration = None
    # keep track of which components have finished
    Int_MessageComponents = Int_Message.components
    for thisComponent in Int_Message.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Int_Message" ---
    Int_Message.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInterval* updates
        
        # if textInterval is starting this frame...
        if textInterval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInterval.frameNStart = frameN  # exact frame index
            textInterval.tStart = t  # local t and not account for scr refresh
            textInterval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInterval, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInterval.started')
            # update status
            textInterval.status = STARTED
            textInterval.setAutoDraw(True)
        
        # if textInterval is active this frame...
        if textInterval.status == STARTED:
            # update params
            pass
        
        # if textInterval is stopping this frame...
        if textInterval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textInterval.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textInterval.tStop = t  # not accounting for scr refresh
                textInterval.tStopRefresh = tThisFlipGlobal  # on global time
                textInterval.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textInterval.stopped')
                # update status
                textInterval.status = FINISHED
                textInterval.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Int_Message.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Int_Message.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Int_Message" ---
    for thisComponent in Int_Message.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Int_Message
    Int_Message.tStop = globalClock.getTime(format='float')
    Int_Message.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Int_Message.stopped', Int_Message.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Int_Message.maxDurationReached:
        routineTimer.addTime(-Int_Message.maxDuration)
    elif Int_Message.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "blank500" ---
    # create an object to store info about Routine blank500
    blank500 = data.Routine(
        name='blank500',
        components=[textBlank],
    )
    blank500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for blank500
    blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blank500.tStart = globalClock.getTime(format='float')
    blank500.status = STARTED
    thisExp.addData('blank500.started', blank500.tStart)
    blank500.maxDuration = None
    # keep track of which components have finished
    blank500Components = blank500.components
    for thisComponent in blank500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    blank500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank* updates
        
        # if textBlank is starting this frame...
        if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.tStart = t  # local t and not account for scr refresh
            textBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textBlank.started')
            # update status
            textBlank.status = STARTED
            textBlank.setAutoDraw(True)
        
        # if textBlank is active this frame...
        if textBlank.status == STARTED:
            # update params
            pass
        
        # if textBlank is stopping this frame...
        if textBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank.tStop = t  # not accounting for scr refresh
                textBlank.tStopRefresh = tThisFlipGlobal  # on global time
                textBlank.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlank.stopped')
                # update status
                textBlank.status = FINISHED
                textBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            blank500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blank500
    blank500.tStop = globalClock.getTime(format='float')
    blank500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('blank500.stopped', blank500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if blank500.maxDurationReached:
        routineTimer.addTime(-blank500.maxDuration)
    elif blank500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_right = data.TrialHandler2(
        name='trials_right',
        nReps=500.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(trials_right)  # add the loop to the experiment
    thisTrials_right = trials_right.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_right.rgb)
    if thisTrials_right != None:
        for paramName in thisTrials_right:
            globals()[paramName] = thisTrials_right[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_right in trials_right:
        currentLoop = trials_right
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_right.rgb)
        if thisTrials_right != None:
            for paramName in thisTrials_right:
                globals()[paramName] = thisTrials_right[paramName]
        
        # --- Prepare to start Routine "trial_right" ---
        # create an object to store info about Routine trial_right
        trial_right = data.Routine(
            name='trial_right',
            components=[next_freq_text_right, yes_button_right, no_button_right, sound_right, mouse_right],
        )
        trial_right.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codetrials_right
        # Update the filename based on the current frequency and dB level
        current_filename_right = f"{sound_file_path}{frequency_right}_{current_dB_right:.1f}_right.wav"
        
        # Check if the current_dB has crossed the limits
        #if current_dB_right > upper_lim_right or current_dB_right < lower_lim_right:
        #    print("Error! You have crossed the limit of this audiometer.")
        #    crossed_limit_right = True  # Set the flag if current_dB crosses the limit
        #else:
        #    crossed_limit_right = False
        
        # Print the current filename and dB level for debugging
        print(f"Filename: {current_filename_right}")
        print(f"Current dB (right): {current_dB_right}")
        
        # Set the sound file explicitly
        sound_right.setSound(current_filename_right, secs=30.0, hamming=False)
        # Initialize play_limit_sound and crossed_limit
        #play_limit_sound = False
        #crossed_limit = False
        #limit_reached = False  # New flag to indicate if the limit has been reached
        #limit_type = None  # New variable to indicate which limit was reached ('upper' or 'lower')
        yes_button_right.setImage('Mouse/Yes.png')
        no_button_right.setImage('Mouse/No.png')
        sound_right.setSound(current_filename_right, secs=30.0, hamming=False)
        sound_right.setVolume(1.0, log=False)
        sound_right.seek(0)
        # setup some python lists for storing info about the mouse_right
        mouse_right.x = []
        mouse_right.y = []
        mouse_right.leftButton = []
        mouse_right.midButton = []
        mouse_right.rightButton = []
        mouse_right.time = []
        mouse_right.clicked_name = []
        gotValidClick = False  # until a click is received
        mouse_right.mouseClock.reset()
        # store start times for trial_right
        trial_right.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial_right.tStart = globalClock.getTime(format='float')
        trial_right.status = STARTED
        thisExp.addData('trial_right.started', trial_right.tStart)
        trial_right.maxDuration = None
        # keep track of which components have finished
        trial_rightComponents = trial_right.components
        for thisComponent in trial_right.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_right" ---
        # if trial has changed, end Routine now
        if isinstance(trials_right, data.TrialHandler2) and thisTrials_right.thisN != trials_right.thisTrial.thisN:
            continueRoutine = False
        trial_right.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *next_freq_text_right* updates
            
            # if next_freq_text_right is active this frame...
            if next_freq_text_right.status == STARTED:
                # update params
                pass
            
            # *yes_button_right* updates
            
            # if yes_button_right is starting this frame...
            if yes_button_right.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                yes_button_right.frameNStart = frameN  # exact frame index
                yes_button_right.tStart = t  # local t and not account for scr refresh
                yes_button_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yes_button_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'yes_button_right.started')
                # update status
                yes_button_right.status = STARTED
                yes_button_right.setAutoDraw(True)
            
            # if yes_button_right is active this frame...
            if yes_button_right.status == STARTED:
                # update params
                pass
            
            # *no_button_right* updates
            
            # if no_button_right is starting this frame...
            if no_button_right.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                no_button_right.frameNStart = frameN  # exact frame index
                no_button_right.tStart = t  # local t and not account for scr refresh
                no_button_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no_button_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'no_button_right.started')
                # update status
                no_button_right.status = STARTED
                no_button_right.setAutoDraw(True)
            
            # if no_button_right is active this frame...
            if no_button_right.status == STARTED:
                # update params
                pass
            
            # *sound_right* updates
            
            # if sound_right is starting this frame...
            if sound_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_right.frameNStart = frameN  # exact frame index
                sound_right.tStart = t  # local t and not account for scr refresh
                sound_right.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_right.started', tThisFlipGlobal)
                # update status
                sound_right.status = STARTED
                sound_right.play(when=win)  # sync with win flip
            
            # if sound_right is stopping this frame...
            if sound_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_right.tStartRefresh + 30.0-frameTolerance or sound_right.isFinished:
                    # keep track of stop time/frame for later
                    sound_right.tStop = t  # not accounting for scr refresh
                    sound_right.tStopRefresh = tThisFlipGlobal  # on global time
                    sound_right.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sound_right.stopped')
                    # update status
                    sound_right.status = FINISHED
                    sound_right.stop()
            # *mouse_right* updates
            
            # if mouse_right is starting this frame...
            if mouse_right.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                mouse_right.frameNStart = frameN  # exact frame index
                mouse_right.tStart = t  # local t and not account for scr refresh
                mouse_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mouse_right.started')
                # update status
                mouse_right.status = STARTED
                prevButtonState = mouse_right.getPressed()  # if button is down already this ISN'T a new click
            if mouse_right.status == STARTED:  # only update if started and not finished!
                x, y = mouse_right.getPos()
                mouse_right.x.append(x)
                mouse_right.y.append(y)
                buttons = mouse_right.getPressed()
                mouse_right.leftButton.append(buttons[0])
                mouse_right.midButton.append(buttons[1])
                mouse_right.rightButton.append(buttons[2])
                mouse_right.time.append(mouse_right.mouseClock.getTime())
                buttons = mouse_right.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames((yes_button_right,no_button_right), namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_right):
                                gotValidClick = True
                                mouse_right.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse_right.clicked_name.append(None)
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[sound_right]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial_right.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_right.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_right" ---
        for thisComponent in trial_right.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial_right
        trial_right.tStop = globalClock.getTime(format='float')
        trial_right.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial_right.stopped', trial_right.tStop)
        # Run 'End Routine' code from codetrials_right
        # Store the current_dB value before updating it
        previous_dB_right = current_dB_right
        
        # Check for mouse clicks on "Yes" or "No" buttons
        clicked_button = None
        while clicked_button is None:
            if mouse_right.isPressedIn(yes_button_right):
                clicked_button = 'y'
            elif mouse_right.isPressedIn(no_button_right):
                clicked_button = 'n'
            core.wait(0.01)
        
        # Update current_dB based on the clicked button
        if clicked_button == 'y':
            print("Yes button clicked")  # Debugging statement
            user_resp_right.append('y')
            current_dB_right -= step * 2
        elif clicked_button == 'n':
            print("No button clicked")  # Debugging statement
            user_resp_right.append('n')
            current_dB_right += step
        
        # Ensure current_dB stays within the defined limits
        if lower_lim_right <= current_dB_right <= upper_lim_right:
            current_filename_right = f"{sound_file_path}{frequency_right}_{current_dB_right:.1f}_right.wav"
            dummy_play_count_right = 0  # Reset dummy play count if within limits
            limit_played_right = False  # Reset limit played flag
        elif current_dB_right > upper_lim_right:
            print("Current dB exceeds upper limit")
            current_dB_right = upper_lim_right  # Ensure current_dB does not exceed upper limit
            if not limit_played_right:
                current_filename_right = f"{sound_file_path}{frequency_right}_{upper_lim_right:.1f}_right.wav"
                limit_played_right = True  # Mark that the limit sound has been played
                print("Playing upper limit sound")
            else:
                if 'n' in user_resp_right[-1]:
                    # Skip to the next frequency
                    frequency_index_right += 1
                    if frequency_index_right < len(frequencies):
                        frequency_right = frequencies[frequency_index_right]
                        current_dB_right = 30.0  # Reset dB for new frequency
                        upper_lim_right = upper_limits[frequency_right]
                        reversals_right = 0
                        reading_num_right = 0
                        trial_num_right = 0
                        user_resp_right = []  # Reset user responses for the new frequency
                        readings_right = []  # Reset readings for the new frequency
                        frequency_updated = False  # ✅ Reset the flag for the new frequency
                        next_freq_message_right = f"Next frequency: {frequency_right} Hz"
                        print(f"Moving to next frequency: {frequency_right} Hz")
                    else:
                        trials_right.finished = True  # End experiment if all frequencies are done
                        print("All frequencies tested, ending Right Ear")
        elif current_dB_right < lower_lim_right:
            print("Current dB below lower limit")
            current_dB_right = lower_lim_right  # Ensure current_dB does not go below lower limit
            if not limit_played_right:
                current_filename_right = f"{sound_file_path}{frequency_right}_{lower_lim_right:.1f}_right.wav"
                limit_played_right = True  # Mark that the limit sound has been played
                print("Playing lower limit sound")
                sound_right.setSound(current_filename_right, secs=30.0, hamming=False)
                sound_right.play()
            else:
                event.clearEvents(eventType='mouse')  # Clear mouse events before detecting clicks
                while not any(mouse_right.getPressed()):
                    pass
                if mouse_right.isPressedIn(yes_button_right):
                    print("Yes button clicked during dummy trial")
                    dummy_play_count_right = 0
                    y_count = 0
                    n_count = 0
                    while dummy_play_count_right < 3:
                        event.clearEvents(eventType='mouse')  # Clear previous events
                        print(f"Playing dummy.wav {dummy_play_count_right + 1} time(s)")
                        
                        # Show a blank screen briefly between trials
                        win.color = (0, 0, 0)  # Set screen to black (or another neutral color)
                        win.flip()
                        core.wait(0.5)  # Keep the screen blank for 500ms
                        
                        # Restore original screen and redraw buttons
                        win.color = (0, 0, 0)  # Assuming white background, adjust as needed
                        yes_button_right.draw()
                        no_button_right.draw()
                        win.flip()
                        
                        sound_right.setSound(dummy_file_path, secs=30.0, hamming=False)
                        sound_right.play()
                        
                        click_detected = False
                        while not click_detected:
                            if any(mouse_right.getPressed()):
                                if mouse_right.isPressedIn(yes_button_right):
                                    print("Yes button clicked during dummy trial playback")
                                    y_count += 1
                                    thisExp.addData(f'dummy_response_{dummy_play_count_right + 1}_right', 'y')
                                    click_detected = True
                                elif mouse_right.isPressedIn(no_button_right):
                                    print("No button clicked during dummy trial playback")
                                    n_count += 1
                                    thisExp.addData(f'dummy_response_{dummy_play_count_right + 1}_right', 'n')
                                    click_detected = True
                            core.wait(0.01)  # Prevent high CPU usage
                        dummy_play_count_right += 1
                    if y_count >= 2:
                        frequency_index_right += 1
                        if frequency_index_right < len(frequencies):
                            frequency_right = frequencies[frequency_index_right]
                            current_dB_right = 30.0
                            upper_lim_right = upper_limits[frequency_right]
                            reversals_right = 0
                            reading_num_right = 0
                            trial_num_right = 0
                            user_resp_right = []
                            readings_right = []  # Reset readings for the new frequency
                            frequency_updated = False  # ✅ Reset the flag for the new frequency
                            print(f"Moving to next frequency: {frequency_right} Hz")
                        else:
                            trials_right.finished = True
                            print("All frequencies tested, ending experiment")
                    elif n_count >= 2:
                        dummy_trial_repeats += 1
                        thisExp.addData('Level_right', -20)
                        readings_right.append(-20)
                        if dummy_trial_repeats < 3:
                            # Go back to the lower limit and start again
                            current_dB_right = lower_lim_right
                            print(f"Restarting from lower limit: {current_dB_right}")
                        else:
                            # Dummy trial concordant check
                            if readings_right.count(-20) >= 3 and dummy_trial_repeats >= 3:
                                if not frequency_updated:  # Ensure frequency update happens only once
                                    if frequency_index_right < len(frequencies) - 1:
                                        frequency_index_right += 1  # Move to next frequency
                                        frequency_right = frequencies[frequency_index_right]  # Update frequency
                                        frequency_updated = True  # Mark that the frequency has been updated
                                        current_dB_right = 30.0  # Reset dB for new frequency
                                        upper_lim_right = upper_limits[frequency_right]
                                        reversals_right = 0
                                        reading_num_right = 0
                                        trial_num_right = 0
                                        user_resp_right = []  # Reset user responses for the new frequency
                                        readings_right = []  # Reset readings for the new frequency
                                        frequency_updated = False  # ✅ Reset the flag for the new frequency
                                        next_freq_message_right = f"Next frequency: {frequency_right} Hz"
                                        print(f"Dummy trial triggered frequency change: {frequency_right} Hz (Index: {frequency_index_right})")
                                    else:
                                        trials_right.finished = True  # End experiment
                                        print("All frequencies tested, ending Right Ear")
                elif mouse_right.isPressedIn(no_button_right):
                    print("No button clicked during dummy trial")  # Debugging statement
                    user_resp_right.append('n')
                    print(f"User response right: {user_resp_right}")  # Debugging statement
                    # Continue with the normal procedure
                    current_dB_right += step
        
        # Track user responses and reversals
        print(f"User response right: {user_resp_right}")  # Debugging statement
        if len(user_resp_right) > 1:
            if user_resp_right[-1] != user_resp_right[-2]:
                reversals_right += 1
                print(f"Reversals right: {reversals_right}")  # Debugging statement
                # Track the value of previous_dB at every 2nd reversal
                if reversals_right % 2 == 0:
                    if user_resp_right[-1] == 'n':
                        # Wait for the next 'y' to record the reading
                        waiting_for_y_right = True
                        print("Waiting for next 'y' to record the reading")  # Debugging statement
                    elif user_resp_right[-1] == 'y':
                        latest_reading_right = previous_dB_right
                        readings_right.append(latest_reading_right)
                        reading_num_right += 1
                        print(f"Recording reading (2nd reversal): {latest_reading_right}")  # Debugging statement
                        thisExp.addData('Readings_right', latest_reading_right)  # Add the latest reading to the experiment data
                        waiting_for_y_right = False  # Reset the flag
                elif waiting_for_y_right and user_resp_right[-1] == 'y':
                    latest_reading_right = previous_dB_right
                    readings_right.append(latest_reading_right)
                    reading_num_right += 1
                    print(f"Recording reading (waiting for y): {latest_reading_right}")  # Debugging statement
                    thisExp.addData('Readings_right', latest_reading_right)  # Add the latest reading to the experiment data
                    waiting_for_y_right = False  # Reset the flag
        
        # Check for concordant readings
        if not frequency_updated and len(readings_right) >= 3:
            most_common_reading = max(set(readings_right), key=readings_right.count)
            if readings_right.count(most_common_reading) >= 3 or len(readings_right) > 10:
                if frequency_index_right < len(frequencies) - 1:
                    frequency_index_right += 1  # Move to next frequency
                    frequency_right = frequencies[frequency_index_right]  # Update frequency
                    current_dB_right = 30.0  # Reset dB level for the new frequency
                    upper_lim_right = upper_limits[frequency_right]  # Reset upper limit for the new frequency
                    reversals_right = 0  # Reset reversals for the new frequency
                    reading_num_right = 0  # Reset reading number for the new frequency
                    trial_num_right = 0  # Reset trial number for the new frequency
                    user_resp_right = []  # Reset user responses for the new frequency
                    readings_right = []  # Reset readings for the new frequency
                    next_freq_message_right = f"Next frequency: {frequency_right} Hz"  # Update the message variable
                    print(f"Normal trials triggered frequency change: {frequency_right} Hz (Index: {frequency_index_right})")
                else:
                    trials_right.finished = True  # End the experiment if all frequencies are done
                    print("All frequencies tested, ending Right Ear")
        # Add data to the experiment
        thisExp.addData('Level_right', current_dB_right)
        trial_num_right += 1
        
        # Print the final filename for debugging
        print(f"Final filename: {current_filename_right}")
        sound_right.pause()  # ensure sound has stopped at end of Routine
        # store data for trials_right (TrialHandler)
        trials_right.addData('mouse_right.x', mouse_right.x)
        trials_right.addData('mouse_right.y', mouse_right.y)
        trials_right.addData('mouse_right.leftButton', mouse_right.leftButton)
        trials_right.addData('mouse_right.midButton', mouse_right.midButton)
        trials_right.addData('mouse_right.rightButton', mouse_right.rightButton)
        trials_right.addData('mouse_right.time', mouse_right.time)
        trials_right.addData('mouse_right.clicked_name', mouse_right.clicked_name)
        # the Routine "trial_right" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[textBlank],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        thisExp.addData('blank500.started', blank500.tStart)
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        # if trial has changed, end Routine now
        if isinstance(trials_right, data.TrialHandler2) and thisTrials_right.thisN != trials_right.thisTrial.thisN:
            continueRoutine = False
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textBlank* updates
            
            # if textBlank is starting this frame...
            if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBlank.frameNStart = frameN  # exact frame index
                textBlank.tStart = t  # local t and not account for scr refresh
                textBlank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlank.started')
                # update status
                textBlank.status = STARTED
                textBlank.setAutoDraw(True)
            
            # if textBlank is active this frame...
            if textBlank.status == STARTED:
                # update params
                pass
            
            # if textBlank is stopping this frame...
            if textBlank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    textBlank.tStop = t  # not accounting for scr refresh
                    textBlank.tStopRefresh = tThisFlipGlobal  # on global time
                    textBlank.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textBlank.stopped')
                    # update status
                    textBlank.status = FINISHED
                    textBlank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank500.stopped', blank500.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 500.0 repeats of 'trials_right'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "blank500" ---
    # create an object to store info about Routine blank500
    blank500 = data.Routine(
        name='blank500',
        components=[textBlank],
    )
    blank500.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for blank500
    blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blank500.tStart = globalClock.getTime(format='float')
    blank500.status = STARTED
    thisExp.addData('blank500.started', blank500.tStart)
    blank500.maxDuration = None
    # keep track of which components have finished
    blank500Components = blank500.components
    for thisComponent in blank500.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    blank500.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank* updates
        
        # if textBlank is starting this frame...
        if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.tStart = t  # local t and not account for scr refresh
            textBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textBlank.started')
            # update status
            textBlank.status = STARTED
            textBlank.setAutoDraw(True)
        
        # if textBlank is active this frame...
        if textBlank.status == STARTED:
            # update params
            pass
        
        # if textBlank is stopping this frame...
        if textBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank.tStop = t  # not accounting for scr refresh
                textBlank.tStopRefresh = tThisFlipGlobal  # on global time
                textBlank.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textBlank.stopped')
                # update status
                textBlank.status = FINISHED
                textBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            blank500.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blank500
    blank500.tStop = globalClock.getTime(format='float')
    blank500.tStopRefresh = tThisFlipGlobal
    thisExp.addData('blank500.stopped', blank500.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if blank500.maxDurationReached:
        routineTimer.addTime(-blank500.maxDuration)
    elif blank500.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "EndScreen" ---
    # create an object to store info about Routine EndScreen
    EndScreen = data.Routine(
        name='EndScreen',
        components=[textEnd, key_respEnd],
    )
    EndScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_respEnd
    key_respEnd.keys = []
    key_respEnd.rt = []
    _key_respEnd_allKeys = []
    # store start times for EndScreen
    EndScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EndScreen.tStart = globalClock.getTime(format='float')
    EndScreen.status = STARTED
    thisExp.addData('EndScreen.started', EndScreen.tStart)
    EndScreen.maxDuration = None
    # keep track of which components have finished
    EndScreenComponents = EndScreen.components
    for thisComponent in EndScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndScreen" ---
    EndScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textEnd* updates
        
        # if textEnd is starting this frame...
        if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEnd.frameNStart = frameN  # exact frame index
            textEnd.tStart = t  # local t and not account for scr refresh
            textEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textEnd.started')
            # update status
            textEnd.status = STARTED
            textEnd.setAutoDraw(True)
        
        # if textEnd is active this frame...
        if textEnd.status == STARTED:
            # update params
            pass
        
        # *key_respEnd* updates
        waitOnFlip = False
        
        # if key_respEnd is starting this frame...
        if key_respEnd.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_respEnd.frameNStart = frameN  # exact frame index
            key_respEnd.tStart = t  # local t and not account for scr refresh
            key_respEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_respEnd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_respEnd.started')
            # update status
            key_respEnd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_respEnd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_respEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_respEnd.status == STARTED and not waitOnFlip:
            theseKeys = key_respEnd.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_respEnd_allKeys.extend(theseKeys)
            if len(_key_respEnd_allKeys):
                key_respEnd.keys = _key_respEnd_allKeys[-1].name  # just the last key pressed
                key_respEnd.rt = _key_respEnd_allKeys[-1].rt
                key_respEnd.duration = _key_respEnd_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EndScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndScreen" ---
    for thisComponent in EndScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EndScreen
    EndScreen.tStop = globalClock.getTime(format='float')
    EndScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EndScreen.stopped', EndScreen.tStop)
    # check responses
    if key_respEnd.keys in ['', [], None]:  # No response was made
        key_respEnd.keys = None
    thisExp.addData('key_respEnd.keys',key_respEnd.keys)
    if key_respEnd.keys != None:  # we had a response
        thisExp.addData('key_respEnd.rt', key_respEnd.rt)
        thisExp.addData('key_respEnd.duration', key_respEnd.duration)
    thisExp.nextEntry()
    # the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
