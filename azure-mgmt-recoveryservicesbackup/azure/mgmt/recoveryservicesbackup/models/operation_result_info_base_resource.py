# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .operation_worker_response import OperationWorkerResponse


class OperationResultInfoBaseResource(OperationWorkerResponse):
    """Base class for operation result info.

    :param status_code: HTTP Status Code of the operation. Possible values
     include: 'Continue', 'SwitchingProtocols', 'OK', 'Created', 'Accepted',
     'NonAuthoritativeInformation', 'NoContent', 'ResetContent',
     'PartialContent', 'MultipleChoices', 'Ambiguous', 'MovedPermanently',
     'Moved', 'Found', 'Redirect', 'SeeOther', 'RedirectMethod', 'NotModified',
     'UseProxy', 'Unused', 'TemporaryRedirect', 'RedirectKeepVerb',
     'BadRequest', 'Unauthorized', 'PaymentRequired', 'Forbidden', 'NotFound',
     'MethodNotAllowed', 'NotAcceptable', 'ProxyAuthenticationRequired',
     'RequestTimeout', 'Conflict', 'Gone', 'LengthRequired',
     'PreconditionFailed', 'RequestEntityTooLarge', 'RequestUriTooLong',
     'UnsupportedMediaType', 'RequestedRangeNotSatisfiable',
     'ExpectationFailed', 'UpgradeRequired', 'InternalServerError',
     'NotImplemented', 'BadGateway', 'ServiceUnavailable', 'GatewayTimeout',
     'HttpVersionNotSupported'
    :type status_code: str or
     ~azure.mgmt.recoveryservicesbackup.models.HttpStatusCode
    :param headers: HTTP headers associated with this operation.
    :type headers: dict[str, list[str]]
    :param operation: OperationResultInfoBaseResource operation
    :type operation:
     ~azure.mgmt.recoveryservicesbackup.models.OperationResultInfoBase
    """

    _attribute_map = {
        'status_code': {'key': 'statusCode', 'type': 'HttpStatusCode'},
        'headers': {'key': 'headers', 'type': '{[str]}'},
        'operation': {'key': 'operation', 'type': 'OperationResultInfoBase'},
    }

    def __init__(self, status_code=None, headers=None, operation=None):
        super(OperationResultInfoBaseResource, self).__init__(status_code=status_code, headers=headers)
        self.operation = operation
