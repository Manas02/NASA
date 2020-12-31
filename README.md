# Martian CLI
## A simple CLI to get images from mars rovers using Nasa's API.

### How it works :
#### When you run `martian` in terminal the program will make a `mars.md` file in your current folder.
#### For it to work you will need API key 🔑 from NASA which you can get from [HERE](http://api.nasa.gov/) (It's free).
#### Use any MarkDown reader to open `mars.md` and see images.

### Demo of V1 of Martian CLI:
![Working Demo](https://github.com/Manas02/Martian/blob/main/animated.gif)

### How To Setup:
#### Go to folder containing martian.py and type `chmod +x martian.py` to make it executable. 
#### Go to your preffered shell(bash,zsh)'s config file i.e .bashrc & .zshrc respectively .
#### Then append `alias martian='path/to/Martian.py'`
#### Then you can call `martian` anywhere in file system.

### Possible Errors:
#### 1️⃣ If `interpretor error` occurs , then change the first line of `martian.py` to PATH of python3 on your system after `#!`. 
#### 2️⃣ While using `V2` of CLI it is important for progress bar to have a dependancy `tqdm`. 
#### To install `tqdm` type `pip install tqdm` in terminal.
