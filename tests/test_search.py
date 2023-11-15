import allure
from allure_commons.types import Severity

from demo_web_shop_diploma.data.search_queries import search_queries
from demo_web_shop_diploma.web_app import web_app


@allure.feature('Search')
@allure.title('Search returns results for a valid query')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Search')
@allure.severity(Severity.CRITICAL)
def test_search_for_valid_query():
    web_app.open()

    web_app.search_page.search_for_query(search_queries.valid_query)

    web_app.search_page.search_results_render()


@allure.feature('Search')
@allure.title('Search doesn\'t return results for a valid query')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.tag('Search')
@allure.severity(Severity.CRITICAL)
def test_search_for_invalid_query():
    web_app.open()

    web_app.search_page.search_for_query(search_queries.invalid_query)

    web_app.search_page.no_search_results_render()
