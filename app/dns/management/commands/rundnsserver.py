from django.core.management.base import BaseCommand

from socket import gethostname, gethostbyname
from socketserver import UDPServer

from dns.server.handler.dns_handler import DNSHandler

import logging


class Command(BaseCommand):
    def handle(self, *args, **options):
        host = None

        if option := options.get('host'):
            host = option
        else:
            host = gethostbyname(
                gethostname(),
            )

        server = UDPServer((host, 53), DNSHandler)
        logging.info(f'Start server on: {host}:53')
        server.serve_forever()

    def add_arguments(self, parser):
        parser.add_argument(
            '--host',
        )
