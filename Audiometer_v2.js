/********************** 
 * Audiometer_V2 *
 **********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Audiometer_v2';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeScreenRoutineBegin());
flowScheduler.add(WelcomeScreenRoutineEachFrame());
flowScheduler.add(WelcomeScreenRoutineEnd());
flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
const trials_leftLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_leftLoopBegin(trials_leftLoopScheduler));
flowScheduler.add(trials_leftLoopScheduler);
flowScheduler.add(trials_leftLoopEnd);



flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
flowScheduler.add(Int_MessageRoutineBegin());
flowScheduler.add(Int_MessageRoutineEachFrame());
flowScheduler.add(Int_MessageRoutineEnd());
flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
const trials_rightLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_rightLoopBegin(trials_rightLoopScheduler));
flowScheduler.add(trials_rightLoopScheduler);
flowScheduler.add(trials_rightLoopEnd);



flowScheduler.add(blank500RoutineBegin());
flowScheduler.add(blank500RoutineEachFrame());
flowScheduler.add(blank500RoutineEnd());
flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Mouse/Yes.png', 'path': 'Mouse/Yes.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'Mouse/No.png', 'path': 'Mouse/No.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var WelcomeScreenClock;
var textWelc;
var textExplain;
var key_respStart;
var blank500Clock;
var textBlank;
var trial_leftClock;
var step;
var sound_file_path;
var dummy_file_path;
var frequencies;
var lower_lim_left;
var upper_limits;
var current_dB_left;
var frequency_index_left;
var frequency_left;
var upper_lim_left;
var reversals_left;
var reading_num_left;
var trial_num_left;
var user_resp_left;
var readings_left;
var dummy_play_count_left;
var limit_played_left;
var waiting_for_y_left;
var dummy_trial_repeats;
var frequency_updated;
var next_freq_text_left;
var yes_button_left;
var no_button_left;
var sound_left;
var mouse_left;
var Int_MessageClock;
var textInterval;
var trial_rightClock;
var lower_lim_right;
var trial_num_right;
var reading_num_right;
var user_resp_right;
var reversals_right;
var readings_right;
var frequency_index_right;
var frequency_right;
var upper_lim_right;
var current_dB_right;
var current_filename_right;
var next_freq_message_right;
var latest_reading_right;
var waiting_for_y_right;
var dummy_play_count_right;
var limit_played_right;
var dummy_responses_right;
var next_freq_text_right;
var yes_button_right;
var no_button_right;
var sound_right;
var mouse_right;
var EndScreenClock;
var textEnd;
var key_respEnd;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  textWelc = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelc',
    text: 'Welcome to the experiment!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textExplain = new visual.TextStim({
    win: psychoJS.window,
    name: 'textExplain',
    text: "This is an audiometry test to measure your absolute threshold of hearing. \n\nYou will be presented with sounds of different frequencies, following which you have to indicate if you hear them (by pressing the 'Yes' button) or not (by pressing the 'No' button).\n\nYou will first hear sounds from your left ear, followed by sounds from your right ear.\n\nPress SPACEBAR to start.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_respStart = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blank500"
  blank500Clock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial_left"
  trial_leftClock = new util.Clock();
  // Run 'Begin Experiment' code from codetrials_left
  step = 5;
  sound_file_path = "Audio_unramped/";
  dummy_file_path = `${sound_file_path}dummy.wav`;
  frequencies = [125, 250, 500, 1000, 2000, 4000, 6000, 8000];
  lower_lim_left = (- 20.0);
  upper_limits = {[125]: 40.0, [250]: 50.0, [500]: 60.0, [1000]: 70.0, [2000]: 70.0, [4000]: 60.0, [6000]: 50.0, [8000]: 50.0};
  current_dB_left = 30.0;
  frequency_index_left = 0;
  frequency_left = frequencies[frequency_index_left];
  upper_lim_left = upper_limits[frequency_left];
  reversals_left = 0;
  reading_num_left = 0;
  trial_num_left = 0;
  user_resp_left = [];
  readings_left = [];
  dummy_play_count_left = 0;
  limit_played_left = false;
  waiting_for_y_left = false;
  dummy_trial_repeats = 0;
  frequency_updated = false;
  
  next_freq_text_left = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_freq_text_left',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  yes_button_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'yes_button_left', units : 'cm', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 8), 0], 
    draggable: false,
    size : [5, 5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  no_button_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'no_button_left', units : 'cm', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [8, 0], 
    draggable: false,
    size : [5, 5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  sound_left = new sound.Sound({
      win: psychoJS.window,
      value: 'A',
      secs: (- 1),
      });
  sound_left.setVolume(1.0);
  mouse_left = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_left.mouseClock = new util.Clock();
  // Initialize components for Routine "Int_Message"
  Int_MessageClock = new util.Clock();
  textInterval = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInterval',
    text: 'All trials for the left ear have finished. We will now proceed to the trials for the right ear.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial_right"
  trial_rightClock = new util.Clock();
  // Run 'Begin Experiment' code from codetrials_right
  step = 5;
  sound_file_path = "Audio_Regen/";
  dummy_file_path = `${sound_file_path}dummy.wav`;
  frequencies = [125, 250, 500, 1000, 2000, 4000, 6000, 8000];
  lower_lim_right = (- 20);
  upper_limits = {[125]: 40, [250]: 50, [500]: 60, [1000]: 70, [2000]: 70, [4000]: 60, [6000]: 50, [8000]: 50};
  trial_num_right = 0;
  reading_num_right = 0;
  user_resp_right = [];
  reversals_right = 0;
  readings_right = [];
  frequency_index_right = 0;
  frequency_right = frequencies[frequency_index_right];
  upper_lim_right = upper_limits[frequency_right];
  current_dB_right = 30.0;
  current_filename_right = `${sound_file_path}${frequency_right}_${util.pad(Number.parseFloat(current_dB_right).toFixed(1), 1)}_right.wav`;
  next_freq_message_right = "";
  latest_reading_right = null;
  waiting_for_y_right = false;
  dummy_play_count_right = 0;
  limit_played_right = false;
  dummy_responses_right = [];
  dummy_trial_repeats = 0;
  
  next_freq_text_right = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_freq_text_right',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  yes_button_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'yes_button_right', units : 'cm', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 8), 0], 
    draggable: false,
    size : [5, 5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  no_button_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'no_button_right', units : 'cm', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [8, 0], 
    draggable: false,
    size : [5, 5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  sound_right = new sound.Sound({
      win: psychoJS.window,
      value: 'A',
      secs: (- 1),
      });
  sound_right.setVolume(1.0);
  mouse_right = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_right.mouseClock = new util.Clock();
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  textEnd = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEnd',
    text: 'Thanks for participating in this experiment! Please notify the experimenter about the completion.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_respEnd = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var WelcomeScreenMaxDurationReached;
var _key_respStart_allKeys;
var WelcomeScreenMaxDuration;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'WelcomeScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    WelcomeScreenClock.reset();
    routineTimer.reset();
    WelcomeScreenMaxDurationReached = false;
    // update component parameters for each repeat
    key_respStart.keys = undefined;
    key_respStart.rt = undefined;
    _key_respStart_allKeys = [];
    psychoJS.experiment.addData('WelcomeScreen.started', globalClock.getTime());
    WelcomeScreenMaxDuration = null
    // keep track of which components have finished
    WelcomeScreenComponents = [];
    WelcomeScreenComponents.push(textWelc);
    WelcomeScreenComponents.push(textExplain);
    WelcomeScreenComponents.push(key_respStart);
    
    for (const thisComponent of WelcomeScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function WelcomeScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WelcomeScreen' ---
    // get current time
    t = WelcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelc* updates
    if (t >= 0.0 && textWelc.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelc.tStart = t;  // (not accounting for frame time here)
      textWelc.frameNStart = frameN;  // exact frame index
      
      textWelc.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textWelc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textWelc.setAutoDraw(false);
    }
    
    
    // *textExplain* updates
    if (t >= 1.0 && textExplain.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textExplain.tStart = t;  // (not accounting for frame time here)
      textExplain.frameNStart = frameN;  // exact frame index
      
      textExplain.setAutoDraw(true);
    }
    
    
    // *key_respStart* updates
    if (t >= 3.0 && key_respStart.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respStart.tStart = t;  // (not accounting for frame time here)
      key_respStart.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respStart.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respStart.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respStart.clearEvents(); });
    }
    
    if (key_respStart.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respStart.getKeys({keyList: ['space'], waitRelease: false});
      _key_respStart_allKeys = _key_respStart_allKeys.concat(theseKeys);
      if (_key_respStart_allKeys.length > 0) {
        key_respStart.keys = _key_respStart_allKeys[_key_respStart_allKeys.length - 1].name;  // just the last key pressed
        key_respStart.rt = _key_respStart_allKeys[_key_respStart_allKeys.length - 1].rt;
        key_respStart.duration = _key_respStart_allKeys[_key_respStart_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WelcomeScreen' ---
    for (const thisComponent of WelcomeScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('WelcomeScreen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respStart.corr, level);
    }
    psychoJS.experiment.addData('key_respStart.keys', key_respStart.keys);
    if (typeof key_respStart.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respStart.rt', key_respStart.rt);
        psychoJS.experiment.addData('key_respStart.duration', key_respStart.duration);
        routineTimer.reset();
        }
    
    key_respStart.stop();
    // the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blank500MaxDurationReached;
var blank500MaxDuration;
var blank500Components;
function blank500RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blank500' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    blank500Clock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    blank500MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('blank500.started', globalClock.getTime());
    blank500MaxDuration = null
    // keep track of which components have finished
    blank500Components = [];
    blank500Components.push(textBlank);
    
    for (const thisComponent of blank500Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blank500RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank500' ---
    // get current time
    t = blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textBlank* updates
    if (t >= 0.0 && textBlank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textBlank.tStart = t;  // (not accounting for frame time here)
      textBlank.frameNStart = frameN;  // exact frame index
      
      textBlank.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textBlank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textBlank.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blank500Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blank500RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank500' ---
    for (const thisComponent of blank500Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('blank500.stopped', globalClock.getTime());
    if (blank500MaxDurationReached) {
        blank500Clock.add(blank500MaxDuration);
    } else {
        blank500Clock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_left;
function trials_leftLoopBegin(trials_leftLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_left = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 500, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_left'
    });
    psychoJS.experiment.addLoop(trials_left); // add the loop to the experiment
    currentLoop = trials_left;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_left of trials_left) {
      snapshot = trials_left.getSnapshot();
      trials_leftLoopScheduler.add(importConditions(snapshot));
      trials_leftLoopScheduler.add(trial_leftRoutineBegin(snapshot));
      trials_leftLoopScheduler.add(trial_leftRoutineEachFrame());
      trials_leftLoopScheduler.add(trial_leftRoutineEnd(snapshot));
      trials_leftLoopScheduler.add(blank500RoutineBegin(snapshot));
      trials_leftLoopScheduler.add(blank500RoutineEachFrame());
      trials_leftLoopScheduler.add(blank500RoutineEnd(snapshot));
      trials_leftLoopScheduler.add(trials_leftLoopEndIteration(trials_leftLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_leftLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_left);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_leftLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_right;
function trials_rightLoopBegin(trials_rightLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_right = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 500, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_right'
    });
    psychoJS.experiment.addLoop(trials_right); // add the loop to the experiment
    currentLoop = trials_right;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_right of trials_right) {
      snapshot = trials_right.getSnapshot();
      trials_rightLoopScheduler.add(importConditions(snapshot));
      trials_rightLoopScheduler.add(trial_rightRoutineBegin(snapshot));
      trials_rightLoopScheduler.add(trial_rightRoutineEachFrame());
      trials_rightLoopScheduler.add(trial_rightRoutineEnd(snapshot));
      trials_rightLoopScheduler.add(blank500RoutineBegin(snapshot));
      trials_rightLoopScheduler.add(blank500RoutineEachFrame());
      trials_rightLoopScheduler.add(blank500RoutineEnd(snapshot));
      trials_rightLoopScheduler.add(trials_rightLoopEndIteration(trials_rightLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_rightLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_right);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_rightLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trial_leftMaxDurationReached;
var current_filename_left;
var gotValidClick;
var trial_leftMaxDuration;
var trial_leftComponents;
function trial_leftRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_left' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trial_leftClock.reset();
    routineTimer.reset();
    trial_leftMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codetrials_left
    current_filename_left = `${sound_file_path}${frequency_left}_${util.pad(Number.parseFloat(current_dB_left).toFixed(1), 1)}_left.wav`;
    sound_left.setSound(current_filename_left, {"secs": 30.0, "hamming": false});
    console.log(`Filename: ${current_filename_left}`);
    console.log(`Current dB (left): ${current_dB_left}`);
    
    yes_button_left.setImage('Mouse/Yes.png');
    no_button_left.setImage('Mouse/No.png');
    sound_left.setValue(current_filename_left);
    sound_left.secs=30.0;
    sound_left.setVolume(1.0);
    // setup some python lists for storing info about the mouse_left
    // current position of the mouse:
    mouse_left.x = [];
    mouse_left.y = [];
    mouse_left.leftButton = [];
    mouse_left.midButton = [];
    mouse_left.rightButton = [];
    mouse_left.time = [];
    mouse_left.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouse_left.mouseClock.reset();
    psychoJS.experiment.addData('trial_left.started', globalClock.getTime());
    trial_leftMaxDuration = null
    // keep track of which components have finished
    trial_leftComponents = [];
    trial_leftComponents.push(next_freq_text_left);
    trial_leftComponents.push(yes_button_left);
    trial_leftComponents.push(no_button_left);
    trial_leftComponents.push(sound_left);
    trial_leftComponents.push(mouse_left);
    
    for (const thisComponent of trial_leftComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function trial_leftRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_left' ---
    // get current time
    t = trial_leftClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *next_freq_text_left* updates
    
    // *yes_button_left* updates
    if (t >= 0.3 && yes_button_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yes_button_left.tStart = t;  // (not accounting for frame time here)
      yes_button_left.frameNStart = frameN;  // exact frame index
      
      yes_button_left.setAutoDraw(true);
    }
    
    
    // *no_button_left* updates
    if (t >= 0.3 && no_button_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_button_left.tStart = t;  // (not accounting for frame time here)
      no_button_left.frameNStart = frameN;  // exact frame index
      
      no_button_left.setAutoDraw(true);
    }
    
    // start/stop sound_left
    if (t >= 0.0 && sound_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_left.tStart = t;  // (not accounting for frame time here)
      sound_left.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_left.play(); });  // screen flip
      sound_left.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (sound_left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (t >= sound_left.tStart + 0.5) {
        sound_left.stop();  // stop the sound (if longer than duration)
        sound_left.status = PsychoJS.Status.FINISHED;
      }
    }
    // *mouse_left* updates
    if (t >= 0.3 && mouse_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_left.tStart = t;  // (not accounting for frame time here)
      mouse_left.frameNStart = frameN;  // exact frame index
      
      mouse_left.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse_left.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_left.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_left.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_left.clickableObjects = eval([yes_button_left, no_button_left])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_left.clickableObjects)) {
              mouse_left.clickableObjects = [mouse_left.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_left.clickableObjects) {
              if (obj.contains(mouse_left)) {
                  gotValidClick = true;
                  mouse_left.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse_left.clicked_name.push(null);
          }
          _mouseXYs = mouse_left.getPos();
          mouse_left.x.push(_mouseXYs[0]);
          mouse_left.y.push(_mouseXYs[1]);
          mouse_left.leftButton.push(_mouseButtons[0]);
          mouse_left.midButton.push(_mouseButtons[1]);
          mouse_left.rightButton.push(_mouseButtons[2]);
          mouse_left.time.push(mouse_left.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial_leftComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _pj;
var previous_dB_left;
var clicked_button;
var most_common_reading;
var next_freq_message_left;
function trial_leftRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_left' ---
    for (const thisComponent of trial_leftComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial_left.stopped', globalClock.getTime());
    // Run 'End Routine' code from codetrials_left
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    previous_dB_left = current_dB_left;
    clicked_button = null;
    while ((clicked_button === null)) {
        if (mouse_left.isPressedIn(yes_button_left)) {
            clicked_button = "y";
        } else {
            if (mouse_left.isPressedIn(no_button_left)) {
                clicked_button = "n";
            }
        }
        core.wait(0.01);
    }
    if ((clicked_button === "y")) {
        console.log("Yes button clicked");
        user_resp_left.push("y");
        current_dB_left -= (step * 2);
    } else {
        if ((clicked_button === "n")) {
            console.log("No button clicked");
            user_resp_left.push("n");
            current_dB_left += step;
        }
    }
    if (((lower_lim_left <= current_dB_left) && (current_dB_left <= upper_lim_left))) {
        current_filename_left = `${sound_file_path}${frequency_left}_${util.pad(Number.parseFloat(current_dB_left).toFixed(1), 1)}_left.wav`;
        dummy_play_count_left = 0;
        limit_played_left = false;
    } else {
        if ((current_dB_left > upper_lim_left)) {
            console.log("Current dB exceeds upper limit");
            current_dB_left = upper_lim_left;
            if ((! limit_played_left)) {
                current_filename_left = `${sound_file_path}${frequency_left}_${util.pad(Number.parseFloat(upper_lim_left).toFixed(1), 1)}_left.wav`;
                limit_played_left = true;
                console.log("Playing upper limit sound");
            } else {
                if (_pj.in_es6("n", user_resp_left.slice((- 1))[0])) {
                    frequency_index_left += 1;
                    if ((frequency_index_left < frequencies.length)) {
                        frequency_left = frequencies[frequency_index_left];
                        current_dB_left = 30.0;
                        upper_lim_left = upper_limits[frequency_left];
                        reversals_left = 0;
                        reading_num_left = 0;
                        trial_num_left = 0;
                        user_resp_left = [];
                        next_freq_message_left = `Next frequency: ${frequency_left} Hz`;
                        console.log(`Moving to next frequency: ${frequency_left} Hz`);
                    } else {
                        trials_left.finished = true;
                        console.log("All frequencies tested, ending Left Ear");
                    }
                }
            }
        } else {
            if ((current_dB_left < lower_lim_left)) {
                console.log("Current dB below lower limit");
                current_dB_left = lower_lim_left;
                if ((! limit_played_left)) {
                    current_filename_left = `${sound_file_path}${frequency_left}_${util.pad(Number.parseFloat(lower_lim_left).toFixed(1), 1)}_left.wav`;
                    limit_played_left = true;
                    console.log("Playing lower limit sound");
                    sound_left.setSound(current_filename_left, {"secs": 30.0, "hamming": false});
                    sound_left.play();
                } else {
                    psychoJS.eventManager.clearEvents({"eventType": "mouse"});
                    while ((! any(mouse_left.getPressed()))) {
                    }
                    if (mouse_left.isPressedIn(yes_button_left)) {
                        console.log("Yes button clicked during dummy trial");
                        dummy_play_count_left = 0;
                        y_count = 0;
                        n_count = 0;
                        while ((dummy_play_count_left < 3)) {
                            psychoJS.eventManager.clearEvents({"eventType": "mouse"});
                            console.log(`Playing dummy.wav ${(dummy_play_count_left + 1)} time(s)`);
                            psychoJS.window.color = [0, 0, 0];
                            psychoJS.window.flip();
                            core.wait(0.5);
                            psychoJS.window.color = [0, 0, 0];
                            yes_button_left.draw();
                            no_button_left.draw();
                            psychoJS.window.flip();
                            sound_left.setSound(dummy_file_path, {"secs": 30.0, "hamming": false});
                            sound_left.play();
                            click_detected = false;
                            while ((! click_detected)) {
                                if (any(mouse_left.getPressed())) {
                                    if (mouse_left.isPressedIn(yes_button_left)) {
                                        console.log("Yes button clicked during dummy trial playback");
                                        y_count += 1;
                                        psychoJS.experiment.addData(`dummy_response_${(dummy_play_count_left + 1)}_left`, "y");
                                        click_detected = true;
                                    } else {
                                        if (mouse_left.isPressedIn(no_button_left)) {
                                            console.log("No button clicked during dummy trial playback");
                                            n_count += 1;
                                            psychoJS.experiment.addData(`dummy_response_${(dummy_play_count_left + 1)}_left`, "n");
                                            click_detected = true;
                                        }
                                    }
                                }
                                core.wait(0.01);
                            }
                            dummy_play_count_left += 1;
                        }
                        if ((y_count >= 2)) {
                            frequency_index_left += 1;
                            if ((frequency_index_left < frequencies.length)) {
                                frequency_left = frequencies[frequency_index_left];
                                current_dB_left = 30.0;
                                upper_lim_left = upper_limits[frequency_left];
                                reversals_left = 0;
                                reading_num_left = 0;
                                trial_num_left = 0;
                                user_resp_left = [];
                                console.log(`Moving to next frequency: ${frequency_left} Hz`);
                            } else {
                                trials_left.finished = true;
                                console.log("All frequencies tested, ending experiment");
                            }
                        } else {
                            if ((n_count >= 2)) {
                                dummy_trial_repeats += 1;
                                psychoJS.experiment.addData("Level_left", (- 20));
                                readings_left.push((- 20));
                                if ((dummy_trial_repeats < 3)) {
                                    current_dB_left = lower_lim_left;
                                    console.log(`Restarting from lower limit: ${current_dB_left}`);
                                } else {
                                    if (((util.count(readings_left, (- 20)) >= 3) && (dummy_trial_repeats >= 3))) {
                                        if ((! frequency_updated)) {
                                            if ((frequency_index_left < (frequencies.length - 1))) {
                                                frequency_index_left += 1;
                                                frequency_left = frequencies[frequency_index_left];
                                                frequency_updated = true;
                                                current_dB_left = 30.0;
                                                upper_lim_left = upper_limits[frequency_left];
                                                reversals_left = 0;
                                                reading_num_left = 0;
                                                trial_num_left = 0;
                                                user_resp_left = [];
                                                next_freq_message_left = `Next frequency: ${frequency_left} Hz`;
                                                console.log(`Dummy trial triggered frequency change: ${frequency_left} Hz (Index: ${frequency_index_left})`);
                                            } else {
                                                trials_left.finished = true;
                                                console.log("All frequencies tested, ending Left Ear");
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    } else {
                        if (mouse_left.isPressedIn(no_button_left)) {
                            console.log("No button clicked during dummy trial");
                            user_resp_left.push("n");
                            console.log(`User response left: ${user_resp_left}`);
                            current_dB_left += step;
                        }
                    }
                }
            }
        }
    }
    console.log(`User response left: ${user_resp_left}`);
    if ((user_resp_left.length > 1)) {
        if ((user_resp_left.slice((- 1))[0] !== user_resp_left.slice((- 2))[0])) {
            reversals_left += 1;
            console.log(`Reversals left: ${reversals_left}`);
            if (((reversals_left % 2) === 0)) {
                if ((user_resp_left.slice((- 1))[0] === "n")) {
                    waiting_for_y_left = true;
                    console.log("Waiting for next 'y' to record the reading");
                } else {
                    if ((user_resp_left.slice((- 1))[0] === "y")) {
                        latest_reading_left = previous_dB_left;
                        readings_left.push(latest_reading_left);
                        reading_num_left += 1;
                        console.log(`Recording reading (2nd reversal): ${latest_reading_left}`);
                        psychoJS.experiment.addData("Readings_left", latest_reading_left);
                        waiting_for_y_left = false;
                    }
                }
            } else {
                if ((waiting_for_y_left && (user_resp_left.slice((- 1))[0] === "y"))) {
                    latest_reading_left = previous_dB_left;
                    readings_left.push(latest_reading_left);
                    reading_num_left += 1;
                    console.log(`Recording reading (waiting for y): ${latest_reading_left}`);
                    psychoJS.experiment.addData("Readings_left", latest_reading_left);
                    waiting_for_y_left = false;
                }
            }
        }
    }
    if (((! frequency_updated) && (readings_left.length >= 3))) {
        most_common_reading = Math.max(set(readings_left));
        if (((util.count(readings_left, most_common_reading) >= 3) || (readings_left.length > 10))) {
            if ((frequency_index_left < (frequencies.length - 1))) {
                frequency_index_left += 1;
                frequency_left = frequencies[frequency_index_left];
                current_dB_left = 30.0;
                upper_lim_left = upper_limits[frequency_left];
                reversals_left = 0;
                reading_num_left = 0;
                trial_num_left = 0;
                user_resp_left = [];
                readings_left = [];
                next_freq_message_left = `Next frequency: ${frequency_left} Hz`;
                console.log(`Normal trials triggered frequency change: ${frequency_left} Hz (Index: ${frequency_index_left})`);
            } else {
                trials_left.finished = true;
                console.log("All frequencies tested, ending Left Ear");
            }
        }
    }
    psychoJS.experiment.addData("Level_left", current_dB_left);
    trial_num_left += 1;
    console.log(`Final filename: ${current_filename_left}`);
    
    sound_left.stop();  // ensure sound has stopped at end of Routine
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_left.x', mouse_left.x);
    psychoJS.experiment.addData('mouse_left.y', mouse_left.y);
    psychoJS.experiment.addData('mouse_left.leftButton', mouse_left.leftButton);
    psychoJS.experiment.addData('mouse_left.midButton', mouse_left.midButton);
    psychoJS.experiment.addData('mouse_left.rightButton', mouse_left.rightButton);
    psychoJS.experiment.addData('mouse_left.time', mouse_left.time);
    psychoJS.experiment.addData('mouse_left.clicked_name', mouse_left.clicked_name);
    
    // the Routine "trial_left" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Int_MessageMaxDurationReached;
var Int_MessageMaxDuration;
var Int_MessageComponents;
function Int_MessageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Int_Message' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Int_MessageClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    Int_MessageMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('Int_Message.started', globalClock.getTime());
    Int_MessageMaxDuration = null
    // keep track of which components have finished
    Int_MessageComponents = [];
    Int_MessageComponents.push(textInterval);
    
    for (const thisComponent of Int_MessageComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Int_MessageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Int_Message' ---
    // get current time
    t = Int_MessageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textInterval* updates
    if (t >= 0.0 && textInterval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textInterval.tStart = t;  // (not accounting for frame time here)
      textInterval.frameNStart = frameN;  // exact frame index
      
      textInterval.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textInterval.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textInterval.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Int_MessageComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Int_MessageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Int_Message' ---
    for (const thisComponent of Int_MessageComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Int_Message.stopped', globalClock.getTime());
    if (Int_MessageMaxDurationReached) {
        Int_MessageClock.add(Int_MessageMaxDuration);
    } else {
        Int_MessageClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trial_rightMaxDurationReached;
var trial_rightMaxDuration;
var trial_rightComponents;
function trial_rightRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_right' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trial_rightClock.reset();
    routineTimer.reset();
    trial_rightMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codetrials_right
    current_filename_right = `${sound_file_path}${frequency_right}_${util.pad(Number.parseFloat(current_dB_right).toFixed(1), 1)}_right.wav`;
    console.log(`Filename: ${current_filename_right}`);
    console.log(`Current dB (right): ${current_dB_right}`);
    sound_right.setSound(current_filename_right, {"secs": 30.0, "hamming": false});
    
    yes_button_right.setImage('Mouse/Yes.png');
    no_button_right.setImage('Mouse/No.png');
    sound_right.setValue(current_filename_right);
    sound_right.secs=30.0;
    sound_right.setVolume(1.0);
    // setup some python lists for storing info about the mouse_right
    // current position of the mouse:
    mouse_right.x = [];
    mouse_right.y = [];
    mouse_right.leftButton = [];
    mouse_right.midButton = [];
    mouse_right.rightButton = [];
    mouse_right.time = [];
    mouse_right.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouse_right.mouseClock.reset();
    psychoJS.experiment.addData('trial_right.started', globalClock.getTime());
    trial_rightMaxDuration = null
    // keep track of which components have finished
    trial_rightComponents = [];
    trial_rightComponents.push(next_freq_text_right);
    trial_rightComponents.push(yes_button_right);
    trial_rightComponents.push(no_button_right);
    trial_rightComponents.push(sound_right);
    trial_rightComponents.push(mouse_right);
    
    for (const thisComponent of trial_rightComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trial_rightRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_right' ---
    // get current time
    t = trial_rightClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *next_freq_text_right* updates
    
    // *yes_button_right* updates
    if (t >= 0.3 && yes_button_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yes_button_right.tStart = t;  // (not accounting for frame time here)
      yes_button_right.frameNStart = frameN;  // exact frame index
      
      yes_button_right.setAutoDraw(true);
    }
    
    
    // *no_button_right* updates
    if (t >= 0.3 && no_button_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_button_right.tStart = t;  // (not accounting for frame time here)
      no_button_right.frameNStart = frameN;  // exact frame index
      
      no_button_right.setAutoDraw(true);
    }
    
    // start/stop sound_right
    if (t >= 0.0 && sound_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_right.tStart = t;  // (not accounting for frame time here)
      sound_right.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_right.play(); });  // screen flip
      sound_right.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (sound_right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (t >= sound_right.tStart + 0.5) {
        sound_right.stop();  // stop the sound (if longer than duration)
        sound_right.status = PsychoJS.Status.FINISHED;
      }
    }
    // *mouse_right* updates
    if (t >= 0.3 && mouse_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_right.tStart = t;  // (not accounting for frame time here)
      mouse_right.frameNStart = frameN;  // exact frame index
      
      mouse_right.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse_right.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_right.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_right.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_right.clickableObjects = eval([yes_button_right, no_button_right])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_right.clickableObjects)) {
              mouse_right.clickableObjects = [mouse_right.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_right.clickableObjects) {
              if (obj.contains(mouse_right)) {
                  gotValidClick = true;
                  mouse_right.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse_right.clicked_name.push(null);
          }
          _mouseXYs = mouse_right.getPos();
          mouse_right.x.push(_mouseXYs[0]);
          mouse_right.y.push(_mouseXYs[1]);
          mouse_right.leftButton.push(_mouseButtons[0]);
          mouse_right.midButton.push(_mouseButtons[1]);
          mouse_right.rightButton.push(_mouseButtons[2]);
          mouse_right.time.push(mouse_right.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial_rightComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var previous_dB_right;
function trial_rightRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_right' ---
    for (const thisComponent of trial_rightComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial_right.stopped', globalClock.getTime());
    // Run 'End Routine' code from codetrials_right
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    previous_dB_right = current_dB_right;
    clicked_button = null;
    while ((clicked_button === null)) {
        if (mouse_right.isPressedIn(yes_button_right)) {
            clicked_button = "y";
        } else {
            if (mouse_right.isPressedIn(no_button_right)) {
                clicked_button = "n";
            }
        }
        core.wait(0.01);
    }
    if ((clicked_button === "y")) {
        console.log("Yes button clicked");
        user_resp_right.push("y");
        current_dB_right -= (step * 2);
    } else {
        if ((clicked_button === "n")) {
            console.log("No button clicked");
            user_resp_right.push("n");
            current_dB_right += step;
        }
    }
    if (((lower_lim_right <= current_dB_right) && (current_dB_right <= upper_lim_right))) {
        current_filename_right = `${sound_file_path}${frequency_right}_${util.pad(Number.parseFloat(current_dB_right).toFixed(1), 1)}_right.wav`;
        dummy_play_count_right = 0;
        limit_played_right = false;
    } else {
        if ((current_dB_right > upper_lim_right)) {
            console.log("Current dB exceeds upper limit");
            current_dB_right = upper_lim_right;
            if ((! limit_played_right)) {
                current_filename_right = `${sound_file_path}${frequency_right}_${util.pad(Number.parseFloat(upper_lim_right).toFixed(1), 1)}_right.wav`;
                limit_played_right = true;
                console.log("Playing upper limit sound");
            } else {
                if (_pj.in_es6("n", user_resp_right.slice((- 1))[0])) {
                    frequency_index_right += 1;
                    if ((frequency_index_right < frequencies.length)) {
                        frequency_right = frequencies[frequency_index_right];
                        current_dB_right = 30.0;
                        upper_lim_right = upper_limits[frequency_right];
                        reversals_right = 0;
                        reading_num_right = 0;
                        trial_num_right = 0;
                        user_resp_right = [];
                        next_freq_message_right = `Next frequency: ${frequency_right} Hz`;
                        console.log(`Moving to next frequency: ${frequency_right} Hz`);
                    } else {
                        trials_right.finished = true;
                        console.log("All frequencies tested, ending Right Ear");
                    }
                }
            }
        } else {
            if ((current_dB_right < lower_lim_right)) {
                console.log("Current dB below lower limit");
                current_dB_right = lower_lim_right;
                if ((! limit_played_right)) {
                    current_filename_right = `${sound_file_path}${frequency_right}_${util.pad(Number.parseFloat(lower_lim_right).toFixed(1), 1)}_right.wav`;
                    limit_played_right = true;
                    console.log("Playing lower limit sound");
                    sound_right.setSound(current_filename_right, {"secs": 30.0, "hamming": false});
                    sound_right.play();
                } else {
                    psychoJS.eventManager.clearEvents({"eventType": "mouse"});
                    while ((! any(mouse_right.getPressed()))) {
                    }
                    if (mouse_right.isPressedIn(yes_button_right)) {
                        console.log("Yes button clicked during dummy trial");
                        dummy_play_count_right = 0;
                        y_count = 0;
                        n_count = 0;
                        while ((dummy_play_count_right < 3)) {
                            psychoJS.eventManager.clearEvents({"eventType": "mouse"});
                            console.log(`Playing dummy.wav ${(dummy_play_count_right + 1)} time(s)`);
                            psychoJS.window.color = [0, 0, 0];
                            psychoJS.window.flip();
                            core.wait(0.5);
                            psychoJS.window.color = [0, 0, 0];
                            yes_button_right.draw();
                            no_button_right.draw();
                            psychoJS.window.flip();
                            sound_right.setSound(dummy_file_path, {"secs": 30.0, "hamming": false});
                            sound_right.play();
                            click_detected = false;
                            while ((! click_detected)) {
                                if (any(mouse_right.getPressed())) {
                                    if (mouse_right.isPressedIn(yes_button_right)) {
                                        console.log("Yes button clicked during dummy trial playback");
                                        y_count += 1;
                                        psychoJS.experiment.addData(`dummy_response_${(dummy_play_count_right + 1)}_right`, "y");
                                        click_detected = true;
                                    } else {
                                        if (mouse_right.isPressedIn(no_button_right)) {
                                            console.log("No button clicked during dummy trial playback");
                                            n_count += 1;
                                            psychoJS.experiment.addData(`dummy_response_${(dummy_play_count_right + 1)}_right`, "n");
                                            click_detected = true;
                                        }
                                    }
                                }
                                core.wait(0.01);
                            }
                            dummy_play_count_right += 1;
                        }
                        if ((y_count >= 2)) {
                            frequency_index_right += 1;
                            if ((frequency_index_right < frequencies.length)) {
                                frequency_right = frequencies[frequency_index_right];
                                current_dB_right = 30.0;
                                upper_lim_right = upper_limits[frequency_right];
                                reversals_right = 0;
                                reading_num_right = 0;
                                trial_num_right = 0;
                                user_resp_right = [];
                                console.log(`Moving to next frequency: ${frequency_right} Hz`);
                            } else {
                                trials_right.finished = true;
                                console.log("All frequencies tested, ending experiment");
                            }
                        } else {
                            if ((n_count >= 2)) {
                                dummy_trial_repeats += 1;
                                psychoJS.experiment.addData("Level_right", (- 20));
                                readings_right.push((- 20));
                                if ((dummy_trial_repeats < 3)) {
                                    current_dB_right = lower_lim_right;
                                    console.log(`Restarting from lower limit: ${current_dB_right}`);
                                } else {
                                    if (((util.count(readings_right, (- 20)) >= 3) && (dummy_trial_repeats >= 3))) {
                                        if ((! frequency_updated)) {
                                            if ((frequency_index_right < (frequencies.length - 1))) {
                                                frequency_index_right += 1;
                                                frequency_right = frequencies[frequency_index_right];
                                                frequency_updated = true;
                                                current_dB_right = 30.0;
                                                upper_lim_right = upper_limits[frequency_right];
                                                reversals_right = 0;
                                                reading_num_right = 0;
                                                trial_num_right = 0;
                                                user_resp_right = [];
                                                next_freq_message_right = `Next frequency: ${frequency_right} Hz`;
                                                console.log(`Dummy trial triggered frequency change: ${frequency_right} Hz (Index: ${frequency_index_right})`);
                                            } else {
                                                trials_right.finished = true;
                                                console.log("All frequencies tested, ending Right Ear");
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    } else {
                        if (mouse_right.isPressedIn(no_button_right)) {
                            console.log("No button clicked during dummy trial");
                            user_resp_right.push("n");
                            console.log(`User response right: ${user_resp_right}`);
                            current_dB_right += step;
                        }
                    }
                }
            }
        }
    }
    console.log(`User response right: ${user_resp_right}`);
    if ((user_resp_right.length > 1)) {
        if ((user_resp_right.slice((- 1))[0] !== user_resp_right.slice((- 2))[0])) {
            reversals_right += 1;
            console.log(`Reversals right: ${reversals_right}`);
            if (((reversals_right % 2) === 0)) {
                if ((user_resp_right.slice((- 1))[0] === "n")) {
                    waiting_for_y_right = true;
                    console.log("Waiting for next 'y' to record the reading");
                } else {
                    if ((user_resp_right.slice((- 1))[0] === "y")) {
                        latest_reading_right = previous_dB_right;
                        readings_right.push(latest_reading_right);
                        reading_num_right += 1;
                        console.log(`Recording reading (2nd reversal): ${latest_reading_right}`);
                        psychoJS.experiment.addData("Readings_right", latest_reading_right);
                        waiting_for_y_right = false;
                    }
                }
            } else {
                if ((waiting_for_y_right && (user_resp_right.slice((- 1))[0] === "y"))) {
                    latest_reading_right = previous_dB_right;
                    readings_right.push(latest_reading_right);
                    reading_num_right += 1;
                    console.log(`Recording reading (waiting for y): ${latest_reading_right}`);
                    psychoJS.experiment.addData("Readings_right", latest_reading_right);
                    waiting_for_y_right = false;
                }
            }
        }
    }
    if (((! frequency_updated) && (readings_right.length >= 3))) {
        most_common_reading = Math.max(set(readings_right));
        if (((util.count(readings_right, most_common_reading) >= 3) || (readings_right.length > 10))) {
            if ((frequency_index_right < (frequencies.length - 1))) {
                frequency_index_right += 1;
                frequency_right = frequencies[frequency_index_right];
                current_dB_right = 30.0;
                upper_lim_right = upper_limits[frequency_right];
                reversals_right = 0;
                reading_num_right = 0;
                trial_num_right = 0;
                user_resp_right = [];
                readings_right = [];
                next_freq_message_right = `Next frequency: ${frequency_right} Hz`;
                console.log(`Normal trials triggered frequency change: ${frequency_right} Hz (Index: ${frequency_index_right})`);
            } else {
                trials_right.finished = true;
                console.log("All frequencies tested, ending Right Ear");
            }
        }
    }
    psychoJS.experiment.addData("Level_right", current_dB_right);
    trial_num_right += 1;
    console.log(`Final filename: ${current_filename_right}`);
    
    sound_right.stop();  // ensure sound has stopped at end of Routine
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_right.x', mouse_right.x);
    psychoJS.experiment.addData('mouse_right.y', mouse_right.y);
    psychoJS.experiment.addData('mouse_right.leftButton', mouse_right.leftButton);
    psychoJS.experiment.addData('mouse_right.midButton', mouse_right.midButton);
    psychoJS.experiment.addData('mouse_right.rightButton', mouse_right.rightButton);
    psychoJS.experiment.addData('mouse_right.time', mouse_right.time);
    psychoJS.experiment.addData('mouse_right.clicked_name', mouse_right.clicked_name);
    
    // the Routine "trial_right" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EndScreenMaxDurationReached;
var _key_respEnd_allKeys;
var EndScreenMaxDuration;
var EndScreenComponents;
function EndScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    EndScreenClock.reset();
    routineTimer.reset();
    EndScreenMaxDurationReached = false;
    // update component parameters for each repeat
    key_respEnd.keys = undefined;
    key_respEnd.rt = undefined;
    _key_respEnd_allKeys = [];
    psychoJS.experiment.addData('EndScreen.started', globalClock.getTime());
    EndScreenMaxDuration = null
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(textEnd);
    EndScreenComponents.push(key_respEnd);
    
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndScreen' ---
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textEnd* updates
    if (t >= 0.0 && textEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEnd.tStart = t;  // (not accounting for frame time here)
      textEnd.frameNStart = frameN;  // exact frame index
      
      textEnd.setAutoDraw(true);
    }
    
    
    // *key_respEnd* updates
    if (t >= 1.0 && key_respEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respEnd.tStart = t;  // (not accounting for frame time here)
      key_respEnd.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respEnd.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respEnd.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respEnd.clearEvents(); });
    }
    
    if (key_respEnd.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respEnd.getKeys({keyList: ['space'], waitRelease: false});
      _key_respEnd_allKeys = _key_respEnd_allKeys.concat(theseKeys);
      if (_key_respEnd_allKeys.length > 0) {
        key_respEnd.keys = _key_respEnd_allKeys[_key_respEnd_allKeys.length - 1].name;  // just the last key pressed
        key_respEnd.rt = _key_respEnd_allKeys[_key_respEnd_allKeys.length - 1].rt;
        key_respEnd.duration = _key_respEnd_allKeys[_key_respEnd_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndScreen' ---
    for (const thisComponent of EndScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EndScreen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respEnd.corr, level);
    }
    psychoJS.experiment.addData('key_respEnd.keys', key_respEnd.keys);
    if (typeof key_respEnd.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respEnd.rt', key_respEnd.rt);
        psychoJS.experiment.addData('key_respEnd.duration', key_respEnd.duration);
        routineTimer.reset();
        }
    
    key_respEnd.stop();
    // the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
