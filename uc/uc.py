from django.conf import settings

from suds.client import Client


def get_client():
    return Client("https://www.uc.se/UCSoapWeb/services/ucOrders2?wsdl")


def get_customer(client):
    customer = client.factory.create("ns0:customer")
    customer.userId = settings.UC_USER_ID
    customer.password = settings.UC_PASSWORD
    return customer


def get_report_query(client, organization_number):
    reportQuery = client.factory.create("ns0:reportQuery")
    #objectRef = client.factory.create("ns0:objectRef")
    objectRef = organization_number
    reportQuery.object = objectRef


def get_company_report(organization_number):
    client = get_client()
    customer = get_customer(client)
    report_query = get_report_query(client, organization_number)
    return client.service.companyReport(customer, report_query)
