from django.test import SimpleTestCase
from telollevo.forms import EnviosForm

class TestForms(SimpleTestCase):

	
	def test_expense_from_no_data(self):
		form = EnviosForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 10)