#
# Copyright 2016 DGraph Labs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains the main user-facing methods for interacting with the
Dgraph server over gRPC.
"""
from pydgraph.utils.proto import api_pb2 as api
from pydgraph.utils.proto.api_pb2_grpc import DgraphStub

from typing import Union

import grpc
import json


class DgraphClient(object):
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel("{host}:{port}".format(host=host, port=port))
        self.stub = DgraphStub(self.channel)

    def query(self, query: str) -> api.Response:
        request = api.Request(query=query)
        response = self.stub.Query(request)
        return response

    def mutate(self, type: str, payload: Union[str, dict], delete: bool = False, commit: bool = True) -> Union[
        api.Assigned, api.TxnContext]:
        assert type in ['json', 'nquads']
        assert delete in [False, True]

        mutation = api.Mutation()

        if isinstance(payload, dict):
            payload = json.dumps(payload).encode()
        elif isinstance(payload, str):
            payload = payload.encode()

        if type == 'json':
            if delete:
                mutation.delete_json = payload
            else:
                mutation.set_json = payload
        elif type == 'nquads':
            if delete:
                mutation.delete_nquads = payload
            else:
                mutation.set_nquads = payload

        assert mutation.IsInitialized()

        transaction = self.stub.Mutate(mutation)

        if commit:
            result = self.stub.CommitOrAbort(transaction.context)
        else:
            result = transaction

        return result

    def schema(self, schema: str) -> api.Payload:
        schema = schema.encode()
        operation = api.Operation(schema=schema)
        return self.stub.Alter(operation)

    def drop_all(self) -> api.Payload:
        operation = api.Operation(drop_all=True)
        return self.stub.Alter(operation)
