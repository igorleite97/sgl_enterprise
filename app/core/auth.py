from fastapi import Depends, HTTPException, status

def get_current_user():
    """
    Stub temporário de autenticação.
    Evoluir depois para JWT / OAuth / RBAC.
    """
    return type(
        "User",
        (),
        {
            "nome": "sistema",
            "role": "ADMIN",
        },
    )()
