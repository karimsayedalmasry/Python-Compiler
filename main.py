import basic
print("Program Started")


def check_function(file_content_lst, types_list):

    if str.lower(file_content_lst[0]) in types_list:
        temp_string = file_content_lst[1][0]
        if not str.isdigit(temp_string):
            if file_content_lst[2] == '(':
                if file_content_lst[3] == 'void':
                    if file_content_lst[4] == ")" and file_content_lst[5] == "{":
                        print("No error in function definition")
                        check_function_body(file_content_lst, None)

                    else:
                        print("Syntax Error: function ",
                              file_content_lst[1], "'s definition is incorrect")
                elif file_content_lst[3] in types_list and file_content_lst[3] != "void":
                    start = 0
                    for i in file_content_lst:
                        if i == ")":
                            end = start
                            break
                        else:
                            start = start + 1
                    i = 3
                    for token in range(3, end, 2):
                        if (file_content_lst[token] in types_list) and (file_content_lst[token] != "void") and (not str.isdigit(file_content_lst[token + 1][0]) and file_content_lst[token + 1] not in types_list) and (file_content_lst[token + 1] != ")"):
                            pass
                        else:
                            print("Syntax Error: Function ",
                                  file_content_lst[1], " invalid paramter form")
                            break
                    print("No error in function definition")
                    check_function_body(file_content_lst, types_list)
                elif file_content_lst[3] not in types_list:
                    print("Syntax Error: Invalid function ",
                          file_content_lst[1], "parameters")
            else:
                print('Syntax Error: Function ',
                      file_content_lst[1], 'is missing a (')
        else:
            print("Syntax Error: Function name cannot start with a letter",
                  file_content_lst[1])

    else:
        print('Syntax Error: function',
              'retrun type invalid')


def check_function_body(file_content_lst, types_list):
    function_body = []
    start = 0
    for token in file_content_lst:  # target the start of the body
        if token != "{":
            start = start + 1
        else:
            start = start + 1
            break
    for i in range(start, len(file_content_lst)-1):
        function_body.append(file_content_lst[i])
        function_body.append(" ")
    function_body_string = ""
    for i in function_body:
        function_body_string = function_body_string + i

    result, error = basic.run('<stdin>', function_body_string)

    if error:
        print(error.as_string())
    else:
        print(result)


file_handler = open("data.txt", "r")
file_content_str = file_handler.read()
file_content_lst = file_content_str.split()
types_list = ["void", 'int', 'float', 'double']
check_function(file_content_lst, types_list)

print("Program Terminated")
