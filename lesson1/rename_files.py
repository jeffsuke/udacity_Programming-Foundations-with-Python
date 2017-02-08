import os
def rename_files():
    file_list = os.listdir("/Users/yusuke/ghq/src/github.com/jeffsuke/python_practice/prank")
    print(file_list)
    # print(os.getcwd())

    os.chdir("/Users/yusuke/ghq/src/github.com/jeffsuke/python_practice/prank")
    for file_name in file_list:
        new_file_name = file_name.translate(None, "0123456789")
        print("Old name" + file_name)
        print("New name" + new_file_name)
        os.rename(file_name, new_file_name)

rename_files()
