import pytest

from app.io.input import read_from_file, read_from_csv_file_with_pandas


def test_read_from_file_reads_empty_file():
    content = read_from_file('mocks/empty_file.txt')
    assert content is ''


def test_read_from_file_reads_file():
    expected_content = 'column_1,column_2,column_3\ncomma,separated,values'
    content = read_from_file('mocks/mock_file.csv')
    assert content == expected_content


def test_read_from_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_from_file('non_existent_file.csv')


def test_read_from_csv_file_with_pandas_exists():
    content = read_from_csv_file_with_pandas("mocks/mock_file.csv")
    assert not content.empty


def test_read_from_csv_file_with_pandas_columns():
    expected_columns = ['column_1', 'column_2', 'column_3']
    content = read_from_csv_file_with_pandas("mocks/mock_file.csv")
    assert list(content.columns) == expected_columns


def test_read_from_csv_file_with_pandas_not_found():
    with pytest.raises(FileNotFoundError):
        read_from_csv_file_with_pandas("non_existent_file.csv")