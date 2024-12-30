import torch
from comfy.samplers import KSAMPLER
from comfy.utils import common_upscale

class ManualSigma:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "sigmas": ("STRING", {"default": "1.0, 0.8, 0.6, 0.4, 0.2", "multiline": True}),
            },
        }

    RETURN_TYPES = ("SIGMAS",)
    FUNCTION = "generate_sigmas"
    CATEGORY = "sampling/custom_scheduler"

    def generate_sigmas(self, sigmas):
        # Convert the comma-separated string into a list of floats
        sigma_list = [float(sigma.strip()) for sigma in sigmas.split(",")]
        
        # Convert the list to a tensor
        sigma_tensor = torch.tensor(sigma_list, dtype=torch.float32)
        
        return (sigma_tensor,)

# Register the node
NODE_CLASS_MAPPINGS = {
    "ManualSigma": ManualSigma,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ManualSigma": "Manual Sigma",
}
