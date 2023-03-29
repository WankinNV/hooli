from src.services.hooligan import HoolGAN
from src.services.services_configs.base_services_cfgs import ModelInferenceConfig


class ModelInference:

    def __init__(self, config: ModelInferenceConfig):
        self.hooligan_model = HoolGAN(config.model_config)

    def generate_img(self):
        return self.hooligan_model.generate()