from django.conf import settings

from suds.client import Client


def get_client():
    url = "https://www.uc.se/UCSoapWeb/services/ucOrders2"
    client = Client(url + "?wsdl")
    client.sd[0].service.setlocation(url)
    return client


def get_customer(client):
    customer = client.factory.create("ns0:customer")
    customer.userId = settings.UC_USER_ID
    customer.password = settings.UC_PASSWORD
    return customer


def get_report_query(client, organization_number):
    reportQuery = client.factory.create("ns0:reportQuery")
    reportQuery.object = organization_number
    reportQuery._xmlReply = "true"
    reportQuery._htmlReply = "false"
    reportQuery._reviewReply = "false"
    reportQuery._lang = "eng"
    return reportQuery


def get_company_report(organization_number):
    client = get_client()
    customer = get_customer(client)
    report_query = get_report_query(client, organization_number)
    return client.service.companyReport(
        customer=customer, companyReportQuery=report_query)


def get_credit_rating(organization_number):
    r = get_company_report(organization_number)
    return r.ucReport[0].xmlReply.reports[0].report[0].group[3].term[0].value
