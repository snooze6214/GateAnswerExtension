## NOTE: There is a better method for calculating GATE marks and your predicted rank: https://gateoverflow.in/gate-cse-rank-predictor/
### Also while you are at it, please checkout [GOClasses](https://www.goclasses.in/)

# GATE Score calculator

![screenshot](screenshot.png?raw=true "screenshot")

## how to use:
- download this repository (either git clone or download zip)
- open chrome
- go to "chrome://extensions/"
- turn on developer mode
- click on open unpacked
- select the folder named "extensions"
- log on to gate portal and look at your response

OR

**watch this video:**

[![video thumbnail](https://img.youtube.com/vi/WgPzONbViIA/0.jpg)](https://www.youtube.com/watch?v=WgPzONbViIA)

(thank you GO Classes for the shoutout <3)

## where are the answers from (only for cs):
the answers are scraped from the gate overflow website using [scrape.py](./scrape.py)

thanks to [@priyavrat-misra](https://priyavr.at) for a fix on Jio networks

## adding answer key for other subjects
Note: For CS, the answer key is automatically fetched from GateOverflow, but for other
subjects, the answer key is community provided to the repo.

## Request for contribution:
If you are from branches other than CS, please make a PR with an answer key for your subject. If you are doing so, please do submit the source of the answer key.
To add an answer key, make a file named `answers_{SUBJECT CODE}.json` 
(for eg. `answers_CS.json`), copy the contents of `answers_template.json` to it, and
enter the correct answers to it. for multiselect, seperate the choices by a `;`
