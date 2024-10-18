from .models import Domain, Record
from django.db.models import QuerySet

from typing import Optional


def get_domain(*, name: str, **kwargs) -> Optional[Domain]:
    return Domain.objects.filter(name=name).first()


def get_domain_records(*, domain: Domain = None, domain_id: int = None, **kwargs) -> QuerySet[Record]:
    domain = _get_domain_by_id(domain=domain, domain_id=domain_id)

    return domain.records.all()


def _get_domain_by_id(*, domain: Domain = None, domain_id: int = None, **kwargs) -> Optional[Domain]:
    if domain is None and domain_id is None:
        raise Exception('domain or domain_id is required!')

    if domain:
        return domain

    return Domain.objects.get(id=domain_id)


__all__ = (
    'get_domain',
    'get_domain_records',
)
