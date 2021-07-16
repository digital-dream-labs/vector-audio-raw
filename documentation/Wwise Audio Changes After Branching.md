## Wwise Audio Changes After Branching
Created by Nishkar Grover

While we do not have the ability to cherry-pick specific audio changes from/to generated soundbanks, we could potentially create branches of the source Wwise data and use that to make specific audio fixes after branching.

Looking at the DEPS file in the release/candidate branch, we branched with (or cherry-picked) revision 99 of soundbanks in that branch...

```
    "victor-audio-assets": {
        "allow_extra_files": "True",
        "version": "99"
    }
```

Checking the #audio_pipeline slack channel, we can see that revision 451 of the victor-wwise project was used to generate revision 99 of the soundbanks (see those version numbers here).

Suppose we want the following revision 465 change from the victor-wwise project in the 1.0.0 release after branching:

```
    ------------------------------------------------------------------------
    r465 | andrew.bertolini | 2018-09-26 13:48:31 -0700 (Wed, 26 Sep 2018) | 1 line
    Changed paths:
    M /trunk/VictorAudio/Actor-Mixer Hierarchy/Robot_Vic_Sfx__Head_and_Lift.wwu
    Removed Robot_Vic_Sfx__Head_Anim_Unused.
    ------------------------------------------------------------------------
```

then we could:

1. Create a release_1_0_0 branch from revision 451 
2. Open the victor-wwise/branches/release_1_0_0 project in Wwise and make the 465 change (assuming we cannot simply cherry-pick the updated Robot_Vic_Sfx__Head_and_Lift.wwu file if, for example, some other changes have also been made in that work unit since revision 451)
3. Commit that change to victor-wwise/branches/release_1_0_0 in SVN
4. Generate soundbanks by running "@buildbot build Wwise_VictorGenerateSoundBanks release_1_0_0" in the #audio_pipeline slack channel
5. Do not merge the resulting pull request that is opened to put those soundbanks in the master git branch. Instead, manually open a new pull request to merge the update-audio-assets branch into the release/candidate git branch.

( Note: Steps 4 and 5 may not be sufficient to properly create the PR to put the changes into the release/candidate git branch. Instead, we may need to provide a way to base the update-audio-assets branch off the release/candidate branch instead of the master branch, either with an extra argument to the existing Wwise_VictorSoundsbanksCladPullRequest job or a different build job that is similar to that. )

The end result is a release branch pull request that should contain one specific change on top of what we already put in that release branch.

If we later wanted to add any more changes to the 1.0.0 release, we'd simply repeat steps 2 - 5

This workflow is probably not ideal since it requires the audio designer to redo a change in the release branch that he has already made in the trunk (if we cannot simply cherry-pick the work unit and/or wav files), but it provides an option for any critical audio changes that may be needed in the release branch.