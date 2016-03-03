#!/usr/bin/env python
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest
from unittest.mock import MagicMock

from gns3.server import Server


@pytest.fixture
def server():
    Server.reset()
    server =  Server({"protocol": "http", "host": "127.0.0.1", "port": "8000"}, MagicMock())
    return server


def test_http_query_forwarded_to_http_client(server):
    """
    The HTTP query should be forwarded to the HTTP client
    """
    server._http_client = MagicMock()
    server.get("/get")
    server._http_client.get.assert_called_with("/get", server=server)
    server.post("/post")
    server._http_client.post.assert_called_with("/post", server=server)
    server.put("/put")
    server._http_client.put.assert_called_with("/put", server=server)
    server.delete("/delete")
    server._http_client.delete.assert_called_with("/delete", server=server)
    server.createHTTPQuery("/create")
    server._http_client.createHTTPQuery.assert_called_with("/create", server=server)
    server.getSynchronous("/synchronous")
    server._http_client.getSynchronous.assert_called_with("/synchronous")


def test_dump(server):

    assert server.dump() == {
        'host': '127.0.0.1',
        'id': 0,
        'local': True,
        'port': 8000,
        'protocol': 'http',
        'ram_limit': 0,
        'vm': False}

