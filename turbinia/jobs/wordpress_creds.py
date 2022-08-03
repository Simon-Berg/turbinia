# -*- coding: utf-8 -*-
# Copyright 2021 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Job to execute wordpress_creds analysis task."""

from turbinia.evidence import CompressedDirectory
from turbinia.evidence import Directory
from turbinia.evidence import DockerContainer
from turbinia.evidence import GoogleCloudDisk
from turbinia.evidence import GoogleCloudDiskRawEmbedded
from turbinia.evidence import RawDisk
from turbinia.evidence import EwfDisk
from turbinia.evidence import ReportText
from turbinia.jobs import interface
from turbinia.jobs import manager
from turbinia.workers.analysis import wordpress_creds


class WordpressCredsAnalysisJob(interface.TurbiniaJob):
  """Wordpress Account analysis job."""

  evidence_input = [
      Directory, RawDisk, GoogleCloudDisk, GoogleCloudDiskRawEmbedded,
      CompressedDirectory, DockerContainer, EwfDisk
  ]
  evidence_output = [ReportText]

  NAME = 'WordpressCredsAnalysisJob'

  def create_tasks(self, evidence):
    """Create task.

    Args:
      evidence: List of evidence objects to process
    Returns:
        A list of tasks to schedule.
    """
    tasks = [wordpress_creds.WordpressCredsAnalysisTask() for _ in evidence]
    return tasks


manager.JobsManager.RegisterJob(WordpressCredsAnalysisJob)
