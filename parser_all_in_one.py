import codecs
import matplotlib.pyplot as plt
from ast import literal_eval
import os
import matplotlib.dates as mdates

from dateutil.parser import parse
import time
from datetime import *

#
# '''
# import fileinput
#
# parsed_info = []
# for linenum, line in enumerate(fileinput.input()):
#     if not line.startswith("#DEBUG"):
#         continue # Skip line
#
#     msg = line.partition("MSG")[1] # Get everything after MSG
#     words = msg.split() # Split on words
#     info = {}
#     for w in words:
#         k, _, v = w.partition(":") # Split each word on first :
#         info[k] = v
#
#     parsed_info.append(info)
#
#     if linenum % 10000 == 0: # Or maybe  if len(parsed_info) > 500:
#         # Insert everything in parsed_info to database
#         ...
#         parsed_info = [] # Clear
# '''


class LogData:
    def __init__(self, time_stamp, method_name, execution_time):
        self.time_stamp = time_stamp
        self.method_name = method_name
        self.execution_time = execution_time


# read file
def get_file_contents(file_name):
    with codecs.open(file_name, mode='r', encoding='utf-8') as tmp_file:
        tmp_data = tmp_file.read()
    return tmp_data


# save data
def save_xml_to_file(xml_data, file_name):
    with codecs.open(file_name, mode='w') as tmp_file:
        tmp_file.write(xml_data)


# 26.02 15:51:46,026 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
# time_stamp => FINISH => method? TIME

counter = 0


def save_plot(path, ext='png', close=True):
    directory = os.path.split(path)[0]
    filename = "%s.%s" % (os.path.split(path)[1], ext)
    if directory == '':
        directory = '.'

    if not os.path.exists(directory):
        os.makedirs(directory)

    save_path = os.path.join(directory, filename)

    plt.savefig(save_path)

    if close:
        plt.close()


def parse_perf_data(data, data_types):
    data_collection = {}
    for line in data.split('\n'):
        if "FINISH" not in line:
            continue
        else:
            # working with selected FINISH line
            for data_type in data_types:
                if data_type in line:
                    chunks = line.split(' ')

                    if data_type not in data_collection:
                        data_collection[data_type] = []

                    current_time = datetime.strptime(chunks[0] + " " + chunks[1], "%d.%m %H:%M:%S,%f")
                    total_time = int(chunks[7][5:])

                    data_collection[data_type].append((current_time, total_time))

                    #data_collection
                    ##global counter
                    #counter +=1
                    # a.append(current_time)
                    #b.append(total_time) # todo: need to convert to ticks

    return data_collection


import matplotlib.cbook as cbook


def my_format_function(x, pos=None):
    x = mdates.num2date(x)
    if pos == 0:
        fmt = '%D %H:%M:%S'
    else:
        fmt = '%H:%M:%S'
    label = x.strftime(fmt)
    label = label.rstrip("0")
    label = label.rstrip(".")
    return label


from matplotlib.ticker import FuncFormatter

if __name__ == "__main__":

    data_types = ("getGoodsCatalogWithTi", "importActionsWithTi", "importCashiersWithTi", "getCardsCatalogWithTi",
                  "writeObjectsToFile", "insertEvent", "getNewProductsToCash", "processDocument")

    result = {}

    for data_type in data_types:
        result[data_type] = []

    for data_file in os.listdir("./data"):
        data_collection = parse_perf_data(get_file_contents("./data/" + data_file), data_types)
        for data_type in data_types:
            if data_type in data_collection:
                result[data_type].extend(data_collection[data_type])

    #base_x.extend(x)
    #base_y.extend(y)

    #max_value = max(base_y)
    #max_value_index = base_y.index(max_value)


    fig, ax = plt.subplots()

    for data_type in data_types:
        if data_type in result:
            ax.plot(map(lambda x: x[0], result[data_type]), map(lambda x: x[1], result[data_type]),
                    label=data_type)

    ax.grid(True)
    ax.format_xdata = mdates.DateFormatter("%H:%M:%S.%f")
    legend = ax.legend(loc='upper left', shadow=False, fontsize='xx-small')

    fig.autofmt_xdate()

    #plt.show()
    save_plot('example')

