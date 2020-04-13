terminalcolors = {"OKGREEN": '\033[92m',
                  "WARNING": '\033[93m',
                  "FAIL": '\033[91m',
                  "ENDC": '\033[0m'}

def print_to_terminal(type, text):
    print(terminalcolors[type] + text + terminalcolors["ENDC"])