from alpha_vantage.timeseries import TimeSeries
from slack_bot_utils import SlackBot
import yaml


def main():
    with open('config.yaml') as f:
        config = yaml.safe_load(f)

    slack_bot = SlackBot(config['slack'])


    #    slack_bot.send_message('message-from-past', 'Hello World')
    ts = TimeSeries('LBNRUHGPEPVH3NQ0', output_format='pandas')
    values, columns = ts.get_intraday(symbol='TSLA', interval='10min')

    #import matplotlib.pyplot as plt
    print(values, columns)

if __name__ == '__main__':
    main()