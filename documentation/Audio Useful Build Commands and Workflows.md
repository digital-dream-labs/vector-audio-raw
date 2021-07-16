# Audio: Useful Build Commands and Workflows
Created by Andrew Bertolini

Many, if not all, of the following commands have dependancies to two scripts: UsefulAliases and UsefulAudioAliases. You will need to follow additional steps to set them up to work properly on your machine.

*Follow the instructions found here: Setting Up Computer to use 'UsefulAliases' and 'UsefulAudioAliases' Scripts*

## Commands:
### Project Build Variations:
* `victor_build_release -f`
    * Forces a re-build of the entire Victor project directory. Will use audio assets found in EXTERNALS/victor-audio-assets.

* `victor_audio_update_local_assets`
    * Updates audio assets using locally generated Soundbanks.
* `victor_audio_robot_build_deploy_update_local_assets`
    * Updates audio assets using locally generated Soundbanks. Compiles the build using said banks and then deploys build to robot. 
    * This is the god command. 
* `victor_audio_webots_build_update_local_assets`
    * Update assets then build for Webots

### Cleaning Assets:

* `victor_audio_clean_local_assets`
    * Delete Victor Project local assets
* `victor_audio_clean_project_assets`
    * Delete Victor Wwise Project generated sound banks dir
* `rm -rf generated`
    * Trash project generated folder
* `rm -rf _build`
    * Trash project build folder


## Workflows:
### Building with Local Soundbanks:

1. Get latest Master off SourceTree.
2. In Wwise, generate local Soundbanks.
3. With your robot on its charger double click its backpack, then raise/lower its arm in quick succession. 
    a. This will bring up its debug menu, write down the IP address listed on the screen.
4. From terminal(in SourceTree) run:
    a. project/victor/scripts/victor_set_robot_ip.sh 192.168.xx.xx
    b. Replacing the IP with the one you wrote down in the previous step.
    c. **This step can be skipped if you have done it previously and your robot has not since changed its IP.**
5. Also from terminal run the following command:
    a. `victor_audio_robot_build_deploy_update_local_assets`
        1. This will build using Master, but will replace the audio assets in Master with your locally generated Soundbanks. 
        2. Once the build is done, it will automatically deploy the build to the robot.

### Build with Master Soundbanks:

1. Get latest Master off SourceTree.
2. With your robot on its charger double click its backpack, then raise/lower its arm in quick succession. 
    a. This will bring up its debug menu, write down the IP address listed on the screen.
3. From terminal(in SourceTree) run:
    a. `project/victor/scripts/victor_set_robot_ip.sh 192.168.xx.xx`
    b. Replacing the IP with the one you wrote down in the previous step.
    c. **This step can be skipped if you have done it previously and your robot has not since changed its IP.**
4. From terminal(in SourceTree) run the following command:
     `victor_build_release -f`
5. When this finishes, run the following:
    * `victor_deploy_release`
6. After the deploy finishes you'll need to restart your robot. Run the following:
    * `victor_restart`
