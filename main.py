import subprocess
import sys
import time

import concurrent.futures

run_id = sys.stdin.readline()
s = True
old_time = time.time()


def collector():
    for i in range(40):
        time.sleep(15)
        save_logs(i)


def save_logs(t):
    print('saving logs for iteration ', t)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(100):
            executor.submit(record_log, i)


def record_log(i):
    f = open('out-' + str(i) + '.json', 'a')
    c = 'tg-celestia-' + str(run_id.split('\n')[0]) + '-validators-' + str(i) + ''
    subprocess.call(
        ['kubectl', 'exec', c, '--', 'cat', '/.celestia-app/data/mempool_metrics.json'],
        stdout=f)


while s:
    current_time = time.time()
    if current_time - old_time < 240:
        collector()
    else:
        s = False
