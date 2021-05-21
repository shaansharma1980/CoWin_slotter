# CoWin_slotter
A simple script which can alert a Mac OS user for available slots for COVID-19 vaccination through the CoWin api. Contains a callable script that can be setup as a cron job on Mac / Linux based systems to alert the user at any time. Can also be used in Windows with some changes.  

## Requirements (Mac)
* Python 3.x version installed on your macbook.
* newman installed through node package manager (npm)
* osascript utility installed (usually by default) on Mac

## Setup
* Install python using homebrew: 
> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
> 
> brew install python

* Next, install npm (node package manager)
> https://nodejs.org/en/download/

* Install the npm package **newman**, *This package provides the ability to fetch availability status from CoWin* :
> sudo npm -g install newman

## Usage
> chmod +x cowin_notifier.bash
> 
> ./cowin_notifier.bash

The above command will show an alert as below:

![GitHub Logo](/images/alert.png)

### Add to a cronjob to run it every 30 minutes 
> crontab -e
> 
> Paste the line below at the end of the editor with a CTRL + V
> 
> 30 * * * * /home/$USER/cowin_notifier.bash
> 
> Type :q! to exit the editor.

 Thats it !

## How it works
* newman is an npm package which provides postman type curl capabilities. It is used to get results from the CoWin api.
* cowin_notifier.py reads the dump of the vaccination data from a tmp file and formats it to call osascript utility.
* osascript is used to display the notification to the mac user (it is available by default on mac)
  * > osascript -e 'display notification "Message" with title "Title"'

## Contributions
* This is free software and if anyone would like to extend it to help create further improvements, please feel free to do so !
* Please ensure that your sole purpose is to help the Indian people in getting vaccination slots across India. 
* Do not overload the api with HTTP requests ! Be nice and let others use it judiciously, put a pragmatic time interval between fetches. 
