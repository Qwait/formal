import unittest

from formal.html import content_tag_string
from formal.html import dasherize
from formal.html import tag
from formal.html import tag_options

class TestHtml(unittest.TestCase):
    def test_dasherize(self):
        self.assertEqual(dasherize('data_test'), 'data-test')

    def test_tag(self):
        self.assertEqual(tag('br'), '<br>')

    def test_tag_options(self):
        self.assertEqual(tag_options({'class': 'my-class'}), 'class="my-class"')
        self.assertEqual(tag_options({'disabled': 'disabled'}), 'disabled="disabled"')
        self.assertEqual(tag_options({'data': {'test': 'true', 'works': 'true'}}),
            'data-test="true" data-works="true"')

    #def test_content_tag_string(self):
    #    self.assertEqual(content_tag_string('p', 'This is a paragraph'), None)
