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

from msrest.serialization import Model


class TestJob(Model):
    """Definition of the test job.

    :param creation_time: Gets or sets the creation time of the test job.
    :type creation_time: datetime
    :param status: Gets or sets the status of the test job.
    :type status: str
    :param status_details: Gets or sets the status details of the test job.
    :type status_details: str
    :param run_on: Gets or sets the runOn which specifies the group name where
     the job is to be executed.
    :type run_on: str
    :param start_time: Gets or sets the start time of the test job.
    :type start_time: datetime
    :param end_time: Gets or sets the end time of the test job.
    :type end_time: datetime
    :param exception: Gets or sets the exception of the test job.
    :type exception: str
    :param last_modified_time: Gets or sets the last modified time of the test
     job.
    :type last_modified_time: datetime
    :param last_status_modified_time: Gets or sets the last status modified
     time of the test job.
    :type last_status_modified_time: datetime
    :param parameters: Gets or sets the parameters of the test job.
    :type parameters: dict[str, str]
    """

    _attribute_map = {
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'status_details': {'key': 'statusDetails', 'type': 'str'},
        'run_on': {'key': 'runOn', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'exception': {'key': 'exception', 'type': 'str'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
        'last_status_modified_time': {'key': 'lastStatusModifiedTime', 'type': 'iso-8601'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
    }

    def __init__(self, creation_time=None, status=None, status_details=None, run_on=None, start_time=None, end_time=None, exception=None, last_modified_time=None, last_status_modified_time=None, parameters=None):
        super(TestJob, self).__init__()
        self.creation_time = creation_time
        self.status = status
        self.status_details = status_details
        self.run_on = run_on
        self.start_time = start_time
        self.end_time = end_time
        self.exception = exception
        self.last_modified_time = last_modified_time
        self.last_status_modified_time = last_status_modified_time
        self.parameters = parameters
