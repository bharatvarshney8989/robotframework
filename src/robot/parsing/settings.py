#  Copyright 2008-2009 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


class Setting(object):

    def __init__(self):
        self.value = []
        self.comment = ''

    def set(self, value, comment=None):
        self._set(value)
        self.comment = comment

    def _set(self, value):
        self.value = value

    def _string_value(self, value):
        return value if isinstance(value, basestring) else ' '.join(value)


class Documentation(Setting):

    def __init__(self):
        self.value = ''

    def _set(self, value):
        self.value = self._string_value(value)


class Fixture(Setting):

    def __init__(self):
        self.name = None
        self.args = []

    def _set(self, value):
        self.name = value[0] if value else ''
        self.args = value[1:]


class Timeout(Setting):

    def __init__(self):
        self.value = None
        self.message = ''

    def _set(self, value):
        self.value = value[0] if value else ''
        self.message = ' '.join(value[1:])


class Tags(Setting):
    pass


class Arguments(Setting):
    pass


class Return(Setting):
    pass


class Metadata(Setting):

    def __init__(self, name, value, comment):
        self.name = name
        self.value = self._string_value(value)
        self.comment = comment


class Import(Setting):

    def __init__(self, name, args=None, alias=None, comment=None):
        self.name = name
        self.args = args or []
        self.alias = alias
        self.comment = comment


class Library(Import):

    def __init__(self, name, args=None, alias=None, comment=None):
        if args and not alias:
            args, alias = self._split_alias(args)
        Import.__init__(self, name, args, alias, comment)

    def _split_alias(self, args):
        if len(args) >= 2 and args[-2].upper() == 'WITH NAME':
            return args[:-2], args[-1]
        return args, None


class Resource(Import):

    def __init__(self, name, invalid_args=None, comment=None):
        if invalid_args:
            name += ' ' + ' '.join(invalid_args)
        Import.__init__(self, name, comment=comment)


class Variables(Import):

    def __init__(self, name, args=None, comment=None):
        Import.__init__(self, name, args, comment=comment)
