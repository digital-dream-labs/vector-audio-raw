# Setting up Wwise on a Virtual Machine

Created by Andrew Bertolini

## Installing Wwise 

1. While on your VM download the Wwise Launcher from https://www.audiokinetic.com/download/
2. Locate the WwiseLauncher.msi file in your Downloads folder and run it.
3. We currently use 2017.2.7.6661. But check with your manager to verify the correct Wwise version to install. 
4. In the installation window be sure to check the following options:

![](images/Screen%20Shot%202018-09-11%20at%204.13.41%20PM.png)


5. Press next and make sure to check the box to install the McDSP bundle on the next screen:

![](images/Screen%20Shot%202018-09-11%20at%204.14.54%20PM.png)


6. Press Install.

## Installing Visual Studio:

1. Go to: https://visualstudio.microsoft.com/vs/

2. Download Visual Studio for Windows. The Community 2017 version will work fine. 

3. Be sure to check the box next to Desktop Development with C++ when prompted to select additional Workloads.

![](images/Screen%20Shot%202019-01-28%20at%203.16.53%20PM.png)

4. Press Install!

## Opening the Victor Project:

1. You will need to have finished the steps for setting up your Cornerstone Repos found in Audio: Setting Up Your Computer prior to opening the Wwise Project. 

2. Before opening the project you will need to setup a Shared Folder to access the Wwise project on your VM. While your VM is open go to the following menus: **Virtual Machine > Settings > Sharing** 

![](images/Screen%20Shot%202019-01-28%20at%203.27.04%20PM.png)


3. From there you will need to check the box at the top of the window labeled Enable Shared Folders.

4. Once you've enabled folder sharing you'll want to press the plus(+) button to add a Shared Folder.

    a. Navigate to your Victor Wwise directory and select it. This will add it as a Shared Folder and grant you access to it. 

5. Once you've setup the Audio Repo, finished downloading the Wwise Project, and setup your Shared Folders you can open the project from the Wwise Launcher.

    a. From the Wwise launcher select 'Open Project' and navigate to your Wwise project directory. Of course, your file path will be different!

![](images/Screen%20Shot%202018-09-11%20at%204.34.39%20PM.png)

6. You will likely encounter various errors when you attempt to launch the Victor Wwise project for the first time. This is because we use custom Wwise plug-ins that you will need to download and install. See below!

## Installing Custom Anki Wwise Plug-ins:

1. First you will need to download the plug-ins found Here (This will likely require you have DropBox setup, as well as appropriate permissions to access the folder.) 

2. Once you have the plug-ins downloaded you will need to move them into the 'plugins' folder found in your Wwise installation directory. 

a. The following photo shows the general file path to where the 'plugins' folder is located on Windows. 
![](images/Screen%20Shot%202018-09-11%20at%204.41.26%20PM.png)

