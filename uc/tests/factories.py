import factory

from ..models import UCRiskReport


class UCReportFactory(factory.DjangoModelFactory):

    class Meta:
        model = UCRiskReport

    rating = None
    last_updated = None
