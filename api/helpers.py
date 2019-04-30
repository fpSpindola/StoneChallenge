from typing import List, Dict, Union, Callable
from flask import Request, g
from sqlalchemy.orm import Session
from api.exceptions import InvalidInput
from .configs import current_config


def load_from_schema(
    request: Request = None, schema=None, data: dict = None, context: dict = None) -> dict:
    instance_schema = schema()
    if context:
        instance_schema.context.update(context)
    data, errors = instance_schema.load((request.json if request else data) or {})
    if not errors:
        return data
    raise InvalidInput(errors)


def current_db_session() -> Session:
    key = "db_session"
    if not g.get(key):
        db_session = current_config().create_session()
        setattr(g, key, db_session)
    return g.get(key)


def current_language() -> Dict[int, Union[str, Callable]]:
    return Languages.PT_BR


def parse_mapping(b: dict, current_field: str = ""):
    for k, v in b.items():
        current_key_name = current_field + "." + k if current_field else k
        if "properties" in v:
            for name in parse_mapping(v["properties"], current_key_name):
                yield name
        else:
            yield current_key_name


def parse_mapping_only_dates(b: dict, current_field: str = ""):
    for k, v in b.items():
        current_key_name = current_field + "." + k if current_field else k
        if "properties" in v:
            for name in parse_mapping_only_dates(v["properties"], current_key_name):
                yield name
        if "type" in v and v["type"] in ("date", "keyword", "long"):
            yield current_key_name


def get_es_fields() -> List[str]:
    config = current_config()
    response = config.es.indices.get_mapping(index=config.LOGS_SEARCH_PATTERN)
    for index_name, values in response.items():
        # Since all indexes do have the same mapping we get the first one.
        return list(parse_mapping(values["mappings"]["logs"]["properties"]))


def get_es_sort_fields() -> List[str]:
    config = current_config()
    response = config.es.indices.get_mapping(index=config.LOGS_SEARCH_PATTERN)
    for index_name, values in response.items():
        # Since all indexes do have the same mapping we get the first one.
        return list(parse_mapping_only_dates(values["mappings"]["logs"]["properties"]))


def wildcard_pg(query: str) -> str:
    query = query.replace("*", "%")
    query = query.replace("?", "_")
    if not query.endswith("*"):
        query = query + "%"
    if not query.startswith("*"):
        query = "%" + query
    return query


def merge(obj, values, blacklist: set = None):
    for key, value in values.items():
        if not blacklist or key not in blacklist:
            setattr(obj, key, value)
    return obj
