import factory

from ..models import UCRiskReport


class UCReportFactory(factory.DjangoModelFactory):
    FACTORY_FOR = UCRiskReport

    rating = None
    last_updated = None
