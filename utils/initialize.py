import datetime
from api.models import Funcionario, Base
from api.factory import create_app


init = [
    {"model": Funcionario,
     "items": [
         {
             "id": 1,
             "nome": "Filipe Pires Spindola",
             "idade": "28",
             "cargo": "Software Developer"}]}
]


def create_funcionario_info(config, flush_database: bool):
    session = config.create_session()
    if flush_database:
        Base.metadata.drop_all(config.engine)
        Base.metadata.create_all(config.engine)
    session.commit()

    for config in init:
        model = config["model"]
        print(f"Creating objects for {model}")
        for values in config["items"]:
            new_obj = model()
            for key, value in values.items():
                setattr(new_obj, key, value)
            session.add(new_obj)
        session.commit()

    print("Initialized successfully.")


if __name__ == "__main__":
    app, current_config = create_app()
    create_funcionario_info(current_config, flush_database=True)
