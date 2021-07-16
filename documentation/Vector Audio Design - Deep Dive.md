# Vector Audio Design: Deep Dive
Created by Andrew Bertolini, Jan 29, 2019

## Basic Vector character notes: 
* Vector, as a life form, is much more creature, than intelligent robot. Curious and reactive, like a parrot, squirrel, chipmunk, or fennec fox. 

* Character on Vector, and all Anki robots, is king. Maintaining accurate and powerful character should be the highest priority for our audio design and implementation. I say this as something to keep in mind when thinking up cool new things we can do with tech, or implementation method. I am 100% behind finding ways to automate SFX, or apply procedural or state systems, as long as it's the best possible way to support character. 

* Utility functions are not part of Vector's personality; they exist in parallel to his character, usually somewhat against Vector's will. Giving Vector agency is something we've tried to maintain all along, and actually gives us fun opportunities to casually abuse him. That sounds awful, but I hope the point makes sense.

## Goals to keep in mind when adding audio to animation:
* Accuracy of intent. The better we do our job, the more lifelike Vector feels, removing mental barriers that an owner may have believing Vector is alive. 

* Variety across individual animations keeps Vector sounding expressively dynamic, and of course, less monotonous. 

* Variety across long term experience means sometimes having some animations less populated with SFX, to make room for more important animations in a feature. For example, for "react to sound", when Vector hears a sound and responds, either having lower probability events in some animations, or removing SFX from some animations altogether allow this feature to not get old (or at least not as fast). 

## Some general rules for adding character SFX to animations and layouts:
* The mood descriptor is not restricted to what actual mood or state that Vector is in; they are only used to separate their shape, and give us access to making creative decisions with those shapes. 

* We do not need to, and in some cases should not have character audio on every tiny movement Vector makes. You may find that often less is more, so that important thought beats and have room to stand out, and so that we don't overwhelm users with constant audio feedback. The accuracy of Vector's expression is most important.

* Variety goes a long way in preventing repetition, meaning that there may be a benefit to using a "lift" SFX where you'd typically use a "head", if you've already used "head." Most often this can be settled by assigning both to multiple keyframes and inversely splitting the probability 70/30.

* The end of animations typically end with Vector returning to a neutral pose, since we never implemented a blending tool for animations. I try to minimize any character in this moment.  

## The primary character SFX groups:
### Head:
While there aren't hard lines on where "head" and "lift" are used, I generally lean toward thinking of "head" as the speaking voice of Vector. Like a squirrel chittering when reacting to something, or to "talk out loud" while processing thought. The best way I would say between choosing "head" or "lift" would be to favor "head" for the stronger reactions that suggest Vector thinking. 
As we talked about, there is no use anymore for distinguishing "up" or "down", so I generally lean toward using "down", with the distant hope of one day eliminating "Up" from animations. 

### Lift:
Very similar to "head", but I generally rely on "lift" SFX if I've already placed a "head" SFX in an animation, if there have been several used across a feature already, or if the reaction Vector is making is clearly shaking his lift around excessively. Though "lift" was designed as being copilot with "head" as a speaking voice for Vector, I think of it as the secondary from of voice, or to ensure the voice has variety across one or many animations. 

### Emote:
While a poor word choice for a SFX group, still an important part of communicating, the emote sound family is less "verbal", and more of a strong feeling being projected out loud. These are good for when Vector is extra curious, happy, sad, or especially when interacting directly with the user. These are generally used only in animations that we can be certain the user in nearby, and were designed to be the cute part of Vector's character, and less chittery creature. 

### Screen:
Similar to Cozmo, Vector has a full suite of expressive telemetry for facial expressions. These work well for breaking up the more important thought beats in animations, to prevent run on reactions. These are also great for preempting, or gracefully concluding another expressive sound, as his eyes are often the first or last thing moving around a reaction.

### Tread:
In addition to all other forms of emotive communication, we have a set of mood shaped tread sounds designed to give another avenue for expressive movements. If Vector reacts to a movement or sound, rotating to look in the direction of the source, tread SFX could do well to indicate his interest. 

### Text To Speech voice:
TTS is Vector's utility to communicate with people. Vector doesn't necessarily understand the words that he's speaking, and this is not his "actual" voice. For example, a limitation we've set for ourselves is that although Vector can understand voice commands, he cannot just initiate intelligent conversation. Voice commands and TTS responses are his utility of channeling the cloud information. 

### Notification:
We have many sounds tied to utility and general notifications, which are ideally within somewhat of a similar style. These include timer, wake word on/success, search for cube, search for charger, stuck on edge, etc.  

### The "etc." SFX:
There are plenty of exceptions, and will continue to be some, outside the character and notification SFX. The creative direction for these are going to be a case by case basis, and we should work toward making sure we are supporting character. These include things like weather, blackjack, and the "Happy Holidays" sequences. 