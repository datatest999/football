import pandas as pd
import matplotlib.pyplot as plt

# Class for Team Performance and Visualizing the Data
class EPLTeamPerformanceAnalyzer:

    def __init__(self, dataframe: pd.DataFrame): 
        self.df = dataframe  

    def calculate_win_percentage(self):
        filtered_df = self.df[self.df['winnerName'] != 'Draw']
        return filtered_df.groupby(['season'])['winnerName'].value_counts(normalize=True) * 100


    def calculate_home_win_percentage(self):
        filtered_df = self.df[self.df['winnerName'] != 'Draw']
        return filtered_df[filtered_df['matchScore'] ==
                       'HOME_TEAM']['winnerName'].value_counts(
                           normalize=True) * 100

    def calculate_away_win_percentage(self):
        filtered_df = self.df[self.df['winnerName'] != 'Draw']
        return filtered_df[filtered_df['matchScore'] ==
                       'AWAY_TEAM']['winnerName'].value_counts(
                           normalize=True) * 100

    def plot_win_percentage(self):
        win_percentage = self.calculate_win_percentage()
        win_percentage.plot(kind='bar',
                            figsize=(14, 6),
                            title='Win Percentage by Team each Year')
        plt.xlabel('Team')
        plt.ylabel('Win Percentage')
        plt.xticks(rotation=85)
        plt.tight_layout()
        plt.show()


    def plot_home_win_percentage(self):
        home_win_percentage = self.calculate_home_win_percentage()
        home_win_percentage.plot(kind='bar',
                                 figsize=(14, 6),
                                 title='Home Win Percentage by Team')
        plt.xlabel('Team')
        plt.ylabel('Home Win Percentage')
        plt.xticks(rotation=85)
        plt.tight_layout()
        plt.show()

    def plot_away_win_percentage(self):
        away_win_percentage = self.calculate_away_win_percentage()
        away_win_percentage.plot(kind='bar',
                                 figsize=(14, 6),
                                 title='Away Win Percentage by Team')
        plt.xlabel('Team')
        plt.ylabel('Away Win Percentage')
        plt.xticks(rotation=85)
        plt.tight_layout()
        plt.show()
