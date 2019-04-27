class Messages:

    BOT_ADDED_SUCCESSFULLY = 1
    MISSING_BOT = 2
    INVALID_BOT_TYPE = 3
    BOT_UPDATED_SUCCESSFULLY = 4
    BOT_DELETED_SUCCESSFULLY = 5
    MISSING_TEAM = 6
    MISSING_ROLE = 7
    DUPLICATED_EMAIL = 8
    MISSING_USER = 9
    USER_DELETED = 10
    USER_ADDED = 11
    USER_UPDATED = 12
    TEAM_ADDED = 13
    TEAM_UPDATED = 14
    TEAM_DELETED = 15
    CANNOT_DELETE_TEAM = 16
    MEMBER_ADDED = 17
    MEMBER_REMOVED = 18
    MEMBER_UPDATED = 19
    DUPLICATED_TEAM_NAME = 20
    DUPLICATED_PROJECT_NAME = 21
    PROJECT_ADDED = 22
    PROJECT_UPDATED = 23
    PROJECT_DELETED = 24
    MISSING_PROJECT = 25
    QUERY_ADDED = 26
    QUERY_NON_UNIQUE_NAME = 27
    QUERY_DELETED = 28
    INVALID_SEARCH = 29
    MISSING_QUERY = 30
    FAILED_LOGIN = 31
    LOGIN_SUCCESSFUL = 32


class Languages:

    PT_BR = {
        Messages.BOT_ADDED_SUCCESSFULLY: "BOT adicionado com sucesso",
        Messages.MISSING_BOT: "BOT não encontrado",
        Messages.INVALID_BOT_TYPE: "Tipo de BOT inválido",
        Messages.BOT_UPDATED_SUCCESSFULLY: "BOT atualizado com sucesso",
        Messages.BOT_DELETED_SUCCESSFULLY: "BOT deletado com sucesso",
        Messages.MISSING_TEAM: "Este time não existe",
        Messages.MISSING_ROLE: "Esta permissão não existe",
        Messages.DUPLICATED_EMAIL: "Já existe um usuário com este e-mail",
        Messages.MISSING_USER: "Esse usuário não existe",
        Messages.USER_DELETED: "Usuário deletado com sucesso",
        Messages.USER_ADDED: "Usuário criado com sucesso",
        Messages.USER_UPDATED: "Usuário atualizado com sucesso",
        Messages.TEAM_ADDED: "Time adicionado com sucesso",
        Messages.TEAM_UPDATED: "Time atualizado com sucesso",
        Messages.TEAM_DELETED: "Time excluído com sucesso",
        Messages.CANNOT_DELETE_TEAM: "Você não pode excluir um time com membros",
        Messages.MEMBER_ADDED: "Membro adicionado com sucesso",
        Messages.MEMBER_REMOVED: "Membro removido com sucesso",
        Messages.MEMBER_UPDATED: "Membro atualizado com sucesso",
        Messages.DUPLICATED_TEAM_NAME: "Já existe um time com este nome",
        Messages.DUPLICATED_PROJECT_NAME: "Já existe um projeto com este nome",
        Messages.PROJECT_ADDED: "Projeto adicionado com sucesso",
        Messages.PROJECT_UPDATED: "Projeto atualizado",
        Messages.PROJECT_DELETED: "Projeto excluído com sucesso",
        Messages.MISSING_PROJECT: "Este projeto não existe",
        Messages.QUERY_ADDED: lambda x: f"Sua query está guardada no projeto {x}",
        Messages.QUERY_DELETED: "Query deletada com sucesso",
        Messages.QUERY_NON_UNIQUE_NAME: "Já existe uma busca com este nome",
        Messages.INVALID_SEARCH: "Verifique os parâmetros de sua busca",
        Messages.MISSING_QUERY: "Esta query não existe",
        Messages.FAILED_LOGIN: "Usuário não existe ou senha incorreta",
        Messages.LOGIN_SUCCESSFUL: lambda x: f"Seja bem-vindo {x}",
    }
