[![Build Status](https://travis-ci.org/FundedByMe/django-uc.svg)](https://travis-ci.org/FundedByMe/django-uc)


django-uc
=========

Django Intergration with UC's API

https://www.uc.se/


Installation
============

    pip install django-uc

In your settings file you need to specify the `settings.UC_USER_ID` and `settings.UC_PASSWORD`.

Usage
=====

    from uc.uc import get_company_report
    get_company_report("556168-2518")
