from flask import render_template, redirect

from dna import dna_blueprint
from dna.forms import DnaForm
from main import db

from model import DNA

import time


@dna_blueprint.route("/", methods=["GET"])
def list_dnas():
    return render_template(
        template_name_or_list="dna/list.html",
        dnas=DNA.query.all())


@dna_blueprint.route("/new", methods=["GET", "POST"])
def new_dna():
    form = DnaForm()

    if form.validate_on_submit():
        dna = DNA(id=int(form.id.data), sequencia=str(form.sequencia.data))
        db.session.add(dna)
        db.session.commit()
        time.sleep(5)
        return redirect('/index')

    return render_template("dna/new.html", form=form)
