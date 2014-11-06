from django.db import models

from .uc import get_company_risk_report


class UCRiskReport(models.Model):
    rating = models.DecimalField(decimal_places=4, max_digits=6)
    last_updated = models.DateTimeField(auto_now=True)

    def create_rating_report(self, organization_number):
        report = get_company_risk_report(organization_number)
        self.rating = report.ucReport[0].xmlReply.reports[0].report[0].\
            group[1].term[0].value
        self.save()
