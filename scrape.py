import requests
from bs4 import BeautifulSoup
import json

go_links = [
    "https://gateoverflow.in/399255/gate-cse-2023-ga-question-1",
    "https://gateoverflow.in/399254/gate-cse-2023-ga-question-2",
    "https://gateoverflow.in/399253/gate-cse-2023-ga-question-3",
    "https://gateoverflow.in/399252/gate-cse-2023-ga-question-4",
    "https://gateoverflow.in/399251/gate-cse-2023-ga-question-5",
    "https://gateoverflow.in/399250/gate-cse-2023-ga-question-6",
    "https://gateoverflow.in/399249/gate-cse-2023-ga-question-7",
    "https://gateoverflow.in/399248/gate-cse-2023-ga-question-8",
    "https://gateoverflow.in/399247/gate-cse-2023-ga-question-9",
    "https://gateoverflow.in/399246/gate-cse-2023-ga-question-10",
    "https://gateoverflow.in/399311/gate-cse-2023-question-1",
    "https://gateoverflow.in/399310/gate-cse-2023-question-2",
    "https://gateoverflow.in/399309/gate-cse-2023-question-3",
    "https://gateoverflow.in/399308/gate-cse-2023-question-4",
    "https://gateoverflow.in/399307/gate-cse-2023-question-5",
    "https://gateoverflow.in/399306/gate-cse-2023-question-6",
    "https://gateoverflow.in/399305/gate-cse-2023-question-7",
    "https://gateoverflow.in/399304/gate-cse-2023-question-8",
    "https://gateoverflow.in/399303/gate-cse-2023-question-9",
    "https://gateoverflow.in/399302/gate-cse-2023-question-10",
    "https://gateoverflow.in/399301/gate-cse-2023-question-11",
    "https://gateoverflow.in/399300/gate-cse-2023-question-12",
    "https://gateoverflow.in/399299/gate-cse-2023-question-13",
    "https://gateoverflow.in/399298/gate-cse-2023-question-14",
    "https://gateoverflow.in/399297/gate-cse-2023-question-15",
    "https://gateoverflow.in/399295/gate-cse-2023-question-16",
    "https://gateoverflow.in/399294/gate-cse-2023-question-17",
    "https://gateoverflow.in/399293/gate-cse-2023-question-18",
    "https://gateoverflow.in/399292/gate-cse-2023-question-19",
    "https://gateoverflow.in/399291/gate-cse-2023-question-20",
    "https://gateoverflow.in/399290/gate-cse-2023-question-21",
    "https://gateoverflow.in/399289/gate-cse-2023-question-22",
    "https://gateoverflow.in/399288/gate-cse-2023-question-23",
    "https://gateoverflow.in/399287/gate-cse-2023-question-24",
    "https://gateoverflow.in/399286/gate-cse-2023-question-25",
    "https://gateoverflow.in/399285/gate-cse-2023-question-26",
    "https://gateoverflow.in/399284/gate-cse-2023-question-27",
    "https://gateoverflow.in/399283/gate-cse-2023-question-28",
    "https://gateoverflow.in/399282/gate-cse-2023-question-29",
    "https://gateoverflow.in/399281/gate-cse-2023-question-30",
    "https://gateoverflow.in/399280/gate-cse-2023-question-31",
    "https://gateoverflow.in/399279/gate-cse-2023-question-32",
    "https://gateoverflow.in/399278/gate-cse-2023-question-33",
    "https://gateoverflow.in/399277/gate-cse-2023-question-34",
    "https://gateoverflow.in/399276/gate-cse-2023-question-35",
    "https://gateoverflow.in/399275/gate-cse-2023-question-36",
    "https://gateoverflow.in/399274/gate-cse-2023-question-37",
    "https://gateoverflow.in/399273/gate-cse-2023-question-38",
    "https://gateoverflow.in/399272/gate-cse-2023-question-39",
    "https://gateoverflow.in/399271/gate-cse-2023-question-40",
    "https://gateoverflow.in/399270/gate-cse-2023-question-41",
    "https://gateoverflow.in/399269/gate-cse-2023-question-42",
    "https://gateoverflow.in/399268/gate-cse-2023-question-43",
    "https://gateoverflow.in/399267/gate-cse-2023-question-44",
    "https://gateoverflow.in/399266/gate-cse-2023-question-45",
    "https://gateoverflow.in/399265/gate-cse-2023-question-46",
    "https://gateoverflow.in/399264/gate-cse-2023-question-47",
    "https://gateoverflow.in/399263/gate-cse-2023-question-48",
    "https://gateoverflow.in/399262/gate-cse-2023-question-49",
    "https://gateoverflow.in/399261/gate-cse-2023-question-50",
    "https://gateoverflow.in/399260/gate-cse-2023-question-51",
    "https://gateoverflow.in/399259/gate-cse-2023-question-52",
    "https://gateoverflow.in/399258/gate-cse-2023-question-53",
    "https://gateoverflow.in/399257/gate-cse-2023-question-54",
    "https://gateoverflow.in/399256/gate-cse-2023-question-55"
]
correct_ans = []

i = 1
for link in go_links:
    data = requests.get(link).text
    soup = BeautifulSoup(data, 'html.parser')
    ans_btn = soup.find_all('button', class_='btn-info')
    if len(ans_btn) != 1:
        continue
    correct_ans.append({"qNo": i, "correctAns": ans_btn[0].getText()})
    i += 1

# For compatibility with old version of the extension
with open('answers.json', 'w') as file:
    file.write(json.dumps(correct_ans))

with open('answers_CS.json', 'w') as file:
    file.write(json.dumps(correct_ans))