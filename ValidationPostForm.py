from flask import flash, request

import re


def validation_form():
    if len(request.form['feedback_username']) > 4:
        flash('Форма успешно отправлена', category='success')
    else:
        flash('В имени должно быть минимум 4 символа а, '
              'так же присутствовать буквы Русского алфавита Ая-аЯ', category='error')

