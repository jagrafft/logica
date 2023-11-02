#!/usr/bin/python
#
# Copyright 2023 Logica Authors
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

from logging import error
from common import color


class TypeRetrievalException(Exception):
  def __init__(self, predicate_text: str):
    error(f'''{color.Format("[ {error}Error{end} ]")} Bad predicate to build scheme for: '{predicate_text}'

Scheme can be built for predicates of the form:
'<PredicateName>(..<name of row>) :- <name table>(..<name of row>);'
          ''')
