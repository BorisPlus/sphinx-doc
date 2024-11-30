# How to make documentation

Почему не генерируется документация для подпакета, например, для `functions.sub_bst`, когда как для корневогофайла `bst.py` документация генерируется успешно? ( см ./docs/_build/html/index.html)

## About

* https://habr.com/ru/companies/netologyru/articles/815563/
* https://habr.com/ru/articles/750968/
* https://habr.com/ru/companies/otus/articles/799687/
* https://www.pythian.com/blog/technical-track/generating-documentation-for-your-python-code-using-cloud-build-and-sphinx

## DOCUMENTATION

```shell
mkdir docs
cd docs

pip3 install sphinx
sphinx-quickstart

sphinx-apidoc -f -o ./ ../project/something_module/
make html
```

Почему не генерируется документация для подпакета, например, для `functions.sub_bst`, когда как для корневого файла `bst.py` документация генерируется успешно?

2024/11/30: нужен `__init__.py` в документируемой директории

## P.S.

```shell
sphinx-build -b html ./ ./_build/html/
```

## Вручную

Можно сделать файл с отсылкой на модуль и прикрепить к проекту для автогенерации документации по докстрингам из файлов модуля.

![index.html](/README.files/index.png)
