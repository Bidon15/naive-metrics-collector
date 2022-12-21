import json

v1 = 'v1_meh'
v2 = 'v2_wow'


def transform_data(dr):
    sum_path = 'out-{0}.json'.format(dr)
    summary = open(sum_path, 'a')
    data = dict()
    for i in range(100):
        path = '{0}/out-{1}.json'.format(dr, i)
        f = open(path, 'r')
        j = json.load(f)

        for v in j:
            if 11000 < v['SuccessfulTxs'] < 12000:
                data[i] = v
    json.dump(data, summary)


transform_data(v1)
transform_data(v2)