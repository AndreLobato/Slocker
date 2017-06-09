import unittest as uni
import requests
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
                            'repo_url': "http://repo_url"}}
        self.app.post('/', data=json.dumps(dockerhub_data),
                             content_type="application/json", 
                             follow_redirects=True)
        print resp.data
        post.assert_called_once()