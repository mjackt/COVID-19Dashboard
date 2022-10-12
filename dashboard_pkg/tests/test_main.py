from main import update_covid_data
from main import news_updater
from main import update_remover
from main import news_remover
from main import update_scheduler


def test_functions_exist():
    update_covid_data({'test':'yeh'})
    news_updater({'test':'yeh'})
    update_remover({'test':'yeh'})
    news_remover('title')
    dictionary={'covidData':0,
                'news':0,
                'repeat':0}
    update_scheduler(dictionary)
    

