# How to make documentation

Почему не генерируется документация для подпакета, например, для `functions.sub_bst`, когда как для корневогофайла `bst.py` документация генерируется успешно?

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

Почему не генерируется документация для подпакета, например, для `functions.sub_bst`, когда как для корневогофайла `bst.py` документация генерируется успешно?

## OFF TOP

```shell
sphinx-build -b html ./ ./_build/html/
```
