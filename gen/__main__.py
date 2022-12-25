import sys, errno, requests, re, browser_cookie3, datetime
sys.dont_write_bytecode = True
from pathlib import Path
from string import Template
from datetime import date
from colorama import Fore, Style
from dotenv import load_dotenv
from bs4 import BeautifulSoup

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

def relative_path(filename):
    path = Path(__file__).parent.resolve()
    project_path = Path(path / "../../../").parent.resolve()
    full_path = Path(path/ filename).resolve()
    r_path = str(full_path).split(str(project_path))
    return r_path[1]

# print a status of the generated files
def info(filename, status):
    r_path = relative_path(filename)
    if status:
        print("{}* creating{} {}".format(Fore.GREEN, Style.RESET_ALL, r_path))
    else:
        print("{}* ignoring{} {} already exists".format(Fore.YELLOW, Style.RESET_ALL, r_path))

# open the file in read mode
def read_file(filename):
    path = Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        return f.read()

# create and write the files
def write_file(filename, content):
    path = Path(__file__).parent.resolve()
    if not Path(path / filename).parent.exists():
        try:
            Path(path / filename).parent.mkdir(parents=True)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    if not Path(path / filename).exists():
        with open(path / filename, 'w') as f:
            f.write(content)

        info(filename, True)
    else:
        info(filename, False)
        return

# get de default year
def default_year():
    today = date.today()
    if today.day == 12:
        return today.year
    else:
        return today.year - 1

# generate the input and puzzle problem text file from the url
def gen_file(path, year, day, session_cookies, filetype):
    if session_cookies is not None:
        if filetype == "input":
            url = f"https://adventofcode.com/{year}/day/{day}/input"
            r = requests.get(url, cookies=session_cookies)
            handle_error_status(r.status_code)
            content = r.text
            DO_NOT_REQUEST = "Please don't repeatedly request this endpoint before it unlocks!"
            if DO_NOT_REQUEST in content:
                print(f"{Fore.RED}Cannot create the input.txt as puzzle is not unlocked yet.{Style.RESET_ALL}")
            else:
                write_file(path, content)
        elif filetype == "problem":
            url = f"https://adventofcode.com/{year}/day/{day}"
            r = requests.get(url, cookies=session_cookies)
            handle_error_status(r.status_code)
            soup = BeautifulSoup(r.text, "html.parser")
            try:
                content = soup.article.text
                write_file(path, content)
            except AttributeError:
                    write_file(path, f"Puzzle not unlocked yet.")
        else:
            write_file(path, "")

# generate the base code from templates
def boilerplate(templates, paths, substitute):
    for i in list(zip(templates, paths)):
        data = read_file(i[0])
        t = Template(data)
        content = t.substitute(substitute)
        path = i[1].format(substitute["module_name"])
        write_file(path, content)

def main():
    load_dotenv()
    if len(sys.argv) != 3:
        print("--- aoc.gen needs only two argument ---")
        return

    d = re.search(r'\d+', sys.argv[2])
    if d is None:
        print("--- The argument must be `d + NUM` (e.g. d01) ---")
        return
    day = str(int(d.group(0)))

    y = re.search(r'\d+', sys.argv[1])
    if y is None:
        print("--- The argument must be `y + 4 digit NUM` (e.g. y2021) ---")
        return
    year = str(int(y.group(0)))
    if str(y) is None:
        year = str(datetime.date.today().year)

    session_cookies = browser_cookie3.chrome(domain_name=".adventofcode.com")

    templates = [
        "./templates/__main__.tpl",
        "./templates/part1.tpl",
        "./templates/part2.tpl",
    ]

    paths = [
        "../{}/__main__.py",
        "../{}/part1.py",
        "../{}/part2.py",
    ]

    input_path = "../{}/day{}/input.txt".format(year, day)
    problem_path = "../{}/day{}/problem.txt".format(year, day)
    boilerplate(templates, paths, {"module_name": f"{year}/day{day}", "day": day, "year": year})
    gen_file(problem_path, year, day, session_cookies, "problem")
    gen_file(input_path, year, day, session_cookies, "input")

if __name__ == "__main__":
    main()
