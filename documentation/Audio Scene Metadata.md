# Audio Scene Metadata

AudioScene is a set of structs which define a group of Audio Banks and Events that are used during a specific period (a scene). These structs are intended to be constructed during apps load phase and given to the AudioEngineController. The app can load and unload the AudioScene as needed.

Audio Scenes can be defined in JSON files, see example below.

Audio Scenes objects can solely load sound banks or events. Similar to Audio Scene Event objects they can solely load Audio Event, Switch Group, Game Group and/or Game Parameter.


```
{
	"SceneName" : "AudioSceneName",
	"Banks" : [
		"SoundbankName_01",
		"SoundbankName_02"
	],
	"ZipFiles" : [
		"FullPathToZipFile_01.zip",
		"FullPathToZipFile_02.zip"
	],
	"Events" : [
		{
			"EventName" : "EventName_01",
			"SwitchStates" : [
				{
					"StateGroupName" : "SwitchGroupName_01",
					"GroupStates" : [
						"State_01",
						"State_02"
					]
				},
				{
					"StateGroupName" : "SwitchGroupName_02",
					"GroupStates" : [
						"State_01",
						"State_02"
					]
				}
			],
			"GameStates" : [
				{
					"StateGroupName" : "GameGroupName_01",
					"GroupStates" : [
						"State_01",
						"State_02"
					]
				},
				{
					"StateGroupName" : "GameGroupName_02",
					"GroupStates" : [
						"State_01",
						"State_02"
					]
				}
			]

			"GameParameters" : [
				{
					"ParameterName" : "GameParameterName_01",
					"ParameterValue" : 1.0
				},
				{
					"ParameterName" : "GameParameterName_02",
					"ParameterValue" : 0.0
				}
			]
		},

		{
			"EventName" : "EventName_02",
			"SwitchStates" : [
				{
					"StateGroupName" : "GroupName_03",
					"GroupStates" : [
						"State_01",
						"State_02"
					]
				},
				{
					"StateGroupName" : "GroupName_04",
					"GroupStates" : [
						"State_01",
						"State_02"
					]
				}
			],

			"GameStates" : [
				{
					"StateGroupName" : "GameGroupName_03",
					"GroupStates" : [
						"State_01",
						"State_02"
					]
				},
				{
					"StateGroupName" : "GameGroupName_04",
					"GroupStates" : [
						"State_01",
						"State_02"
					]
				}
			]
		}
	]
}
```