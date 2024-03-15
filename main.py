# -*- coding: utf-8 -*-
"""
Created on Thursday March 14 2024

@author: Amin Abbasnejad
"""
#-------------------------------- Import Necessary Libraries --------------------------------

import json
from data_handler import DataHandler
from performance_analysis import EPLTeamPerformanceAnalyzer
import argparse



def get_args_parser():
    parser = argparse.ArgumentParser('EPLTeamPerformanceAnalyzer', add_help = False)
    parser.add_argument('--extract_csv', action = 'store_true', help='generate csv file')
    parser.add_argument('--plt_win_prct', action = 'store_true', help='plot win percentage')
    parser.add_argument('--plt_home_win', action = 'store_true', help='plot home win')
    parser.add_argument('--plt_away_win', action = 'store_true', help='plot away win')
    return parser



def load_config():
    # Load configuration from file
    with open('config.json') as f:
        config = json.load(f)
    return config

def main(args):
    config = load_config()

    # create an instance of the data handler
    data_handler = DataHandler(config)

    # call the fetch_data_api
    data = data_handler.fetch_data_api()
    # transform to csv
    data_handler.transform_data_to_csv(data)

    # Analysis and Visulisation

    # Create an instance of the EPLTeamPerformanceAnalyzer class
    data_frame = data_handler.get_data_frame()
    analyzer = EPLTeamPerformanceAnalyzer(data_frame)

    if args.plt_win_prct:
        analyzer.plot_win_percentage()

    # Plotting Home Win Percentage
    if args.plt_home_win:
        analyzer.plot_home_win_percentage()

    # Plotting Away Win Percentage
    if args.plt_away_win:
        analyzer.plot_away_win_percentage()




if __name__ == "__main__":
    parser=argparse.ArgumentParser('EPL Team Performance Analyzer script', parents= [get_args_parser()])
    args = parser.parse_args()
    main(args)

