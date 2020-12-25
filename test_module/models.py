from django.db import models


# Create your models here.
class Tests(models.Model): # - тесты
	name = models.CharField(max_length=200, verbose_name='Название теста')
	description = models.CharField(max_length=500, verbose_name='Описание')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тест'
		verbose_name_plural = 'Тесты'


class Questions(models.Model): # - вопросы
	type_choices = [
		('Выбор', 'Выборочный вариант'),
		('Ввод', 'Вводимый вариант'),
	]
	test_id = models.ForeignKey(
		Tests,
		on_delete=models.CASCADE,
		verbose_name='Название теста'
	)
	question = models.CharField(max_length=300, verbose_name='Вопрос')
	type_of_question = models.CharField(
		max_length=5,
		choices=type_choices,
		default='Выбор',
		verbose_name='Укажите тип ответа'
	)

	def __str__(self):
		return self.question

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'


class Answers(models.Model): # - варианты
	answer_choices = [
		('Да', 'Да'),
		('Нет', 'Нет'),
	]
	question_id = models.ForeignKey(
		Questions,
		on_delete=models.CASCADE,
		verbose_name='Вопрос'
	)
	answer = models.CharField(max_length=30, verbose_name='Ответы')
	is_correct = models.CharField(
		max_length=3,
		choices=answer_choices,
		default='Нет',
		verbose_name='Верный ответ?',
	)

	def __str__(self):
		return self.answer

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'


# class Correct_answers(models.Model): # - ответы
# 	id


class Results(models.Model): # - результаты
	user = models.CharField(max_length=20, verbose_name='Имя пользователя')
	test_id = models.ForeignKey(
		Tests,
		on_delete=models.PROTECT,
		verbose_name='Название теста'
	)
	number_of_correct_answers = models.IntegerField(verbose_name='Количество правильных ответов')

	def __str__(self):
		return f'{self.user}, {self.test_id}, {self.number_of_correct_answers}'

	class Meta:
		# ordering = ("user", "test_id", "number_of_correct_answers")
		verbose_name = 'Результат'
		verbose_name_plural = 'Результаты'