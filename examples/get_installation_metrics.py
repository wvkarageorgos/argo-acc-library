#!/usr/bin/env python

import sys
from argparse import ArgumentParser

from argo_acc_library import ArgoAccountingService

if __name__ == "__main__":
    parser = ArgumentParser(description="Simple Argo Accounting metric fetch example")
    parser.add_argument(
        "--host",
        type=str,
        default="api.devel.acc.argo.grnet.gr",
        help="FQDN of Argo Accounting Service",
    )
    parser.add_argument(
        "--token", type=str, required=True, help="JWT authentication token"
    )
    parser.add_argument(
        "-f",
        help="treat the JWT authentication token argument as a path to a file holding the token",
        action="store_true",
    )
    parser.add_argument(
        "--installation",
        type=str,
        required=True,
        help="ID of installation registered in Argo Accounting Service",
    )
    args = parser.parse_args()

    if args.f:
        try:
            with open(args.token, "r") as tokenfile:
                token = tokenfile.read()
        except Exception as e:
            print("Error while reading token from file:", str(e), file=sys.stderr)
            exit(1)
    else:
        token = args.token

    acc = ArgoAccountingService(args.host, token)
    try:
        cnt = 0
        for m in acc.installations[args.installation].metrics:
            # print each metric value and type
            print(m.value, m.metric_definition.metric_type)
            # alternatively, print all metric data as JSON string
            # print(m)
            cnt += 1
        if cnt == 0:
            print("No metrics found for requested installation")
    except Exception as e:
        print("Installation not found:", str(e), file=sys.stderr)
