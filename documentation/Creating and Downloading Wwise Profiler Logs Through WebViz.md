# Creating and Downloading Wwise Profiler Logs Through WebViz

Created by Andrew Bertolini  Aug 08, 2018

The goal of this documentation is to outline how to properly use WebViz to export a readable Wwise Profiler log. These log files can then be used by the Audio team to investigate audio related issues or bugs.

When reporting Audio bugs it would be ideal if these logs are created and uploaded along with other related media(video captures) for their respective Jira tickets.

## Accessing Audio CVars on Webviz:
In your web browser navigate to 192.168.xx.xxx:8889

   Be sure to replace the placeholders with the last five digits of your robot’s IP Address.

   For example: 192.168.00.000

Once you’ve successfully loaded the Web Server you’ll want to navigate to the Consolevars section by pressing the button seen below:

![](Screen%20Shot%202018-07-25%20at%2012.13.10%20PM.png)

Once the Consolevars have loaded you’ll need to navigate to the Audio tab:

![](Audio_Tab.png)

In this tab you’ll see various Audio Cvars, but the ones that we need to focus on for this are the following:

* WriteAudioProfilerCapture
* WriteAudioProfilerMaxLogCount

## Enabling and Using WebViz’s Automatic Profiler Write Feature:
To enable WebViz’s Automatic profile logging you will need to enable the following CVar: *WriteAudioProfilerCapture*

![](Enable_Log_Set_Max.png)

After enabling that, you will want to adjust the value of: WriteAudioProfilerMaxLogCount

This Cvar controls the maximum number of Profiler Logs the robot will store in its internal cache.

Set this to however many logs you wish to save. If the total log count exceeds the designated number, it will begin deleting the oldest logs stored in the cache.

Once you have set both of those, you will need to Save your Console Vars on Webviz.

![](Save_CVars.png)

***Note: These changes will not take effect until you restart your robot***

## Enabling One-Shot Profile Logging:
If you would prefer to enable logging as a one time thing, instead of using automatic logging you can do that using: *SetWriteAudioProfilerCapture*

![](One_Shot_Prof_Logs.png)

To toggle this on/on you will use two bools:

1. *true* - Will enable the write process.
2. *false* - Will disable the write process.


When you are ready to start writing a profiler log type true in the text field next to SetWriteAudioProfilerCapture and press “Call”

This will start the write process and this will continue until you cancel/stop it.

When you are ready to stop the writing process type *false* in the text field next to *SetWriteAudioProfilerCapture* and press “Call”

This will stop the writing process and create your finished Wwise Profiler log.

## Locating your Wwise Profiler log:
At the top of your screen, just under the title “Victor Web Server” you’ll see a row of button. You’ll need to navigate to the one called “Files”:

![](Screen%20Shot%202018-07-25%20at%2012.14.00%20PM.png)

Once this page loads navigate to “Sound”:

![](Screen%20Shot%202018-07-25%20at%2012.14.05%20PM.png)

Your sound directory should look something like this if you’ve successfully created a Wwise Profiler log:

![](Screen%20Shot%202018-07-25%20at%2012.14.31%20PM.png)

To download your log, simply right click on the file itself and select “Save Link As”

Save it and rename it something applicable. If it is related to a specific bug, and that bug has a Jira ticket associated with it, please include the ticket number in the log name.

## Deleting Saved Profiler Logs:
If for whatever reason you need to completely delete the logs store in your robot's cache simply click the following button.

![](Delete_Audio_Prof_Logs.png)
