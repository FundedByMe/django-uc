import logging
import unittest
from mock import patch

from uc.uc import get_company_risk_report


logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.INFO)
logging.getLogger('suds.resolver').setLevel(logging.INFO)


request_body = """<ns0:Body>
   <ns1:companyReport ns1:product="4" ns1:version="2.1">
      <ns1:customer>
         <ns1:userId>ll</ns1:userId>
         <ns1:password>aa</ns1:password>
      </ns1:customer>
      <ns1:companyReportQuery xmlReply="true" htmlReply="false" reviewReply="false" lang="eng">
         <ns1:object>5561682518</ns1:object>
         <ns1:override/>
      </ns1:companyReportQuery>
   </ns1:companyReport>
</ns0:Body>"""


class UCTests(unittest.TestCase):

    @patch('__builtin__.print')
    def test_get_company_risk_report(self, print_mock):
        with patch("uc.uc.settings") as settings_mock:
            settings_mock.UC_USER_ID = "ll"
            settings_mock.UC_PASSWORD = "aa"
            get_company_risk_report("5561682518")
            print_mock.assert_called_once_with(request_body)

