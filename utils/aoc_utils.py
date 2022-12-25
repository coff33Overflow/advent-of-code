from bs4 import BeautifulSoup
from colorama import Fore, Style
import os, sys, requests, browser_cookie3, click
sys.dont_write_bytecode = True

CURRENT_DIR = os.getcwd()
PUZZLE_LOCKED = "Puzzle not unlocked yet."

# Get cookies from the browser
SESSION_COOKIE = browser_cookie3.chrome(domain_name=".adventofcode.com")

def handle_error_status(code):
    if code == 404:
        print(f"{Fore.RED}{code}: This day is not available yet!{Style.RESET_ALL}")
        quit()
    elif code == 400:
        print(f"{Fore.RED}{code}: Bad credentials!{Style.RESET_ALL}")
        quit()
    elif code > 400:
        print(f"{Fore.RED}{code}: General error!{Style.RESET_ALL}")
        quit()
def update_problem(path, year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(url, cookies=SESSION_COOKIE)
    handle_error_status(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    content = '\n\n\n'.join([a.text for a in soup.select('article')])
    if content == "":
         content = PUZZLE_LOCKED
    with open(path, 'w') as f:
        f.write(content)

def submit(answer, level, year, day):
    if len(str(answer)) > 0:
        if click.confirm(f"\nYou are trying to submit answer for part {level}: {answer}. Do you want to continue?", default=None):
            data = {"level": str(level), "answer": str(answer)}
            response = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", cookies=SESSION_COOKIE, data=data)
            handle_error_status(response.status_code)
            print(f"\n{Fore.CYAN}For day {day} part {level}, you submitted: {answer}{Style.RESET_ALL}\n")
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                message = soup.article.text
            except AttributeError:
                message = f"{Fore.RED} {PUZZLE_LOCKED} {Style.RESET_ALL}"
                print(message)

            if "that's the right answer" in message.lower():
                print(f"\n{Fore.GREEN}Correct! ⭐️{Style.RESET_ALL}")
            elif "not the right answer" in message.lower():
                print(f"\n{Fore.RED}Wrong answer 🎅🏾🙅🏼‍♀️! For details:\n{Style.RESET_ALL}")
                print(message)
            elif "answer too recently" in message.lower():
                print(f"\n{Fore.YELLOW}You gave an answer too recently{Style.RESET_ALL}")
            elif "already complete it" in message.lower():
                print(f"\n{Fore.YELLOW}You have already solved this.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Answer cannot be blank.{Style.RESET_ALL}")

    update_problem(f"{CURRENT_DIR}/problem.txt", year, day)