# Zip Code to Timezone App

## Summary

Simple python app to take a US Zip Code and find info on it relating to the Timezones for the 50 U.S. states.  This was built as a workup for Python and curating some data.  Also to use Google less on data I tend to use sometimes and don't need a full blown webapp or database for.

<br/>

## Data Sources
All timezones and zipcodes were retrieved from public domain websites and curated to connect.  I'll shift the data over time to include a more robust, as some of it is available in different ways and needs to be connected on refrencing data fields.

## Issues or Missing Data
Feel free to reach out.  I'll create an issue template for missing zip codes or timezones.  At the moment they are all timezones that affect the US.

## Create an EXE

In case running just an .exe file works best for you.  You can create this using PyInstaller following these steps.

1) In terminal make sure you have pyinstaller installed, run the following command

    ``` python
    pip install pyinstaller
    ```

2) Using terminal, go to the directory for 'index.py'
    ex. C:\src\ZipCodeToTimezone

3) Type in the following syntax in order to run pyinstaller and create the .exe file

    ``` python
    pyinstaller --onefile index.py
    ```
4) Once finished, you will see a folder called dist.  Copy the images and data folder into that.

5) Now in the 'dist' folder you should have index.exe and the files it needs to run as an executable and can use it as a shortcut on your desktop or in a macro.


