import os

import random
from controversy.random_walks import random_walks, random_walks_centrality
from controversy.change_side_controversy import change_side_controversy
from controversy.GMCK import start_GMCK
import logging
from datetime import datetime
import networkx as nx
from controversy.logs import log_write_start_end
from networkx.algorithms.shortest_paths.generic import average_shortest_path_length


def start_detection():
    logging.basicConfig(filename='controversy.log', level=logging.INFO, format='%(message)s')
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    logging.info(f'RUN TIME: {today}')

    vax_graph()

def vax_graph():
    logging.basicConfig(filename='controversy.log', level=logging.INFO, format='%(message)s')

    log_write_start_end(True, 'Vaccination')
    graph = nx.read_gml('D:\AAA_NUS\CS5344\data\graph\Final_Graph_sentiment_Vax.gml')
    print('down')
    shortest_path = average_shortest_path_length(graph)
    logging.info(f'Average shortest path: {shortest_path}')
    print('sp down')
    random_walks(graph, 0.6, shortest_path*2, 1)
    random_walks_centrality(graph, 1)
    print('rw down')

    change_side_controversy(graph, 0.6, shortest_path*2, 1)
    print('change down')

    start_GMCK(graph, 'sentimentComm')
    print('gmck down')

    #start_EC(graph, 'sentimentComm')
    #print()
    starting_path = os.getcwd()
    os.chdir(starting_path)
    log_write_start_end(False)

start_detection()