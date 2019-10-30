#!/usr/bin/env python

import argparse
import requests

username = 'm--z'
password = '1'
token = 'cea3bc--------475e1e82abb1d9029a2'

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', help='utility version')
parser.add_argument('-u', '--username', help='GitHub username',
                    default=username)
parser.add_argument('-p', '--password', help='GitHub password',
                    default=password)
parser.add_argument('-r', '--repository', help='Repository name',
                    default='devops_lab')
parser.add_argument('-m', '--number', action='store_true',
                    help='Pull requests number.')
parser.add_argument('-c', '--created', action='store_true',
                    help='Pull requests creation date.')
parser.add_argument('-up', '--updated', action='store_true',
                    help='Pull requests updated date.')
parser.add_argument('-st', '--status', action='store_true',
                    help='Pull request status.', default=True)
parser.add_argument('-t', '--token', help='Token string', type=str)

args = parser.parse_args()

# from https://github.com/user/settings/tokens
if args.version:
    print('Utility version: 0.0.132')
    quit()

gitUrl = 'https://api.github.com/repos/alenaPy/' + args.repository + '/pulls'

# create a re-usable session object with the user creds in-built
r = requests.get(gitUrl, auth=(username, password))

if r.status_code != 200:
    print('ERROR URL:', r.json().get('message'))

if args.updated:
    my_dict = []
    for item in r.json():
        my_dict = {'Title': item.get('title'), 'Date': item.get('updated_at')}
        print('Pull request , updated at:')
        for i in my_dict:
            print(my_dict[i])

if args.created:
    my_dict = []
    for item in r.json():
        ''' my_dict = {'Title': item.get('title'),
         'User': item.get('user').get('login'), 'Date': item.get('created_at')}'''
        my_dict = {'Title': item.get('title'), 'Date': item.get('created_at')}
        print('Pull request , createad at:')
        for i in my_dict:
            print(my_dict[i])

if args.status:
    my_dict = []
    for item in r.json():
        my_dict = {'Title': item.get('title'), 'State': item.get('state')}
        print('State of pull request:')
        for i in my_dict:
            print(my_dict[i])

if args.number:
    my_dict = []
    for item in r.json():
        my_dict = {'Title': item.get('title'), 'Number ': item.get('number')}
        print('Pull request number:')
        for i in my_dict:
            print(my_dict[i])
