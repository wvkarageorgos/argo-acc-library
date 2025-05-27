#!/usr/bin/env python

from argparse import ArgumentParser
from argo_acc_library import ArgoAccountingService
import sys

if __name__ == "__main__":
    parser = ArgumentParser(description="Simple Argo Accounting metric assignment example")
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
    parser.add_argument(
        "--metricdefid",
        type=str,
        required=True,
        help="Reference Id from the metric definition.",
    )
    parser.add_argument(
        "--tstart",
        type=str,
        required=True,
        help="Timestamp of the starting date time (Zulu timestamp)",
    )
    parser.add_argument(
        "--tend",
        type=str,
        required=True,
        help="Timestamp of the end date time (Zulu timestamp)",
    )
    parser.add_argument(
        "--value",
        type=str,
        required=True,
        help="Value of the metric for the given period.",
    )
    parser.add_argument(
        "--gid",
        type=str,
        required=True,
        help="Group Id associated with the metric.",
    )
    parser.add_argument(
        "--uid",
        type=str,
        required=True,
        help="User Id associated with the metric.",
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
        acc.installations[args.installation].metrics.add({
            "metric_definition_id": args.metricdefid,
            "time_period_start": args.tstart,
            "time_period_end": args.tend,
            "value": args.value,
            "group_id": args.gid,
            "user_id": args.uid,
        })
    except Exception as e:
        print("Error while assigning metric to installation:", str(e), file=sys.stderr)
