from dnslib import (
    A, NS, CNAME, SOA, PTR, MX, TXT, RP, AAAA, LOC,
    SRV, NAPTR, DNAME, DS, SSHFP, RRSIG, NSEC,
    DNSKEY, TLSA, HTTPS, CAA,
)


RECORDS = {
    'A': (1, A),
    'NS': (2, NS),
    'CNAME': (5, CNAME),
    'SOA': (6, SOA),
    'PTR': (12, PTR),
    'MX': (15, MX),
    'TXT': (16, TXT),
    'RP': (17, RP),
    'AAAA': (28, AAAA),
    'LOC': (29, LOC),
    'SRV': (33, SRV),
    'NAPTR': (35, NAPTR),
    'DNAME': (39, DNAME),
    'DS': (43, DS),
    'SSHFP': (44, SSHFP),
    'RRSIG': (46, RRSIG),
    'NSEC': (47, NSEC),
    'DNSKEY': (48, DNSKEY),
    'TLSA': (52, TLSA),
    'HTTPS': (65, HTTPS),
    'CAA': (257, CAA),
}


def get_record(name: str):
    return RECORDS.get(name)


__all__ = (
    'get_record',
)
