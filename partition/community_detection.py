import os
from tqdm import tqdm
from datetime import datetime
import logging

from partition.utils import community_detection, note_difference
from partition.logs import log_write_start_end


def start_community_detection():
    logging.basicConfig(filename='community_log.log', level=logging.INFO, format='%(message)s')
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    logging.info(f'RUN TIME: {today}')
    vax_graph()


def vax_graph():
    path = "./data/graph"
    log_write_start_end(True, 'VACCINATION GRAPH')
    # info_no_sent_metis, info_no_sent_fluid = community_detection('Vax', path, 'weight')
    info_sent_metis, info_sent_fluid = community_detection('Vax', path, 'sentiment')
    # info_topic_metis, info_topic_fluid = community_detection('Vax', path, 'topic')
    # info_hybrid_metis, info_hybrid_fluid = community_detection('Vax', path, 'hybrid')

    # note_difference(info_no_sent_metis, info_sent_metis, 'Metis', 'sentiment')
    # note_difference(info_no_sent_metis, info_topic_metis, 'Metis', 'topic')
    # note_difference(info_no_sent_metis, info_hybrid_metis, 'Metis', 'hybrid')

    
    # note_difference(info_no_sent_fluid, info_sent_fluid, 'Fluid')
    log_write_start_end(False, 'Vax')