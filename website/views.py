from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import current_user, login_required
from website import db
from sqlalchemy import update

views = Blueprint('views', __name__)


@views.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('views.berichtshefter'))
    else:
        return redirect(url_for('auth.login'))


@views.route('/berichtshefter', methods=['GET', 'POST'])
@login_required
def berichtshefter():
    if request.method == 'POST':
        id = int(request.form.get('id'))
        type = request.form.get('type')
        berichtshefter = None
        for bh in current_user.berichtshefter:
            if bh.id == id:
                berichtshefter = bh
                break

        if type == '0':
            if berichtshefter:
                if berichtshefter.erstellt==False:
                    berichtshefter.erstellt = True
                else:
                    berichtshefter.erstellt = False
        elif type == '1':
            if berichtshefter:
                if berichtshefter.hochgeladen == False:
                    berichtshefter.hochgeladen = True
                else:
                    berichtshefter.hochgeladen = False
        db.session.commit()
        return redirect(url_for('views.berichtshefter'))

    scroll_position = request.args.get('scroll_position')
    sorted_berichtshefter = sorted(current_user.berichtshefter, key=lambda bh: bh.id)
    return render_template('berichtshefter.html', user=current_user, berichtshefter=sorted_berichtshefter, scroll_position=scroll_position)

# @views.route('/update-berichtshefter/<int:id>/<int:type>', methods=["POST"])
# @login_required
# def update_berichtshefter(id, type):
#     for berichtshefter in db.session.query(current_user.berichtshefter).filter_by(id=id):
#         if type==0:
#             berichtshefter.erstellt=True
#         elif type==1:
#             berichtshefter.hochgeladen=True
#     db.session.commit()
#     for berichtshefter in db.session.query(current_user.berichtshefter).filter_by(id=id):
#         print(berichtshefter)
#     return render_template('berichtshefter.html', user=current_user)
