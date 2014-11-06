[![Build Status](https://travis-ci.org/FundedByMe/django-uc.svg)](https://travis-ci.org/FundedByMe/django-uc)


django-uc
=========

Django Intergration with UC's API

https://www.uc.se/


Installation
============

    pip install django-uc

In your settings file you need to specify the `UC_USER_ID` and `UC_PASSWORD`
that you recieved when you set up your account with UC.

Usage
=====

You can use it with the built-in database-backing.

You can use the db-backing via the models. On create, the report will be fetched
automatically and the rating and the date will be saved to the model.

    from uc.models import UCRiskReport
    UCRiskReport.create_rating_report("556168-2518")


You can also fetch the reports from the API directly without using the models.

    from uc.uc import get_company_full_report, get_company_risk_report
    full_report = get_company_report("556168-2518")
    risk_report = get_company_risk_report("556168-2518")
