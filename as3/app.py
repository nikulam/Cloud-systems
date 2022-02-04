from flask import Flask
from flask_mongoengine import MongoEngine
from flask import jsonify
from flask import request

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db':'db',
    'host':'localhost',
    'port':27017
}

db = MongoEngine(app)

class Album(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField()

class Photo(db.Document):
    name = db.StringField(required=True)
    tags = db.ListField()
    location = db.StringField()
    #image_file = db.FileField(required=True)
    albums = db.ReferenceField(Album)


@app.route('/albums')
def get_albums():
    albums = Album.objects()
    return jsonify(albums), 200

@app.route('/listPhotos')
def get_photos():
    photos = Photo.objects()
    return jsonify(photos), 200

@app.route('/listPhoto/<id>')
def got_a_photo(id: str):
    photo = Photo.objects(id=id).first_or_404()
    return jsonify(photo), 200

@app.route('/listPhoto/', methods=["POST"])
def add_photo():
    body = request.get_json()
    photo = Photo(**body).save()
    return jsonify('Photo successfully created', 'id: ' + str(photo.id)), 201

@app.route('/listPhoto/<id>', methods=['PUT'])
def update_photo(id):
    body = request.get_json()
    photo = Photo.objects(id=id).get_or_404()
    photo.update(**body)
    return jsonify('Photo successfully updated', 'id: ' + str(photo.id)), 200

@app.route('/listPhoto/<id>', methods=['DELETE'])
def delete_movie(id):
    photo = Photo.objects(id=id).get_or_404()
    photo.delete()
    return jsonify('Photo successfully deleted', 'id: ' + str(photo.id)), 200

if __name__ == "__main__":
    app.run(debug=True)