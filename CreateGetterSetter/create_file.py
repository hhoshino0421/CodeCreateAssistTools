

def create_header_file(output_name_obj, variable_list):

    with open(output_name_obj.output_header_file_name, mode='w') as file_obj:

        # 定義部出力
        file_obj.write("class " + output_name_obj.class_name + " {" + "\n")
        file_obj.write("\n")

        # 関数部定義出力
        file_obj.write("public:\n")

        file_obj.write("    // getter関数 \n")

        for line_data in variable_list:
            line_out_data = "    " + line_data.variable_type + "  get" + line_data.variable_name.capitalize() + "();"
            file_obj.write(line_out_data)
            file_obj.write("\n")

        file_obj.write("\n")

        file_obj.write("    // setter関数 \n")

        for line_data in variable_list:
            line_out_data = "    void set" + line_data.variable_name.capitalize() \
                            + "(" + line_data.variable_type + " in" + line_data.variable_name.capitalize() + ");"
            file_obj.write(line_out_data)
            file_obj.write("\n")

        file_obj.write("\n")

        # 変数部出力
        file_obj.write("private: \n")
        for line_data in variable_list:

            line_out_data = "    " + line_data.variable_type + "  " + line_data.variable_name + ";"
            file_obj.write(line_out_data)
            file_obj.write("\n")

        file_obj.write("}\n")

    # 正常終了
    return 0


def create_cpp_file(output_name_obj, variable_list):

    with open(output_name_obj.output_cpp_file_name, mode='w') as file_obj:

        # getter関数出力
        for variable_data in variable_list:

            line_data = variable_data.variable_type + " " + output_name_obj.class_name \
                        + "::" + " get" + variable_data.variable_name.capitalize() + "() {\n"
            file_obj.write(line_data)

            line_data = "    return " + variable_data.variable_name + ";\n"
            file_obj.write(line_data)

            line_data = "}\n"
            file_obj.write(line_data)

            file_obj.write("\n")

        # setter関数出力
        for variable_data in variable_list:

            line_data = "void " + output_name_obj.class_name \
                        + "::" + " set" + variable_data.variable_name.capitalize() \
                        + "(" + variable_data.variable_type \
                        + " in" + variable_data.variable_name.capitalize() + ") {\n"
            file_obj.write(line_data)

            line_data = "    " + variable_data.variable_name \
                        + " = std::move(in" + variable_data.variable_name.capitalize() + ");\n"
            file_obj.write(line_data)

            line_data = "}\n"
            file_obj.write(line_data)

            file_obj.write("\n")

    # 正常終了
    return 0
