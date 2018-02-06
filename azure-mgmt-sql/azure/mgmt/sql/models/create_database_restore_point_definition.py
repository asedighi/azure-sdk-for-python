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


class CreateDatabaseRestorePointDefinition(Model):
    """Contains the information necessary to perform a create database restore
    point operation.

    :param restore_point_label: The restore point label to apply
    :type restore_point_label: str
    """

    _validation = {
        'restore_point_label': {'required': True},
    }

    _attribute_map = {
        'restore_point_label': {'key': 'restorePointLabel', 'type': 'str'},
    }

    def __init__(self, restore_point_label):
        super(CreateDatabaseRestorePointDefinition, self).__init__()
        self.restore_point_label = restore_point_label
