from covid_data_handler import parse_csv_data
from covid_data_handler import process_covid_csv_data
from covid_data_handler import covid_API_request
from covid_data_handler import schedule_time_calculator
from covid_data_handler import schedule_covid_updates

def test_parse_csv_data():
    data = parse_csv_data('nation_2021-10-28.csv')
    assert isinstance(data[0],str)
    assert data[1]=="E92000001,England,nation,2021-10-28,,7019,"
    assert len(data) == 639

def test_process_covid_csv_data():
    last7days_cases , current_hospital_cases , total_deaths = \
        process_covid_csv_data ( parse_csv_data (
            'nation_2021-10-28.csv' ) )
    assert last7days_cases == 240_299
    assert current_hospital_cases == 7_019
    assert total_deaths == 141_544

def test_covid_API_request():
    data = covid_API_request()
    assert isinstance(data, dict)

    covid_API_request("Bath and North East Somerset","ltla")
    covid_API_request("Wales","nation")
    covid_API_request("Somerset","utla")

def test_schedule_covid_updates():
    schedule_covid_updates(update_interval=10, update_name='update test')

def test_schedule_time_calculator():
    interval=schedule_time_calculator("11:11")
    assert isinstance(interval,int)
    assert interval>=0
