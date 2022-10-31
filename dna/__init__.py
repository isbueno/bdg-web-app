from flask import Blueprint

dna_blueprint = Blueprint(
    "dna_blueprint", __name__, url_prefix="/dna")


from .routes import *
