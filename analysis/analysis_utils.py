import networkx as nx
import networkx as nx
import os
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
import ast
from PIL import Image
from nltk.tokenize import TweetTokenizer
import re
import random
import pickle
import gensim
from collections import Counter
import itertools
from networkx.algorithms.centrality import out_degree_centrality, betweenness_centrality, degree_centrality
import ast

def create_graph_df(graph):
    graph_df = pd.DataFrame(columns=['username', 'sentiment', 'sentimentComm'])
    #graph_df = pd.DataFrame(columns=['username', 'sentiment', 'weightComm', 'sentimentComm'])
    for node in tqdm(graph.nodes(data=True)):
        new_row = [node[0], node[1]['sentiment'], node[1]['sentimentComm']]
        #new_row = [node[0], node[1]['sentiment'], node[1]['weightComm'], node[1]['sentimentComm']]
        graph_df.loc[len(graph_df)] = new_row
    return graph_df


def extract_community(G, id_com, type_com):
    community_node = list()

    for node in G.nodes():
        if  G.nodes[node][type_com] == id_com:
            community_node.append(node)
    subgraph = G.subgraph(community_node)
    return subgraph

def create_direct_multigraph(graph):
    G_multi = nx.MultiDiGraph()
    for edge in graph.edges(data = True):
        weight = edge[2]['weight']
        for _ in range(int(weight)):
            G_multi.add_edge(edge[0], edge[1])

    print(nx.info(G_multi))
    return G_multi

def compute_degree(graph, opt):
    graph_multi = create_direct_multigraph(graph)
    print(nx.info(graph_multi))

    if opt == 0:
        degree = degree_centrality(graph_multi)
    elif opt == 1:
        degree = out_degree_centrality(graph_multi)

    degree_sorted = sorted(degree.items(), key=lambda x: x[1], reverse=True)
    print('degree:', degree_sorted[0:10])

def compute_betweenness(graph):
    graph_multi = create_direct_multigraph(graph)
    print(nx.info(graph_multi))

    k = int(len(graph)*0.6)
    betweenness = betweenness_centrality(graph, k = k, normalized = True, weight = 'weight')
    betweenness_sorted = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)
    print('between:',betweenness_sorted[0:10])


def community_pie_chart(graph, comm_type, name):

    communities = dict()
    for node in graph.nodes(data=True):
        if not(f'community: {node[1][comm_type]}' in communities):
            communities[f'community: {node[1][comm_type]}'] = 1
        else:
            communities[f'community: {node[1][comm_type]}'] += 1


    com = list(communities.keys())
    com_comp = list(communities.values())
    colors = ['#b50000', '#0045b5']
    if com[0] != 'community: 1':
        com[0], com[1] = com[1], com[0]
        com_comp[0], com_comp[1] = com_comp[1], com_comp[0]


    fig, ax = plt.subplots()
    ax.pie(com_comp, labels = com, explode = [0, 0.1], shadow=True,
           startangle = 90, colors = colors, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%', textprops={'fontsize': 16})
    ax.set_title(f'{name}', fontsize=20)
    plt.savefig(f'vax_{name}.png')
    plt.show()

def plot_sentiment_distribution1(compact_graph, name, sentiment_df):

    fig, ax = plt.subplots()
    ax = sns.distplot(sentiment_df['sentiment'], hist=False, label='Sentiment Score of whole tweets')
    ax.set_title(f'{name}', fontsize=20)
    ax.set_xlabel('Sentiment Score')
    ax.set_ylabel('Distribution Probability')
    ax.legend()
    plt.savefig(f'vax_{name}_whole.png')
    plt.show()

def plot_sentiment_distribution2(compact_graph, name, sentiment_df):
    fig, ax = plt.subplots()
    column = 'sentimentComm'
    sentiment_df_weight_0 = sentiment_df.query(f'{column} == 0')
    sentiment_df_weight_1 = sentiment_df.query(f'{column} == 1')
    ax = sns.distplot(sentiment_df_weight_0['sentiment'], color='b', hist=False, label='Community 0')
    ax = sns.distplot(sentiment_df_weight_1['sentiment'], color='r', hist=False, label='Community 1')
    ax.set_title('Distribution of Sentiment Score in Two Communities', fontsize=20)
    ax.set_xlabel('Sentiment Score', fontsize=16)
    ax.set_ylabel('Distribution Probability', fontsize=16)
    ax.xaxis.set_tick_params(labelsize=13)
    ax.yaxis.set_tick_params(labelsize=13)
    ax.legend(prop={"size":20})
    plt.savefig(f'vax_{name}_twocomm.png')
    plt.show()


def plot_degree_distribution(graph, name, opt):
    degree_distribution = pd.DataFrame(columns=['degree_value', 'community', 'towards', 'placeholder'])
    colors = ['#b50000', '#0045b5']

    for node in tqdm(graph.nodes(data=True)):
        if opt == 0:
            title = f'Distribuzione per {name}'

            out_edges = list(graph.out_edges(node[0], data=True))
            in_edges = list(graph.in_edges(node[0], data=True))
            out_degree_values = 0
            in_degree_values = 0

            comm = node[1]['sentimentComm']

            for edge in out_edges:
                out_degree_values += edge[2]['weight']

            for edge in in_edges:
                in_degree_values += edge[2]['weight']

            degree_distribution.loc[len(degree_distribution)] = [out_degree_values, comm, 'outdegree', '']
            degree_distribution.loc[len(degree_distribution)] = [in_degree_values, comm, 'indegree', '']
        else:
            graph_name = graph.name.split('graph')[1]
            title = f'Distribution of {graph_name}'
            edges = list(graph.edges(node[0], data=True))
            edge_degree = 0
            comm = node[1]['weightComm']
            for edge in edges:
                edge_degree += edge[2]['weight']
            degree_distribution.loc[len(degree_distribution)] = [edge_degree, comm, 'total_degree', '']

    degree_value = degree_distribution['degree_value']
    removed_outliers = degree_value.between(degree_value.quantile(.25), degree_value.quantile(0.85))
    index_names = degree_distribution[~removed_outliers].index
    degree_distribution.drop(index_names, inplace=True)
    degree_distribution['degree_value'] = degree_distribution['degree_value'].apply(lambda x: float(x))


    fig, ax = plt.subplots()
    if opt == 1:
        x_value = 'placeholder'
    else:
        x_value = 'towards'

    ax = sns.violinplot(x=x_value, y='degree_value', hue='community', data=degree_distribution, split=True, palette=['blue', 'red'], scale='count', bw=0.2)
    ax.set_title(title, fontsize=15)
    ax.set_xlabel('Distribution of degree', fontsize=15)
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.legend(title='Community', prop={"size":15})
    ax.xaxis.set_tick_params(labelsize=15)
    ax.yaxis.set_tick_params(labelsize=15)
    plt.savefig(f'vax_{name}_twocomm.png')
    plt.show()