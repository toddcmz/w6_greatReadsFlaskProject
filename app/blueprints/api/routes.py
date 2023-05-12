from flask import request, jsonify
from . import bp
from app.models import BookList, User

# get all reviews
@bp.get('/allreviews')
def api_allreviews():
    result = []
    # add to this list all reviews in the database
    theseReviews = BookList.query.all()
    for eachReview in theseReviews:
        result.append({'id' : eachReview.book_id,
                       'title' : eachReview.title,
                       'author' : eachReview.author,
                       'review' : eachReview.review})
    return jsonify(result), 200

# get reviews from a single user
@bp.get('allreviews/<thisReviewer>')
def api_allreviews_reader(thisReviewer):
    thisReader = User.query.filter_by(username=thisReviewer).first()
    if thisReader:
        result = []
        for eachReview in thisReader.book_list:
            result.append({'id' : eachReview.book_id,
                           'title' : eachReview.title,
                           'author' : eachReview.author,
                           'review' : eachReview.review})
        return jsonify(result), 200
    return jsonify([{'message': "No account with that username"}]), 404

# verify a user
@bp.post('/verifyreader')
def api_verify_reader():
    content = request.json
    thisUsername = content['username']
    thisPassword = content['password']
    thisReader = User.query.filter_by(username=thisUsername).first()
    if thisReader and thisReader.check_password(thisPassword):
        return jsonify([{'user id': thisReader.user_id}])
    return jsonify([{'message':'Invalid credentials supplied'}]), 404

# register a user
@bp.post('/newreader')
def api_new_reader():
    content = request.json
    thisFirstName = content['first_name']
    thisLastName = content['last_name']
    thisFavBook = content['fav_book']
    thisUsername = content['username'] # written like this assuming we're keying into a passed in json obj
    thisEmail = content['email'] # again, this is all predicated on user posting a json file here.
    thisPassword = content['password']
    thisUserCheck = User.query.filter_by(username=thisUsername).first()
    if thisUserCheck:
        return jsonify([{'message':'Username taken, try again.'}])
    thisEmailCheck = User.query.filter_by(email=thisEmail).first()
    if thisEmailCheck:
        return jsonify([{'message':'Email taken, try again.'}])
    thisNewUser = User(first_name = thisFirstName, last_name=thisLastName, fav_book=thisFavBook, email = thisEmail, username=thisUsername)
    thisNewUser.password = thisNewUser.hash_password(thisPassword)
    thisNewUser.commit()
    print(thisNewUser)
    return jsonify([{'message': f"{thisNewUser.username} registered"}])
