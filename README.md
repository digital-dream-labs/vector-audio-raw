# vector-audio-raw  
The resources in this repository can be used to build new sounds for Vector! Once engine source is available, you can then pair these sounds with animations, etc. for new behaviors. For now, this audio can be used to adjust existing sounds/behaviors. Please see the "documentation" folder for more details on usage of these tools.

You may need a license to [Audiokinetic's Wwise](https://www.audiokinetic.com/products/wwise/) program to make full use of the code in this repository.

NOTE: When installing WWise, please be sure to install and use version 2017.2.10.6745 with these assets. If the project is converted to a newer format, it may not work with the Vector robot until robot-side changes are made.

## Plug-ins
Please note that there are several plugins which may be needed for WWise that are unable to be open-sourced due to paid licensing for each plugin:
* HijackAudio  
* WavePortal  
* Ak Alsa Sink  
* Victor ALSA Sink  
* Krotos Vocoder  
* WavePortal  
* Anki Streaming Wave Portal 
* iZotope Hybrid Reverb  
* iZotope Trash Box Modeler (Deprecated- you may wish to use Trash v2 from iZotope)  
* SoundSeed Grain  
* Wwise Convolution Reverb

## To create the sound banks

To generate the sound banks from the command line:
1. cd to folder containing VictorAudio
2. Run the command:
```
    "C:\Program Files (x86)\Audiokinetic\Wwise 2017.2.10.6745\Authoring\x64\Release\bin\WwiseCLI.exe" "VictorAudio\VictorAudio.wproj" -GenerateSoundBanks -Verbose
```

3. When that completes, have it package up the files. Run the "victor-create-zip-files" script from the build-scripts directory:
```
    ./victor-create-zip-files
```

The script will create a bunch of zip files. Inside assets/victor_robot/vector are zip files for the different parts, and a .json file.  (Inside of  assets/victor_robot/mac are the audio files for the webots simulation)

Notes:
1. The script includes the init.bnk file included in this respository.  This is necessary.  Without it, the WWise project only generates working soundbanks on the Windows build with all of the plugins installed.  This init.bnk includes the key setup information that Vector needs.

## To install on vector

Below is an example of how to install the new sound bank on Vector.

1. On Vector, mount the file system writable 
```
    sudo mount -o remount rw /
```
2. SCP the zip files to Vector from your computer:
```
    scp -r -i <SSH Key Location> <Zip File Location on Computer> root@<Vector IP Address>:/anki/data/assets/cozmo_resources/
```

3. On Vector, make a new directory with the new sounds:
```
    cd /anki/data/assets/cozmo_resources
    mkdir sound.new
```  

4. Move those zips to the sound.new folder:
```
mv <zip name> sound.new
```  

5. Unzip each of the zip files. When prompted if you want to overwrite files, click **YES.**. (Some sounds are shared in multiple soundbanks, so are duplicated in the zip files)  
```
unzip -o <zip file name>
```
7. delete the .zip files:
```
rm <zip file name>
```

Now you are ready to test the sound bank.  This will save the old soundbank and put the new one in.
```
    mv sound sound.old
    mv sound.new sound
    reboot
```

If Vector plays sounds as expected, you can remove the "sound.old" folder.
```
    sudo mount -o remount,rw /
    rm -rf /anki/data/assets/cozmo_resources/sound.old
```

If the sounds did not work as expected, you can restore the originals:
```
    sudo mount -o remount,rw /
    cd /anki/data/assets/cozmo_resources
    mv sound sound.new
    mv sound.old sound
    rm -rf sound.new
    reboot
```
