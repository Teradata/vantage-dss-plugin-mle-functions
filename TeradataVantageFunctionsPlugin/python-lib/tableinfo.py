# -*- coding: utf-8 -*-
'''
Copyright © 2019 by Teradata.
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

class tableinfo(object):    
    def __init__(self, connectioninfo, datasetname):
        self._schemaname = None if not connectioninfo.get('schema', "") else connectioninfo['schema'] # or add select defaultdatabase from dbc.UsersV where username = 'dssUser';
        self._tablename = connectioninfo['table']
        self._datasetname = datasetname
        
    @property
    def tablename(self):
        if self._schemaname == None:
            print('Defaulting to user\'s default database')
            return self._tablename
        else:
            print('Defaulting to user\'s default database')
            return ".".join(['"{}"'.format(self._schemaname),
                        '"{}"'.format(self._tablename)])
    
    @property
    def datasetname(self):
        dname = self._datasetname.split('.')
        return dname[len(dname) - 1] if dname else ""
