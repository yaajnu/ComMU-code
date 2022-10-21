import torch

from commu.midi_generator.container import ModelArguments
from model_initializer import ModelInitializeTask
from info_preprocessor import PreprocessTask
from midi_inferrer import InferenceTask
from sequence_postprocessor import PostprocessTask


class MidiGenerationPipeline:
    def __init__(self, model_arguments: dict):
        self.map_location = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(self.map_location)
        self.model_args = ModelArguments(**model_arguments)

        self.model_initialize_task = ModelInitializeTask(
            model_args=self.model_args,
            map_location=self.map_location,
            device=self.device
        )
        self.preprocess_task = PreprocessTask()
        self.inference_task = InferenceTask()
        self.postprocess_task = PostprocessTask()