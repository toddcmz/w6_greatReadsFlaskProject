from flask import render_template, flash, redirect, url_for
from . import bp
from app.models import BookList
from app.forms import BookReviewForm
from flask_login import current_user

@bp.route('/reviews', methods=['GET', 'POST'])
def reviews():
    form = BookReviewForm()
    if form.validate_on_submit():
        thisTitle = form.title.data
        thisAuthor = form.author.data
        thisReview = form.review.data
        thisFullReview = BookList(user_id=current_user.user_id, title=thisTitle, author=thisAuthor, review=thisReview)
        thisFullReview.commit()
        flash(f'{current_user.username} submitted a review for {thisTitle}', 'success')
        return redirect(url_for('main.home'))
    else:
        flash('Invalid book review, try again.', 'warning')
    return render_template('reviews.jinja', title='My Reviews', form=form)

@bp.route('/wishlist')
def wishlist():
    return render_template('wishlist.jinja', title='My Wishlist')