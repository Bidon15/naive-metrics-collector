import json

# path = 'cat-9'
# v0 = 'v0'
# v1 = 'v1'
# v2 = 'v2'
#
# path = 'cat-9/hybrid-v1-v2'
path = 'cat-simple-1'


def transform_data(dr, ver):
    sum_path = 'out-{0}.json'.format(ver)
    summary = open(sum_path, 'a')
    data = dict()
    for i in range(50):
        # pathj = '{0}/{1}/out-{2}.json'.format(dr, ver, i)
        pathj = '{0}/out-{1}.json'.format(dr, i)
        f = open(pathj, 'r')
        j = json.load(f)

        for v in j:
            if 9000 < v['SuccessfulTxs'] < 11050:
                data[i] = v
    json.dump(data, summary)


# transform_data(path, v0)
transform_data(path, 'v2')
# transform_data(path, v2)
