import os
import ast
import networkx as nx
import pandas as pd
from tqdm import tqdm
import numpy as np

from data.utils2 import (add_edge, manage_and_save)


def read_data(path):
    """
    Read the relative fields that are usefull in building the paths.
    Results will be be saved in a new file ./data/Final_data_2.csv
    """
    df = pd.read_csv(path, usecols=['date', 'username', 'replies_count', 'retweets_count',
                                    'likes_count', 'hashtags', 'tweet', 'reply_to',])
    df['reply_to'].replace('[]', "['Self']", inplace=True)
    df['hashtags'].replace('[]', "['noOne']", inplace=True)
    df.to_csv('./data/Final_data_2.csv', encoding='utf-8', index=False)
    print('VACCINATION DATA FINAL SHAPE')
    print(df.shape)

def build_vaccination_graph(path):
    """
    Build the vaccination graph.
    """

    # Read Twitter data from csv file
    df = pd.read_csv(path + './Final_data_2.csv', lineterminator='\n')

    # Build empty Graph and DiGraph
    G_dg = nx.DiGraph()
    G_g = nx.Graph()

    for _, row in tqdm(df.iterrows(), desc="Rows processed"):
        # if pd.isnull(row[7]):
        #reply = ast.literal_eval(row[7])
        # else: reply = ['self']
        reply = f(row[7])
        if 'self' in reply:
            G_dg = add_edge(G_dg, row[2], row[6], row[5], row[4], row[3], row[1], row[1])
        else:
            for re in reply:
                G_dg = add_edge(G_dg, row[2], row[6], row[5], row[4], row[3], row[1], re)
                G_g = add_edge(G_g, None, None, None, None, None, row[1], re)

    G_dg.name = 'Starter vax Direct Graph'
    G_g.name = 'Starter vax Graph'

    graphs = [G_dg, G_g]
    manage_and_save(graphs, path)

def f(x):
    try:
        return ast.literal_eval(str(x))
    except Exception as e:
        print(e)
        return []

if __name__ == '__main__':
    path = "./data/small.csv"
    read_data(path)