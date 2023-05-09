from flask import render_template
from . import bp

@bp.route('/reviews')
def reviews():
    return render_template('reviews.jinja', title='My Reviews')

@bp.route('/wishlist')
def wishlist():
    return render_template('wishlist.jinja', title='My Wishlist')