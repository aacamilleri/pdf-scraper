# PDF Ripper

Use this code to rip a PDF from BibliU (or any other annoying textbook provider) by automatically looping through your textbook, taking a screenshot of each page, and combining the screenshots into a PDF. This project was created to allow annotating a textbook within an iPad note-taking app.

## Installation (for non-techy people)
Coming soon. I'm planning on uploading standalone executable files so people don't need to understand Python to use this PDF Ripper app.

## Installation (from source code -- for techy people)
### 1. Install [Python3](https://www.python.org/downloads/) 
Check if you already have it installed or if you installed it successfully with the `python3 --version` command in your Terminal / Command Prompt

### 2. Install [pipenv](https://pypi.org/project/pipenv/) 
I installed it using [Homebrew](https://brew.sh/) on Mac with the command `brew install pipenv`

### 3. Use pipenv to install all of the project's required packages in a virtual environment
Download this repository (i.e. `git clone https://github.com/jalexw/pdf-ripper.git`), make it your active directory (i.e. `cd pdf-ripper`), and run `pipenv install` to download all required packages defined in the `Pipfile`.

### 4. Running the program
After installation, use `pipenv run start` to start the application. Use `pipenv run dev` for additional logging if you're trying to add a feature or troubleshoot.

### Known Errors
- If you get an error on Mac related to tkinter, see [this StackOverflow post](https://stackoverflow.com/questions/5459444/tkinter-python-may-not-be-configured-for-tk). You may need to use [Homebrew](https://brew.sh/) to install python-tk to fix the problem on Mac, `brew install python-tk`.

## Using the GUI 
### 1. Open your textbook in the BibliU web application
- Open up BibliU on the web to the textbook you would like to rip. 

### 2. Resize your browser window to get the screenshots as big as you can
- Note: Screenshots must be taken on your primary monitor. However, it is convenient to have a second monitor where the GUI doesn't block the textbook. Otherwise, minimize the window after starting the rip and selecting the screenshot area.
- Resize the textbook to be as large as possible.
- Play around with zooming in/out.
- You can open your browser's developer tools menu (Usually 'Command + Option + I' on Mac) to resize the textbook page better. BibliU doesn't allow you to right click such that you can open Developer Tools; however, you can do this from the menu in the top right corner of Google Chrome (or with 'Command + Option + I' on Mac).

### 3. Start PDF Ripper Application

### 4. Input settings for PDF ripping
- Enter the start/finish page here.
- Enter whether coordinates of screenshot area should be doubled (see [this issue](https://github.com/python-pillow/Pillow/issues/3293) for more details). It seems like some computers need to have the coordinates doubled, while others don't. Try both and see what works for you.
- Choose an output directory to save the PDF in.
- Choose how long to wait after going to a new page to take a screenshot. If you have slow internet you might want to give the app time to load the page so your PDF doesn't end up with loading screens in it
- Select the region on your screen that should be screenshot. You do this by hovering your mouse over the top left corner and the bottom right corner of the area that should be screenshot after pushing the respective button.
- Finally, hover your mouse over the page selection menu at the bottom of the page to tell the script where it should type in new page numbers to go to the next page.

### 5. The script takes control of your device
- Hit 'Start Ripping'
- On Mac, a pop-up should ask you to allow the script to record your screen and use accessibility services ( to control keyboard/mouse). You may need to restart the program after giving it permission, so do a test run first before actually trying to rip a textbook.
- The script will take control of your mouse and keyboard while it loops through the pages and takes screenshots for the PDF! Don't touch anything while it works its magic! 
- Screenshots are combined into a PDF file at your chosen output location

## To-do
- [x] Create GUI from original PDF ripper script
- [ ] Test on Linux
- [ ] Create standalone executables
- [ ] Make text in PDF screen reader friendly

## Contributing
Tested on Mac and Windows. Contributors welcome! Feel free to make a PR :)
