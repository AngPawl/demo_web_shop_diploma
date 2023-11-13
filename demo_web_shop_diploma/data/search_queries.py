import dataclasses


@dataclasses.dataclass
class SearchQueries:
    valid_query: str
    invalid_query: str
    for_order_placing: str


search_queries = SearchQueries(
    valid_query='computer',
    invalid_query='abracadabra',
    for_order_placing='laptop',
)
