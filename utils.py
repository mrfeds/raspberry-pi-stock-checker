import termcolor
import requests
import time
import yaml


def print_logo() -> None:
    logo = """______  ___   ___________ _____      _____ _____ ______  ___  ______ ___________ 
| ___ \/ _ \ /  ___| ___ \_   _|    /  ___/  __ \| ___ \/ _ \ | ___ \  ___| ___ \\
| |_/ / /_\ \\\\ `--.| |_/ / | |______\ `--.| /  \/| |_/ / /_\ \| |_/ / |__ | |_/ /
|    /|  _  | `--. \  __/  | |______|`--. \ |    |    /|  _  ||  __/|  __||    / 
| |\ \| | | |/\__/ / |    _| |_     /\__/ / \__/\| |\ \| | | || |   | |___| |\ \ 
\_| \_\_| |_/\____/\_|    \___/     \____/ \____/\_| \_\_| |_/\_|   \____/\_| \_|"""
    print(termcolor.colored(logo, color='magenta', attrs=['bold']), end='')
    print(termcolor.colored('  by Louie Cai\n', color='magenta', attrs=['bold']))


def pretty_print(name: str, price: str, in_stock: bool, start='', date=None, other=None) -> None:
    if other is not None:
        other = other.rstrip()
        print(f'{start}{name}: {termcolor.colored(other, "yellow", attrs=["bold"])}')
    elif in_stock:
        print(f'{start}{name}: {termcolor.colored("In stock", "green", attrs=["bold"])}', end='')
        if date is not None and date != '':
            print(termcolor.colored(f' ({date})', attrs=['dark']))
        else:
            print()
    else:
        print(f'{start}{name}: {termcolor.colored("Out of stock", "red", attrs=["bold"])}')

    print(f'{start * 2}Price: {termcolor.colored(price, attrs=["reverse"])}')


def better_request(url: str, name: str, retry_time=4.0) -> requests.models.Response:

    my_headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36", 
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    while True:
        try:
            request = requests.get(url, headers=my_headers)
            if "200" not in str(request):
                raise ConnectionError

            return request
        except KeyboardInterrupt:
            exit()
        except:
            print(termcolor.colored(f'Request to {name} failed. Retrying in {retry_time} seconds...', 'red'))
            time.sleep(retry_time)


def parse_config(path: str) -> dict:
    with open(path) as config_file:
        return yaml.load(config_file, Loader=yaml.FullLoader)
