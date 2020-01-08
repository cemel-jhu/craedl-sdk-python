# Copyright 2019 The Johns Hopkins University
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

import getpass
import os
import stat
import sys

from craedl import auth
from craedl.auth import default_path

import click

TOKEN_PATH = default_path()


def try_upload(profile, source, destination):
    destinations = destination.split(":")
    if len(destinations) != 2:
        raise Exception(
            "Provide a project and a path in destination for uploading.")
    versioned = destinations.pop().split("@")
    path = versioned[0]
    if len(versioned) != 1:
        raise Exception("Cannot specify an upload version.")
    profile.get_project(destinations[0]).get_data().create_directory(path).get(
        path).create_file(source, progress=True)


def try_download(profile, source, destination):
    sources = source.split(":")
    if len(sources) != 2:
        raise Exception(
            "Provide a project and a path in source for downloading.")
    versioned = sources.pop().split("@")
    path = versioned[0]
    version = None
    if len(versioned) == 2:
        try:
            version = int(versioned.pop())
        except:
            raise Exception(
                "Not sure what version you're specifying for download...")
    profile.get_project(sources[0]).get_data().get(path).download(
        destination, version_index=version)


@click.command()
@click.option("--config",
              default=TOKEN_PATH,
              help=("Path of settings token"
                    "location."))
@click.argument("source")
@click.argument("destination")
def craedl(config, source, destination):
    """
    The ``craedl-token`` console script entry point for configuring the Craedl
    authentication token.
    """
    profile = auth()
    errors = []
    # Massive hack. Should determine whether download or source instead of just
    # trying and breaking.
    try:
        try_download(profile, source, destination)
    except Exception as e:
        errors.append(e)
        try:
            try_upload(profile, source, destination)
        except Exception as e2:
            errors.append(e2)
            raise Exception(errors)


if __name__ == "__main__":
    craedl()
