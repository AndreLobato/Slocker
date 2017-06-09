import unittest as uni
import requests
import flask
import mock
import json

from .slocker import *

class TestSlocker(uni.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_load_json(self):
        channel, mentions = SearchRepoName('NameUserDocker/NameRepoDocker')
        self.assertEqual(channel, "#YourSlackChannel")
        self.assertEqual(mentions, ["@mentions1","@mentions2"])

    def test_hello(self):
        resp = self.app.get('/')
        self.assertEqual(resp.data, '...Relay ON....')

    @mock.patch('requests.post')
    def test_post_dockerhub(self, post):
        dockerhub_data = {'push_data': {'tag':'some_crazy_tag'},
                          'repository': {
                            'repo_name':'NameUserDocker/NameRepoDocker',
                            'repo_url': "http://None"}}

        with app.test_request_context('/', method='POST', 
                                      content_type='application/json',
                                      data=json.dumps(dockerhub_data)):
            ReceiveBuild()
            post.assert_called_once()