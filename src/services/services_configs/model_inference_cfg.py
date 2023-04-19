import os

from src.services.services_configs.base_services_cfgs import ModelInferenceConfig, HooliGANConfig


img_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/services/hooligan_ans/1"
InferenceConfig = ModelInferenceConfig(
                            model_config=HooliGANConfig(ans_path_dir=img_path)
                    )