# Asset and Wwise Naming Conventions
Created by Andrew Bertolini Jan 04, 2019

## General Rules:
* Content should always be named in such a way that isolated files are identifiable down to their product, usage in the product, and alphabetize easily within a folder; especially Wwise Originals.
* Naming should begin with broad, then increasingly more specific, information from left to right. This allows assets to fall in order automatically. 
* For transparency within the Wwise project, it would also be preferred if event names include the full name of the content or container that it primarily impacts. 
* Only the first letter of any given word is capitalized. For example, "Sfx" and "Vo", as opposed to "SFX" or "VO."
* Unless you are absolutely sure there is no chance of ever needing variations for an asset, you should add 2 digit variation number at the end of imported assets. (i.e _01, _02).
* For the sake of engineers that will not be seeing the event action at the head of each event name (it gets parsed off), please add the event action to the end of any content that has anything other than simple Play actions (i.e., if you have a Play and Stop, include "_Play" and "_Stop" at the end of the event names). Otherwise engineers cannot tell which is which.

## Examples:
### Content:
_Robot_Name_SourceType__SourceGroup_SourceDetails_Variation_

Robot_Vic_Sfx__Head_Up_Curious_01
Robot_Vic_Sfx__Shared_Curious_Short_01
Robot_Vic_Sfx__Scan_Face_Loop_01

### Event Names:
#### One-Shot Events:
_EventAction__Robot_Name_SourceType__SourceGroup_SourceDetails_

* Play__Robot_Vic_Sfx__Head_Up_Curious
* Play__Robot_Vic_Vo__Shared_Curious_Short

#### Looping Events:
_EventAction__Robot_Name_SourceType__SourceGroup_SourceDetails_EventAction_

* Play__Robot_Vic_Sfx__Scan_Face_Loop_Play
* Stop__Robot_Vic_Sfx__Scan_Face_Loop_Stop

### Game Syncs:
#### RTPC:
_Robot_Name_SourceDetails_

* Robot_Vic_Purr_Level
* Robot_Vic_Stimulation_Level
* Robot_Vic_Treads_Forward
* Robot_Vic_Treads_Backward

#### States:
_Robot_Name_SourceDetails_

* Robot_Vic_Mood_Happy
* Robot_Vic_Mode_Quiet

#### Switches:
_Robot_Name_SourceDetails_

* Robot_Vic_Lift_Stressed

