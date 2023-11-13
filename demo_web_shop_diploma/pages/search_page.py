import allure
from selene import browser, have, be


class SearchPage:
    @allure.step('Search for query: {query}')
    def search_for_query(self, query):
        browser.element('.search-box #small-searchterms').send_keys(query).press_enter()

    @allure.step('No search results render')
    def no_search_results_render(self):
        browser.element('.result').should(
            have.exact_text('No products were found that matched your criteria.')
        )
        browser.all('.item-box').should(have.size(0))

    @allure.step('Search results render')
    def search_results_render(self):
        browser.element('.search-input').should(be.visible)
        browser.all('.item-box').should(have.size_greater_than(0))
