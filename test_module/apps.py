from django.apps import AppConfig


class TestModuleConfig(AppConfig):
    name = 'test_module'


answer = ['их работа', 'работа']
r_answer = ['их рабwта', 'работа']

if answer == r_answer:
    print(True)
else:
    print(False)


answer = ['их работа']
r_answer = ['их рабwта']

for i in range(len(answer)):
    print(answer[i])