from flask import render_template, flash, redirect, url_for
from . import bp
from app.models import BookList, User
from app.forms import BookReviewForm
from flask_login import current_user, login_required

@bp.route('/newreview', methods=['GET', 'POST'])
@login_required
def newreview():
    form = BookReviewForm()
    if form.validate_on_submit():
        thisTitle = form.title.data
        thisAuthor = form.author.data
        thisReview = form.review.data
        if current_user.is_authenticated:
            thisUser = current_user.user_id
            thisFullReview = BookList(user_id=thisUser, title=thisTitle, author=thisAuthor, review=thisReview)
            thisFullReview.commit()
            flash(f'{current_user.username} submitted a review for {thisTitle}', 'success')
            return redirect(url_for('mybooks.all_reviews', thisReviewer=current_user.username))
        else:
            flash('Please sign in before trying to make a book review.', 'warning')
            return redirect(url_for('mybooks.newreview'))
    return render_template('newreview.jinja', title='New Review', form=form)

@bp.route('/allReviews/<thisReviewer>')
@login_required
def all_reviews(thisReviewer):
    thisReader = User.query.filter_by(username=thisReviewer).first()
    return render_template('userreviews.jinja', title='My Reviews', reader=thisReader)

@bp.route('/wishlist')
@login_required
def wishlist():
    return render_template('wishlist.jinja', title='My Wishlist')