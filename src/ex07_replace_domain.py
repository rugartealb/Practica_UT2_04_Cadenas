"""
Ejercicio 7: dado un correo electrónico, cambiar su dominio por "ceu.es".

La función:

Mantiene la parte local (antes de la arroba).

Sustituye el dominio por el indicado (por defecto "ceu.es").

Si el correo no tiene exactamente una arroba, lanza ValueError.
"""

def replace_domain(email: str, new_domain: str = "ceu.es") -> str:
    """Devuelve el correo con el dominio sustituido por new_domain."""
    # TODO: separa con split("@"), valida y construye la nueva dirección
    raise NotImplementedError("Implementa replace_domain(email, new_domain)")