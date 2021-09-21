################################################################################
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Created Date: 21-09-19
# Author: Gabriel Danjon
# -----
# Last Modified: 
# Modified By: 
# -----
# Copyright (c) 2021 Da2ny's world
# 
# A clean code for a better programming
# -----
################################################################################

from typing import Any
import yaml
import os


class Yaml:
    def read_yaml(self, yaml_path: str) -> Any:
        if (yaml_path and os.path.isfile(yaml_path)):
            try:
                with open(yaml_path, 'r') as stream:
                    result: Any = yaml.safe_load(stream)
                return result
            except:
                return None
        return None