"""
Contains unit tests for spotify.py for linux
"""
import unittest
from swaglyrics.spotify import get_info_linux, song, artist
from mock import mock, patch, Mock
import platform

@patch('platform.system', return_value='Linux')
class LinuxTests(unittest.TestCase):
	"""
	Unit tests
	"""

	def setup(self, mock_os):
		pass

	@patch('swaglyrics.spotify.get_info_linux')
	def test_that_artist_function_calls_get_info(self, mock, mock_os):
		"""
		test that test artist function calls get_info_linux function
		"""
		x = artist()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_linux')
	def test_that_song_function_calls_get_info(self, mock, mock_os):
		"""
		test that test song function calls get_info_linux function
		"""
		x = song()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_linux', side_effect=ValueError)
	def test_that_artist_function_returns_None_when_error(self, mock, mock_os):
		"""
		test that test artist function returns None when the get_info_linux function will return an error
		"""
		x = artist()
		self.assertEqual(x, None)

	@patch('swaglyrics.spotify.get_info_linux', side_effect=ValueError)
	def test_that_song_function_returns_None_when_error(self, mock, mock_os):
		"""
		test that test song function returns None when the get_info_linux function will return an error
		"""
		x = song()
		self.assertEqual(x, None)

@mock.patch('platform.system', return_value='Windows')
class WindowsTests(unittest.TestCase):
	"""
	Unit tests
	"""

	def setup(self, mock_os):
		pass

	@patch('swaglyrics.spotify.get_info_windows')
	def test_that_artist_function_calls_get_info(self, mock, mock_os):
		"""
		test that test artist function calls get_info_windows function
		"""
		x = artist()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_windows')
	def test_that_song_function_calls_get_info(self, mock, mock_os):
		"""
		test that test song function calls get_info_windows function
		"""
		x = song()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_windows', side_effect=ValueError)
	def test_that_artist_function_returns_None_when_error(self, mock, mock_os):
		"""
		test that test artist function returns None when the get_info_windows function will return an error
		"""
		x = artist()
		self.assertEqual(x, None)

	@patch('swaglyrics.spotify.get_info_windows', side_effect=ValueError)
	def test_that_song_function_returns_None_when_error(self, mock, mock_os):
		"""
		test that test song function returns None when the get_info_windows function will return an error
		"""
		x = song()
		self.assertEqual(x, None)

@mock.patch('platform.system', return_value='Darwin')
class DarwinTests(unittest.TestCase):
	"""
	Unit tests
	"""

	def setup(self, mock_os):
		pass

	@patch('swaglyrics.spotify.get_info_mac')
	def test_that_artist_function_calls_get_info(self, mock, mock_os):
		"""
		test that test artist function calls get_info_darwin function
		"""
		x = artist()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_mac')
	def test_that_song_function_calls_get_info(self, mock, mock_os):
		"""
		test that test song function calls get_info_darwin function
		"""
		x = song()
		self.assertTrue(mock.called)

	@patch('swaglyrics.spotify.get_info_mac', side_effect=ValueError)
	def test_that_artist_function_returns_None_when_error(self, mock, mock_os):
		"""
		test that test artist function returns None when the get_info_darwin function will return an error
		"""
		x = artist()
		self.assertEqual(x, None)

	@patch('swaglyrics.spotify.get_info_mac', side_effect=ValueError)
	def test_that_song_function_returns_None_when_error(self, mock, mock_os):
		"""
		test that test song function returns None when the get_info_darwin function will return an error
		"""
		x = song()
		self.assertEqual(x, None)


if __name__ == '__main__':
	unittest.main()
