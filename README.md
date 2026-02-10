# VideoToGrayscalePhotos
Takes videos and converts every frame into a grayscale photo.

## Requirements
1. Make sure that you have Python 3.x.x installed on your computer (the newer the better)

## Installation
1. Clone the repository (copy this link `https://github.com/vader2010/VideoToGrayscalePhotos.git` and `git clone` onto your computer in your preferred directory)
2. Open the project in your IDE of choice and a bash terminal in your project's directory as well.
3. Create a virtual environment in your terminal using `python3 -m venv .venv`. This is only if you want packages locally (only accessable by this project) instead of globally (accessible for all projects). **LOCALLY IS RECOMMENDED**.
4. Enter your virtual environment by running the command `. .venv/bin/activate` in your terminal. If this is successful you should see a `(.venv)` to the left side of the terminal (on your input line). Example: <img width="416" height="12" alt="image" src="https://github.com/user-attachments/assets/8af6b083-bb89-4456-8d06-36d30a72fed7" />
5. If the last step succeeded, you should be able to run the command `pip install -r requirements.txt` which install all the correct versions of the packages used.
6. Make sure to remove the .gitkeep files from each of the directories so that it doesn't cause any errors with the program

## Usage
1. Put all the videos you want to break apart into the input directory
2. Run main.py while you're inside of the virtual environment (just run `. .venv/bin/activate` while you're inside the project directory)
3. Should return the grayscale frames in the outputs directory.
