from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create a new user with an email is successful"""
        test_email = 'test@emailsender.com'
        test_password = 'testpassword1234'
        user = get_user_model().objects.create_user(
            email=test_email,
            password=test_password,
        )

        self.assertEqual(user.email, test_email)
        self.assertTrue(user.check_password(test_password))
        # check_password return boolean
