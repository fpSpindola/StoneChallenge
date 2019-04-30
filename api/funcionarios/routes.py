from flask import Blueprint, request, jsonify, g

from api.models import Funcionario
from . import schemas
from ..helpers import current_db_session, load_from_schema
from logging import getLogger

logger = getLogger(name="funcionarios")
funcionarios = Blueprint("funcionarios", __name__, url_prefix="/v1/funcionarios")


@funcionarios.route("/search", methods=["GET"])
def search():
    session = current_db_session()
    query = session.query(Funcionario)
    logger.warning("Retornando resultados de busca de funcionarios")
    return jsonify({"results": [x.as_json() for x in list(query.all())]})


@funcionarios.route("/search/<int:func_id>", methods=["GET"])
def search_funcionario(func_id):
    session = current_db_session()
    if func_id:
        logger.warning(f"Buscando funcionário de id {func_id}")
        query = session.query(Funcionario).filter(Funcionario.id == func_id)
    else:
        query = session.query(Funcionario).all()
    logger.warning("Retornando resultados de busca de funcionarios")
    return jsonify({"results": [x.as_json() for x in list(query.all())]})


@funcionarios.route("/add", methods=["POST"])
def add_funcionario():
    session = current_db_session()
    data = load_from_schema(request, schemas.AddSchema)
    new_funcionario = Funcionario()
    for attribute_name, value in data.items():
        setattr(new_funcionario, attribute_name, value)
    session.add(new_funcionario)
    session.commit()
    logger.info("Funcionário incluido com sucesso")

    return jsonify({"msg": "Funcionario incluido com sucesso"})


@funcionarios.route("/<int:func_id>", methods=["PUT"])
def update_funcionario(func_id: int):
    session = current_db_session()
    data = request.json
    data["func_id"] = func_id
    data = load_from_schema(schema=schemas.UpdateSchema, data=data)
    found_func = g.get("func")
    for attribute_name, value in data.items():
        if attribute_name == "func_id":
            continue
        setattr(found_func, attribute_name, value)
        session.add(found_func)
        session.commit()
        logger.info("Funcionário atualizado com sucesso")
    return jsonify({"msg": "Funcionario atualizado com sucesso"})


@funcionarios.route("/<int:func_id>", methods=["DELETE"])
def delete_funcionario(func_id: int):
    session = current_db_session()
    load_from_schema(schema=schemas.DeleteSchema, data={"func_id": func_id})
    found_func = g.get("func")
    session.delete(found_func)
    session.commit()
    return jsonify({"msg": "Funcionario excluido com sucesso"})
