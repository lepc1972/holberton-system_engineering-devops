#!/usr/bin/python3
"""get info from a rest-api"""
import requests
import sys

if __name__=="__main__":
    todo_s = requests.get('https://jsonplaceholder.typicode.com/todo_s').json()
    print(todo_s)