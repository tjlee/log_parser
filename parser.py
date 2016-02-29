import os
import codecs
import argparse
from datetime import *

import matplotlib.pyplot as plt
import matplotlib.dates as m_dates


def get_file_contents(file_name):
    with codecs.open(file_name, mode='r', encoding='utf-8') as tmp_file:
        tmp_data = tmp_file.read()
    return tmp_data


def save_plot(path, ext='png', close=True):
    directory = os.path.split(path)[0]
    filename = "%s.%s" % (os.path.split(path)[1], ext)
    if directory == '':
        directory = '.'

    if not os.path.exists(directory):
        os.makedirs(directory)

    save_path = os.path.join(directory, filename)

    plt.savefig(save_path, format=ext, papertype='b10')

    if close:
        plt.close()


def parse_perf_data(data, data_types):
    result_collection = {}
    for line in data.split('\n'):
        if "FINISH" not in line:
            continue
        else:
            # working with selected FINISH line
            for data_type in data_types:
                # 26.02 15:51:46,026 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
                if data_type in line:
                    chunks = line.split(' ')

                    if data_type not in result_collection:
                        result_collection[data_type] = []

                    # getting log time
                    current_time = datetime.strptime(chunks[0] + " " + chunks[1], "%d.%m %H:%M:%S,%f")
                    # getting number from Time:XXXXX
                    total_time = int(chunks[7][5:])

                    result_collection[data_type].append((current_time, total_time))

    return result_collection


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", default="./data/",
                        help="Absolute path to directory with log files(default: ./data/")
    parser.add_argument("-e", "--ext", default="png",
                        help="Saved plot extension(default=png). Available: png, svg, pdf")
    parser.add_argument("-s", "--show", default=False, help="Show plot in runtime")
    parser.add_argument("-t", "--types", nargs="+", type=str,
                        default=["getGoodsCatalogWithTi", "importActionsWithTi", "importCashiersWithTi",
                                 "getCardsCatalogWithTi",
                                 "writeObjectsToFile", "insertEvent", "getNewProductsToCash", "processDocument"],
                        help='''Data types to analyze(default:"getGoodsCatalogWithTi" "importActionsWithTi" "importCashiersWithTi" "getCardsCatalogWithTi" "writeObjectsToFile" "insertEvent" "getNewProductsToCash" "processDocument"
                        To pass parameters use: -t "one" "two" "four"''')

    args = parser.parse_args()

    data_types_set = args.types
    data_folder = args.data

    result = {}

    for data_type in data_types_set:
        result[data_type] = []

    # reading data from all files in data_folder
    for data_file in os.listdir(data_folder):
        data_collection = parse_perf_data(get_file_contents(data_folder + data_file), data_types_set)
        for data_type in data_types_set:
            if data_type in data_collection:
                result[data_type].extend(data_collection[data_type])

    fig, ax = plt.subplots()

    # making plot
    for data_type in data_types_set:
        if data_type in result:
            print "=== Data type: %s ===" % data_type

            y_data = map(lambda x: x[1], result[data_type])

            if len(y_data) > 0:
                print "Max: %f" % max(y_data)
                print "Avg: %f" % float(sum(map(lambda x: x[1], result[data_type])) / float(len(result[data_type])))

                ax.plot(map(lambda x: x[0], result[data_type]), y_data,
                        label=data_type)
            else:
                print "No data"

    # printing and saving plot
    ax.grid(True)
    ax.format_xdata = m_dates.DateFormatter("%H:%M:%S.%f")
    legend = ax.legend(loc='upper left', shadow=False, fontsize='xx-small')
    fig.autofmt_xdate()

    if args.show:
        plt.show()
    else:
        save_plot('example', ext=args.ext)

