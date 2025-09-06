#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
#from functions.write_file import write_file


def main():
    working_dir = "calculator"
    print(get_files_info({'directory': '.'}))



main()