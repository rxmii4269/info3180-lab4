from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed



class UploadForm(FlaskForm):
    uploadfield = FileField('Upload Image Here',validators=[
        FileRequired(),FileAllowed(['jpg','jpeg','png'],'Images only!')
    ])
