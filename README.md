# How to make documentation

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

sphinx-apidoc --implicit-namespaces -eTf -o ./output ../project/something_module/
make html
```

## RESULT

![index.html](/README.files/index.png)
