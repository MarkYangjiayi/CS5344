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
    _, _ = community_detection('Vax', path, 'sentiment')
    log_write_start_end(False, 'Vax')