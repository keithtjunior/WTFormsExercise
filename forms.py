from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, BooleanField, TextAreaField, validators

class AdoptionForm(FlaskForm):
    """Pet wtform data and validation"""
    name         = StringField("Pet's Name", [validators.Length(min=1, max=70), validators.DataRequired()])
    species      = StringField('Species', [
        validators.Length(min=3, max=70), 
        validators.AnyOf(['cat', 'dog', 'porcupine'], message='Species must be either "cat", "dog", or "porcupine"'),
        validators.DataRequired()
    ])
    age          = DecimalField('Age in Years (Optional)', [validators.NumberRange(min=0, max=30), validators.Optional()])
    notes        = TextAreaField('Additional Notes (Optional)', [validators.Length(max=2200), validators.Optional()])
    available    = BooleanField('Pet Available', default='checked')
    photo_url    = StringField('Photo URL (Optional)', [ 
        validators.Length(max=2048), 
        validators.URL(message='Please enter a valid URL'),
        validators.Optional()
    ])


