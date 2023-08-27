import sys
import os

from output_name import OutputName
from create_file import *
from input_file_data import *

# 使い方
def usage():

    print("")
    print("[使い方]-------------------------------")
    print("python main.py [入力ファイル名]")
    print("(例)")
    print("python main.py VirusTotalAPIData.txt")
    print("--------------------------------------")
    print("")


def validate(argv):

    argc = len(argv)

    # for debug
    # print("argc:", argc)
    #
    # i = 0
    # for data in argv:
    #     print("argv:[", i, "]:", data)
    #     i = i + 1

    # パラメータ数チェック
    if argc < 2 or argc > 3:
        print("Parameter count error.")
        usage()
        # 異常終了
        return 1, ""

    # パラメータ長チェック
    file_name = argv[1]

    if len(file_name) <= 0:
        print("Parameter length error.")
        usage()
        # 異常終了
        return 1, ""

    # ファイル存在チェック
    is_file = os.path.isfile(file_name)
    if not is_file:
        print("指定されたファイルは存在しません.FileName:", file_name)
        usage()
        # 異常終了
        return 1, ""

    # 正常終了
    return 0, file_name


def output_name_create(file_path_name):
    input_data = file_path_name.split("/")
    data_len = len(input_data)

    file_name = input_data[data_len - 1]
    directory_name = '/'.join(input_data[0: data_len - 1])

    file_name_array = file_name.split(".")

    class_name = file_name_array[0]

    output_header_file_name = directory_name + '/' + class_name + '.h'
    output_cpp_file_name = directory_name + '/' + class_name + '.cpp'

    # for debug
    # print("file_name:", file_name)
    # print("directory_name:", directory_name)
    # print("class_name:", class_name)
    # print("output_header_file_name:", output_header_file_name)
    # print("output_cpp_file_name:", output_cpp_file_name)

    output_name = OutputName()
    output_name.file_name = file_name
    output_name.directory_name = directory_name
    output_name.class_name = class_name
    output_name.output_header_file_name = output_header_file_name
    output_name.output_cpp_file_name = output_cpp_file_name

    return output_name


def main():
    argv = sys.argv

    # パラメータチェック
    ret, file_path_name = validate(argv)

    if ret == 1:
        # 異常終了
        return

    # for debug
    # print(ret)
    # print(file_name)

    # ファイルデータ読み込み処理
    variable_list, ret = input_file_data(file_path_name)

    if ret == 1:
        # 異常終了
        return

    # for debug
    # print(len(variable_list))
    # print(variable_list)
    # for variable_data in variable_list:
    #     print(variable_data.variable_type)
    #     print(variable_data.variable_name)

    # 各名称設定
    output_name_obj = output_name_create(file_path_name)

    # for debug
    # print("file_name:", output_name_obj.file_name)
    # print("directory_name:", output_name_obj.directory_name)
    # print("class_name:", output_name_obj.class_name)
    # print("output_header_file_name:", output_name_obj.output_header_file_name)
    # print("output_cpp_file_name:", output_name_obj.output_cpp_file_name)

    # ヘッダファイル出力
    ret = create_header_file(output_name_obj, variable_list)

    if ret == 1:
        # 異常終了
        return

    # cppファイル出力
    ret = create_cpp_file(output_name_obj, variable_list)

    if ret == 1:
        # 異常終了
        return


if __name__ == '__main__':
    main()

