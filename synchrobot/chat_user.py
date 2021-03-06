# -*- coding: utf-8 -*-
# Author: Ivan Senin

import calendar
import time
import datetime as dt
import json

class User(object):
	def __init__(self, id, name, last_seen, want_time, muted, username="", additional_keys="{}"):
		super(User, self).__init__()
		self.id = id
		self.name = name
		self.username = username
		self._last_seen = last_seen
		self._want_time = want_time
		self._muted = muted
		self.dirty = True
		self.other_keys = json.loads(additional_keys) if additional_keys else {}

	def get_seen(self): return self._last_seen

	def set_seen(self, seen):
		self._last_seen = seen
		self.dirty = True
	last_seen = property(get_seen, set_seen)

	def get_want_time(self): return self._want_time

	def set_want_time(self, new_val):
		self._want_time = new_val
		self.dirty = True
	want_time = property(get_want_time, set_want_time)

	def get_muted(self): return self._muted

	def set_muted(self, new_val):
		self._muted = new_val
		self.dirty = True
	muted = property(get_muted, set_muted)


	def update_seen_time(self):
		self.last_seen = calendar.timegm(time.gmtime())

	def __str__(self):
		seen_str = dt.datetime.fromtimestamp(self.last_seen).strftime('%Y-%m-%d %H:%M:%S')

		return "User: ({0}{1}, id: {2}, last_seen: {3}, want_time: {4}, muted: {5})".format(
				self.name.encode('utf-8'), " (" + self.username + ")" if self.username else "", self.id, seen_str,
				self.want_time, self.muted)

	def serialized_keys(self):
		return json.dumps(self.other_keys)

