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


class JobNavigation(Model):
    """Software update configuration machine run job navigation properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Id of the job associated with the software update configuration
     run
    :vartype id: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self):
        super(JobNavigation, self).__init__()
        self.id = None
