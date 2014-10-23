context = client.service.companyReport(customer=customer, companyReportQuery=reportQuery)

<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://www.uc.se/schemas/ucOrderRequest/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <SOAP-ENV:Header/>
    <ns0:Body>
        <ns1:companyReport>
            <ns1:customer>
                <ns1:userId>KOT92</ns1:userId>
                <ns1:password>UC</ns1:password>
            </ns1:customer>
            <ns1:companyReportQuery>
                <ns1:object>540711-5616</ns1:object>
                <ns1:override/>
            </ns1:companyReportQuery>
        </ns1:companyReport>
    </ns0:Body>
</SOAP-ENV:Envelope>


