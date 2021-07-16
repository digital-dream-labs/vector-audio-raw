# Audio Asset Specs for Wwise

We will always want to maintain the highest quality assets when exporting from your DAW, for use in both marketing and import to Wwise. We should identify whether something is formatted for marketing (production asset), or for use on robot (Wwise master) with the appropriate suffix, after final asset normalization. 

* Unless otherwise necessary, all final production assets should be mono, 24/96k, normalized at -16LUFS, and given the suffix "_PA."
ex:
    * Robot_Vic_Sfx__Head_Up_Curious_01_PA

No asset should ever be imported into the Wwise project without the proper suffix, so that we can be certain that what plays on robot was prepared for playback on robot speakers. 

* Unless otherwise necessary, all final Wwise masters should be mono, 24/48k, mastered with the appropriate mastering batch process chain, normalized at -16LUFS, and given the suffix "_WM."
ex:
    * Robot_Vic_Sfx__Head_Up_Curious_01_WM