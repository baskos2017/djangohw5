from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Дуже погпно'),
        (2, '2 - Погано'),
        (3, '3 - Пройде'),
        (4, '4 - Добре'),
        (5, '5 - Дуже добре'),
    ]

    user_email = models.EmailField('User Email')
    description = models.TextField('Опис')
    rating = models.IntegerField('Рейтинг', choices=RATING_CHOICES)
    is_positive = models.BooleanField('Positive Review')
    phone_number = models.CharField('Номер телефону', max_length=15)
    image = models.ImageField('Image', upload_to='reviews/', blank=True, null=True)

    def __str__(self):
        return f'Review by {self.user_email}'
