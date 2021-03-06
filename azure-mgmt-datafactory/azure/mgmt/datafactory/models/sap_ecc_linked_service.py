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

from .linked_service import LinkedService


class SapEccLinkedService(LinkedService):
    """Linked service for SAP ERP Central Component(SAP ECC).

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    :param url: The URL of SAP ECC OData API. For example,
     '[https://hostname:port/sap/opu/odata/sap/servicename/]'. Type: string (or
     Expression with resultType string).
    :type url: str
    :param username: The username for Basic authentication. Type: string (or
     Expression with resultType string).
    :type username: str
    :param password: The password for Basic authentication.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Either encryptedCredential or username/password must
     be provided. Type: string (or Expression with resultType string).
    :type encrypted_credential: str
    """

    _validation = {
        'type': {'required': True},
        'url': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'typeProperties.url', 'type': 'str'},
        'username': {'key': 'typeProperties.username', 'type': 'str'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'str'},
    }

    def __init__(self, url, additional_properties=None, connect_via=None, description=None, username=None, password=None, encrypted_credential=None):
        super(SapEccLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description)
        self.url = url
        self.username = username
        self.password = password
        self.encrypted_credential = encrypted_credential
        self.type = 'SapEcc'
