from dataclasses import dataclass


@dataclass
class HooliGANConfig:
    ans_path_dir: str

@dataclass
class ModelInferenceConfig:
    model_config: HooliGANConfig


