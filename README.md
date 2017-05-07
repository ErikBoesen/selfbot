# selfbot
A simple selfbot which I use to automate some tasks on Discord.

This code may be hard to read, messy, or poorly written. I make no promises.

## Dependencies
* [Python 3](https://www.python.org/downloads)
* Python packages:

        pip3 install -r requirements.txt


## Running
1. First you'll need to get your token. Open Discord, go to View > Developer > Toggle Developer Tools, or press `Cmd+Alt+I` if on a Mac and `Ctrl+Alt+I` otherwise.
2. Navigate to the Application tab of the developer tools panel.
3. Open the Local Storage dropdown on the left panel and select the only option which appears.
4. Copy the `token` field, which should be at the bottom of the value list.
5. Rename or copy `config.ini.example` to `config.ini`.
6. Write your token in `config.ini` in the `selfbot` directory. You should not surround it with quotation marks.
7. While in `selfbot` directory, run:

        python3 bot.py


## Author
This software was created by [Erik Boesen](https://github.com/ErikBoesen).

## License
This software is protected under the [MIT License](LICENSE).
