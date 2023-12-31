#!/usr/bin/env python3

import argparse
from src.ssm import AdapterSSM

parser = argparse.ArgumentParser(description='Read SSM Parameter')
parser.add_argument('--project', help='The project scope', required=True)
parser.add_argument('--name', help='SSM Param Name', required=True)
parser.add_argument('--value', help='SSM Param Value', required=True)
# profile from args
parser.add_argument('--profile', help='AWS profile')

args = parser.parse_args()

# TODO: make not dependable on profile, should also work with env vars
ssm = AdapterSSM(project=args.project, boto={ 'profile_name': args.profile })

if not ssm.isProjectEnabled():
  print('Project is not enabled')
  exit(1)

ssm.put_parameter(args.name, args.value)
