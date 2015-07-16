from decimal import Decimal

from django.db import models

from .uc import (get_company_risk_report,
                 get_credit_rating_group_term_indices)


class UCRiskReport(models.Model):
    rating = models.DecimalField(decimal_places=4, max_digits=6)
    last_updated = models.DateTimeField(auto_now=True)

    def create_rating_report(self, organization_number):
        report = get_company_risk_report(organization_number)

        # Reports are split into different groups / terms
        # Just to make sure we're getting the correct one
        # we'll traverse the lists we get.
        group_id, term_id = get_credit_rating_group_term_indices(report)

        self.rating = Decimal(
            report.ucReport[0].xmlReply.reports[0].report[0].group[group_id].term[term_id].value)

        self.save()
