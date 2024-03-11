import pytest

from app.io.input import read_from_file

def test_read_from_file_reads_empty_file():
    content = read_from_file('mocks/empty_file.txt')
    assert content is not None

def test_read_from_file_reads_file():
    expected_content = 'comma,separated,values'
    content = read_from_file('mocks/mock_file.csv')
    assert content, expected_content


def test_read_from_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_from_file('non_existent_file.csv')