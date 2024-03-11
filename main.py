from app.io.input import grab_input, read_from_file, read_from_csv_file_with_pandas
from app.io.output import print_to_console, write_to_file


def main():
    filename = grab_input()

    file_content = read_from_file(filename)
    print_to_console(file_content)
    write_to_file('data/output.txt', file_content + '\n')

    df_content = read_from_csv_file_with_pandas(filename)
    df_content_str = df_content.to_string()
    print_to_console(df_content_str)
    write_to_file('data/output.txt', df_content_str + '\n')

if __name__ == '__main__':
    main()