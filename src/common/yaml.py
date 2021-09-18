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