from threading import Event
from four_character.domain import Report, FourCharacterAnalyzer
import four_character

from unittest.mock import patch

def test_new_report():
    report = Report()
    assert report.total_numbers == 0
    assert report.last_total_numbers == 0
    assert report.last_duplicated_numbers == 0
    assert report.digits == {}

def test_add_new_report():
    report = Report()
    report.add_digit("1")
    assert report.total_numbers == 1
    assert report.last_total_numbers == 1
    assert report.last_duplicated_numbers == 0
    assert report.digits == {'1': 1}

def test_add_duplicated_report():
    report = Report()
    report.add_digit("1")
    report.add_digit("1")
    assert report.total_numbers == 2
    assert report.last_total_numbers == 2
    assert report.last_duplicated_numbers == 1
    assert report.digits == {'1': 2}

def test_check_reset_report():
    report = Report()
    report.add_digit("1")
    report.reset()
    report.add_digit("1")
    assert report.total_numbers == 2
    assert report.last_total_numbers == 1
    assert report.last_duplicated_numbers == 0
    assert report.digits == {'1': 1}

@patch('four_character.tcp.run_client')
def test_terminate_message(_mock_run_client):
    stop = Event()
    report = Report()
    four_character_analyzer = FourCharacterAnalyzer("localhost", 1111, stop, report)
    four_character_analyzer.run("terminate")
    assert stop.is_set() == True

@patch('four_character.tcp.run_client')
def test_nine_digits(_mock_run_client):
    stop = Event()
    report = Report()
    four_character_analyzer = FourCharacterAnalyzer("localhost", 1111, stop, report)
    four_character_analyzer.run("000000001")
    assert report.total_numbers == 1
    assert report.last_total_numbers == 1
    assert report.last_duplicated_numbers == 0
    assert report.digits == {'000000001': 1}


@patch('four_character.tcp.run_client')
def test_none_nine_digits(_mock_run_client):
    stop = Event()
    report = Report()
    four_character_analyzer = FourCharacterAnalyzer("localhost", 1111, stop, report)
    four_character_analyzer.run("00000001")
    assert report.total_numbers == 0
    assert report.last_total_numbers == 0
    assert report.last_duplicated_numbers == 0
    assert report.digits == {}

@patch('four_character.tcp.run_client')
def test_none_digits(_mock_run_client):
    stop = Event()
    report = Report()
    four_character_analyzer = FourCharacterAnalyzer("localhost", 1111, stop, report)
    four_character_analyzer.run("aaa1")
    assert report.total_numbers == 0
    assert report.last_total_numbers == 0
    assert report.last_duplicated_numbers == 0
    assert report.digits == {}

