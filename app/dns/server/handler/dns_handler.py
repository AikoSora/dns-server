from socketserver import BaseRequestHandler

from dnslib import DNSRecord, DNSHeader, RR

from dns.crud import get_domain_records, get_domain
from dns.server.types.records import get_record
from dns.server.resolve import dns_lookup


class DNSHandler(BaseRequestHandler):

    def handle(self):
        data, socket_object = self.request

        try:
            request = DNSRecord.parse(data)

            reply = DNSRecord(
                header=DNSHeader(
                    id=request.header.id,
                    qr=1,
                    aa=1,
                    ra=1,
                ),
                q=request.q,
            )

            qname = str(request.q.qname)

            if domain := get_domain(name=qname[:len(qname) - 1]):

                for record in get_domain_records(domain=domain):

                    record_type, record_parser = get_record(
                        record.record_type.capitalize()
                    )

                    reply.add_answer(
                        RR(
                            rname=qname,
                            rtype=record_type,
                            rdata=record_parser(record.ip_address),
                        )
                    )

            else:
                response = dns_lookup(qname[:len(qname) - 1], '8.8.8.8')

                if response is not None:

                    for key in response.keys():
                        code, parser = get_record(key)

                        for record in response[key]:
                            reply.add_answer(
                                RR(
                                    rname=qname,
                                    rtype=code,
                                    rdata=parser(record)
                                )
                            )

            socket_object.sendto(reply.pack(), self.client_address)

        except Exception as ex:
            print(ex)
            return ex


__all__ = (
    'DNSHandler',
)
