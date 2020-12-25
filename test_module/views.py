from django.shortcuts import render, redirect
from test_module.models import Tests, Questions, Answers, Results
from test_module.forms import ResultFrom


# Create your views here.
def show_all_tests(request):
	list_of_tests = Tests.objects.all()
	return render(request, 'show_tests.html', {"list_of_tests": list_of_tests})


# Выводим тест с вопросами
def passing_test(request, test_name):
	if request.method == 'POST':
		print('request.POST', request.POST)

	test_id = Tests.objects.get(name=test_name)
	question = Questions.objects.filter(test_id=test_id)

	test = []
	for q in question:
		question_dict = {}
		answer = Answers.objects.filter(question_id=q)
		question_dict.update({'question': q, 'answer': answer})
		test.append(question_dict)
	return render(request, 'pass_test.html', {'test': test})


# Проверям ответы
def check_answer(request, test_name):
	if request.method == 'POST':
		print('request.POST', request.POST)
		test_id = Tests.objects.get(name=test_name)
		question = Questions.objects.filter(test_id=test_id)

		number = 0
		user_name = request.POST.get('user_name')
		for q in question:
			answer = request.POST.getlist(str(q.id))
			right_answers = Answers.objects.filter(question_id=q, is_correct='Да').order_by(
				'answer')  # values('answer')
			r_answer = []
			for r in right_answers:
				r_answer.append(r.answer)

			if len(answer) == len(r_answer):
				if len(answer) == 1 and answer == r_answer:
					number += 1
				else:
					check = 0
					for i in range(len(answer)):
						if answer[i] == r_answer[i]:
							check += 1
					if check == len(answer):
						number += 1
			else:
				print('Ответ не верный')

		result_form = ResultFrom(
			{'user': user_name,
			 'test_id': test_id.id,
			 'number_of_correct_answers': number}
		)

		if result_form.is_valid():
			result_form.save()

		return render(request, 'results.html', {'user': user_name,
		                                        'test_name': test_id,
		                                        'number': number}
		              )
	return redirect(show_all_tests)