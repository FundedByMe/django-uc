from __future__ import print_function
from django.conf import settings

from suds.client import Client
from suds.plugin import MessagePlugin


def get_client(product_code):
    url = "https://www.uc.se/UCSoapWeb/services/ucOrders2"
    client = Client(url + "?wsdl", plugins=[VersionPlugin(product_code)])
    client.sd[0].service.setlocation(url)
    return client


class VersionPlugin(MessagePlugin):
    def __init__(self, product_code):
        self.product_code = product_code

    def marshalled(self, context):
        body = context.envelope.getChild('Body')
        company_report = body[0]
        company_report.set('ns1:product', self.product_code)
        company_report.set('ns1:version', '2.1')
        print(str(context.envelope.getChild('Body')))


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


def get_company_report(client, organization_number):
    customer = get_customer(client)
    report_query = get_report_query(client, organization_number)
    return client.service.companyReport(
        customer=customer, companyReportQuery=report_query)


def get_company_full_report(organization_number):
    return get_company_report(get_client("410"), organization_number)


def get_company_risk_report(organization_number):
    return get_company_report(get_client("4"), organization_number)
