
from input_data import *


def input_file_data(input_file_name):

    variable_list = []

    with open(input_file_name) as file_obj:

        for line_data in file_obj:

            # for debug
            # print("line_data,len:", line_data, len(line_data))

            if len(line_data) <= 1:
                pass
            else:
                line_data_strip = line_data.strip()

                # for debug
                #print("line_data_strip", line_data_strip)

                split_line_data = line_data_strip.split(" ")

                # for debug
                # print("split_line_data", split_line_data)

                split_len = len(split_line_data)

                if split_len == 2:
                    # 処理可能なデータ
                    input_data_obj = InputData()
                    input_data_obj.variable_type = split_line_data[0]
                    input_data_obj.variable_name = split_line_data[1].strip(";")

                    variable_list.append(input_data_obj)

                else:
                    # 処理できないデータ
                    print("unprocessed data:", split_line_data)
                    pass

    return variable_list, 0
