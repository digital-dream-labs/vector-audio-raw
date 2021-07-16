# Audio Console Vars & Functions
To start profile capture or audio output capture at startup

| Type | Console Variable  | Description |
|------|-------------------|-------------| 
|bool  |WriteAudioProfilerCapture|Write Wwise profiler log to &lt;sound asset root dir&gt;/VictorProfilerSession.prof|
|bool  |WriteAudioOutputCapture	|Write Wwise audio output to &lt;sound asset root dir&gt;/VictorOutputSession.wav|


To change console var and perform task during run time
| Console Function  | Argument             | Description |
|-------------------|----------------------|-------------| 
|SetWriteAudioProfilerCapture | bool writeProfiler|Start/Stop Writing Wwise profiler log to &lt;sound asset root dir&gt;/VictorProfilerSession.prof|
|SetWriteAudioProfilerCapture | bool writeOutput |Start/Stop Writing Wwise audio output to &lt;sound asset root dir&gt;/VictorOutputSession.wav
|SetRobotMasterVolume	|float volume|Set the robot's master volume, valid volume values are 0.0 - 1.0|
|ToggleOnOffProceduralAudio|NONE|Turn procedural audio On/Off (Off by default)|
|ResetToDefaultVolume|NONE|Reset all volume settings (Use Audio Project's default settings)|
|TestAudio_PinkNoise|NONE|Play pink noise to test if the audio engine is running|
|PostAudioEvent	|string eventName, optional uint64 gameObjectId|Post an audio event with name and optional gameObjectId, if not set will use the "default" GameObject (see audioEventTypes.h & audioGameObjectTypes.h)|
|SetAudioState|string stateGroup, string state|Set audio state (see audioStateTypes.h)|
|SetAudioSwitchState|string switchGroup, string state, uint64 gameObjectId|Set audio switch state (see audioSwitchTypes.h & audioGameObjectTypes.h)|
|SetAudioParameter|string parameter, float value, optional uint64 gameObjectId|Set audio parameter, if GameObject is not set parameter will be updated globally (see audioParameterTypes.h & audioGameObjectTypes.h)|
|StopAllAudioEvents|optional uint64 gameObjectId|Stop all audio events on GameObject, if not set all events will be globally stopped (see audioGameObjectTypes.h)|


To perform a console var or function from Webots expand the WebotsKeyboardController menu and find consoleVarName & consoleVarValue variables. Type the name and value you want to set, to set a ConsoleVar use key command 'alt ]' and to call a ConsoleFunc use key command 'alt }'. (Note: Make sure the main window with the robot has focus before sending the command) 

