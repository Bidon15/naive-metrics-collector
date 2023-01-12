import json

v2 = 'v2'


def transform_data(dr):
    sum_path = 'out-{0}.json'.format(dr)
    summary = open(sum_path, 'r')
    vals = json.load(summary)
    return vals


def stats(vals, tag):
    low: int = vals['0'][tag]
    high: int = 0
    avg: int = 0

    c: int = 0
    for val in vals:
        c += 1
        if vals[val][tag] > high:
            high = vals[val][tag]
        if low > vals[val][tag]:
            low = vals[val][tag]
        avg += vals[val][tag]
    print('\nlowest {0} is {1}'.format(tag, low))
    print('highest {0} is {1}'.format(tag, high))
    print('average {0} is {1} \n'.format(tag, avg/len(vals)))
    return low, high, avg/len(vals)


v2vals = transform_data(v2)

print('100 validators set and 1100 PFBs from 1100 Celestia Nodes')


print('\nV2 Mempool')
stats(v2vals, 'AlreadySeenTxs')
stats(v2vals, 'AlreadyRejectedTxs')
stats(v2vals, 'RequestedTxs')
stats(v2vals, 'RerequestedTxs')
stats(v2vals, 'LostTxs')
stats(v2vals, 'ReceivedTxBytes')
stats(v2vals, 'ReceivedStateBytes')


mb = 1024 * 1024

print('\nV2 Mempool')
v2_ltb, v2_htb, v2_avgtb = stats(v2vals, 'SentTransactionBytes')
v2_lsb, v2_hsb, v2_avgsb = stats(v2vals, 'SentStateBytes')


print('\nV2 Mempool')
print('SentTransactionBytes + SentStateBytes counted in MBs')
print('Lowest is {0} MBs'.format((v2_ltb+v2_lsb)/mb))
print('Highest is {0} MBs'.format((v2_htb+v2_hsb)/mb))
print('Average is {0} MBs'.format((v2_avgtb+v2_avgsb)/mb))




