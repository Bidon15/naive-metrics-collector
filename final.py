import json

v0 = 'v0'
v1 = 'v1'
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


v0vals = transform_data(v0)
v1vals = transform_data(v1)
v2vals = transform_data(v2)

print('100 validators set and 1100 PFBs from 1100 Celestia Nodes')

print('V0 Mempool')
stats(v0vals, 'AlreadySeenTxs')
stats(v0vals, 'AlreadyRejectedTxs')
stats(v0vals, 'RequestedTxs')
stats(v0vals, 'RerequestedTxs')
stats(v0vals, 'LostTxs')
stats(v0vals, 'ReceivedTxBytes')
stats(v0vals, 'ReceivedStateBytes')

print('V1 Mempool')
stats(v1vals, 'AlreadySeenTxs')
stats(v1vals, 'AlreadyRejectedTxs')
stats(v1vals, 'RequestedTxs')
stats(v1vals, 'RerequestedTxs')
stats(v1vals, 'LostTxs')
stats(v1vals, 'ReceivedTxBytes')
stats(v1vals, 'ReceivedStateBytes')


print('\nV2 Mempool')
stats(v2vals, 'AlreadySeenTxs')
stats(v2vals, 'AlreadyRejectedTxs')
stats(v2vals, 'RequestedTxs')
stats(v2vals, 'RerequestedTxs')
stats(v2vals, 'LostTxs')
stats(v2vals, 'ReceivedTxBytes')
stats(v2vals, 'ReceivedStateBytes')


mb = 1024 * 1024


print('\nV0 Mempool')
v0_ltb, v0_htb, v0_avgtb = stats(v0vals, 'SentTransactionBytes')
v0_lsb, v0_hsb, v0_avgsb = stats(v0vals, 'SentStateBytes')
print('\nV1 Mempool')
v1_ltb, v1_htb, v1_avgtb = stats(v1vals, 'SentTransactionBytes')
v1_lsb, v1_hsb, v1_avgsb = stats(v1vals, 'SentStateBytes')
print('\nV2 Mempool')
v2_ltb, v2_htb, v2_avgtb = stats(v2vals, 'SentTransactionBytes')
v2_lsb, v2_hsb, v2_avgsb = stats(v2vals, 'SentStateBytes')

print('\nV0 Mempool')
print('SentTransactionBytes + SentStateBytes counted in MBs')
print('Lowest is {0} MBs'.format((v0_ltb+v0_lsb)/mb))
print('Highest is {0} MBs'.format((v0_htb+v0_hsb)/mb))
print('Average is {0} MBs'.format((v0_avgtb+v0_avgsb)/mb))

print('\nV1 Mempool')
print('SentTransactionBytes + SentStateBytes counted in MBs')
print('Lowest is {0} MBs'.format((v1_ltb+v1_lsb)/mb))
print('Highest is {0} MBs'.format((v1_htb+v1_hsb)/mb))
print('Average is {0} MBs'.format((v1_avgtb+v1_avgsb)/mb))

print('\nV2 Mempool')
print('SentTransactionBytes + SentStateBytes counted in MBs')
print('Lowest is {0} MBs'.format((v2_ltb+v2_lsb)/mb))
print('Highest is {0} MBs'.format((v2_htb+v2_hsb)/mb))
print('Average is {0} MBs'.format((v2_avgtb+v2_avgsb)/mb))

print('\nV0 is consuming more bytes then V2 fold wise')
print('Lowest being x{0} more '.format(int((v0_ltb+v0_lsb)/(v2_ltb+v2_lsb))))
print('Highest being x{0} more '.format(int((v0_htb+v0_hsb)/(v2_htb+v2_hsb))))
print('Average being x{0} more '.format(int((v0_avgtb+v0_avgsb)/(v2_avgtb+v2_avgsb))))

print('\nV1 is consuming more bytes then V2 fold wise')
print('Lowest being x{0} more '.format(int((v1_ltb+v1_lsb)/(v2_ltb+v2_lsb))))
print('Highest being x{0} more '.format(int((v1_htb+v1_hsb)/(v2_htb+v2_hsb))))
print('Average being x{0} more '.format(int((v1_avgtb+v1_avgsb)/(v2_avgtb+v2_avgsb))))




