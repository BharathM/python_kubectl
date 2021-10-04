import subprocess
import re

if __name__ == '__main__':

    process = subprocess.Popen(args=['kubectl', 'get', 'pods', '-o', 'wide'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    output, errors = process.communicate()
    postString = output.strip()
    process.terminate()

    lines = re.split('\n', postString)
    # for x in range(0, len(lines)):
    #     print(lines[x])

    data_split = []
    for line in lines:
        data_split.append(line.split())

    data = []
    pod_list = ["server"]
    search_list = '(?:% s)' % '|'.join(pod_list)
    for x in range(0, len(data_split)):
        if re.match(search_list, data_split[x][0]):
            data.append(tuple((data_split[x][0], data_split[x][5])))
    # print(data)

    for x in range(0, len(data)):
        process = subprocess.Popen(args=['kubectl', 'exec', data[x][0], '--', 'curl', 'localhost:8091/status'],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = process.communicate()
        postString = output.strip()
        print (postString)
    process.terminate()



