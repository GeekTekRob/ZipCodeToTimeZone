# Zip Code to Timezone App

## Summary

Simple python app to take a US Zip Code and find info on it relating to the Timezones for the 50 U.S. states.  This was built as a workup for Python and curating some data.  Also to use Google less on data I tend to use sometimes and don't need a full blown webapp or database for.

The EXE is generated using pyinstaller and included for those that want to run in just a window and no command prompt.

<br/>

## Data Sources
All timezones and zipcodes were retrieved from public domain websites and curated to connect.  I'll shift the data over time to include a more robust, as some of it is available in different ways and needs to be connected on refrencing data fields.

## Issues or Missing Data
Feel free to reach out.  I'll create an issue template for missing zip codes or timezones.  At the moment they are all timezones that affect the US.

## Create your own EXE

In case you want to modify the python script or change the data, the exe file was created using PyInstaller.  After modifying the files you can create a new exe by following the below steps:

1) In terminal make sure you have pyinstaller installed, run the following command

    ``` python
    pip install pyinstaller
    ```

2) Using terminal, go to the directory for 'index.py'
    ex. C:\src\ZipCodeToTimezone

3) Type in the following syntax in order to run pyinstaller and create the .exe file

    ``` python
    pyinstaller --onefile --windowed --distpath . --add-data="./images/copy_icon.png;./images" --add-data="./data/zipcode.json;./data" --add-data="./data/timezone.json;./data" index.py
    ```
4) Once finished, you will see index.exe has been updated.

5) Feel free to run and verify your changes worked.  Good Luck and happy coding.


## MIT License

Copyright (c) 2022 Brandon Miller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.