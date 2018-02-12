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


class RunbookCreateOrUpdateDraftProperties(Model):
    """The parameters supplied to the create or update dratft runbook properties.

    :param log_verbose: Gets or sets verbose log option.
    :type log_verbose: bool
    :param log_progress: Gets or sets progress log option.
    :type log_progress: bool
    :param runbook_type: Gets or sets the type of the runbook. Possible values
     include: 'Script', 'Graph', 'PowerShellWorkflow', 'PowerShell',
     'GraphPowerShellWorkflow', 'GraphPowerShell'
    :type runbook_type: str or ~azure.mgmt.automation.models.RunbookTypeEnum
    :param draft: Gets or sets the draft runbook properties.
    :type draft: ~azure.mgmt.automation.models.RunbookDraft
    :param description: Gets or sets the description of the runbook.
    :type description: str
    :param log_activity_trace: Gets or sets the activity-level tracing options
     of the runbook.
    :type log_activity_trace: int
    """

    _validation = {
        'runbook_type': {'required': True},
        'draft': {'required': True},
    }

    _attribute_map = {
        'log_verbose': {'key': 'logVerbose', 'type': 'bool'},
        'log_progress': {'key': 'logProgress', 'type': 'bool'},
        'runbook_type': {'key': 'runbookType', 'type': 'str'},
        'draft': {'key': 'draft', 'type': 'RunbookDraft'},
        'description': {'key': 'description', 'type': 'str'},
        'log_activity_trace': {'key': 'logActivityTrace', 'type': 'int'},
    }

    def __init__(self, runbook_type, draft, log_verbose=None, log_progress=None, description=None, log_activity_trace=None):
        super(RunbookCreateOrUpdateDraftProperties, self).__init__()
        self.log_verbose = log_verbose
        self.log_progress = log_progress
        self.runbook_type = runbook_type
        self.draft = draft
        self.description = description
        self.log_activity_trace = log_activity_trace
