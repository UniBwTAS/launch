# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for the ScopedIncludeLaunchDescription action."""

from typing import List

from .pop_environment import PopEnvironment
from .pop_launch_configurations import PopLaunchConfigurations
from .push_environment import PushEnvironment
from .push_launch_configurations import PushLaunchConfigurations
from ..frontend import expose_action
from ..launch_context import LaunchContext
from ..launch_description_entity import LaunchDescriptionEntity
from ..actions.include_launch_description import IncludeLaunchDescription


@expose_action('scoped_include')
class ScopedIncludeLaunchDescription(IncludeLaunchDescription):
    def execute(self, context: LaunchContext) -> List[LaunchDescriptionEntity]:
        return [PushLaunchConfigurations(),
                PushEnvironment(),
                *super().execute(context),
                PopEnvironment(),
                PopLaunchConfigurations()]
