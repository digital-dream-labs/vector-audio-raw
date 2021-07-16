# Build and update sound bank version

## Generate sound banks assets
The easiest way to build sound banks is to use the Slack channel "audio_pipeline" and type "@buildbot build Wwise_VictorGenerateSoundBanks". The build server will update to the latest version of the Victor's Wwise project (trunk branch), generate sound banks, run project scripts and upload the assets to victor-audio-assets SVN repo. Build Bot will respond when the build is complete and give you details about the build.

## Generate sound bank assets for other Wwise Project Branches
Similar to building sound banks for the trunk branch simply add the name of the name of the branch to the command, "@buildbot build Wwise_VictorGenerateSoundBanks branch_name".

NOTE: Branch names can not contain '-' character.

## Update assets in project
From the Build Bot response get the SVN revision: #. For example if you look at this Slack Log you will see this line "SVN revision: 10"

In Victor's repo root use script ./tools/audio/UpdateAudioAssets.py to update the DEPS and audioEventMetadata.csv files then use generate command to update audio clad files.

	#!/usr/bin/env bash
	./tools/audio/UpdateAudioAssets.py update 10
	./tools/audio/UpdateAudioAssets.py generate

Commit the changes.

Developers can run `./project/victor/scripts/fetch-build-deps.sh` to update local assets

See Audio for Software Engineers for more details


## Locally generate sound banks and run
If you want to use audio assets generated locally you can use ./tools/audio/UseLocalAudioAssets.py script. The script is intended to perform all the scripts needed to generate audio metadata, organize assets, build and deploy the project for both Robot & Mac builds (See script's help for command options). When you run the script you need to provide the Wwise Victor project branch you want to pull assets from. The script does not generate the assets, that needs to be done within Wwise's authoring tool and it expects them to be in the default directory VictorAudio/GeneratedSoundBanks.

	#!/usr/bin/env bash
	./tools/audio/UseLocalAudioAssets.py <VictorWWiseProjectRepo>/trunk <additional args>

or

	./tools/audio/UseLocalAudioAssets.py <VictorWWiseProjectRepo>/branches/<branch_name> <additional args>

See: <victor repo>/project/victor/scripts/usefulAudioAliases.sh for helpful audio aliases to build and deploy.  Note: To use alias this file must be added to your ~/.bash_profile