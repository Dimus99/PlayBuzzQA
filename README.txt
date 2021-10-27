После прохождения каждого теста скриншот результата сохраняется в папку screenshots

Quick start linux

python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
pytest

for html output use
pytest --html=result.html

Пару слов:
можно добавить конечно ещё больше тестов,
чтобы покрывать больше случаев, например покрыть границу успеха/неуспеха,
так же можно выделить сущность сайта в отдельный класс.
Я решил что лучше не загромождать тестовое задание.
